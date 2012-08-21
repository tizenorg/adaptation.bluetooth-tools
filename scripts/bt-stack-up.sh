#!/bin/sh

#
# Script for executing Bluetooth stack
#

# Register BT Device
/usr/etc/bluetooth/bt-dev-start.sh

if !(/usr/sbin/hciconfig | grep hci); then
	echo "Registering BT device is failed."
	exit 1
fi

# Execute BlueZ BT stack
echo "Run bluetoothd"
/usr/sbin/bluetoothd -d
/usr/bin/bluetooth-share &

exit 0
