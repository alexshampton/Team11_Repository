#!/bin/bash
# Path to the jabcodeWriter binary
JABCODE_WRITER="$HOME/Team11_Repository/Jabcode/jabcodeRepo/src/jabcodeWriter/bin/jabcodeWriter"
BASE_NAME="md5sum"
COMPRESSED_FILE="$BASE_NAME.tar.gz"
ENCRYPTED_FILE="$COMPRESSED_FILE.enc"

mkdir -p jabcodes
make -C $HOME/Team11_Repository/Jabcode/jabcodeRepo/src/jabcodeWriter
tar -czvf "$COMPRESSED_FILE" md5sum.txt  #Compresses md5sum file
openssl enc -aes-256-cbc -salt -in "$COMPRESSED_FILE" -out "$ENCRYPTED_FILE" 

$JABCODE_WRITER --input-file $ENCRYPTED_FILE --output "jabcodes/$BASE_NAME.png"
echo "Processed $ENCRYPTED_FILE -> jabcodes/$BASE_NAME.png"

