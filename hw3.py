import re


def normalize_phone(phone_number):
    cleand_number = re.sub(r"[^\d+]", "", phone_number.strip())
    if cleand_number.startswith("380"):
        cleand_number = "+" + cleand_number
    if not cleand_number.startswith("+"):
        cleand_number = "+38" + cleand_number
    return cleand_number


print(normalize_phone("0936753567"))
print(normalize_phone("380987653829"))
print(normalize_phone("% +380956784537"))
print(normalize_phone("(093)456-87-45"))
print(normalize_phone("098-789-67-67"))
