#!/bin/bash
# Path to the jabcodeWriter binary
JABCODE_WRITER="$HOME/Team11_Repository/Jabcode/jabcodeRepo/src/jabcodeWriter/bin/jabcodeWriter"

# Input directory containing binary files
BIN_SPLIT_DIR="$HOME/Team11_Repository/RaspberryPiCode/assets/splitFiles"
MD5SUM_DIR="../assets/md5sums"
COMPRESSED_FILE="../assets/compressedAndZippedFiles/Death_Star_Images.tar.gz"
ENCRYPTED_FILE="../assets/compressedAndZippedFiles/Death_Star_Images.tar.gz.enc"
IMAGES_FILE="../assets/death_star_images"
FILENAME="Death_Star_Images"

# Create output directory if it doesn't exist
mkdir -p "../assets/dsImagesJabcodes"
mkdir -p "../assets/splitFiles"
mkdir -p "../assets/compressedAndZippedFilesRP"
mkdir -p "../assets/md5sums"

make -C $HOME/Team11_Repository/Jabcode/jabcodeRepo/src/jabcodeWriter
tar -czvf "$COMPRESSED_FILE" "$IMAGES_FILE" #Compresses images folder
md5sum "$COMPRESSED_FILE" > "$MD5SUM_DIR/md5sumRP.txt"
openssl enc -aes-256-cbc -salt -in "$COMPRESSED_FILE" -out "$ENCRYPTED_FILE" 
split -b 4k "$ENCRYPTED_FILE" "$BIN_SPLIT_DIR/$FILENAME"_

# Iterate over each .bin file in the bin directory
COUNT=0
for split_file in $BIN_SPLIT_DIR/*; do
    # Extract the base filename without extension
    base_name=$(basename "$split_file")
    
    # Define the output file name
    output_file="../assets/dsImagesJabcodes/$base_name.png"
    
    # Run the jabcodeWriter command
    $JABCODE_WRITER --input-file "$split_file" --output "$output_file"
    ((COUNT++))
    # Print status
    echo "Processed $split_file -> $output_file Count: $COUNT"
done
