import csv


def load_csv(file_path):
    problems = []
    rows = []
    try:
        with open(file_path, "r" ,newline = "", encoding = "utf-8") as file: 
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                 problems.append(f"file is empty : {file_path}")
            else:
                 rows = list(reader)
                 if not rows:
                      problems.append(f"file has no data rows : {file_path}")            
    except FileNotFoundError:
            problems.append(f"file not found : {file_path}")

    return {"rows": rows , "problems" : problems}
            
            

if __name__ == "__main__":
    print(load_csv("data/orders1.csv"))

