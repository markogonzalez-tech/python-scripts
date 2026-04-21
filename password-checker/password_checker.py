def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    score = 0

    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1

    if score == 4:
        return "Strong password"
    elif score == 3:
        return "Medium password"
    else:
        return "Weak password"


password = input("Enter a password: ")
result = check_password_strength(password)
print(result)
