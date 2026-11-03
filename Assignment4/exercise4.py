import re

def redact_phone_numbers(text):
    return re.sub(r'\b\d{10}\b|\+84\d+', '[REDACTED]', text)


text = input("Enter a document: ")
print(redact_phone_numbers(text))