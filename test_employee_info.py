import employee_info as EInfo
from employee_info import employee_data as EData


def test_calc_average_salary():
    expected_result = 60166.67
    test_result = EInfo.calculate_average_salary()
    assert (test_result == expected_result)

def test_get_employees_by_dept():
    expected_result = [EData[0], EData[-1]]
    test_result = EInfo.get_employees_by_dept("Sales")
    assert (test_result == expected_result)

def test_get_employees_by_dept():
    expected_result = [EData[1], EData[2]]
    test_result = EInfo.get_employees_by_dept("Marketing")
    assert (test_result == expected_result)

def test_get_employees_by_age_range():
    expected_result = [EData[0], EData[4]]
    age_lower_limit = 26
    age_upper_limit = 33
    test_result = EInfo.get_employees_by_age_range(age_lower_limit, age_upper_limit)
    assert (test_result == expected_result)