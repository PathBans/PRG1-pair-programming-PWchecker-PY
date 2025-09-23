import datetime

OUTPUT_FILE = "./checking_password_log.txt"
INPUT_FILE = "./common_passwords.txt"

def get_current_datetime_formatted():
    now = datetime.datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")


def read_in_file(filename):
    with open(filename, "r") as f:
            return f.read()
    

def is_strong_password(password):
    if len(password) <= 8:
        return False
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    
    return has_upper and has_lower


def is_common_password(password):
    """Check if a password is in the list of common passwords."""
    common_passwords_text = read_in_file(INPUT_FILE)
    common_passwords_list = common_passwords_text.splitlines()
    
    return password in common_passwords_list


def check_password(password):
    
    is_strong = is_strong_password(password)

    # NEW: Check if password is common
    if is_common_password(password):
        print("⚠️  WARNING: This is one of the 25 most commonly used passwords!")
        print("   Please choose a different, more secure password.")
    
    # Log the check
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        strength = "Strong" if is_strong else "Weak"
        current_time_and_date = get_current_datetime_formatted()
        f.write(f"{current_time_and_date} - Password checked: {strength}\n")
    
    return is_strong



# Sample calls to test the program

print(check_password("ada"))  # Predict weak password (false)
print(check_password("AdaLovelace123"))  # Predict strong password (strong is debatable!)  (true)
print(check_password("password"))  # Should trigger warning!
print(check_password("123456"))  # Should trigger warning!