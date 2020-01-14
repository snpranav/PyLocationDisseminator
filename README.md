# PyLocationDisseminator
PyLocationDisseminator is a script that uses an IP Location API to disseminate location details of your device.

The frequency for the script to run can be set based on user preference (Ex- Reboot, every 5 hours) using crontabs

This can help you keep track of your devices at any point in time.

## Environment Variables
----
I have made this script use environment variables to enable plug and play of API's, DB's, API Keys, etc.

I have attached an env_var_sample file which is a sample shell script that should be run to set the environment variables.

These environment variables also helps hide API keys ports and URLs during production.

## Location API
----
The API does not matter as long as it works. I have used ipgeolocation.io in my case. However, there are multiple other ip location API's out there that can be used.

**Note - While using an API of choice, please make sure to adhere to the API's terms of service and privacy policy**

## Data Dissemination
----
The script has currently been configured to write to a MongoDB. Essentially, the future goal is to be able to trigger any method of data dissemination.
### MongoDB Configuration
For the current mongodb configuration, change environment variables based on use case.

If you are using a DB hosted on your local machine, change the IP_ADDRESS in the environment variable file to "localhost" and the PORT to the port you have set it to. (Default MongoDB port is 27017)

## **How to run the Script**
1) Install the python module requirements from the `requirements.txt` file:
```shell
pip install -r requirements.txt
```
2) Edit the `env_var_sample.sh` to add the environmental variables.

3) Excecute the environmental variable shell script file by running:
```shell
source ./env_var_sample.sh
```

4) Run the script:
```shell
python3 main.py
```

**OR**

Run it using a crontab to trigger the script at particular time intervals by editing the crontab file by running:
```shell
crontab -e
```

