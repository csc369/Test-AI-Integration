# WARNING: This code contains a hardcoded password, which is a security vulnerability.
# It is provided for educational purposes only to demonstrate insecure coding practices.

def authenticate_user(username, password):
    # Hardcoded credentials (vulnerability)
    hardcoded_username = "admin"
    hardcoded_password = "password123"  # Vulnerability: Hardcoded password

    if username == hardcoded_username and password == hardcoded_password:
        return "Authentication successful!"
    else:
        return "Authentication failed!"

# Example usage
if __name__ == "__main__":
    # Simulating user input
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    # Authenticate user
    result = authenticate_user(user, pwd)
    print(result)
