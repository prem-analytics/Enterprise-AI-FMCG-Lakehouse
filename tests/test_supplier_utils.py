from utils.supplier_utils import *

print("Testing Supplier Utility\n")

for _ in range(10):

    name = random_supplier_name()

    print({

        "Supplier": name,

        "Type": random_supplier_type(),

        "Email": random_supplier_email(name),

        "Phone": random_supplier_phone(),

        "Payment": random_payment_term(),

        "Currency": random_currency(),

        "Rating": random_supplier_rating(),

        "Lead Time": random_lead_time(),

        "Preferred": random_preferred_supplier(),

        "PAN": random_pan(),

        "GSTIN": random_gstin(),

        "Status": random_supplier_status()

    })