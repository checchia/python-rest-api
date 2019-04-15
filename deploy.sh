#!/bin/bash

echo "Deploying application to target host"
IP="18.234.238.121"

echo "Check if application tar already exists..."
if [ -f "config-tool.tar" ]
then
	echo "Delete existing app tar."
	rm config-tool.tar
fi

echo "Tar config tool application source and configuration files"
tar -cvf config-tool.tar config-tool/config.py config-tool/application.py config-tool/resources/Service.py config-tool/resources/PackageInstall.py config-tool/resources/PackageUpdate.py config-tool/resources/PackageRemove.py config-tool/README.md config-tool/requirements.txt config-tool/run.py config-tool/package-config.json

echo "Create staging directory in target host"
ssh root@$IP mkdir /root/staging

echo "Secure copy application tar and boot script to target host"
scp config-tool.tar root@$IP:~/staging
ssh root@$IP "cd /root/staging && tar -xvf config-tool.tar"
scp bootscript.sh root@$IP:~/staging
scp home.php root@$IP:~/staging
scp -r config root@$IP:~/staging

