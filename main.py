import requests
import main_functions
url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-US/MIA-sky/JFK-sky/anytime"

querystring = {"inboundpartialdate":"anytime"}

headers = {
    'x-rapidapi-key': "8b810fb046mshf35c1db2d319878p14dfbbjsnd75f1275f083",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring).json()

main_functions.save_to_file(response,"JSON Files/response.json")
