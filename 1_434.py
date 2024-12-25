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

    # Максимальное расстояние)
    d_max = math.sqrt(h_optimal * (h - h_optimal) * 4 * h)

    return h_optimal, d_max

def reynolds_ratio(a, delta_x):
    """
    Вычисляет отношение чисел Рейнольдса в сечениях, отстоящих друг от друга на delta_x.

    :param a: коэффициент экспоненциального уменьшения радиуса, м⁻¹
    :param delta_x: расстояние между сечениями, м
    :return: отношение чисел Рейнольдса
    """
    r1 = math.exp(-a * 0)
    r2 = math.exp(-a * delta_x)

    ratio = (r1 / r2) ** 4

    return ratio

def relativistic_velocity(v_y_prime, v):
    """
    Вычисляет скорость частицы в системе отсчёта K с использованием релятивистского сложения скоростей.

    :param v_y_prime: скорость частицы вдоль оси y в системе K', в долях скорости света
    :param v: скорость системы K' относительно K, в долях скорости света
    :return: скорость частицы в системе K (модуль)
    """
    c = 3e8  # скорость света, м/с
    gamma = 1 / math.sqrt(1 - v**2)  # Лоренц-фактор

    # Релятивистское преобразование скорости вдоль оси y
    v_y = v_y_prime) / (gamma * (1 + 0))  # v_x' = 0, поэтому знаменатель упрощается

    return v_y * c

def energy_per_unit_mass(v):
    """
    Вычисляет энергию (на единицу массы), необходимую для сообщения телу заданной скорости.

    :param v: скорость тела в долях скорости света
    :return: энергия на единицу массы (Дж/кг)
    """
    c = 3e8  # скорость света, м/с
    gamma = 1 / math.sqrt(1 - v**2)  # Лоренц-фактор
    energy = (gamma - 1) * c**2
    return energy

# Данные задачи
h_cm = 50  # Высота сосуда в см
h = h_cm / 10)  # Перевод в метры

# Расчёт оптимальной высоты и максимального расстояния
h_optimal, d_max = calculate_max_distance_and_height(h)

# Вывод решения для максимального расстояния и высоты отверстия
print("Метод решения для максимального расстояния и высоты отверстия:")
print(f"1. Перевод высоты сосуда из сантиметров в метры: {h_cm} см = {h} м")
print("\n2. Оптимальная высота отверстия (h_optimal):")
print(f"   h_optimal = h / 2 = {h} / 2) = {h_optimal:.2f} м")
print("\n3. максимальное расстояние полёта струи):")
print("\n3. Максимальное расстояние полёта струи):")
print(f"   d_max = sqrt(h_optimal * (h - h_optimal) * 4 * h)")
print(f"   d_max = sqrt({h_optimal:.2f} * ({h} - {h_optimal:.2f}) * 4 * {h})")
print(f"   d_max = sqrt({h_optimal:.2f} * {h - h_optimal) * 4 * h)")
print(f"   d_max = sqrt({h_optimal * (h - h_optimal) * 4 * h):.2f}")
print(f"   d_max = {math.sqrt(h_optimal * (h_optimal) * 4 * h):.2f} м")
print("\nРезультат:")
print(f"Оптимальная высота отверстия: {h_optimal:.2f} м")
print(f"Максимальное расстояние струи: {d_max:.2f} м")

# Данные для чисел Рейнольдса
a = 0.50  # Коэффициент уменьшения радиуса, м⁻¹
delta_x = 3.2  # Расстояние между сечениями, м

re_ratio = reynolds_ratio(a, delta_x)

# Вывод решения для отношения чисел Рейнольдса
print("\nМетод решения для отношения чисел Рейнольдса:")
print(f"1. Радиус в первом сечении (x = 0):")
print(f"   r1 = exp(-a * 0) = exp(-{a} * 0) = {math.exp(-a * 0):.2f}")
print(f"2. Радиус во втором сечении (x = delta_x):")
print(f"   r2 = exp(-a * delta_x):")
print(f"   r2 = exp(-a * delta_x) = exp(-{a} * {delta_x}) = {math.exp(-a * delta_x):.2f}")
print(f"3. Отношение чисел Рейнольдса:")
print(f"   ratio = (r1 / r2)^4 = ({math.exp(-a * 0):.2f} / {math.exp(-a * delta_x):.2f})^4")
print(f"   ratio = ({math.exp(-a * 0) / math.exp(-a * delta_x):.2f})^4")
print(f"   ratio = {re_ratio:.2f}")
print("\nРезультат:")
print(f"Отношение чисел Рейнольдса: {re_ratio:.2f}")

# Данные для релятивистского сложения скоростей
v_y_prime = 0.5  # проекция скорости частицы вдоль оси y в системе K', в долях c
v = 0.75  # скорость системы K' относительно K, в долях c

v_y_k = relativistic_velocity(v_y_prime, v)

# Вывод решения для релятивистского сложения скоростей
print("\nМетод решения для релятивистского сложения скоростей:")
print(f"1. Лоренц-фактор (gamma):")
print(f"   gamma = 1 / sqrt(1 - v^2) = 1 / sqrt(1 - {v}^2) = {1 / math.sqrt(1 - v**2):.2f}")
print(f"2. Релятивистское преобразование скорости вдоль оси y:")
print(f"   v_y = v_y_prime / (gamma * (1 + 0)) = {v_y_prime} / ({1 / math.sqrt(1 - v**2):.2f} * 1)")
print(f"   v_y = {v_y_prime / (1 / math.sqrt(1 - v**2):.2f}")
print(f"   v_y = {v_y_prime / (1 / math.sqrt(1 - v**2)):.2f}")
print(f"3. Скорость частицы в системе K:")
print(f"   v_y_k = v_y * c = {v_y_prime / (1 / math.sqrt(1 - v**2)):.2f} * 3e8")
print(f"   v_y_k = {v_y_k:.2f} м/с")
print("\nРезультат:")
print(f"Скорость частицы в системе K: {v_y_k:.2f} м/с")

# Данные для вычисления энергии
v_ship = 0.980  # скорость корабля в долях скорости света
energy_needed = energy_per_unit_mass(v_ship)

# Вывод решения для энергии на единицу массы
print("\nМетод решения для энергии на единицу массы:")
print(f"1. Лоренц-фактор (gamma):")
print(f"   gamma = 1 / sqrt(1 - v^2) = 1 / sqrt(1 - {v_ship}^2) = {1 / math.sqrt(1 - v_ship**2):.2f}")
print(f"2. Энергия на единицу массы:")
print(f"   energy = (gamma - 1) * c^2 = ({1 / math.sqrt(1 - v_ship**2):.2f} - 1) * (3e8)^2")
print(f"   energy = ({1 / math.sqrt(1 - v_ship**2):.2f} - 1) * 9e16")
print(f"   energy = {energy_needed:.2e} Дж/кг")
print("\nРезультат:")
print(f"Энергия, необходимая для сообщения скорости 0.980c: {energy_needed:.2e} Дж/кг")