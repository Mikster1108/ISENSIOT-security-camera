# This is the repository for the ISENSIOT security camera project

In this repository you will find all the programs responsible for managing the sensors that will be used for the security camera. There are also some other things here like scripts for sending data to the database. 

# Executing bash scripts

In order to run bash scripts as executables you first need to make them executable. This can be done using `chmod +x script.sh`. Afterwards you can execute them with `./script.sh`

# Env setup

Copy the env.example.txt file in the Python folder and name it .env. The local video directory should be set to the path of the directory where the videos are saved on the Pi and the drive mount path should be the path to the Raw-footage directory on the mounted NAS.

# Crontab setup

Some scripts should automatically start running on boot. These scripts should be added to the crontab file using `crontab -e`. The following scripts should be included in the crontab file:
- start_motion.sh
- start_combining.sh
- start_ldr.sh
- start detecting
- video_storage.py

# Motion

Settings for motion can be adjusted in the motion.conf file. Motion starts automatically with crontab but to start it manually you can use `sudo libcamerify motion`.