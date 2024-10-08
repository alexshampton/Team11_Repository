from PIL import Image
import os

# Converts image to binary
# Uses image path to find image
def image_binary_data(image_path):
    try:
        image = Image.open(image_path)
        image = image.convert('RGB')
        img_data = image.tobytes()

    except FileNotFoundError:
        print(f"Error: File not found - {image_path}")

    except OSError:
        print(f"Error: Cannot open image (unsupported format or corrupted file) - {image_path}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return(img_data)

def binary_file_add(imageDirectory, binaryDirectory):

    # Loops through files in the images directory
    picCheck = 0
    for file in os.listdir(imageDirectory):
        if os.path.splitext(file)[0] != ".gitkeep":
            picCheck = 1
            file_data = image_binary_data(imageDirectory + "/" + file)
            filename = os.path.splitext(file) #splits file by the extension 

            # Open and create a file in binary write mode
            with open(binaryDirectory + '/' + filename[0] + '.bin', 'wb') as binary_file:
                binary_file.write(file_data)

            # print(f"{binaryDirectory + '/' + filename[0]}.bin written successfully!")

    if picCheck == 0:
        print("No images are in the images directory!")

if __name__ == "__main__":
    image_dir = 'death_star_images'
    bin_dir = 'binary'

    if not os.path.exists(image_dir):
    # Create the directory
        os.makedirs(image_dir)
        print(f"Directory {image_dir} created.\nAdd images to directory")
        exit()

    if not os.path.exists(bin_dir):
    # Create the directory
        os.makedirs(bin_dir)
        print(f"Directory {bin_dir} created.")

    
    binary_file_add(image_dir, bin_dir)