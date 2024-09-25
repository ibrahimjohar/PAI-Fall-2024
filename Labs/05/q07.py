#name: ibrahim johar farooqi
#date: 18 september 2024
#lab: 05
#task: 7

import re

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails

text = """
please contact us at support@example.com for more info.
also reach out to k230074@nu.edu.pk or harry_maguire@example.co.uk.
for institution inquiries, email admin@website.org.
"""

extracted_emails = extract_emails(text)
print("extracted email addresses:")
for email in extracted_emails:
    print(email)
