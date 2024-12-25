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

# Вывод решения
print("Метод решения:")
print("1. Разложение магнитной индукции на нормальную и тангенциальную составляющие:")
print(f"   Угол = {angle}°, угол в радианах = {math.radians(angle):.2f} рад")
print(f"   Нормальная составляющая: B_normal = B * cos(угол) = {B} * cos({math.radians(angle):.2f}) = {B * math.cos(math.radians(angle)):.4f} Тл")
print(f"   Тангенциальная составляющая: B_tangential = B * sin(угол) = {B} * sin({math.radians(angle):.2f}) = {B * math.sin(math.radians(angle)):.4f} Тл")
print("\n2. Вычисление индукции внутри магнетика:")
print(f"   Нормальная составляющая внутри магнетика: B_normal_inside = B_normal / μ = {B * math.cos(math.radians(angle)):.4f} / {mu} = {B * math.cos(math.radians(angle)) / mu:.4f} Тл")
print(f"   Тангенциальная составляющая внутри магнетика: B_tangential_inside = B_tangential = {B * math.sin(math.radians(angle)):.4f} Тл")
print("\n3. Вычисление полного вектора индукции внутри магнетика:")
print(f"   B_inside = sqrt(B_normal_inside² + B_tangential_inside²)")
print(f"   B_inside = sqrt({(B * math.cos(math.radians(angle)) / mu)**2:.4e} + {(B * math.sin(math.radians(angle)))**2:.4e})")
print(f"   B_inside = {math.sqrt((B * math.cos(math.radians(angle)) / mu)**2 + (B * math.sin(math.radians(angle)))**2):.4f} Тл")
print("\nРезультат:")
print(f"Магнитная индукция внутри магнетика: {B_inside:.4f} Тл")