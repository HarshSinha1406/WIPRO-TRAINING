import re

password = "Strong@123"

pattern_password = r"""
^
(?=.*[A-Z])        # At least one uppercase letter
(?=.*[a-z])        # At least one lowercase letter
(?=.*\d)           # At least one digit
(?=.*[@$!%*?&])    # At least one special character
.{8,}              # Minimum 8 characters
$
"""

if re.match(pattern_password, password, re.VERBOSE):
    print("1. Password Validation")
    print("Strong Password")
else:
    print("Weak Password")

print("-" * 50)

text_case = "Python programming is FUN"
pattern_case = r"fun"

print("2. IGNORECASE Modifier")
if re.search(pattern_case, text_case, re.IGNORECASE):
    print("Match found (case-insensitive)")
else:
    print("No match found")

print("-" * 50)

text_multiline = """Python is easy
Java is powerful
Python is popular"""

pattern_multiline = r"^Python"

print("3. MULTILINE Modifier")
matches = re.findall(pattern_multiline, text_multiline, re.MULTILINE)
print("Lines starting with 'Python':", matches)

print("-" * 50)

text_dotall = "Hello\nWorld"

pattern_dotall = r"Hello.*World"

print("4. DOTALL Modifier")
if re.search(pattern_dotall, text_dotall, re.DOTALL):
    print("DOTALL allows '.' to match newline")
else:
    print("DOTALL did not match")

print("-" * 50)

print("5. Without DOTALL Modifier")
if re.search(pattern_dotall, text_dotall):
    print("Matched without DOTALL")
else:
    print("No match without DOTALL")
