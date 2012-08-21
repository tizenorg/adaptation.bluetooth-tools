#!/bin/sh

#
# Script for stopping Bluetooth stack
#

# Remove BT device
/usr/etc/bluetooth/bt-dev-end.sh

# Kill BlueZ bluetooth stack
killall bluetoothd
killall obexd obex-client
killall bt-syspopup
killall bluetooth-share
killall bluetooth-pb-agent
killall bluetooth-map-agent
killall bluetooth-hfp-agent

# result
exit 0
