echo Please enter a country to find its capital.
echo countries available: Iraq, India, Japan, Australia and Pakistan.
echo enter \'exit\' to exit.
echo ~~~~~~~~~~~~~~~~~~~~~~~
while :
do
read country
case $country in
  "Iraq" | "iraq")
    echo Iraq\'s capital is Baghdad ;;
  "India" | "india")
    echo The capital of $country is New Delhi ;;
  "Japan" | "japan")
    echo The capital of $country is Tokyo ;;
  "Australia" | "australia")
    echo The capital of $country is Canberra ;;
  "Pakistan" | "pakistan")
    echo The capital of $country is Islamabad ;;
  "exit" | "exit" | "EXIT")
      exit;;

esac
done
