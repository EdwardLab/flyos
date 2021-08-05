export NEWT_COLORS='
window=red,blue
border=white,red
textbox=white,red
button=black,white
'
{
    for ((i = 0 ; i <= 100 ; i+=20)); do
        sleep 1
        echo $i
    done
} | whiptail --gauge "Please wait while installing" 6 60 0
