JABCODE_READER="$HOME/Team11_Repository/Jabcode/jabcodeRepo/src/jabcodeReader/bin/jabcodeReader"

# Directories to be used by scripts
JABCODE_DIR="$HOME/Team11_Repository/RaspberryPiCode/assets/md5sumJabcodes" #CHANGE DIR TO JABCODE IMAGES
MD5SUM_DIR="$HOME/Team11_Repository/RaspberryPiCode/assets/md5sums"
CAZ_FILE_DIR="$HOME/Team11_Repository/RaspberryPiCode/assets/compressedAndZippedFilesServer"

# Files to be used by script
MD5SUM_RP_FILE="../assets/md5sums/md5sumRP.txt"
MD5SUM_SERVER_FILE="../assets/md5sums/md5sumServer.txt"
ENCRYPTED_FILE="$CAZ_FILE_DIR/md5sumServer.tar.gz.enc"
COMPRESSED_FILE="$CAZ_FILE_DIR/md5sumServer.tar.gz"
JABCODE_MD5SUM_FILE="$JABCODE_DIR/md5sumJabcode.png"

# Create output directory if it doesn't exist
mkdir -p "encryptedFiles"
mkdir -p "../assets/md5sumJabcodes"
mkdir -p "../assets/compressedAndZippedFilesServer"
make -C $HOME/Team11_Repository/Jabcode/jabcodeRepo/src/jabcodeReader

$JABCODE_READER "$JABCODE_MD5SUM_FILE" --output "$ENCRYPTED_FILE"

openssl enc -aes-256-cbc -d -in "$ENCRYPTED_FILE" -out "$COMPRESSED_FILE"
tar -xzvf "$COMPRESSED_FILE" > "$MD5SUM_SERVER_FILE"
diff "$MD5SUM_SERVER_FILE" "$MD5SUM_RP_DIR"