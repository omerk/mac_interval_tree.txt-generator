import os
import csv

if not os.path.exists("mac-vendors-export.csv"):
    print("CSV File 'mac-vendors-export.csv' not found.")
    print("Download it from https://maclookup.app/downloads/csv-database")
    exit()

csv_file = open("mac-vendors-export.csv", "r", encoding="utf-8")
csv_data = csv.reader(csv_file, delimiter=",")
next(csv_data, None)  # skip the CSV headers

output = open("mac_interval_tree.txt", "w", encoding="utf-8")

print("Generating mac_interval_tree.txt...")
for line in csv_data:
    mac = line[0].replace(":", "").ljust(12, "F")
    vendor = line[1]
    output.write(f"{mac} {vendor}\n")

csv_file.close()
output.close()
print("Done!")
