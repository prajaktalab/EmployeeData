from employee import employee_info

def test_employee_info():
    result = employee_info("Andrew", 101, "IT", 30000)

    expected = (
        "Employee Name: Andrew\n"
        "Employee ID: 101\n"
        "Department: IT\n"
        "Salary: 70000"
    )

    assert result == expected