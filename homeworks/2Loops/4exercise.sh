if [[ $# -lt 1 ]]
then
  echo Please enter the dir you would like to delete pls.
  exit
fi
files=$(ls -1b $1 )
if [[ -z $files ]]
then
  rmdir $1
  echo $1 deleted successfully.
  exit
fi
cd $1

for i in ${files}
do
  if [[ -f $i ]]
  then
    rm $i
  elif [[ -d $i ]] #delete nonempty subdirectories as well
  then
    .$0 $i
  fi
done
cd ..
rmdir $1
echo $1 deleted successfully.
