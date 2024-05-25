# Kethryn E Mansfield, Dorothea Nitsch, Liam Smeeth, Krishnan Bhaskaram, Laurie A Tomlinson, 2024.

import sys, csv, re

codes = [{"code":"U602311","system":"readv2"},{"code":"U602315","system":"readv2"},{"code":"U602312","system":"readv2"},{"code":"U602317","system":"readv2"},{"code":"U602318","system":"readv2"},{"code":"66Al.00","system":"readv2"},{"code":"66Ak.00","system":"readv2"},{"code":"U60231E","system":"readv2"},{"code":"U60231A","system":"readv2"},{"code":"U60231B","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-mellitus-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes-mellitus-excretion---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes-mellitus-excretion---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes-mellitus-excretion---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
