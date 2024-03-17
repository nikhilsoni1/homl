#!/bin/bash

# Define variables
CONTAINER_NAME="dump-postgres-container"
DB_USER="postgres"
DB_NAME="dev01"
BACKUP_FILE="/tmp/dev01_$(date +%Y%m%d_%H%M)_bkp.sql" # Add HH:MM to the file name
DESTINATION_DIR="store"
mkdir -p store

# Create a database dump inside the Docker container
docker exec -t "$CONTAINER_NAME" pg_dump -U "$DB_USER" -d "$DB_NAME" -f "$BACKUP_FILE"

# Copy the backup file from the Docker container to the local directory
docker cp "$CONTAINER_NAME":"$BACKUP_FILE" "$DESTINATION_DIR"

# Check if the copy was successful
if [ $? -eq 0 ]; then
  echo "Backup completed successfully and copied to $DESTINATION_DIR"

  # Calculate the size of the backup file in MB
  BACKUP_SIZE=$(du -m "$DESTINATION_DIR/$(basename "$BACKUP_FILE")" | cut -f1)
  echo "Backup size: $BACKUP_SIZE MB"

  # Display the filename of the latest backup
  echo "Latest backup file: $(basename "$BACKUP_FILE")"
else
  echo "Backup failed"
fi
