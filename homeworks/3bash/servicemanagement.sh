
child=$!

if [[ $# -ne 1 ]]
then
	echo 'Enter argument (run/stop/status)'
	exit
fi
if [[ ! -f runningproc ]]
then
	touch runningproc
fi
if [[ $1 = 'run' ]]
then
	isrunning=$(ps | grep "$(cat runningproc)" )
	if [[ -z "$isrunning" || -z "$(cat runningproc)" ]]
	then
		sleep 3600 &
		echo $! > runningproc
		echo started on PID on $(cat runningproc)
		exit
	else
		echo proc is already running
	fi
elif [[ $1 = 'stop' ]]
then
	proc=$(cat runningproc)
	isrunning=$(ps | grep "$(cat runningproc)" )
	if [[ -n "$isrunning" && -n "$(cat runningproc)" ]]
	then
		echo  stoppig the process $proc ....
		kill -SIGTERM $proc
	else
		echo The process is not running m80
	fi
	#kill -9 $proc
elif [[ $1 = 'status' ]]
then
	isrunning=$(ps | grep "$(cat runningproc)" )
	if [[ -n "$isrunning" &&  -n "$(cat runningproc)" ]]
	then
		echo proc is running on $(cat runningproc)
	else
		echo The process is not running m80
	fi
else
	echo "not a valid command :("
	exit
fi
