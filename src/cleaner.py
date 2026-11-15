from loaders import load_all

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

def clean_status_column(rows, id_column, status_column, allowed):
    results = []

    for row in rows:
        status_value = row.get(status_column, "")
        checked = clean_status(status_value ,allowed)

        entry = {
            "record_id" : row[id_column],
            "column" : status_column,
            "original": checked["original"],
            "clean" : checked["clean"],
            "flag" : checked["flag"]
        }
        results.append(entry)
    return results


    