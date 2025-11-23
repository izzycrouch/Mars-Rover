#!/bin/bash
sleep 0.5
echo -e '\n--------------------------------------------'
echo -e '--------------------------------------------\n'
# sleep 0.5
echo -e '        🚀  WELCOME TO MARS-ROVER  🚀 \n'
# sleep 0.5
echo -e '--------------------------------------------'
echo -e '--------------------------------------------\n'

sleep 1.5

# echo -e 'INFORMATION:\n'

# sleep 1

instructions_text() {
    local var
    var=$(cat start_up.txt)

    for (( i=0; i<${#var}; i++ )); do
        echo -ne "${var:$i:1}"
        sleep 0.04
    done

    echo
}

instructions_text

# sleep 1

# echo -e '\nHAVE FUN!!!\n'

# sleep 0.5

# echo -e 'Lets get this started!\n'

# sleep 0.5
