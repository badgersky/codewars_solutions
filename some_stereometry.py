from math import pi, sqrt


def stereometry(r, h):
    s_area = round(4 * pi * r**2, 3)

    c_radius = sqrt(r**2 - h**2)
    c_area = round(pi * c_radius**2, 3)

    c_perim = round(2 * pi * c_radius, 3)

    return s_area, c_area, c_perim


if __name__ == '__main__':
    print(stereometry(2, 1))
