import pyotp
import qrcode
import pandas as pd
from PIL import Image
import hashlib

# Load the Excel file containing usernames, passwords, and secret keys
def load_user_data(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None

# Hash the password for secure comparison (you can modify this part as needed)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Check the username and password, and retrieve the user's secret key
def validate_user(username, password, df):
    # Hash the password for comparison
    # hashed_password = hash_password(password)
    
    # Search for the user in the DataFrame
    user_row = df.loc[df['Username'] == username]
    
    if not user_row.empty:
        stored_password = user_row.iloc[0]['Password']
        print(stored_password)
        
        # Check if the hashed password matches
        if password == stored_password:
            secret_key = user_row.iloc[0]['Secret Key']
            return True, secret_key
        else:
            return False, None
    else:
        return False, None
    
# Generate a secret key for the user
def generate_secret():
    # Create a base32 secret (this will be unique for each user)
    return pyotp.random_base32()

# Create a provisioning URI for Google Authenticator
def generate_qr_code(user_name, secret_key):
    provisioning_uri = pyotp.totp.TOTP(secret_key).provisioning_uri(user_name, issuer_name="Team11")

    # Generate a QR code image
    qr_img = qrcode.make(provisioning_uri)
    
    # Save the QR code as an image file
    qr_img_filename = "otp_qr_code.png"
    qr_image_dirpath = "static/img/" + qr_img_filename
    qr_img.save(qr_image_dirpath)
    
    print(f"QR code saved as {qr_image_dirpath}. Scan it with Google Authenticator.")
    
    # Optionally, open the image (on most systems, this will open the default image viewer)
    img = Image.open(qr_image_dirpath)
    img.show()

    return provisioning_uri

# Validate OTP input from Google Authenticator
def validate_otp(secret_key, otp_input):
    totp = pyotp.TOTP(secret_key)
    return totp.verify(otp_input)

def main():
    file_path = "users.xlsx"
    df = load_user_data(file_path)

    if df is None:
        print("Failed to load user data.")
        return
    
    username = input("Enter your name: ")
    password = input("Enter your password: ")
    
    isObiwan, secret_key = validate_user(username, password, df)

    if(isObiwan):
        user_otp = input("Enter the OTP from Google Authenticator: ")
        if validate_otp(secret_key, user_otp):
            print("Login successful!")
        else:
            print("Invalid OTP. Login failed.")
    else:
        print("Not obiwan")


    # # Generate secret for the first time (save this securely for future logins)
    # secret_key = generate_secret()
    # print(f"Your secret key is: {secret_key}")
    
    # Generate and show QR code for Google Authenticator
    # generate_qr_code(username, secret_key)
    
    # Ask for OTP from the user (they would get this from their Google Authenticator app)
    
    # Validate OTP


if __name__ == "__main__":
    main()