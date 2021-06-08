cd ~/src/john/run
wordlistlocation=~/Desktop/College/CySecJ/create-wordlist.py #change this later
echo "Enter full address of filename to be cracked. If the file is present in any folder within the current directory then partial addresses will be sufficient.File must be john readable."
read filename
python $wordlistlocation 
./john $filename -w=wordlist.lst --rules=all
./john --show $filename

