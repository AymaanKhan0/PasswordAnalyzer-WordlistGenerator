# password_analyzer.py

password = input("Enter a password to analyze: ")

length_score = len(password) >= 8
upper_score = any(c.isupper() for c in password)
lower_score = any(c.islower() for c in password)
digit_score = any(c.isdigit() for c in password)
symbol_score = any(not c.isalnum() for c in password)

score = sum([length_score, upper_score, lower_score, digit_score, symbol_score])

print("\nPassword Strength:")
if score == 5:
    print("Strong 💪")
elif score >= 3:
    print("Medium 😐")
else:
    print("Weak 😢")
