import math

def calculate_magnetic_induction(B, angle, mu):
    """
    Рассчитывает магнитную индукцию вблизи поверхности магнетика.

    :param B: индукция магнитного поля в вакууме (Тл)
    :param angle: угол между вектором B и нормалью к поверхности (в градусах)
    :param mu: магнитная проницаемость магнетика (безразмерная)
    :return: магнитная индукция B' в магнетике (Тл)
    """
    angle_rad = math.radians(angle)  # Преобразование угла в радианы
    B_normal = B * math.cos(angle_rad)  # Нормальная составляющая поля
    B_tangential = B * math.sin(angle_rad)  # Тангенциальная составляющая поля

    # Индукция внутри магнетика
    B_normal_inside = B_normal / mu
    B_tangential_inside = B_tangential

    # Полный вектор индукции внутри магнетика
    B_inside = math.sqrt(B_normal_inside**2 + B_tangential_inside**2)
    return B_inside

# Исходные данные
B = 0.03  # Индукция в вакууме, Тл
angle = 45  # Угол в градусах
mu = 1000  # Магнитная проницаемость магнетика

# Вычисление
B_inside = calculate_magnetic_induction(B, angle, mu)

print(f"Магнитная индукция внутри магнетика: {B_inside:.4f} Тл")
