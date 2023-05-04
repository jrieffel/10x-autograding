#!/usr/bin/env bash

cd /autograder/source

apt-get install -y python3 python3-pip python3-dev

ls -al

mkdir -p /root/.ssh
cp ssh_config /root/.ssh/config
# Make sure to include your private key here
cp deploy_key /root/.ssh/deploy_key
chmod 400 /root/.ssh/deploy_key
# To prevent host key verification errors at runtime
ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts

# Clone autograder files
git clone git@github.com:jrieffel/10x-autograding.git
# Install python dependencies
pip install gradescope-utils
