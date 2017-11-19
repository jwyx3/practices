#!/bin/bash

ADDR=10.10.10.11
TEST3_URL=http://127.0.0.1:5000/test3
ab -t 120 -c 500 -n 10000 -H "Remote-Addr:$ADDR" $TEST3_URL

