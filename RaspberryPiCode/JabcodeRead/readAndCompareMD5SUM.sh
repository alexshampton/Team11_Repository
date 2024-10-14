JABCODE_READER="$HOME/Team11_Repository/Jabcode/jabcodeRepo/src/jabcodeReader/bin/jabcodeReader"

# Input directory containing binary files
JABCODE_DIR="$HOME/Team11_Repository/ServerCode/JabcodeReadWrite/JabcodeRead/jabcodes" #CHANGE DIR TO JABCODE IMAGES
MD5SUM_DIR="$HOME/Team11_Repository/RaspberryPiCode/JabcodeRead"

# Create output directory if it doesn't exist
mkdir -p "encryptedFiles"
mkdir -p "jabcode"
make -C $HOME/Team11_Repository/Jabcode/jabcodeRepo/src/jabcodeReader

$JABCODE_READER "jabcode/md5sumServer.png" --output "$MD5SUM_DIR/md5sumServer.tar.gz.enc"

openssl enc -aes-256-cbc -d -in md5sumServer.tar.gz.enc -out md5sumServer.tar.gz
tar -xzvf md5sumServer.tar.gz > md5sumServer.txt
diff md5sumServer.txt ../Binary_Conversion/md5sum.txt