import pyotp
import qrcode
from PIL import Image


# Step 1: Generate a secret key for the user
def generate_secret():
    # Create a base32 secret (this will be unique for each user)
    return pyotp.random_base32()

# Step 2: Create a provisioning URI for Google Authenticator
def generate_qr_code(user_email, secret_key):
    provisioning_uri = pyotp.totp.TOTP(secret_key).provisioning_uri(user_email, issuer_name="Team11")

    # Generate a QR code image
    qr_img = qrcode.make(provisioning_uri)
    
    # Save the QR code as an image file
    qr_img_filename = "otp_qr_code.png"
    qr_img.save(qr_img_filename)
    
    print(f"QR code saved as {qr_img_filename}. Scan it with Google Authenticator.")
    
    # Optionally, open the image (on most systems, this will open the default image viewer)
    img = Image.open(qr_img_filename)
    img.show()

    return provisioning_uri

# Step 3: Validate OTP input from Google Authenticator
def validate_otp(secret_key, otp_input):
    totp = pyotp.TOTP(secret_key)
    return totp.verify(otp_input)

# Main Logic
if __name__ == "__main__":
    # Normally, the secret_key would be stored in a database and unique to the user
    user_email = input("Enter your email: ")
    
    # Generate secret for the first time (save this securely for future logins)
    secret_key = generate_secret()
    print(f"Your secret key is: {secret_key}")
    
    # Generate and show QR code for Google Authenticator
    generate_qr_code(user_email, secret_key)
    
    # Ask for OTP from the user (they would get this from their Google Authenticator app)
    user_otp = input("Enter the OTP from Google Authenticator: ")
    
    # Validate OTP
    if validate_otp(secret_key, user_otp):
        print("Login successful!")
    else:
        print("Invalid OTP. Login failed.")
