import csv
with open('MCAS.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
    	if row['Subject'] == "MTH":
    		print(row['Org Name'], row['P+A #'], row['P+A %'])