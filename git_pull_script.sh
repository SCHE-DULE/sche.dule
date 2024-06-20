sudo su << ROOT
# Now you are in a root shell

eval $(ssh-agent -s)
export SSH_PASSPHRASE="$SSH_PASSPHRASE"
expect ssh-add-passphrase.exp

# Perform Git commands
git fetch
git pull
git status

# Remove all SSH Agents
sudo pkill -f "ssh-agent"

# Change ownership if necessary
chown ubuntu:ubuntu . -R

# Django Server Restart
pkill -f "python manage.py runserver"
nohup python3 manage.py runserver 0.0.0.0:8080 &

# Install Dependencies
poetry install --with homolog

# Exit the root shell
exit
ROOT

# Exit the script
exit

