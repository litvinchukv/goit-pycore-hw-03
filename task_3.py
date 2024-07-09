import re

def normalize_phone(phone_number):

    normalized_phone_number = re.sub(r"[^\d+]", "", phone_number)

    if normalized_phone_number.startswith("380"):
        return f"+{normalized_phone_number}"
    
    if not normalized_phone_number.startswith('+'):
        return f"+38{normalized_phone_number}"
    
    return normalized_phone_number

