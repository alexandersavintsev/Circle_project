from entities.constants import x_0, y_0, r1, n_points, time, h, a, b, c
from actions.funcs import create_mb, move_mb, move_ts
from actions.plotting import plot_trajectory, plot_velocity_fields
from actions.plotting import plot_initial_and_deformed

def build():
    # Создание тела
    material_body = create_mb(x_0, y_0, r1, n_points)

    # Расчёт траекторий
    move_body = move_mb(time, h, material_body, a, b, c)

    # Построение графиков
    plot_trajectory(material_body, move_body)  # Траектории
    velocity_fields = move_ts(1, 0.1)          # Поля скоростей
    plot_velocity_fields(velocity_fields)     # Поля скоростей и линии тока
    plot_initial_and_deformed(material_body, move_body)  # Начальная и деформированная формы тела

if __name__ == "__main__":
    build()
