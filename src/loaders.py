import csv

Required_columns = {
     "orders" :["order_id", "customer_id", "order_date", "order_status", "order_amount", "currency"],
     "payments" : ["payment_id", "order_id", "payment_date", "payment_amount", "payment_status", "currency"],
     "refunds" : ["refund_id","order_id","payment_id","refund_date","refund_amount","refund_status","currency"],
     "shipments" : ["shipment_event_id","order_id","event_date","shipment_status","notes"],
     "support_history" : ["support_message_id","order_id","message_date","agent_id","message_text"],
}


def load_csv(file_path , required_columns):
    problems = []
    rows = []
    try:
        with open(file_path, "r" ,newline = "", encoding = "utf-8") as file: 
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                 problems.append(f"file is empty : {file_path}")
            else:
                 missing = [c for c in required_columns if c not in reader.fieldnames]
                 if missing: 
                      problems.append(f"missing columns {missing} in {file_path}")
                 else:     
                      rows = list(reader)
                      if not rows:
                            problems.append(f"file has no data rows : {file_path}") 
                             
                
                        
    except FileNotFoundError:
            problems.append(f"file not found : {file_path}")

    return {"rows": rows , "problems" : problems}
            
            

# if __name__ == "__main__":
#     print(load_csv("data/orders.csv" , Required_columns["orders"]))
def load_all(data_folder):
    results = {}         

    for name in Required_columns:
        path = f"{data_folder}/{name}.csv"      
        columns = Required_columns[name]                          
        results[name] = load_csv(path , columns)                   
    return results

if __name__ == "__main__":
     all_data = load_all("data")
     print(all_data)