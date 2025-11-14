import logging

def authenticate_user(username, password):
    # Hardcoded credentials (vulnerability)
    hardcoded_username = "admin"
    hardcoded_password = "superSecretPassword123!"  # Sensitive information exposed

    if username == hardcoded_username and password == hardcoded_password:
        logging.info(f"User {username} authenticated successfully with password {password}")  # Vulnerability: Logging sensitive information
        return True
    else:
        logging.warning(f"Failed login attempt for user {username} with password {password}")  # Vulnerability: Logging sensitive information
        return False

# Example usage
if __name__ == "__main__":
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    authenticate_user(user, pwd)
