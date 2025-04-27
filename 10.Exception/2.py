def password_check(password):
    if len(password)<8:
        raise Exception('Password must be greater than 8 characters')