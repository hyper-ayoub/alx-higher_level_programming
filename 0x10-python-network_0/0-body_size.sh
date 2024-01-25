#!/bin/bash
# 0. cURL body size
curl -Is "$1" | grep 'Content-Length' | awk '{print $2}'
