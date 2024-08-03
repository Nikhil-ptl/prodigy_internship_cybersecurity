import re

def password_strength(password):

    if len(password) >= 8:
        length_criteria = True
    else:
        length_criteria = False

    if re.search(r'[A-Z]', password) is not None:
        uppercase_criteria = True
    else:
        uppercase_criteria = False

    if re.search(r'[a-z]', password) is not None:
        lowercase_criteria = True
    else:
        lowercase_criteria = False

    if re.search(r'[0-9]', password) is not None:
        number_criteria = True
    else:
        number_criteria = False

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None:
        special_char_criteria = True
    else:
        special_char_criteria = False

    score = 0
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if number_criteria:
        score += 1
    if special_char_criteria:
        score += 1

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = "Password Strength: " + strength + "\n"
    feedback += "Length: " + ("✓" if length_criteria else "✗") + "\n"
    feedback += "Uppercase Letters: " + ("✓" if uppercase_criteria else "✗") + "\n"
    feedback += "Lowercase Letters: " + ("✓" if lowercase_criteria else "✗") + "\n"
    feedback += "Numbers: " + ("✓" if number_criteria else "✗") + "\n"
    feedback += "Special Characters: " + ("✓" if special_char_criteria else "✗") + "\n"

    return feedback

password = input("Enter your password: ")
print(password_strength(password))
