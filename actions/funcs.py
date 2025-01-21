import numpy as np
import entities.classfile as model
from entities.classfile import MaterialBody, BodyTrajectory
from entities.math_utils import func_x, func_y

def create_mb(x_0, y_0, r1, n_points):
    material_body = MaterialBody()
    material_body.setBody(x_0, y_0, r1, n_points)
    return material_body

def move_mb(time, h, mb, a, b, c):
    body_trajectory = BodyTrajectory()
    body_trajectory.setBodyTrajectory(time, h, mb, a, b, c)
    return body_trajectory

def move_ts(time, h):
    t = h
    m = 0
    a = np.linspace(-5, 5, 11)
    x_s, y_s = np.meshgrid(a, a)
    velocity_fields = []
    for n in range(int(time / h)):  # Можно использовать "_" для игнорирования переменной
        space_points = []
        for i in range(11):
            for j in range(11):
                x = x_s[i, j]
                y = y_s[i, j]
                space_points.append(model.SpacePoint(m, x, y, func_x(t, x), func_y(t, y), t))
                m += 1
        velocity_fields.append(model.SpaceGrid(space_points))
        t += h
    return velocity_fields
