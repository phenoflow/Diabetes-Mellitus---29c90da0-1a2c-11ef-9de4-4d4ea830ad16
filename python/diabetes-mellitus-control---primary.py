# Kethryn E Mansfield, Dorothea Nitsch, Liam Smeeth, Krishnan Bhaskaram, Laurie A Tomlinson, 2024.

import sys, csv, re

codes = [{"code":"C109711","system":"readv2"},{"code":"C10E800","system":"readv2"},{"code":"42W3.00","system":"readv2"},{"code":"42W1.00","system":"readv2"},{"code":"C10F711","system":"readv2"},{"code":"C108811","system":"readv2"},{"code":"C108812","system":"readv2"},{"code":"C109712","system":"readv2"},{"code":"42c0.00","system":"readv2"},{"code":"C10E811","system":"readv2"},{"code":"C10F700","system":"readv2"},{"code":"42c2.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-mellitus-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes-mellitus-control---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes-mellitus-control---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes-mellitus-control---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)