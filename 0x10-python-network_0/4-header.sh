#!/bin/bash
#Script that sends a GET request to URL and displays body of response
curl -s "$1" -X GET -H "X-School-User-Id: 98"
