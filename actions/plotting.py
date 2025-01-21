import numpy as np
import matplotlib.pyplot as plt
from entities.math_utils import func_x, func_y  # Убедитесь, что эти функции определены

def plot_trajectory(mb, tr):
    for i in mb.material_points:
        plt.plot(i.coord_x, i.coord_y, 'r.')

    for i in tr.point_trajectories:
        plt.plot(i.x, i.y, 'b', linewidth = 0.5)
        time = len(i.x) - 1
        plt.plot(i.x[time], i.y[time], 'g.')

    plt.axis('equal')
    plt.grid()
    plt.savefig('assets/plot_trajectory.svg', format='svg', dpi=1200)

def plot_velocity_fields(vf):
    h = vf[0].space_points[0].t
    t = h
    for n in range(len(vf)):
        plt.figure(n)
        plt.suptitle('t = ' + str(t))
        m = 0
        coord_x = []
        coord_y = []
        v_x = []
        v_y = []
        for i in range(11):
            for j in range(11):
                coord_x.append(vf[n].space_points[m].coord_x)
                coord_y.append(vf[n].space_points[m].coord_y)
                v_x.append(vf[n].space_points[m].velocity_x)
                v_y.append(vf[n].space_points[m].velocity_y)
                m += 1
        plt.subplot(1, 2, 1)
        plt.quiver(coord_x, coord_y, v_x, v_y)

        for p in range(0, 2):
            for q in range(0, 10):
                x = np.linspace(0, 1.0, 1000)
                
                # Изменяем способ вычисления d
                if func_x(t, 1) != 0:
                    d = func_y(t, 1) / func_x(t, 1)
                else:
                    d = np.inf  # Если деление на ноль, ставим бесконечность
                
                # Пропускаем возведение в степень, если d вызывает деление на 0
                if p == 0 and d < 0:
                    # Если p == 0 и d отрицательно, пропускаем этот расчет
                    continue
                
                # Если d отрицательно, ограничим значение x, чтобы избежать деления на 0
                if d < 0:
                    x = np.clip(x, 1e-10, None)  # Убираем слишком маленькие значения x

                # Проверка перед возведением в степень
                if p != 0:
                    c = q * (p ** d)  # Теперь безопасно возводим в степень
                else:
                    c = 0  # Для p == 0 результат всегда будет 0
                
                y = c * (x ** d)

                # Ограничение на значения y
                y = np.clip(y, -1e10, 1e10)  # Ограничиваем y, если оно становится слишком большим

                plt.subplot(1, 2, 2)
                plt.axis([-0.5, 2, -0.5, 10])
                plt.plot(x, y)

        t += h
        plt.savefig('assets/velocity_fields' + str(n) + '.svg', format='svg', dpi=1200)

def plot_initial_and_deformed(material_body, body_trajectory, t_index=-1):
    """
    :param material_body: объект класса MaterialBody
    :param body_trajectory: объект класса BodyTrajectory
    :param t_index: индекс времени конечного положения (по умолчанию последнее)
    """
    # Начальные координаты
    initial_x = [point.coord_x for point in material_body.material_points]
    initial_y = [point.coord_y for point in material_body.material_points]

    # Деформированные координаты
    deformed_x = [trajectory.x[t_index] for trajectory in body_trajectory.point_trajectories]
    deformed_y = [trajectory.y[t_index] for trajectory in body_trajectory.point_trajectories]

    # Построение графика
    plt.figure(figsize=(8, 6))
    plt.plot(initial_x, initial_y, label="Начальная форма тела", marker="o", linestyle="--")
    plt.plot(deformed_x, deformed_y, label="Деформированная форма тела", marker="x")
    plt.title("Начальная и еформированная форма тела (3-ая четверть)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.savefig('assets/initial_and_deformed_form.svg', format='svg', dpi=1200)
