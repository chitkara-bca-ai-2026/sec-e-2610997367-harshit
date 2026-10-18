username = input("Enter your username: ")
password = input("Enter your password: ")

length_ok = len(password) >= 8
digit_ok = any(char.isdigit() for char in password)
uppercase_ok = any(char.isupper() for char in password)

print("=" * 40)
print("       PASSWORD VALIDATION REPORT")
print("=" * 40)
print("Username:", username)
print("Password:", "*" * len(password))

print("\n--- Validation Rules ---")

if length_ok:
    print(f"[PASS] Minimum 8 characters ({len(password)} characters)")
else:
    print(f"[FAIL] Minimum 8 characters ({len(password)} characters)")

if digit_ok:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

if uppercase_ok:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

print("\n--- Result ---")

if length_ok and digit_ok and uppercase_ok:
    print("Password is VALID!")
    print("Account created successfully for", username + "!")
else:
    print("Password is INVALID")

print("=" * 40)