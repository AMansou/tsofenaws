lol=$(ls )
cnt=0
# echo ${lol[@]:8}
for i in ${lol}
do
  if [[ -d $i ]]
  then
    echo $i
  fi
done
####Super long version of code above is : ###
# lol=$(ls -l)
# cnt=0
# # echo ${lol[@]:8}
# for i in ${lol[@]:8}
# do
#   if [[ $(( cnt%9 )) -eq 0 && ${i:0:1} = 'd' ]]
#   then
#     flag=1
#   elif [[ $(( cnt%9 )) -eq 8 && $flag -eq 1 ]]
#   then
#     flag=0
#     echo $i
#   fi
#
#   [[ $(( cnt%9 )) -eq 0 ]]
#   first=$?
#   [[ ${i:0:1} = 'd' ]]
#   second=$?
#   # echo $(( cnt%9 )) ${i:0:1}
#   cnt=$(( cnt + 1 ))
# done
