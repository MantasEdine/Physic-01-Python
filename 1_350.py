import math

def critical_frequency(radius_cm, density, tensile_strength, diameter_cm):
    # Константы
    radius_m = radius_cm / 100  # Перевод радиуса в метры
    diameter_m = diameter_cm / 100  # Перевод диаметра в метры

    # Площадь поперечного сечения проволоки
    cross_section_area = math.pi * (diameter_m / 2) ** 2

    # Масса кольца (объём = площадь поперечного сечения * длина)
    length = 2 * math.pi * radius_m  # Длина проволоки
    mass = density * cross_section_area * length

    # Критическая угловая скорость
    omega_critical = math.sqrt(tensile_strength / (mass / length))

    # Перевод в частоту вращения
    frequency_critical = omega_critical / (2 * math.pi)

    return frequency_critical

# Данные задачи
radius_cm = 25  # Радиус кольца в см
density = 11340  # Плотность свинца в кг/м^3
tensile_strength = 1.7e7  # Максимальное натяжение в Па
diameter_cm = 0.5  # Диаметр проволоки в см

# Расчёт критической частоты
critical_freq = critical_frequency(radius_cm, density, tensile_strength, diameter_cm)

print(f"Критическая частота вращения: {critical_freq:.2f} Гц")
