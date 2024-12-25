import math

def calculate_force(chi, A, B, mu_0):
    """
    Вычисляет силу, действующую на стержень в магнитном поле.

    :param chi: магнитная восприимчивость материала
    :param A: площадь поперечного сечения стержня (м²)
    :param B: магнитная индукция (Тл)
    :param mu_0: магнитная постоянная (Гн/м)
    :return: сила (Н)
    """
    # Сила, действующая на стержень
    F = (chi * A / mu_0) * B**2
    return F

# Данные задачи
chi = 0.01  # восприимчивость парамагнетика
A = 5e-4  # площадь поперечного сечения стержня (м²)
B = 0.1  # магнитная индукция в центре катушки (Тл)
mu_0 = 4 * math.pi * 1e-7  # магнитная постоянная (Гн/м)

# Вычисление силы
force = calculate_force(chi, A, B, mu_0)

# Вывод решения
print("Метод решения:")
print("1. Формула для силы, действующей на стержень в магнитном поле:")
print("   F = (χ * A / μ₀) * B²,")
print("   где:")
print("   - χ - магнитная восприимчивость материала,")
print("   - A - площадь поперечного сечения стержня (м²),")
print("   - B - магнитная индукция (Тл),")
print("   - μ₀ - магнитная постоянная (Гн/м).")
print("\n2. Подстановка значений:")
print(f"   χ = {chi},")
print(f"   A = {A} м²,")
print(f"   B = {B} Тл,")
print(f"   μ₀ = {mu_0:.2e} Гн/м.")
print("\n3. Вычисление силы:")
print(f"   F = (χ * A / μ₀) * B² = ({chi} * {A} / {mu_0:.2e}) * {B}²")
print(f"   F = ({chi * A / mu_0:.2e}) * {B**2}")
print(f"   F = {force:.2e} Н")
print("\nРезультат:")
print(f"Сила, действующая на стержень: {force:.2e} Н")