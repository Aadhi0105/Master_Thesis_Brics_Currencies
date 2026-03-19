"""
Convert the October 2022 RMB Evolution Excel file to clean CSV.
Run this first before running extract_swift.py.

Usage: python3 convert_oct22.py <path_to_file>
e.g.  python3 convert_oct22.py "/Users/psat0501/Desktop/HSG/Master Thesis/Thesis Data/SWIFT Dataset/October_22_-_Evolution_of_RMB_s_share.csv"
"""

import sys
import zipfile
import xml.etree.ElementTree as ET
import csv
from datetime import datetime, timedelta

def excel_date(serial):
    if serial > 59:
        serial -= 1
    dt = datetime(1899, 12, 31) + timedelta(days=int(serial))
    return dt.strftime('%Y-%m')

def convert(input_path):
    output_path = input_path.replace(
        "October_22_-_Evolution_of_RMB_s_share.csv",
        "RMB_Evolution_2019_2022.csv"
    )

    rows = []
    with zipfile.ZipFile(input_path) as z:
        ss_xml = z.read('xl/sharedStrings.xml')
        ss_tree = ET.fromstring(ss_xml)
        ns = {'ns': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
        strings = [si.find('.//ns:t', ns).text 
                   for si in ss_tree.findall('ns:si', ns)]
        
        sheet_xml = z.read('xl/worksheets/sheet1.xml')
        sheet_tree = ET.fromstring(sheet_xml)
        data_rows = sheet_tree.findall('.//ns:row', ns)

        for row in data_rows[2:]:  # skip title and header rows
            cells = []
            for c in row.findall('ns:c', ns):
                t = c.get('t')
                v = c.find('ns:v', ns)
                if v is not None:
                    cells.append(strings[int(v.text)] if t == 's' else v.text)
                else:
                    cells.append('')
            if len(cells) >= 2 and cells[0]:
                try:
                    date = excel_date(float(cells[0]))
                    share = round(float(cells[1]) * 100, 2)
                    ranking = cells[2] if len(cells) > 2 else ''
                    rows.append({
                        'Date': date,
                        'RMB_Share_Pct': share,
                        'RMB_Ranking': ranking,
                        'Source': 'SWIFT RMB Tracker Oct 2022 (rolling chart)'
                    })
                except Exception as e:
                    pass

    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, 
                    fieldnames=['Date','RMB_Share_Pct','RMB_Ranking','Source'])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Converted {len(rows)} rows")
    print(f"Date range: {rows[0]['Date']} to {rows[-1]['Date']}")
    print(f"Saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Default path
        default = ("/Users/psat0501/Desktop/HSG/Master Thesis/Thesis Data/"
                   "SWIFT Dataset/October_22_-_Evolution_of_RMB_s_share.csv")
        print(f"No path provided, using default:\n{default}")
        convert(default)
    else:
        convert(sys.argv[1])
