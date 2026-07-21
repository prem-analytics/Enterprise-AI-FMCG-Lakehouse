"""
Employee Utility Functions
Enterprise AI FMCG Lakehouse
"""

import random
import string
from pathlib import Path

import pandas as pd
from faker import Faker

from configs.employee_master import (
    COMPANY_EMAIL_DOMAIN,
    DEPARTMENTS,
    DESIGNATIONS,
    EMPLOYMENT_TYPES,
    EMPLOYEE_STATUS,
    SHIFTS,
    GRADES,
    MIN_SALARY,
    MAX_SALARY,
    MIN_EXPERIENCE,
    MAX_EXPERIENCE,
    PHONE_PREFIX,
)

from configs.designation_mapping import DESIGNATION_MAPPING

fake = Faker("en_IN")

# ==========================================================
# MASTER DATA PATHS
# ==========================================================

BASE_PATH = Path("data/generated")

FACTORY_FILE = BASE_PATH / "factories" / "factories.csv"
WAREHOUSE_FILE = BASE_PATH / "warehouses" / "warehouses.csv"
STORE_FILE = BASE_PATH / "stores" / "stores.csv"


# ==========================================================
# LOAD MASTER DATA
# ==========================================================

def load_master_data(file_path):
    """
    Safely load a master dataset.
    Returns an empty DataFrame if the file doesn't exist.
    """
    if file_path.exists():
        return pd.read_csv(file_path)

    return pd.DataFrame()


factories = load_master_data(FACTORY_FILE)
warehouses = load_master_data(WAREHOUSE_FILE)
stores = load_master_data(STORE_FILE)

# ==========================================================
# DEPARTMENT LOCATION MAPPING
# ==========================================================

DEPARTMENT_LOCATION = {

    # Factory
    "Manufacturing": "Factory",
    "Quality Assurance": "Factory",
    "Research & Development": "Factory",

    # Warehouse
    "Supply Chain": "Warehouse",
    "Procurement": "Warehouse",
    "Operations": "Warehouse",

    # Store
    "Sales": "Store",
    "Marketing": "Store",
    "Customer Service": "Store",

    # Head Office
    "Finance": "Head Office",
    "Human Resources": "Head Office",
    "Information Technology": "Head Office"
}


# ==========================================================
# Employee ID
# ==========================================================

def generate_employee_id(number: int) -> str:
    return f"EMP{number:06d}"


# ==========================================================
# Employee Code
# ==========================================================

def generate_employee_code() -> str:
    return "E" + "".join(random.choices(string.digits, k=7))


# ==========================================================
# Name
# ==========================================================

def generate_name():
    first_name = fake.first_name()
    last_name = fake.last_name()
    return first_name, last_name


# ==========================================================
# Gender
# ==========================================================

def generate_gender():
    return random.choice(["Male", "Female"])


# ==========================================================
# Date of Birth
# ==========================================================

def generate_date_of_birth():
    return fake.date_of_birth(
        minimum_age=21,
        maximum_age=60
    )


# ==========================================================
# Email
# ==========================================================

def generate_email(first_name, last_name):

    email = (
        f"{first_name}.{last_name}"
        .replace(" ", "")
        .replace("'", "")
        .lower()
    )

    return f"{email}@{COMPANY_EMAIL_DOMAIN}"


# ==========================================================
# Phone
# ==========================================================

def generate_phone():
    return f"{PHONE_PREFIX} {random.randint(6000000000, 9999999999)}"


# ==========================================================
# Address
# ==========================================================

def generate_address():

    return (
        fake.street_address(),
        fake.city(),
        fake.state(),
        fake.postcode(),
    )


# ==========================================================
# Department
# ==========================================================

def generate_department():
    return random.choice(DEPARTMENTS)


# ==========================================================
# Designation
# ==========================================================

def generate_designation(department):
    """
    Generate designation based on department.
    """

    designations = DESIGNATION_MAPPING.get(department)

    if designations:
        return random.choice(designations)

    return random.choice(DESIGNATIONS)


# ==========================================================
# Employment Type
# ==========================================================

def generate_employment_type():
    return random.choice(EMPLOYMENT_TYPES)


# ==========================================================
# Grade
# ==========================================================

def generate_grade():
    return random.choice(GRADES)


# ==========================================================
# Salary
# ==========================================================

def generate_salary():
    return random.randint(
        MIN_SALARY,
        MAX_SALARY
    )


# ==========================================================
# Experience
# ==========================================================

def generate_experience():
    return random.randint(
        MIN_EXPERIENCE,
        MAX_EXPERIENCE
    )


# ==========================================================
# Joining Date
# ==========================================================

def generate_joining_date():

    return fake.date_between(
        start_date="-15y",
        end_date="today"
    )


# ==========================================================
# Status
# ==========================================================

def generate_status():
    return random.choice(EMPLOYEE_STATUS)


# ==========================================================
# Shift
# ==========================================================

def generate_shift():
    return random.choice(SHIFTS)


# ==========================================================
# Manager ID
# ==========================================================

def generate_manager_id(employee_number: int):
    """
    First 10 employees are top-level managers.
    Others report to one of the previous employees.
    """

    if employee_number <= 10:
        return None

    manager_number = random.randint(
        1,
        employee_number - 1
    )

    return generate_employee_id(manager_number)


# ==========================================================
# Factory Assignment
# ==========================================================

def generate_factory_id():

    if factories.empty:
        return None

    row = factories.sample(1).iloc[0]

    return row["factory_id"]


# ==========================================================
# Warehouse Assignment
# ==========================================================

def generate_warehouse_id():

    if warehouses.empty:
        return None

    row = warehouses.sample(1).iloc[0]

    return row["warehouse_id"]


# ==========================================================
# Store Assignment
# ==========================================================

def generate_store_id():

    if stores.empty:
        return None

    row = stores.sample(1).iloc[0]

    return row["store_id"]


# ==========================================================
# Work Assignment
# ==========================================================

def generate_work_assignment(department):
    """
    Assign an employee based on department.

    Returns:
        location_type,
        factory_id,
        warehouse_id,
        store_id
    """

    location = DEPARTMENT_LOCATION.get(
        department,
        "Head Office"
    )

    if location == "Factory":

        return (
            location,
            generate_factory_id(),
            None,
            None
        )

    elif location == "Warehouse":

        return (
            location,
            None,
            generate_warehouse_id(),
            None
        )

    elif location == "Store":

        return (
            location,
            None,
            None,
            generate_store_id()
        )

    return (
        "Head Office",
        None,
        None,
        None
    )