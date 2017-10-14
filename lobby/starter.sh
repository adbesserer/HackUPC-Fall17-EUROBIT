/home/isma/Desktop/hackthon/pruebas/lobby/reset.sh&
echo uno
/home/isma/Desktop/hackthon/pruebas/lobby/counter.sh&
echo dos
/home/isma/Desktop/hackthon/pruebas/lobby/addplayers.sh&
echo tres

sleep $1

pkill inotifywait
