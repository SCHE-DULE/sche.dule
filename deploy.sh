#!/bin/bash

# Set the path to your private key file
SSH_KEY=${ACCESS_KEY}

TMP_SSH_KEY_FILE=$(mktemp)

# Retrieve the SSH private key from the secret variable and write it to the temporary file
echo "$SSH_KEY" > "$TMP_SSH_KEY_FILE"

# Set the permissions for the temporary key file
chmod 600 "$TMP_SSH_KEY_FILE"

# Set the SSH username and hostname of your remote server
SSH_USER=${SSH_USER}
SSH_HOST=${SSH_HOST}

# Set the path to your Git repository on the remote server
GIT_REPO_PATH=${GIT_REPO_PATH}

SSH into the remote server and run Git commands
ssh -o StrictHostKeyChecking=no -i "$TMP_SSH_KEY_FILE" "$SSH_USER@$SSH_HOST" << EOF
  cd "$GIT_REPO_PATH"
  $(pwd)
  sudo su
  $(pwd)
  eval $(ssh-agent -s)
  ./ssh-add-passphrase.exp
  git fetch
  git pull
  chown ubuntu:ubuntu . -R
EOF