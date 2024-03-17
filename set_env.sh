#!/bin/bash
# source set_env.sh .env
# Default to ".env" if no argument is provided
ENV_FILE=${1:-".env"}

# Check if the .env file exists
if [ ! -f "$ENV_FILE" ]; then
    echo "Error: $ENV_FILE does not exist."
    exit 1
fi

# Read each line in the .env file
while IFS= read -r line
do
    # Skip empty lines and lines starting with a comment
    if [ -z "$line" ] || [[ "$line" == \#* ]]; then
        continue
    fi

    # Use eval to handle the export if it's included in the .env file
    if [[ "$line" == EXPORT* ]]; then
        eval "$line"
    else
        export "$line"
    fi
done < "$ENV_FILE"

echo "Environment variables set."
