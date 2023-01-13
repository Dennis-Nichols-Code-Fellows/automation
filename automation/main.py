import re

# Given a document potential-contacts, find and collect all email addresses and phone numbers.
# Phone numbers may be in various formats.
# (xxx) yyy-zzzz, yyy-zzzz, xxx-yyy-zzzz, etc.
# phone numbers with missing area code should presume 206
# phone numbers should be stored in xxx-yyy-zzzz format.
# Once emails and phone numbers are found they should be stored in two separate documents.
# The information should be sorted in ascending order.
# Duplicate entries are not allowed.


def find_contacts(filepath):
    with open(filepath, 'r') as file:
        text = file.read()

    print(text)
    email_pattern = r"\w+@\w+[-]?\w+\.\w{2,}"
    emails = re.findall(email_pattern, text)
    emails = list(set(emails))

    phone_pattern = r'(?:\+1[-. ]?)?(?:\(?([0-9][0-9][0-9])\)?[-. ]?)?([0-9][0-9]{2})[-. ]?([0-9]{4})(?:[-. ]?([0-9]{4}))?'
    phone_numbers = re.findall(phone_pattern, text)

    formatted_numbers = ['-'.join([sub_el for sub_el in element if sub_el != '']) for element in phone_numbers]
    formatted_numbers = set(formatted_numbers)

    phone_numbers_count = len(formatted_numbers)
    emails_count = len(emails)

    with open('../assets/emails.txt', 'w') as file:
        file.writelines(line + '\n' for line in emails)

    with open('../assets/phone_numbers.txt', 'w') as file:
        file.writelines(line + '\n' for line in formatted_numbers)

    return emails_count, phone_numbers_count


print(find_contacts('../assets/potential-contacts.txt'))
