#!/bin/sh

#--------------------------------------
#    bluetooth hci
#--------------------------------------

BLUETOOTH_DEBUG=${1}/bluetooth
PREV_PWD=${PWD}
BT_DUMP_DIR=/opt/usr/media/.bluetooth

if [ ! -e ${BT_DUMP_DIR} ]
then
	exit 0
fi

mkdir -p ${BLUETOOTH_DEBUG}

cd ${BT_DUMP_DIR}
/bin/tar -cvzf ${BLUETOOTH_DEBUG}/bt_dump.tar.gz *

cd ${PREV_PWD}
