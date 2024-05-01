#!/bin/bash
#DIsplays the size of the body of the http response.
curl -s "$1" | wc -c
