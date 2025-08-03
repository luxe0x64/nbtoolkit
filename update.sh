#!/bin/bash

try_to_update(){
	clear
	echo "Checking for updates..."
	sleep 0.3
	check_for_updates=$(cat nbtoolkit.py | grep Version)

	if [[ $check_for_updates == *"2.4" ]]; then
		clear
		touch .no_updates_required.txt && echo "No updates required. " > .no_updates_required.txt
		echo "No updates required. "
		exit
		echo "No updates required. "
		python3 ./nbtoolkit.py && exit
	else
		echo "Update required. "
		git clone https://github.com/luxe0x64/nbtoolkit.git
	fi
}

Updated() {
	if try_to_update; then
		echo "Updated. "
		exit
	else
		echo "Something went wrong. "
		exit
	fi
}

Main() {
	try_to_update
	Updated
	exit
}

Main
