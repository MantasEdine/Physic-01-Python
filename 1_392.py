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

def reynolds_ratio(a, delta_x):
    """
    Вычисляет отношение чисел Рейнольдса в сечениях, отстоящих друг от друга на delta_x.

    :param a: коэффициент экспоненциального уменьшения радиуса, м⁻¹
    :param delta_x: расстояние между сечениями, м
    :return: отношение чисел Рейнольдса
    """
    r1 = math.exp(-a * 0)  # Радиус в первом сечении (x = 0)
    r2 = math.exp(-a * delta_x)  # Радиус во втором сечении (x = delta_x)

    ratio = (r1 / r2) ** 4  # Отношение чисел Рейнольдса

    return ratio

# Данные задачи
h_cm = 50  # Высота сосуда в см
h = h_cm / 100  # Перевод в метры

# Расчёт оптимальной высоты и максимального расстояния
h_optimal, d_max = calculate_max_distance_and_height(h)

# Вывод решения для максимального расстояния и высоты отверстия
print("Метод решения для максимального расстояния и высоты отверстия:")
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

# Данные для чисел Рейнольдса
a = 0.50  # Коэффициент уменьшения радиуса, м⁻¹
delta_x = 3.2  # Расстояние между сечениями, м

# Расчёт отношения чисел Рейнольдса
re_ratio = reynolds_ratio(a, delta_x)

# Вывод решения для отношения чисел Рейнольдса
print("\nМетод решения для отношения чисел Рейнольдса:")
print(f"1. Радиус в первом сечении (x = 0):")
print(f"   r1 = exp(-a * 0) = exp(-{a} * 0) = {math.exp(-a * 0):.2f}")
print(f"2. Радиус во втором сечении (x = delta_x):")
print(f"   r2 = exp(-a * delta_x) = exp(-{a} * {delta_x}) = {math.exp(-a * delta_x):.2f}")
print(f"3. Отношение чисел Рейнольдса:")
print(f"   ratio = (r1 / r2)^4 = ({math.exp(-a * 0):.2f} / {math.exp(-a * delta_x):.2f})^4")
print(f"   ratio = ({math.exp(-a * 0) / math.exp(-a * delta_x):.2f})^4")
print(f"   ratio = {re_ratio:.2f}")
print("\nРезультат:")
print(f"Отношение чисел Рейнольдса: {re_ratio:.2f}")