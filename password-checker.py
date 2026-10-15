
import getpass
import string

def check_password(password):
    score = 0
    tips = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 12 characters.")

    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Add numbers.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        tips.append("Consider adding symbols.")

    if password.lower() in {
        "password", "password123",
        "qwerty123", "admin123"
    }:
        score = 0
        tips.append("Avoid common passwords.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, tips


password = getpass.getpass("Enter a test password: ")
strength, tips = check_password(password)

print("\nPassword strength:", strength)

if tips:
    print("\nSuggestions:")
    for tip in tips:
        print("-", tip)
else:
    print("No basic improvements suggested.")
