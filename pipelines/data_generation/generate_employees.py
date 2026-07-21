"""
Employee Master Generator
Enterprise AI FMCG Lakehouse
"""

import random
from datetime import datetime

import pandas as pd

from configs.employee_master import (
    EMPLOYEE_COUNT,
)

from configs.job_profiles import JOB_PROFILES

from utils.employee_utils import (
    generate_employee_id,
    generate_employee_code,
    generate_name,
    generate_gender,
    generate_date_of_birth,
    generate_email,
    generate_phone,
    generate_address,
    generate_department,
    generate_designation,
    generate_employment_type,
    generate_joining_date,
    generate_status,
    generate_shift,
    generate_manager_id,
    generate_work_assignment,
)

from utils.pipeline_runner import run_pipeline

print("File loaded successfully")

def main():

    employees = []

    print("\nGenerating Employee Master...")

    for i in range(1, EMPLOYEE_COUNT + 1):

        # ==========================================================
        # BASIC INFORMATION
        # ==========================================================

        employee_id = generate_employee_id(i)

        employee_code = generate_employee_code()

        first_name, last_name = generate_name()

        gender = generate_gender()

        dob = generate_date_of_birth()

        email = generate_email(
            first_name,
            last_name
        )

        phone = generate_phone()

        address, city, state, postal_code = generate_address()

        # ==========================================================
        # ORGANIZATION
        # ==========================================================

        department = generate_department()

        designation = generate_designation(
            department
        )

        employment_type = generate_employment_type()

        joining_date = generate_joining_date()

        status = generate_status()

        shift = generate_shift()

        manager_id = generate_manager_id(i)

        # ==========================================================
        # JOB PROFILE
        # ==========================================================

        profile = JOB_PROFILES.get(designation)

        if profile:

            grade = profile["grade"]

            experience = random.randint(
                profile["experience"][0],
                profile["experience"][1]
            )

            salary = random.randint(
                profile["salary"][0],
                profile["salary"][1]
            )

        else:

            grade = None

            experience = 0

            salary = 0

        # ==========================================================
        # WORK LOCATION
        # ==========================================================

        (
            location_type,
            factory_id,
            warehouse_id,
            store_id
        ) = generate_work_assignment(
            department
        )

        # ==========================================================
        # EMPLOYEE RECORD
        # ==========================================================

        employee = {

            # -------------------------------
            # Primary Keys
            # -------------------------------

            "employee_id": employee_id,
            "employee_code": employee_code,

            # -------------------------------
            # Personal Information
            # -------------------------------

            "first_name": first_name,
            "last_name": last_name,
            "full_name": f"{first_name} {last_name}",

            "gender": gender,
            "date_of_birth": dob,

            "email": email,
            "phone": phone,

            # -------------------------------
            # Address
            # -------------------------------

            "address": address,
            "city": city,
            "state": state,
            "postal_code": postal_code,

            # -------------------------------
            # Employment
            # -------------------------------

            "department": department,
            "designation": designation,

            "grade": grade,

            "employment_type": employment_type,

            "joining_date": joining_date,

            "experience_years": experience,

            "annual_salary": salary,

            "employee_status": status,

            "shift": shift,

            "manager_id": manager_id,

            # -------------------------------
            # Work Assignment
            # -------------------------------

            "location_type": location_type,

            "factory_id": factory_id,

            "warehouse_id": warehouse_id,

            "store_id": store_id,

            # -------------------------------
            # Metadata
            # -------------------------------

            "created_at": datetime.now(),

            "updated_at": datetime.now(),

            "is_active": status == "Active"

        }

        employees.append(employee)
    
    # ==========================================================
    # CREATE DATAFRAME
    # ==========================================================

    df = pd.DataFrame(employees)

    print(f"\nGenerated {len(df):,} employees.")

    # ==========================================================
    # DEBUG NULL VALUES
    # ==========================================================

    print("\nNull values by column:")
    print(df.isnull().sum()[df.isnull().sum() > 0])

    print("\nTotal null values:", df.isnull().sum().sum())

    # ==========================================================
    # RUN PIPELINE
    # ==========================================================

    run_pipeline(
        dataframe=df,
        folder="master",
        filename="employees",
        id_column="employee_id",
        required_columns=[
            "employee_id",
            "employee_code",
            "full_name",
            "department",
            "designation",
            "email",
            "employee_status",
        ],
        nullable_columns=[
            "manager_id",
            "factory_id",
            "warehouse_id",
            "store_id",
        ],
        title="Employee Master Pipeline",
    )

if __name__ == "__main__":
    print("Starting Employee Generator...")
    main()