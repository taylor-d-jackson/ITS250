import requests
import os.path
import json
import datetime
from influxdb import InfluxDBClient

url = "https://covid-19-data.p.rapidapi.com/totals"

querystring = {"format":"json"}

headers = {
    'x-rapidapi-key': "3706084193msh9239e64187dcd0ap10739fjsn52bd4db7bcee",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

# Creates the GET request with the type of request, the url, headers and parameters.
response = requests.request("GET", url, headers=headers, params=querystring)

# Sets client information to connect to INFLUXdb
client = InfluxDBClient(host='IP_ADDRESS', port=PORT_NUMBER, username='DB_USERNAME', password='DB_PASSWORD')

# Creates the database with whatever name you specify.
# client.create_database('covid')

# Switches to the desired database.
client.switch_database('covid')

# Checks to see if the file specified already exists. If it does it writes the data in JSON to the file.
# If it does not exist it creates the file and then writes the data.

#file_exists = os.path.isfile('covid19_data.json')

#if file_exists:
#    with open('covid19_data.json', 'w') as file:
#        json.dump(response.json(), file, indent = 4)

#else:
#    with open('covid19_data.json', 'w') as file:
#        json.dump(response.json(), file, indent = 4)

# Saves the GET request response as a list of dictionaries.
data = response.json()

# Saves the dictionary in index 0 of the data list as a variable.
# Used to access and dynamically insert JSON Key values into Influxdb JSON body.
a = data[0]

# Sets the format for JSON body that INFLUXdb requires when uploading information.
# Measurement, and tags set manually. Field keys are set manually, whereas field values are set dynamically based on the value from the API request.
json_body = [
        {
            "measurement": "covid",
            "tags": {
                "world": "totals"
                
            },
            "time": str(datetime.datetime.now()),
            "fields": {
                "Confirmed": a['confirmed'],
                "Recovered": a['recovered'],
                "Critical": a['critical'],
                "Deaths": a['deaths'],
                "Last Change": a['lastChange'],
                "Last Update": a['lastUpdate']
            }
        }
    ]

# Converts the JSON body into line points and writes to the INFLUXdb
client.write_points(json_body)


    


