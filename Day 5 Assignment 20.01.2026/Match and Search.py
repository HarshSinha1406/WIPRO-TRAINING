import re

emp_id = "EMP123"

pattern_emp = r"(EMP)(\d{3})"

match_emp = re.match(pattern_emp, emp_id)

print("1. Employee ID Validation")
if match_emp:
    print("Valid Employee ID")
    print("Matched Groups:")
    print("Group 1 (Prefix):", match_emp.group(1))
    print("Group 2 (Digits):", match_emp.group(2))
else:
    print("Invalid Employee ID")

print("-" * 40)
text = "Please contact us at support_team99@gmail.com for assistance."

pattern_email = r"(\w+[\w\.]*@\w+\.\w+)"

search_email = re.search(pattern_email, text)

print("2. Email Search")
if search_email:
    print("Email Found:", search_email.group())
    print("Captured Group:", search_email.group(1))
else:
    print("No Email Found")

print("-" * 40)

sample_text = "Order ID: A12  Quantity: 50"

pattern_meta = r"(\w+)\s+ID:\s+(\w+)\s+Quantity:\s+(\d+)"

match_meta = re.search(pattern_meta, sample_text)

print("3. Meta-characters & Special Sequences")
if match_meta:
    print("Full Match:", match_meta.group())
    print("Word (\\w+):", match_meta.group(1))
    print("Alphanumeric Code:", match_meta.group(2))
    print("Digits (\\d+):", match_meta.group(3))

print("-" * 40)

text2 = "color colour colr"

pattern_optional = r"colou?r"

matches = re.findall(pattern_optional, text2)

print("4. Meta-characters Demonstration")
print("Pattern used: colou?r")
print("Matches found:", matches)
