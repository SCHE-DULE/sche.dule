sudo su << ROOT
# Now you are in a root shell

eval $(ssh-agent -s)

expect ssh-add-passphrase.exp

# Perform Git commands
git fetch
git pull
git status

# Change ownership if necessary
chown ubuntu:ubuntu . -R

# Exit the root shell
exit
ROOT

# Exit the script
exit

