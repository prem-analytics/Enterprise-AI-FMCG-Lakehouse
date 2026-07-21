from utils.procurement_validation import *

validate_quantity(100)

validate_unit_price(125)

validate_status("Approved")

validate_approval("Approved")

validate_shipping("Road")

validate_payment_terms("Net 30")

validate_gst(18)

validate_total(100000)

print("All Procurement Validation Tests Passed")