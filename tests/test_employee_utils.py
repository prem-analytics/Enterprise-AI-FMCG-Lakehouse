"""
Unit Tests - Employee Utilities
Enterprise AI FMCG Lakehouse
"""

from utils.employee_utils import (
    generate_employee_id,
    generate_employee_code,
    generate_name,
    generate_gender,
    generate_email,
    generate_phone,
    generate_department,
    generate_designation,
    generate_employment_type,
    generate_grade,
    generate_salary,
    generate_experience,
    generate_status,
    generate_shift,
    generate_manager_id,
    generate_work_assignment,
)


def test_generate_employee_id():
    emp_id = generate_employee_id(1)

    assert emp_id == "EMP000001"


def test_generate_employee_code():
    code = generate_employee_code()

    assert code.startswith("E")
    assert len(code) == 8


def test_generate_name():
    first, last = generate_name()

    assert isinstance(first, str)
    assert isinstance(last, str)

    assert len(first) > 0
    assert len(last) > 0


def test_generate_gender():
    gender = generate_gender()

    assert gender in [
        "Male",
        "Female"
    ]


def test_generate_email():
    email = generate_email(
        "Prem",
        "Jaguar"
    )

    assert "@enterprisefmcg.com" in email


def test_generate_phone():
    phone = generate_phone()

    assert phone.startswith("+91")


def test_generate_department():
    department = generate_department()

    assert isinstance(
        department,
        str
    )


def test_generate_designation():
    designation = generate_designation()

    assert isinstance(
        designation,
        str
    )


def test_generate_employment_type():
    employment = generate_employment_type()

    assert isinstance(
        employment,
        str
    )


def test_generate_grade():
    grade = generate_grade()

    assert isinstance(
        grade,
        str
    )


def test_generate_salary():
    salary = generate_salary()

    assert salary >= 300000
    assert salary <= 3000000


def test_generate_experience():
    exp = generate_experience()

    assert exp >= 0
    assert exp <= 35


def test_generate_status():
    status = generate_status()

    assert isinstance(
        status,
        str
    )


def test_generate_shift():
    shift = generate_shift()

    assert isinstance(
        shift,
        str
    )


def test_generate_manager():
    manager = generate_manager_id(100)

    assert manager.startswith("EMP")


def test_ceo_has_no_manager():
    manager = generate_manager_id(1)

    assert manager is None


def test_work_assignment_factory():

    (
        location,
        factory,
        warehouse,
        store
    ) = generate_work_assignment(
        "Manufacturing"
    )

    assert location == "Factory"

    assert warehouse is None
    assert store is None


def test_work_assignment_warehouse():

    (
        location,
        factory,
        warehouse,
        store
    ) = generate_work_assignment(
        "Supply Chain"
    )

    assert location == "Warehouse"

    assert factory is None
    assert store is None


def test_work_assignment_store():

    (
        location,
        factory,
        warehouse,
        store
    ) = generate_work_assignment(
        "Sales"
    )

    assert location == "Store"

    assert factory is None
    assert warehouse is None


def test_work_assignment_headoffice():

    (
        location,
        factory,
        warehouse,
        store
    ) = generate_work_assignment(
        "Finance"
    )

    assert location == "Head Office"

    assert factory is None
    assert warehouse is None
    assert store is None


if __name__ == "__main__":

    print("Running Employee Utility Tests...\n")

    test_generate_employee_id()
    test_generate_employee_code()
    test_generate_name()
    test_generate_gender()
    test_generate_email()
    test_generate_phone()
    test_generate_department()
    test_generate_designation()
    test_generate_employment_type()
    test_generate_grade()
    test_generate_salary()
    test_generate_experience()
    test_generate_status()
    test_generate_shift()
    test_generate_manager()
    test_ceo_has_no_manager()
    test_work_assignment_factory()
    test_work_assignment_warehouse()
    test_work_assignment_store()
    test_work_assignment_headoffice()

    print("All Employee Utility Tests Passed Successfully.")