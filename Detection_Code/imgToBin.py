# Required Libraries
from PIL import Image

def image_to_jabcode(image_path, output_jabcode_path):
    # Step 1: Load the image using Pillow
    image = Image.open(image_path)
    
    # Step 2: Convert the image into bytes (optional: resize to reduce complexity)
    image = image.convert('RGB')
    img_data = image.tobytes()

    return(img_data)

# Example usage
file_data = image_to_jabcode("images/test.png", "output_jabcode.png")

# Open a file in binary write mode
with open("binary/output.bin", "wb") as binary_file:
    # Write some binary data to the file
    binary_file.write(file_data)

print("Binary file written successfully!")