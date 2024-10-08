#!/bin/bash
# python3 imgToBin.py

# Path to the jabcodeWriter binary
JABCODE_WRITER="$HOME/Team11_Repository/Jabcode/jabcodeRepo/src/jabcodeWriter/bin/jabcodeWriter"

# Input directory containing binary files
BIN_DIR="binary"
BIN_SPLIT_DIR="binary/binarySplit"
IMAGES_DIR="$HOME/Team11_Repository/Death_Star_Images/Testing_Images" #CHANGE DIR TO DETECTED IMAGES
COMPRESSED_FILE="Death_Star_Images.tar.gz"
ENCRYPTED_FILE="Death_Star_Images.tar.gz.enc"

# Create output directory if it doesn't exist
mkdir -p "jabcodes"
mkdir -p "binary/binarySplit"
# chmod -R 755 "$BIN_DIR"
# chmod -R 755 "$BIN_SPLIT_DIR"
make -C $HOME/Team11_Repository/Jabcode/jabcodeRepo/src/jabcodeWriter
tar -czvf "$COMPRESSED_FILE" "$IMAGES_DIR" #Compresses images folder
md5sum "$COMPRESSED_FILE" > md5sum.txt
openssl enc -aes-256-cbc -salt -in "$COMPRESSED_FILE" -out "$ENCRYPTED_FILE" 
split -b 4k "$ENCRYPTED_FILE" "$BIN_SPLIT_DIR/$ENCRYPTED_FILE"_
# for bin_file in "$BIN_DIR"/*.bin; do
#     base_name=$(basename "$bin_file" .bin)
#     split -b 4k "$bin_file" "$BIN_SPLIT_DIR/$base_name-"
#     echo $base_name 
# done

# Iterate over each .bin file in the bin directory
COUNT=0
for split_file in $BIN_SPLIT_DIR/*; do
    # Extract the base filename without extension
    base_name=$(basename "$split_file")
    
    # Define the output file name
    output_file="$base_name.png"
    
    # Run the jabcodeWriter command
    $JABCODE_WRITER --input-file "$split_file" --output "jabcodes/$output_file"
    ((COUNT++))
    # Print status
    echo "Processed $split_file -> $output_file Count: $COUNT"
done
