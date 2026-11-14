Allowed_statuses = {
    "order_status": ["Pending", "Shipped", "Delivered", "Cancelled"],
    "payment_status": ["Succeeded", "Pending", "Failed"],
    "shipment_status": ["Dispatched", "In Transit", "Delivery Attempt Failed", "Delivered"],
    "refund_status": ["Pending", "Processing", "Completed", "Rejected"],
}

def clean_status(value , allowed):
    if value is None or value.strip() == "":
        return {
            "original" : value,
           "clean" : None,
           "flag" : f"Missing status Value"
        }


    tidy = value.strip().lower()

    for status in allowed:
        if tidy == status.lower():
            return {
                 "original": value,
                "clean": status,
                "flag": None,
            }
    return {
        "original": value, 
        "clean": None, 
        "flag": f"invalid status: '{value}'"
    }


if __name__ == "__main__":
    test_values = [
        "Delivered",
        "  delivered ",
        "DELIVERED",
        "Delivred",
        None,
        "",
        "   ",
    
    ]

    allowed = Allowed_statuses["order_status"]

    for value in test_values:
        result = clean_status(value, allowed)
        print(result)


    