cd ~/src/john/run
echo "This script assumes you have a base unencrypted pdf to use for password crack testing purposes. Please enter the full location of the file located within this folder:"
read pdf2encrypt
echo "Please enter the password you would like to encrypt this file with:"
read pw
echo "Please enter the name of the output pdf file[no file type extension]:"
read outputfile
pdftk $pdf2encrypt output "$outputfile.pdf" user_pw $pw
./pdf2john.pl "$outputfile.pdf" > "$outputfile.hash"
echo "File is stored as '$outputfile.hash'. Please use this when using 'bash decrypt-pass.sh'"
