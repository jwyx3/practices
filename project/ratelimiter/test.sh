#!/bin/bash

USER=user1
TEST1_URL=http://127.0.0.1:5000/test1
ab -t 120 -c 3 -n 3 -H "Remote-User:$USER" $TEST1_URL

ADDR2=10.10.10.10
TEST2_URL=http://127.0.0.1:5000/test2
ab -t 120 -c 3 -n 3 -H "Remote-Addr:$ADDR2" $TEST2_URL

ADDR3=10.10.10.9
TEST3_URL=http://127.0.0.1:5000/test3
ab -t 120 -c 3 -n 3 -H "Remote-Addr:$ADDR3" $TEST3_URL
