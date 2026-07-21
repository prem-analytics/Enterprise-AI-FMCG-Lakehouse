from utils.procurement_numbering import (
    generate_po_number,
    generate_grn_number,
    generate_supplier_invoice_number,
    generate_payment_number,
    generate_pr_number,
    reset_counters
)


def test_number_generation():

    reset_counters()

    print(generate_po_number())
    print(generate_po_number())

    print(generate_grn_number())

    print(generate_supplier_invoice_number())

    print(generate_payment_number())

    print(generate_pr_number())


if __name__ == "__main__":
    test_number_generation()