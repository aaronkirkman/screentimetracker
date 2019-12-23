This program uses the Python interface to `Xlib` to keep track of which program window has focus over time.

	usage: screentimetracker [-h] [-n INTERVAL] [-l LOGFILE] [-p PROCESS]

	optional arguments:
	  -h, --help            show this help message and exit
	  -n INTERVAL, --interval INTERVAL
							Specify update interval in seconds
	  -l LOGFILE, --logfile LOGFILE
							Specify log file location
	  -p PROCESS, --process PROCESS
							Specify custom process name

Dependencies:

	sudo apt-get install python3-psutil python3-xlib
