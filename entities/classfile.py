import numpy as np
from entities.math_utils import func_x, func_y, runge_method

class MaterialPoint:
    def __init__(self, coord_x, coord_y, x_0, y_0):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.x_0 = x_0
        self.y_0 = y_0

class MaterialBody:
    def __init__(self):
        self.material_points = None

    def setBody(self, x_0, y_0, r1, n_points):
        mpoint = []
        theta = np.linspace(np.pi, 3 * np.pi / 2, n_points)
        x_r1 = x_0 + r1 * np.cos(theta)
        y_r1 = y_0 + r1 * np.sin(theta)
        for xcord, ycord in zip(x_r1, y_r1):
            mpoint.append(MaterialPoint(xcord, ycord, xcord, ycord))
        self.material_points = mpoint

class PointTrajectory:
    def __init__(self, material_point, x, y):
        self.material_point = material_point
        self.x = x
        self.y = y

class BodyTrajectory:
    def __init__(self):
        self.material_body = None
        self.point_trajectories = None

    def setBodyTrajectory(self, time, h, mb, a, b, c):
        pointtr = []
        for i in mb.material_points:
            x_0 = i.x_0
            y_0 = i.y_0

            n = int(time / h) + 1
            x_t = runge_method(x_0, h, n, func_x, a, b, c)
            y_t = runge_method(y_0, h, n, func_y, a, b, c)
            pointtr.append(PointTrajectory(i, x_t, y_t))

        self.point_trajectories = pointtr
        self.material_body = mb

class SpacePoint:
    def __init__(self, i, coord_x, coord_y, velocity_x, velocity_y, t):
        self.i = i
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.t = t

class SpaceGrid:
    def __init__(self, space_points):
        self.space_points = space_points

    def setSpaceGrid(self, t):
        spoints = []
        m = 0
        a = np.linspace(-5, 5, 11)
        x_s, y_s = np.meshgrid(a, a)
        for i in range(11):
            for j in range(11):
                x = x_s[i, j]
                y = y_s[i, j]
                spoints.append(SpacePoint(x, y, func_x(t, x), func_y(t, y), t, i))
                m += 1
        self.space_points = spoints
