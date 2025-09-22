import re

def validate(email, username, password):
    if email is None or username is None or password is None:
        return False
    email_pattern = "\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"
    username_pattern = "/^[0-9A-Za-z]{6,16}$/"
    password_pattern = "/^(?=.*?[0-9])(?=.*?[A-Za-z]).{8,32}$/"

    if re.search(email_pattern, email) and re.search(username_pattern, username) and re.search(password_pattern, password):
        return True
    return False