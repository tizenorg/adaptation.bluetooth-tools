#!/bin/sh

#
# Script for stopping Bluetooth stack
#

PGREP="/usr/bin/pgrep"

# Remove BT device
/usr/etc/bluetooth/bt-dev-end.sh

# Kill BlueZ bluetooth stack
pid=`${PGREP} bt-syspopup`
kill $pid
pid=`${PGREP} bluetooth-hf`
kill $pid
pid=`${PGREP} bluetooth-ag`
kill $pid
pid=`${PGREP} bluetoothd`
kill $pid

# result
exit 0
