# 0.1.0
- Establish connection to the Spotify API and implement access token management (renewal and storage)
- Create a module to handle questions
- Spotify service:
  * Retrieve user information from Spotify.
  * Manage artists, albums and songs linked to a user.
- Database:
  * Creation of a PostgreSQL database
  * Creation of a `QueryExecutor` class to execute SQL queries.
  * Export seeds in a SQL file.
  * CRUD operations of `artist`, `album`, `song` entities and their relationships.
  * Insert relationships between users and their favourite artists, albums and songs.
- Dockerisation
    * Configuration of services via `docker-compose` (API and database).
    * Management of volumes to persist PostgreSQL data. 
    * Creation of a `shutdown.sh` script to manage container shutdown and data export.