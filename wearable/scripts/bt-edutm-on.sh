#!/bin/sh

#
# Script for turning on Bluetooth EDUTM
#

HCIDUMP_ENABLE="true"	# Available values : true | false (default : false)
HCIDUMP_FILENAME="bt_hcidump"
HCIDUMP_DIR="/opt/var/lib/bluetooth"
HCIDUMP_PATH="${HCIDUMP_DIR}/${HCIDUMP_FILENAME}"

# Register BT Device
/usr/etc/bluetooth/bt-dev-start.sh

if !(/usr/sbin/hciconfig | grep hci); then
	echo "BT EDUTM failed. Registering BT device is failed."
	exit 1
fi

if [ -e /usr/sbin/hcidump -a ${HCIDUMP_ENABLE} = "true" ]
then
	if [ ! -e ${HCIDUMP_DIR}/old_hcidump ]
	then
		/bin/mkdir -p ${HCIDUMP_DIR}/old_hcidump
	fi

	/bin/rm -f ${HCIDUMP_DIR}/old_hcidump/*			# In order to keep old log, please remove this line.
	/bin/mv ${HCIDUMP_PATH}* ${HCIDUMP_DIR}/old_hcidump/
#	/usr/sbin/hcidump -w ${HCIDUMP_PATH}_`date +%s_%N` &	# You can get unique file name.
	/usr/sbin/hcidump -w ${HCIDUMP_PATH} &
fi

echo "Configure BT device"
hcitool cmd 0x3 0x0005 0x02 0x00 0x02

echo "Send BT edutm command"
hcitool cmd 0x06 0x0003

# Execute BlueZ BT stack
echo "Run bluetoothd"
/usr/sbin/bluetoothd
/usr/bin/bt-service &
sleep 0.1

/usr/sbin/hciconfig hci0 name TIZEN-Mobile

/usr/sbin/hciconfig hci0 piscan

if [ -e "/sys/devices/hci0/idle_timeout" ]
then
	echo "Set idle time"
	echo 0> /sys/devices/hci0/idle_timeout
fi

if [ -e /usr/etc/bluetooth/TIInit_* ]
then
	echo "Reset device"
	hcitool cmd 0x3 0xFD0C
fi

echo "BT edutm done"

# result
exit 0
