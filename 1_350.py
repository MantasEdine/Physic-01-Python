import math

def critical_frequency(radius_cm, density, tensile_strength, diameter_cm):
    # Перевод единиц измерения
    radius_m = radius_cm / 100  # Перевод радиуса из см в метры
    diameter_m = diameter_cm / 100  # Перевод диаметра из см в метры

    # Площадь поперечного сечения проволоки
    cross_section_area = math.pi * (diameter_m / 2) ** 2

    # Длина проволоки (окружность кольца)
    length = 2 * math.pi * radius_m

    # Масса кольца (плотность * объём)
    mass = density * cross_section_area * length

    # Критическая угловая скорость
    omega_critical = math.sqrt(tensile_strength / (mass / length))

    # Перевод угловой скорости в частоту вращения
    frequency_critical = omega_critical / (2 * math.pi)

    return frequency_critical

# Данные задачи
radius_cm = 25  # Радиус кольца в см
density = 11340  # Плотность свинца в кг/м^3
tensile_strength = 1.7e7  # Максимальное натяжение в Па
diameter_cm = 0.5  # Диаметр проволоки в см

# Расчёт критической частоты
critical_freq = critical_frequency(radius_cm, density, tensile_strength, diameter_cm)

# Вывод решения
print("Метод решения:")
print("1. Перевод всех единиц измерения в систему СИ:")
print(f"   - Радиус кольца: {radius_cm} см = {radius_cm / 100} м")
print(f"   - Диаметр проволоки: {diameter_cm} см = {diameter_cm / 100} м")
print(f"   - Плотность свинца: {density} кг/м^3")
print(f"   - Максимальное натяжение: {tensile_strength} Па")
print("\n2. Расчёт площади поперечного сечения проволоки:")
print(f"   Площадь = π * (диаметр/2)^2 = π * ({diameter_cm / 100} / 2)^2 = {math.pi * (diameter_cm / 200) ** 2:.6f} м^2")
print("\n3. Расчёт длины проволоки (окружности кольца):")
print(f"   Длина = 2 * π * радиус = 2 * π * {radius_cm / 100} = {2 * math.pi * (radius_cm / 100):.2f} м")
print("\n4. Расчёт массы кольца:")
print(f"   Масса = плотность * площадь * длина = {density} * {math.pi * (diameter_cm / 200) ** 2:.6f} * {2 * math.pi * (radius_cm / 100):.2f} = {density * math.pi * (diameter_cm / 200) ** 2 * 2 * math.pi * (radius_cm / 100):.2f} кг")
print("\n5. Расчёт критической угловой скорости:")
print(f"   Критическая угловая скорость = sqrt(натяжение / (масса / длина)) = sqrt({tensile_strength} / ({density * math.pi * (diameter_cm / 200) ** 2 * 2 * math.pi * (radius_cm / 100):.2f} / {2 * math.pi * (radius_cm / 100):.2f})) = {math.sqrt(tensile_strength / (density * math.pi * (diameter_cm / 200) ** 2 * 2 * math.pi * (radius_cm / 100) / (2 * math.pi * (radius_cm / 100)))):.2f} рад/с")
print("\n6. Перевод угловой скорости в частоту вращения:")
print(f"   Частота = угловая скорость / (2 * π) = {math.sqrt(tensile_strength / (density * math.pi * (diameter_cm / 200) ** 2 * 2 * math.pi * (radius_cm / 100) / (2 * math.pi * (radius_cm / 100)))):.2f} / (2 * π) = {critical_freq:.2f} Гц")
print("\nРезультат:")
print(f"Критическая частота вращения: {critical_freq:.2f} Гц")