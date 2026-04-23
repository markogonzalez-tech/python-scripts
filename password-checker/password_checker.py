def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    issues = []

    if length < 8:
        issues.append("Password is too short")
    if not has_upper:
        issues.append("Missing uppercase letter")
    if not has_lower:
        issues.append("Missing lowercase letter")
    if not has_digit:
        issues.append("Missing number")
    if not has_special:
        issues.append("Missing special character")

    if len(issues) == 0:
        return "Strong password"
    else:
        return "Weak password:\n- " + "\n- ".join(issues)


password = input("Enter a password: ")
print(check_password_strength(password))
