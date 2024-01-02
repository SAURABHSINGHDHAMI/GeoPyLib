import math

class CoordinateGeometry2D:
    def __init__(self):
        pass

    def distance_formula(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def section_formula(self, x1, y1, x2, y2, m, n):
        x = (m*x2 + n*x1) / (m + n)
        y = (m*y2 + n*y1) / (m + n)
        return x, y

    def midpoint_formula(self, x1, y1, x2, y2):
        x = (x1 + x2) / 2
        y = (y1 + y2) / 2
        return x, y

    def slope_formula(self, x1, y1, x2, y2):
        return (y2 - y1) / (x2 - x1)

    def point_slope_form(self, x1, y1, m, x):
        y = m * (x - x1) + y1
        return y

    def slope_intercept_form(self, m, b, x):
        y = m * x + b
        return y

    def intercept_form(self, a, b, x):
        y = (b / a) - (x / a)
        return y

    def two_point_form(self, x1, y1, x2, y2, x):
        y = ((y2 - y1) / (x2 - x1)) * (x - x1) + y1
        return y

    def triangle_area(self, x1, y1, x2, y2, x3, y3):
        area = 0.5 * abs((x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1))
        return area

    def circle_equation(self, h, k, r, x):
        return math.sqrt(r**2 - (x - h)**2) + k, -math.sqrt(r**2 - (x - h)**2) + k

    def parabola_equation(self, a, x):
        return 4 * a * x**2

    def ellipse_equation(self, a, b, x):
        return math.sqrt(1 - (x**2 / a**2)) * b

    def hyperbola_equation(self, a, b, x):
        return math.sqrt((x**2 / a**2) - 1) * b, -math.sqrt((x**2 / a**2) - 1) * b

class CoordinateGeometry3D:
    def __init__(self):
        pass

    def distance_formula(self, x1, y1, z1, x2, y2, z2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    def section_formula(self, x1, y1, z1, x2, y2, z2, m, n):
        x = (m*x2 + n*x1) / (m + n)
        y = (m*y2 + n*y1) / (m + n)
        z = (m*z2 + n*z1) / (m + n)
        return x, y, z

    def midpoint_formula(self, x1, y1, z1, x2, y2, z2):
        x = (x1 + x2) / 2
        y = (y1 + y2) / 2
        z = (z1 + z2) / 2
        return x, y, z

    def line_equation_vector_form(self, a, b, lambda_val):
        r = [a[0] + lambda_val * b[0], a[1] + lambda_val * b[1], a[2] + lambda_val * b[2]]
        return r

    def line_equation_cartesian_form(self, x1, y1, z1, a, b, c, x, y, z):
        return (x - x1) / a, (y - y1) / b, (z - z1) / c

    def plane_equation_general_form(self, A, B, C, D, x, y, z):
        return A*x + B*y + C*z + D

    def plane_equation_vector_form(self, n, d, x, y, z):
        return n[0]*x + n[1]*y + n[2]*z - d

    def angle_between_lines(self, a, b):
        cos_theta = (a[0]*b[0] + a[1]*b[1] + a[2]*b[2]) / (math.sqrt(a[0]**2 + a[1]**2 + a[2]**2) * math.sqrt(b[0]**2 + b[1]**2 + b[2]**2))
        return math.acos(cos_theta)

    def shortest_distance_point_line(self, a, b, p):
        d = math.sqrt(((a[0] - p[0])**2 + (a[1] - p[1])**2 + (a[2] - p[2])**2))
        return d

    def shortest_distance_point_plane(self, p, n, d):
        numerator = abs(p[0]*n[0] + p[1]*n[1] + p[2]*n[2] - d)
        denominator = math.sqrt(n[0]**2 + n[1]**2 + n[2]**2)
        return numerator / denominator

    def sphere_equation(self, a, b, c, r, x, y, z):
        return (x - a)**2 + (y - b)**2 + (z - c)**2 - r**2

    def cone_equation(self, k, x, y, z):
        return x**2 + y**2 - k**2 * z**2
