echo Please enter the name of the file that you would like to find the longest word it contains:
read filename
content=$(cat $filename | tr -d ",\':;\")([]{}./" )
maxlen=0
echo Word lengths:
for word in ${content}
do
  length=$(( $( echo $word | wc -c  ) - 1 ))
  echo $word: $length
  if [[ $length -gt $maxlen ]]
  then
    maxlen=$length
    longest=$word
  fi
done
echo THE LONGEST WORD IS: $longest
