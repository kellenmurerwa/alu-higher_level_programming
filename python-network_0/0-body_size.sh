#!/bin/bash
#script that takes, sends a request to that URL, and displays
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
