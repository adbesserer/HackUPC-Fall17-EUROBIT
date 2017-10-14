./reset.sh&
echo uno
./counter.sh&
echo dos
./addplayers.sh&
echo tres

sleep $1

pkill inotifywait
