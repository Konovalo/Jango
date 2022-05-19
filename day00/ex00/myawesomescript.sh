#!/bin/sh
curl -s -I $1 | grep -i 'Location:' | cut -b 11-
