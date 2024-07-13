from dotenv import load_dotenv
import os
import requests
from sys import argv


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


# Function that returns auth header
def get_auth_header(token):
    # According to the Spotify docuemntation any API we make must include the access token
    return {"Authorization" : "Bearer " + token}


# Function that searches for artist and returns the artist id
def search_spotify_for_artist(token, artist_name):
    # spotify search endpoint
    url_search = "https://api.spotify.com/v1/search"
    # get header 
    header = get_auth_header(token)

    # identify the most popular artist 
    query = f"q={artist_name}&type=artist&limit=1"

    # construct the endpoint for search a given artist
    url_search_for_artist = url_search + "?" + query

    # get json data from endpoint
    response = requests.get(url=url_search_for_artist,headers=header)
   
    result = response.json()

    artist_id = result["artists"]["items"][0]["id"]

    print(artist_id)



# main
if __name__ == "__main__":

    token = get_token()

    artist_name = argv[1]

    search_spotify_for_artist(token, artist_name)

    
