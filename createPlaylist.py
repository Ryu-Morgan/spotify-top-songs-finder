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
def search_spotify_for_artist_id(token, artist_name):
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

    return artist_id

# Function that gets the top tracks of an artist based on the artist id
def get_top_tracks(token, artist_id):
    # spotify top tracks endpoint
    url_top_tracks = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=US"

    # get header
    header = get_auth_header(token)

    # get json data from endpoint
    response = requests.get(url=url_top_tracks, headers=header)

    result = response.json()

    # get the top 3 songs of the artist
    song_list = []
    for i in range(3):
        # get the name of the song
        songs_name = result["tracks"][i]["name"]
        # get song url
        songs_url = result["tracks"][i]["external_urls"]["spotify"]
        # append the song name and url to the song list
        song_list.append((songs_name + ": " + songs_url))
    # return the top 3 songs
    return song_list


# Function that formats the top tracks of an artist
def format_top_tracks(top_tracks):
    for i in range(3):
        print(f"{i+1}. {top_tracks[i]}\n")


# Main Function
def main():
    # get the token
    token = get_token()
    # get artist name from command line
    artist_name = argv[1]
    # # identify the artist id
    artist_id = search_spotify_for_artist_id(token, artist_name)
    # get the top tracks of the artist
    songs = get_top_tracks(token, artist_id)
    # format the top tracks
    format_top_tracks(songs)

# main
if __name__ == "__main__":
    main()

