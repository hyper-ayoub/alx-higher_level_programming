#!/bin/bash
# cURL a JSON file
curl -s "$1" -H "content-type: application/json" -d @"$2"
