# Python based configuration management tool

This is a simple configuration management tool that runs basic Linux automations tasks. These include installing/updating and removing packages, controlling services and deploying application files.

## Goals and requirements

The tool should support configuring Linux servers for managing pre-defined profiles. For example it should be able to configure a Linux server to serve PHP pages.
1. The tool should allow installing packages
2. Updating packages
3. Removing packages
4. Controlling services
5. Extensible for adding profiles for different hosts
6. Distributed system - central management from master to all remote nodes.

## Design and technology stack

The configuration management tool should be remotely managed. The tool would be deployed to all hosts that are in a managed footprint. The technolgy stack is as simple as possible and those that are natively supported on Linux operating system.

### Technology Stack
1. Python
2. Flask REST API libraries
3. Nginx for reverse proxying
4. Green Unicorn for launching Python app (gunicorn)
5. Client interface is demonstrated using curl script.

## API specifications

| Endpoint                  | Description                | Client usage                                       |
| ------------------------- |:--------------------------:| --------------------------------------------------:|
| /api/install/pkgName      | Installs package "pkgName" | curl -s -v http:/$IP/api/install/<pkgName> -X POST |
| /api/update/pkgName       | Updates package "pkgName"  | curl -s -v http:/$IP/api/update/<pkgName> -X POST  |
| /api/remove/pkgName       | Removes package "pkgName"  | curl -s -v http:/$IP/api/remove/<pkgName> -X POST  |
| /api/restart/svcName      | Restart service "svcName"  | curl -s -v http:/$IP/api/restart/<svcName> -X POST |

($IP is the target Linux Host IP address where we want to configure.)

## Application deployment

The application could be deployed in several ways - one of which is to do a secure copy of the app tar bundle and extract it in a staging directory on target host. 

1. Setup SSH keys from the client desktop to target Linux host. Refer to [Setting up SSH keys](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
2. Refer to deployment script deploy.sh (Please update as needed to your environment)
3. App would be deployed to target host /root/staging folder

## Application launch

The application would be launched on target Linux host on a Python virtual enironment.

### Requirements on target host for application launch
1. Update and upgrade Linux packages - apt-get update && apt-get upgrade
2. Install NGinx - apt-get install nginx
3. Create a new site and enable it - provided in config/default
4. Restart nginx service
5. Install PHP - apt-get install php5-fpm package
6. Deploy index.php to document root /var/www/html

Application boot script creates a Python virtual environment, pip install all app requirements, launches application through Green Unicorn (gunicorn) on default port 8000.

### From target host:
1. cd ~/staging
2. ./bootscript.sh

## Configuration and Future extension

The configuration tool is modelled through package-config.json file. The data is modelled using primary keys "package", "service", "deploy" and "host-profile". Each of them defines various predefined packages and their install, update and remove commands.

The host profile could be extended to include multiple packages and deployment tasks. 

For example:

  	"host-profile":	{
					"18.234.238.121":	{
		                "package": ["apache2", "php5-fpm"],
                    "deploy": ["file1", "file2"]
									}, 
					"54.226.108.226": {
		                "package": ["xyz1", "php5-fpm"],
                    "deploy": ["file12", "file22"]
					}



