#!/bin/bash

# Made by: luxe0x64
# for nbtoolkit
# version: 2.5

check_ff() {
	check=$(ls .a | grep ".no_updates_required.txt")
	if [[ "$check" =~ ".no_updates_required.txt" ]]; then
		echo "No updates required. "
	else
		try_to_update
	fi
}

try_to_update(){
	clear
	echo "Checking for updates..."
	sleep 0.3
	check_for_updates=$(curl https://github.com/luxe0x64/nbtoolkit/blob/main/version.txt | grep "VERSION")

	if [[ "$check_for_updates" =~ "2.4" ]]; then
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
	check
	Updated
	exit
}

Main
