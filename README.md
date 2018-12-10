### Author : Sathish 

### Installation

	1. Copy the python files and the shell scripts to /var/solarmonj directory 
	``` sudo mkdir -p /var/solarmonj 
	    sudo cp {root}/*.py {root}/*.sh  /var/solarmonj ```

	2. Now install the cron jobs for periodic polling
	``` copy the last 4 lines in 'crontab' to /etc/crontab
