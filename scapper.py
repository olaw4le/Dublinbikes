import requests
#Api to get the data
bikes_url= "https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=b0979801c4ff351dc53e4bf7120f76de43e10959"
weather_url=""

# function to get data save in specified format
def get_data():
    bike_data= requests.get(bikes_url)
    file_type= bike_data.json()
    return file_type



