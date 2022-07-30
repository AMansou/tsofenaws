#!/bin/bash
echo Running...
touch newscript.sh
chmod +x newscript.sh
echo "if [[ ! -d dir99 ]]" > newscript.sh
echo "then" >> newscript.sh
echo "mkdir dir99" >> newscript.sh
echo "fi" >> newscript.sh
echo "echo hello bash > ./dir99/hello.txt" >> newscript.sh

./newscript.sh
rm ./newscript.sh
echo Success!
