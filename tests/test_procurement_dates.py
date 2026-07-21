from utils.procurement_dates import *

order = generate_order_date()

delivery = generate_expected_delivery_date(order)

receipt = generate_receipt_date(delivery)

invoice = generate_invoice_date(receipt)

due = generate_due_date(
    invoice,
    "Net 30"
)

payment = generate_payment_date(due)

print("Order      :", order.date())
print("Delivery   :", delivery.date())
print("Receipt    :", receipt.date())
print("Invoice    :", invoice.date())
print("Due        :", due.date())
print("Payment    :", payment.date())