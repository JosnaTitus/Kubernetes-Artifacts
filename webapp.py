#Python3 code to demonstrate 
# Getting current date and time

# Import date class from datetime module
from datetime import date
from datetime import datetime

# Returns the current local date
today = date.today()
print("Current Date : ", today)

# Returns the current local time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time :", current_time)



# Python3 code to display hostname and
# Public & Private IP addresses
  
# Importing socket library
import socket
  
# Function to display hostname and
# private IP address
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname :  ",host_name)
        print("My private IP address : ",host_ip)
    except:
        print("Unable to get Hostname and IP")
  
# Driver code
get_Host_name_IP() #Function call

#public IP address
from requests import get

ip = get('https://api.ipify.org').text
print('My public IP address : {}'.format(ip))



#Python3 code to demonstrate 
# Getting current Location

# import module
from geopy.geocoders import Nominatim
  
# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")
  
  
# Latitude & Longitude input
Latitude = "18.520430"
Longitude = "73.856743"
  
location = geolocator.reverse(Latitude+","+Longitude)
  
address = location.raw['address']
  
# traverse the data
city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')
code = address.get('country_code')
#zipcode = address.get('postcode')
print('City : ', city)
print('Region : ', state)
print('Country : ', country)
#print('Zip Code : ', zipcode)
