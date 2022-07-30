if [[ $# -lt 1 ]]
then
  echo Please enter the dir you would like to delete pls.
fi

lol=$(ls )
sum=0
for i in ${lol}
do
  if [[ -f $i ]]
  then
    sum=$(( `echo $i|wc -c ` - 1 + $sum ))
  fi
done
echo The file names in this directory have $sum characters in them
