# Kethryn E Mansfield, Dorothea Nitsch, Liam Smeeth, Krishnan Bhaskaram, Laurie A Tomlinson, 2024.

import sys, csv, re

codes = [{"code":"8CS0.00","system":"readv2"},{"code":"66A8.00","system":"readv2"},{"code":"66AU.00","system":"readv2"},{"code":"C10M.00","system":"readv2"},{"code":"66AJ100","system":"readv2"},{"code":"C350011","system":"readv2"},{"code":"Kyu0300","system":"readv2"},{"code":"K01x111","system":"readv2"},{"code":"C10FS00","system":"readv2"},{"code":"8CP2.00","system":"readv2"},{"code":"66Ae.00","system":"readv2"},{"code":"K01x100","system":"readv2"},{"code":"N08.3","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diabetes-mellitus-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diabetes-mellitus---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diabetes-mellitus---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diabetes-mellitus---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
