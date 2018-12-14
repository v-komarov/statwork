echo "Wellcome!"
echo "Testing of receiving cdr data"

while read line
do 
    echo "$line">>/srv/cdrlog.txt
done