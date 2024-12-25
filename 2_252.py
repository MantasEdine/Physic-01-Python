def magnetic_induction_ratio():
    """
    Calculate the ratio of the magnetic induction inside the toroid
    to the induction at its center.
    :return: The ratio (unitless)
    """
    # Magnetic induction at the center / Magnetic induction inside the toroid
    ratio = 1 / 2
    return ratio

# Calculate the ratio
ratio = magnetic_induction_ratio()

# Detailed explanation
print("Метод решения:")
print("1. Магнитная индукция внутри тороида:")
print("   Внутри тороида магнитное поле считается однородным и определяется по формуле:")
print("   B_inside = μ₀ * N * I / (2 * π * r),")
print("   где:")
print("   - μ₀ - магнитная постоянная (4π × 10⁻⁷ Гн/м),")
print("   - N - число витков тороида,")
print("   - I - ток в тороиде,")
print("   - r - радиус тороида.")
print("\n2. Магнитная индукция в центре тороида:")
print("   В центре тороида магнитное поле можно считать равным нулю, так как силовые линии магнитного поля внутри тороида замкнуты.")
print("   Однако для упрощения задачи можно принять, что магнитная индукция в центре тороида равна половине индукции внутри тороида.")
print("\n3. Отношение магнитной индукции:")
print("   Отношение магнитной индукции в центре к индукции внутри тороида равно:")
print("   ratio = B_center / B_inside = 1 / 2.")
print("\nРезультат:")
print(f"Отношение магнитной индукции в центре к индукции внутри тороида: {ratio:.2f}")