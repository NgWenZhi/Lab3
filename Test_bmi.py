import Lab2.bmi as bmi  # adjust this import if your Lab2 folder has a different name

def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.73, 50)  # BMI ≈ 16.7
    assert result == -1

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.73, 68)  # BMI ≈ 22.7
    assert result == 0

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.73, 80)  # BMI ≈ 26.7
    assert result == 1