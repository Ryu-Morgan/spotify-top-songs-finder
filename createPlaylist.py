from dotenv import load_dotenv
import os
import requests


# Global Variables 
load_dotenv()
client_id = os.getenv("CLIENT-ID")
client_secret = os.getenv("CLIENT-SECRET")



# Get the token
def get_token():
    # access token endpoint
    access_token_url = os.getenv("ACCESS-TOKEN-URL")

    # header
    header = {
        "Content-Type" : "application/x-www-form-urlencoded"
    } 

    # data
    data = {
        "grant_type" : "client_credentials",
        "client_id" : client_id,
        "client_secret" : client_secret
    }

    # make request to endpoint
    response = requests.post(access_token_url, headers=header, data=data)

    # assign result to json data
    result = response.json()

    # get the value of the access token from the json data
    access_token = result["access_token"]

    # return access token
    return access_token


# main
if __name__ == "__main__":

    token = get_token()

    print(token)
