# [WIP] Quizzify :musical_score:

Are you a music expert? Quizzify will challenge your musical knowledge. Quizzify invites music enthusiasts to test their expertise! Delve into a challenging and fun quiz experience designed to push your musical knowledge to the limit.

## :round_pushpin: Quick start

### Installation

To install the project, you need to clone the repository. It is recommended to create a virtual environment.

```bash
git clone git@github.com:alannadevgen/quizzify.git
cd quizzify
```

### Local setup

The following instructions will guide you through the setup of the project on your local machine.

1. Set the environment variables in an `.env` file in the root directory of the project. The `.env` file should contain the following variables:

```bash
SPOTIFY_CLIENT_ID=<YOUR SPOTIFY CLIENT ID>  # TBD
SPOTIFY_CLIENT_SECRET=<YOUR SPOTIFY CLIENT SECRET>  # TBD
SPOTIFY_REDIRECT_URI=<YOUR REDIRECT URI AS DEFINED IN YOUR SPOTIFY DASHBOARD APP> # TBD
SPOTIFY_AUTH_URL=https://accounts.spotify.com/authorize
SPOTIFY_TOKEN_URL=https://accounts.spotify.com/api/token
SPOTIFY_AUTH_SCOPE="LIST OF SCOPES TO DEFINE"  # TBD
```

2. Pre-commit hooks:

Pre-commit hooks have been defined to ensure a good code quality. To enable these pre-commit hooks, the following commands should be executed.

```bash
# install pre-commit
pip3 install pre-commit
# set up the git hook scripts
pre-commit install 
```

3. Build & run the docker image for the API.

a. Build & run the docker image using Docker.

````bash
docker build -t quizzify .
docker run -it --rm --name quizzify -p 8000:8000 quizzify
````

b. Build & run the docker image using Docker compose.

The following commands build the images and then run the containers.

````bash
docker-compose build
docker-compose up quizzify-api
````

It is also possible to build and run the containers in one command.

````bash
docker-compose up quizzify-api --build
````

To stop the containers, you can use the following commands. The tag `-v` removes the volumes that are associated with the containers.

````bash
docker-compose down
docker-compose down -v
````
You can now access the API at http://localhost:8000.

## Architecture

TBD

```mermaid
erDiagram
    USERS_SPOTIFY {
        VARCHAR(50) spotify_id PK
        VARCHAR(100) spotify_username
        VARCHAR(150) spotify_email
        VARCHAR(100) spotify_image_url
        VARCHAR(100) spotify_uri
    }
    
    USERS_QUIZZIFY {
        VARCHAR(50) user_id PK
        VARCHAR(100) username
        VARCHAR(150) email
        BYTEA hashed_pwd
        TIMESTAMP created_at
    }
    
    ARTISTS {
        VARCHAR(50) id PK
        VARCHAR(100) name
        INT popularity
        VARCHAR(50)[] genres
        INT followers
        VARCHAR(150) image_url
    }
    
    RELATED_ARTISTS {
        VARCHAR(50) artist_id FK
        VARCHAR(50) related_artist_id FK
    }
    
    TOP_ARTISTS {
        VARCHAR(50) artist_id FK
        VARCHAR(50) user_id FK
    }
    
    ALBUMS {
        VARCHAR(50) id PK
        VARCHAR(200) name
        INT popularity
        VARCHAR(4) release_year
        VARCHAR(4) release_decade
        INT total_tracks
        VARCHAR(150) image_url
    }
    
    ALBUMS_ARTISTS {
        VARCHAR(50) artist_id FK
        VARCHAR(50) album_id FK
    }
    
    TOP_ALBUMS {
        VARCHAR(50) album_id FK
        VARCHAR(50) user_id FK
    }
    
    SONGS {
        VARCHAR(50) id PK
        VARCHAR(200) name
        INT popularity
        INT duration_ms
        INT track_number
        VARCHAR(25) artist_id FK
        VARCHAR(25) album_id FK
    }
    
    TOP_SONGS {
        VARCHAR(50) song_id FK
        VARCHAR(50) user_id FK
    }
    
    USERS_QUIZZIFY ||--o{ USERS_SPOTIFY: "user_id references spotify_id"
    USERS_QUIZZIFY ||--o{ TOP_ARTISTS: "user_id"
    USERS_QUIZZIFY ||--o{ TOP_ALBUMS: "user_id"
    USERS_QUIZZIFY ||--o{ TOP_SONGS: "user_id"
    ARTISTS ||--o{ RELATED_ARTISTS: "id references artist_id, related_artist_id"
    ARTISTS ||--o{ TOP_ARTISTS: "id references artist_id"
    ARTISTS ||--o{ ALBUMS_ARTISTS: "id references artist_id"
    ARTISTS ||--o{ SONGS: "id references artist_id"
    ALBUMS ||--o{ ALBUMS_ARTISTS: "id references album_id"
    ALBUMS ||--o{ TOP_ALBUMS: "id references album_id"
    ALBUMS ||--o{ SONGS: "id references album_id"
    SONGS ||--o{ TOP_SONGS: "id references song_id"
```


## Contributors :woman_technologist:

<a href="https://github.com/alannadevgen/quizzify/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=alannadevgen/quizzify" />
</a>