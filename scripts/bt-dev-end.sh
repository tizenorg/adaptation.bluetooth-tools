#!/bin/sh

#
# Script for stopping Bluetooth stack
#

# Device down
/usr/sbin/hciconfig hci0 down

# Turn off Bluetooth Chip
rfkill block bluetooth