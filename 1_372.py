import math

def calculate_max_distance_and_height(h):
    """
    Вычисляет высоту отверстия и максимальное расстояние полёта струи из цилиндрического сосуда.

    :param h: высота сосуда (в метрах)
    :return: высота отверстия (в метрах) и максимальное расстояние (в метрах)
    """
    g = 9.81  # ускорение свободного падения, м/с^2

    # Оптимальная высота отверстия
    h_optimal = h / 2

    # Максимальное расстояние
    d_max = math.sqrt(h_optimal * (h - h_optimal) * 4 * h)

    return h_optimal, d_max

# Данные задачи
h_cm = 50  # Высота сосуда в см
h = h_cm / 100  # Перевод в метры

# Расчёт оптимальной высоты и максимального расстояния
h_optimal, d_max = calculate_max_distance_and_height(h)

# Вывод решения
print("Метод решения:")
print(f"1. Перевод высоты сосуда из сантиметров в метры: {h_cm} см = {h} м")
print("\n2. Оптимальная высота отверстия (h_optimal):")
print(f"   h_optimal = h / 2 = {h} / 2 = {h_optimal:.2f} м")
print("\n3. Максимальное расстояние полёта струи (d_max):")
print(f"   d_max = sqrt(h_optimal * (h - h_optimal) * 4 * h)")
print(f"   d_max = sqrt({h_optimal:.2f} * ({h} - {h_optimal:.2f}) * 4 * {h})")
print(f"   d_max = sqrt({h_optimal:.2f} * {h - h_optimal:.2f} * 4 * {h})")
print(f"   d_max = sqrt({h_optimal * (h - h_optimal) * 4 * h:.2f})")
print(f"   d_max = {math.sqrt(h_optimal * (h - h_optimal) * 4 * h):.2f} м")
print("\nРезультат:")
print(f"Оптимальная высота отверстия: {h_optimal:.2f} м")
print(f"Максимальное расстояние струи: {d_max:.2f} м")