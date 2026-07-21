"""
Job Profiles Configuration
Enterprise AI FMCG Lakehouse

Each designation defines:
- Grade
- Experience Range (Years)
- Annual Salary Range (INR)
"""

JOB_PROFILES = {

    # ======================================================
    # SALES
    # ======================================================

    "Sales Trainee": {
        "grade": "G1",
        "experience": (0, 1),
        "salary": (300000, 400000)
    },

    "Sales Executive": {
        "grade": "G2",
        "experience": (1, 3),
        "salary": (400000, 600000)
    },

    "Senior Sales Executive": {
        "grade": "G3",
        "experience": (3, 6),
        "salary": (650000, 900000)
    },

    "Area Sales Manager": {
        "grade": "M1",
        "experience": (6, 10),
        "salary": (900000, 1400000)
    },

    "Regional Sales Manager": {
        "grade": "M2",
        "experience": (10, 15),
        "salary": (1500000, 2200000)
    },

    "National Sales Manager": {
        "grade": "D1",
        "experience": (15, 25),
        "salary": (2200000, 3200000)
    },

    # ======================================================
    # MARKETING
    # ======================================================

    "Marketing Executive": {
        "grade": "G2",
        "experience": (1, 3),
        "salary": (400000, 600000)
    },

    "Digital Marketing Executive": {
        "grade": "G2",
        "experience": (1, 3),
        "salary": (450000, 650000)
    },

    "Brand Executive": {
        "grade": "G3",
        "experience": (3, 6),
        "salary": (650000, 900000)
    },

    "Brand Manager": {
        "grade": "M1",
        "experience": (6, 10),
        "salary": (1000000, 1500000)
    },

    "Marketing Manager": {
        "grade": "M2",
        "experience": (10, 15),
        "salary": (1500000, 2200000)
    },

    "Marketing Director": {
        "grade": "D1",
        "experience": (15, 25),
        "salary": (2200000, 3200000)
    },

    # ======================================================
    # FINANCE
    # ======================================================

    "Accounts Executive": {
        "grade": "G2",
        "experience": (1, 3),
        "salary": (400000, 600000)
    },

    "Accountant": {
        "grade": "G3",
        "experience": (2, 5),
        "salary": (500000, 750000)
    },

    "Senior Accountant": {
        "grade": "G4",
        "experience": (5, 8),
        "salary": (750000, 1000000)
    },

    "Finance Analyst": {
        "grade": "G4",
        "experience": (4, 7),
        "salary": (700000, 1100000)
    },

    "Finance Manager": {
        "grade": "M2",
        "experience": (8, 15),
        "salary": (1300000, 1800000)
    },

    "Finance Director": {
        "grade": "D1",
        "experience": (15, 25),
        "salary": (2200000, 3200000)
    },

    # ======================================================
    # HR
    # ======================================================

    "HR Executive": {
        "grade": "G2",
        "experience": (1, 3),
        "salary": (400000, 600000)
    },

    "HR Business Partner": {
        "grade": "G4",
        "experience": (4, 8),
        "salary": (700000, 1000000)
    },

    "HR Manager": {
        "grade": "M2",
        "experience": (8, 12),
        "salary": (1200000, 1700000)
    },

    "Senior HR Manager": {
        "grade": "M3",
        "experience": (12, 18),
        "salary": (1800000, 2400000)
    },

    "HR Director": {
        "grade": "D1",
        "experience": (18, 25),
        "salary": (2500000, 3200000)
    },

    # ======================================================
    # IT
    # ======================================================

    "Software Engineer": {
        "grade": "G2",
        "experience": (1, 3),
        "salary": (500000, 800000)
    },

    "Senior Software Engineer": {
        "grade": "G4",
        "experience": (4, 7),
        "salary": (900000, 1400000)
    },

    "System Analyst": {
        "grade": "G5",
        "experience": (6, 9),
        "salary": (1200000, 1700000)
    },

    "Tech Lead": {
        "grade": "M2",
        "experience": (8, 12),
        "salary": (1600000, 2200000)
    },

    "IT Manager": {
        "grade": "M3",
        "experience": (10, 15),
        "salary": (1800000, 2500000)
    },

    "IT Director": {
        "grade": "D1",
        "experience": (15, 25),
        "salary": (2500000, 3500000)
    },

    # ======================================================
    # SUPPLY CHAIN
    # ======================================================

    "Supply Chain Executive": {
        "grade": "G2",
        "experience": (1, 3),
        "salary": (450000, 650000)
    },

    "Supply Chain Analyst": {
        "grade": "G3",
        "experience": (3, 6),
        "salary": (650000, 900000)
    },

    "Supply Chain Manager": {
        "grade": "M2",
        "experience": (8, 12),
        "salary": (1400000, 1900000)
    },

    "Supply Chain Head": {
        "grade": "D1",
        "experience": (15, 25),
        "salary": (2400000, 3300000)
    },

    # ======================================================
    # PROCUREMENT
    # ======================================================

    "Procurement Executive": {
        "grade": "G2",
        "experience": (1, 3),
        "salary": (450000, 650000)
    },

    "Senior Procurement Executive": {
        "grade": "G3",
        "experience": (3, 6),
        "salary": (700000, 950000)
    },

    "Procurement Manager": {
        "grade": "M2",
        "experience": (8, 12),
        "salary": (1300000, 1800000)
    },

    "Strategic Sourcing Manager": {
        "grade": "M3",
        "experience": (10, 15),
        "salary": (1700000, 2400000)
    },

    # ======================================================
    # MANUFACTURING
    # ======================================================

    "Production Operator": {
        "grade": "G1",
        "experience": (0, 2),
        "salary": (250000, 350000)
    },

    "Production Technician": {
        "grade": "G2",
        "experience": (2, 4),
        "salary": (350000, 500000)
    },

    "Production Engineer": {
        "grade": "G3",
        "experience": (3, 6),
        "salary": (600000, 900000)
    },

    "Production Supervisor": {
        "grade": "M1",
        "experience": (6, 10),
        "salary": (900000, 1300000)
    },

    "Production Manager": {
        "grade": "M2",
        "experience": (10, 15),
        "salary": (1500000, 2200000)
    },

    "Plant Head": {
        "grade": "D1",
        "experience": (15, 25),
        "salary": (2500000, 3800000)
    },

    # ======================================================
    # QUALITY ASSURANCE
    # ======================================================

    "QA Executive": {
        "grade": "G2",
        "experience": (1, 3),
        "salary": (400000, 600000)
    },

    "QA Engineer": {
        "grade": "G3",
        "experience": (3, 5),
        "salary": (600000, 850000)
    },

    "Senior QA Engineer": {
        "grade": "G4",
        "experience": (5, 8),
        "salary": (850000, 1200000)
    },

    "QA Manager": {
        "grade": "M2",
        "experience": (8, 12),
        "salary": (1400000, 1900000)
    },

    "Quality Head": {
        "grade": "D1",
        "experience": (15, 25),
        "salary": (2500000, 3500000)
    },

    # ======================================================
    # OPERATIONS
    # ======================================================

    "Operations Executive": {
        "grade": "G2",
        "experience": (1, 3),
        "salary": (400000, 600000)
    },

    "Operations Analyst": {
        "grade": "G3",
        "experience": (3, 5),
        "salary": (600000, 850000)
    },

    "Operations Manager": {
        "grade": "M2",
        "experience": (8, 12),
        "salary": (1400000, 1900000)
    },

    "Operations Head": {
        "grade": "D1",
        "experience": (15, 25),
        "salary": (2500000, 3500000)
    },

    # ======================================================
    # RESEARCH & DEVELOPMENT
    # ======================================================

    "Research Associate": {
        "grade": "G2",
        "experience": (1, 3),
        "salary": (500000, 700000)
    },

    "Research Scientist": {
        "grade": "G4",
        "experience": (4, 7),
        "salary": (800000, 1200000)
    },

    "Senior Scientist": {
        "grade": "G5",
        "experience": (7, 10),
        "salary": (1200000, 1800000)
    },

    "R&D Manager": {
        "grade": "M2",
        "experience": (10, 15),
        "salary": (1800000, 2500000)
    },

    "R&D Director": {
        "grade": "D1",
        "experience": (15, 25),
        "salary": (2800000, 3800000)
    },

    # ======================================================
    # CUSTOMER SERVICE
    # ======================================================

    "Customer Support Executive": {
        "grade": "G2",
        "experience": (1, 3),
        "salary": (350000, 500000)
    },

    "Senior Customer Support Executive": {
        "grade": "G3",
        "experience": (3, 6),
        "salary": (500000, 700000)
    },

    "Customer Success Manager": {
        "grade": "M2",
        "experience": (8, 12),
        "salary": (1200000, 1800000)
    },

    "Customer Service Head": {
        "grade": "D1",
        "experience": (15, 25),
        "salary": (2200000, 3200000)
    }

}