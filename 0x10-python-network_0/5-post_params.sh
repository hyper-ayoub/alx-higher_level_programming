#!/bin/bash
#Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -s -F "email=test@gmail.com" -F "subject=I will always be here for PLD" "$1"
