#!/bin/bash

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "Poetry is not installed. Please install Poetry before running this script."
    exit 1
fi

# Read each line from requirements.txt and add to Poetry
while IFS= read -r line; do
    # Skip empty lines and comments
    if [[ -z "$line" || "$line" == \#* ]]; then
        continue
    fi

    # Extract package name and version from the line
    package_name=$(echo "$line" | cut -d '=' -f 1)
    package_version=$(echo "$line" | cut -d '=' -f 2)

    # Add the package to Poetry
    poetry add "$package_name@$package_version"
done < requirements.txt

# Install the dependencies
poetry install
