echo Please enter a word to see if it comes after the word "telephone" in the dictionary.
read word
if [[ -z $word ]]
then
  echo I AM UNBREAKABLE
  exit
fi
if [ "$word" \> "telephone" ]
then
  echo \'$word\' appears after the word  \'telephone\'
else
  echo \'$word\' appears before the word  \'telephone\'
fi
