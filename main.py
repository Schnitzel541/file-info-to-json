import os
import datetime
import fitz
import json

file_path = str(input("Please insert file path: "))

data_list = []

# Obtaining the data
file_size = os.path.getsize(file_path)
file_name = os.path.basename(file_path)
file_type = os.path.splitext(file_path)
creation_timestamp = os.path.getctime(file_path)
modification_timestamp = os.path.getmtime(file_path)

# Datetime conversion/formatting
dtc = datetime.datetime.fromtimestamp(creation_timestamp, datetime.timezone.utc)
created_at = dtc.strftime("%d-%m-%Y %H:%M")

dtm = datetime.datetime.fromtimestamp(modification_timestamp, datetime.timezone.utc)
modified_at = dtm.strftime("%d-%m-%Y %H:%M")

data = {
    "file_name": file_name,
    "file_size (bytes)": file_size,
    "file_type": file_type[1],
    "creation_date": created_at,
    "last_modified_at": modified_at,
    }
data_list.append(data)


# Check to see if the file is a PDF file
if file_type[1] == ".pdf":
    pdf_document = fitz.open(file_path)
    metadata = pdf_document.metadata
    pdf_document.close
    data_list.append(metadata)
    print(data_list)
    export_to_json = str(input("Would you like to export this file to JSON? (Y/N): "))
    
    if export_to_json == "Y":
        with open("metadata.json", "w") as json_file:
            json.dump(data_list, json_file)
else:
    print(data_list)
    export_to_json = str(input("Would you like to export this file to JSON? (Y/N)"))
    
    if export_to_json == "Y":
        with open("metadata.json", "w") as json_file:
            json.dump(data_list, json_file)