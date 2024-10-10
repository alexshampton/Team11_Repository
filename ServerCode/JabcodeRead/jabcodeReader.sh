JABCODE_READER="$HOME/Team11_Repository/Jabcode/jabcodeRepo/src/jabcodeReader/bin/jabcodeReader"

# Input directory containing binary files
JABCODE_DIR="$HOME/Team11_Repository/ServerCode/JabcodeRead/jabcodes" #CHANGE DIR TO JABCODE IMAGES
ENCRYPTED_DIR="$HOME/Team11_Repository/ServerCode/JabcodeRead/encryptedFiles"
COMPRESSED_DIR="$HOME/Team11_Repository/ServerCode/JabcodeRead/compressedFiles"
IMAGE_DIR="$HOME/Team11_Repository/ServerCode/JabcodeRead/death_star_images"

COMPRESSED_FILE="Death_Star_Images.tar.gz"
ENCRYPTED_FILE="Death_Star_Images.tar.gz.enc"

# Create output directory if it doesn't exist
mkdir -p "encryptedFiles"
mkdir -p "death_star_images"
mkdir -p "compressedFiles"
make -C $HOME/Team11_Repository/Jabcode/jabcodeRepo/src/jabcodeReader


COUNT=0
for split_file in $JABCODE_DIR/*; do
    base_name=$(basename "$split_file")
    output_file="$base_name.tar.gz.enc"

    $JABCODE_READER "$split_file" --output "$ENCRYPTED_DIR/$output_file"
    ((COUNT++))
    # Print status
    echo "Read $split_file -> $ENCRYPTED_DIR/$output_file Count: $COUNT"
done

cat encryptedFiles/* > folder.tar.gz.enc
openssl enc -aes-256-cbc -d -in folder.tar.gz.enc -out folder.tar.gz
tar -xzvf folder.tar.gz -C death_star_images/
