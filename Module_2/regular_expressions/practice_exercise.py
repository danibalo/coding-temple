import re 
records = [
    "Name: Alice Johnson | Email: alice.j@gmail.com | Phone: (555) 123-4567 | Joined: 01/15/2023",
    "Name: Bob Smith | Email: bob_smith@yahoo.com | Phone: 555.987.6543 | Joined: 03-22-2023",
    "Name: Charlie Brown | Email: charlie@outlook.com | Phone: 555 111 2222 | Joined: 2023/07/01",
    "Name: Diana Prince | Email: diana.prince@company.co.uk | Phone: (555)444-3333 | Joined: 11/30/2023",
]

def extract_names(records):
    """
    1. extracts first name and last name
    2. appends the names to the list 
    3. returns the list
    """
    names = []
    for text in records:
        name = re.search("\\s([A-Za-z]+\\s[A-Za-z]+)", text)
        names.append(name.group())
    return names
#returns the list of extracted emails
def extract_emails(records):
    emails = []
    for text in records:
        email = re.search("[\\w.+-]+@[\\w.-]+\\.[\\w.]+", text)
        emails.append(email.group())
    return emails
#returns the list of normalized phones
def normalize_phones(records):
    phones = []
    for text in records:
    #Extract the phone number
        match = re.search(r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}", text)
        if match:
            phone = match.group()

        # Keep only digits
        digits = re.sub(r"\D", "", phone)

        # Format as ddd-ddd-dddd
        normalized = f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"

        phones.append(normalized)

    return phones

def extract_dates(records):
    dates = []

    pattern = r"\d{2}[/-]\d{2}[/-]\d{4}|\d{4}[/-]\d{2}[/-]\d{2}"

    for text in records:
        match = re.search(pattern, text)
        if match:
            dates.append(match.group())

    return dates


def parsed_dict(records):
    return {
        "names": extract_names(records),
        "emails": extract_emails(records),
        "phones": normalize_phones(records),
        "dates": extract_dates(records)
    }
print(parsed_dict(records))