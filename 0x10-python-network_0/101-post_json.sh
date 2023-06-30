#!/bin/bash
#a Script sends a JSON POST request to a URL first argument, displays the body of response
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
