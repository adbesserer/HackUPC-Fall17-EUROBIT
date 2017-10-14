function adding {
	phrase=`tail -n 1 changing_file.txt`
	if grep -q -i "AP-STA-CONNECTED" "$phrase" then 
		mac=`tail -n 1 changing_file.txt | grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}'`
		if ! grep -q -i "$mac" listado_jugadores.txt; then
			echo jugador afegit
		  	echo "$mac" `cat nplayers` >> listado_jugadores.txt
		fi
	fi
}

mac=0
#ejecutamos el scanner
inotifywait -q -m -e close_write changing_file.txt |
while read -r filename event; do
	echo "solicitud recibida"
	adding
done

