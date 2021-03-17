import requests
import main_functions
import os
from dotenv import load_dotenv
url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/US/USD/en-US/MIA-sky/JFK-sky/anytime"

querystring = {"inboundpartialdate":"anytime"}
SECRET_Key = os.getenv("SECRET_KEY")
headers = {
    'x-rapidapi-key': str(SECRET_KEY),
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring).json()

main_functions.save_to_file(response,"JSON Files/response.json")
