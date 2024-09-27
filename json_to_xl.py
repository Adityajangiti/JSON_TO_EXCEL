import pandas as pd
import json

def json_to_excel(json_file, excel_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    df = pd.json_normalize(data)
    df.to_excel(excel_file, index=False)
    print(f"JSON data has been successfully converted to Excel format: {excel_file}")

#Example usage
json_file = "product_re‪view.json"
excel_file = "output.xlsx"

json_to_excel(json_file, excel_file)
