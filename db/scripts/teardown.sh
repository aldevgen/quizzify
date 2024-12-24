#!/bin/bash

# Load environment variables from .env file
export $(grep -v '^#' .env | xargs)

# Export the PostgreSQL data using pg_dump
echo "Exporting data from PostgreSQL..."
docker-compose exec -T db bash -c "pg_dump -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER -d $POSTGRES_DB --data-only --column-inserts > /tmp/latest-seeds.sql"

# Check if the dump file was created inside the container
echo "Checking if the dump file was created..."
docker-compose exec -T db bash -c "ls -l /tmp/latest-seeds.sql"

# Check if the command was successful
if [ $? -eq 0 ]; then
    echo "Data export successful. Copying the file to local machine..."
    # Copy the file from the Docker container to the local machine
    docker cp $(docker-compose ps -q db):/tmp/latest-seeds.sql ./db/seeds/latest-seeds.sql
    if [ $? -eq 0 ]; then
        echo "File copied successfully. Proceeding to teardown."
    else
        echo "File copy failed. Aborting teardown."
        exit 1
    fi
else
    echo "Data export failed. Aborting teardown."
    exit 1
fi

# Teardown the Docker Compose services
echo "Tearing down Docker Compose services..."
docker-compose down
