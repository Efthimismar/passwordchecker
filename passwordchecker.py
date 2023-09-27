password = str(input("Give your password: "))
while ' ' in password or len([c for c in password if c.isalpha()]) < 3:
    print("String must have at least 3 letters and no whitespaces. Please try again.")
    password = input("Enter a string (at least 3 letters, no whitespaces): ")

special_characters = ['@', '#', '$', '%', '^', '&']

def password_checker(password):
    points = 0
    
    if any(c.isdigit() for c in password):
        points += 1
    
    if any(c.isupper() for c in password):
        points += 1
    
    if len(password) >= 8:
        points += 1
    
    if any(c.islower() for c in password):
        points += 1
    
    if any(char in special_characters for char in password):
        points += 1
    
    return points

password_strength = password_checker(password)

if password_strength <= 2:
    print("Your password is weak.")
elif 2 < password_strength <= 4:
    print("Your password is moderate.")
else:
    print("Your password is strong.")
