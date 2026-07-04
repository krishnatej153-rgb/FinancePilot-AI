import re


def extract_amount(text):

    amounts = re.findall(r"\d+\.\d+|\d+", text)

    if amounts:
        return max(amounts, key=float)

    return None