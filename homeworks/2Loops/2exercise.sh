echo Please enter a file name.
while :
do
  read doIexist
  if [[ -f $doIexist ]]
  then
    echo this file exists ... Exiting
    exit
  fi
  echo This file does not exist ... Please enter a file name that exists
done
