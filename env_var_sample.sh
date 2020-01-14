#!/bin/sh
# Run the script as "source ./filename.sh" as the shell script needs to run with reference to the terminal's current environment

# You can use any API. In this case, I have used ipgeolocation.io's API
## Note - While using an API of choice, please make sure to adhere to the API's terms of service and privacy policy
export API_URL='https://api.ipgeolocation.io/ipgeo?apiKey='

# API Key only needed if API being used requires an API key
export API_KEY='API_KEY'


# IP Address of MongoDB
export IP_ADDRESS='localhost' # default
# PORT MongoDB is hosted on
export PORT='27017' # default

# Database Name
export DB_NAME='locationDetails'
# Device's Name stored as the collection's name
export COLLECTION_NAME='DEVICE_NAME'