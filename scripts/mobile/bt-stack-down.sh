#!/bin/sh

#
# Script for stopping Bluetooth stack
#

PGREP="/usr/bin/pgrep"

# Remove BT device
/usr/etc/bluetooth/bt-dev-end.sh

# Kill BlueZ bluetooth stack
pid=`${PGREP} obexd`
kill $pid
pid=`${PGREP} bt-syspopup`
kill $pid
pid=`${PGREP} bluetooth-pb`
kill $pid
pid=`${PGREP} bluetooth-map`
kill $pid
pid=`${PGREP} bluetooth-ag`
kill $pid
pid=`${PGREP} bluetoothd`
kill $pid

# result
exit 0
