inotifywait -q -m -e close_write listado_jugadores.txt |
while read -r filename event; do
        n=`cat nplayers`
        ((n++))
        echo $n > nplayers
done
