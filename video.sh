#!/bin/bash -ex

rm -f fifo.500
mkfifo fifo.500
cat fifo.500 | nc.traditional 10.243.188.212 9001 &
/opt/vc/bin/raspivid -o fifo.500 -t 0 -b 1000000
rm fifo.500
