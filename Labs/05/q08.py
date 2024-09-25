#name: ibrahim johar farooqi
#date: 18 september 2024
#lab: 05
#task: 8

import re

def extract_dates(text):
    date_pattern = r'\b(?:\d{1,2}/\d{1,2}/\d{4}|' \
                   r'\d{4}-\d{1,2}-\d{1,2}|' \
                   r'[A-Za-z]{3} \d{1,2}, \d{4})\b'

    dates = re.findall(date_pattern, text)
    return dates

text = """
date one: 12/09/2023. 
date two: 2023-09-12.
date three: Sep 12, 2023.
date four: 01/01/2024 and date five: 2024-01-01.
"""
extracted_dates = extract_dates(text)

print("extracted dates:")
for date in extracted_dates:
    print(date)
