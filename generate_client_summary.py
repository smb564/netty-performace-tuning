import sys
import json
import os
import csv

folder_name = sys.argv[1] if sys.argv[1][-1] == "/" else sys.argv[1] + "/"
case_name = sys.argv[2]

# read the summary json from std-input
data = json.loads(sys.stdin.read())["HTTP Request"]

# update the client_summary.csv in the parent folder
# check whether summary file exists
if not os.path.exists(folder_name + "client_summary.csv"):
    # if the summary file does not exists, create file with the headers
    with open(folder_name + "client_summary.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Case Name"] + list(data.keys()))

# update the server_summary.csv file
with open(folder_name + "client_summary.csv", "a") as f:
    writer = csv.writer(f)
    record = [case_name]

    for key in list(data.keys()):
        record.append(data[key])
    writer.writerow(record)
