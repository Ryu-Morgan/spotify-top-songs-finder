# spotify-playlist-creation-automation
This code allows users to input their favorite artists and the artists top songs using the spotify api

To run the project please create your secrets using the spotify web api documentation:
- access token URL -> https://developer.spotify.com/documentation/web-api/concepts/access-token
- client-id and client-secret -> https://developer.spotify.com/documentation/web-api

## Features
- Input multiple artists within a menu system
- Automatically fetch each artist's top tracks leveraging the Spotify Web API
- Playlist generation logic (coming soon)

# DOCKER INSTRUCTIONS
The project image can be found here -> (https://hub.docker.com/repository/docker/rkm730/spotify-project/general)

Please make sure you have access to docker hub, if you're able to login to dockerhub please pull down the image **rkm730/spotify-project:0.0.2** using the command -> 
```
docker pull rkm730/spotify-project:0.0.2
```

After pulling down the image, run the container using the command ->
```
docker run rkm730/spotify-project:0.0.2
```

Since the container is running identify the container name and enter the container using the command ->
```
docker exec -it <container_name> bash 
```

Once inside the container add the missing .env file with the values:
- CLIENT-ID=
- CLIENT-SECRET=
- ACCESS-TOKEN-URL=


After the .env file is added run the container using the command ->
```
python findTopSongs.py
```
