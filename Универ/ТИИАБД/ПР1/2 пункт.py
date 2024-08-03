import math

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_rectangle_area(length, width):
    return length * width

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_figures_area():
    figures = {
        "triangle": {
            "base": float(input("Введите длину основания треугольника: ")),
            "height": float(input("Введите высоту треугольника: "))
        },
        "rectangle": {
            "length": float(input("Введите длину прямоугольника: ")),
            "width": float(input("Введите ширину прямоугольника: "))
        },
        "circle": {
            "radius": float(input("Введите радиус круга: "))
        }
    }

    result = {}

    for figure, params in figures.items():
        if figure == "triangle":
            area = calculate_triangle_area(params["base"], params["height"])
        elif figure == "rectangle":
            area = calculate_rectangle_area(params["length"], params["width"])
        elif figure == "circle":
            area = calculate_circle_area(params["radius"])
        result[figure] = area

    return result

areas = calculate_figures_area()
print(areas)