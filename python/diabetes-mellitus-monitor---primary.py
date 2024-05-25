# Kethryn E Mansfield, Dorothea Nitsch, Liam Smeeth, Krishnan Bhaskaram, Laurie A Tomlinson, 2024.

import sys, csv, re

codes = [{"code":"9OLA.11","system":"readv2"},{"code":"9OL7.00","system":"readv2"},{"code":"66AZ.00","system":"readv2"},{"code":"9OLA.00","system":"readv2"},{"code":"9OLN.00","system":"readv2"},{"code":"9OL..00","system":"readv2"},{"code":"66A..00","system":"readv2"},{"code":"9OL9.00","system":"readv2"},{"code":"9OL5.00","system":"readv2"},{"code":"9OLZ.00","system":"readv2"},{"code":"66o..00","system":"readv2"},{"code":"8A17.00","system":"readv2"},{"code":"66b1.00","system":"readv2"},{"code":"9OL8.00","system":"readv2"},{"code":"9OL1.00","system":"readv2"},{"code":"9OL6.00","system":"readv2"},{"code":"9OL2.00","system":"readv2"},{"code":"8A12.00","system":"readv2"},{"code":"9OL4.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-mellitus-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes-mellitus-monitor---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes-mellitus-monitor---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes-mellitus-monitor---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
