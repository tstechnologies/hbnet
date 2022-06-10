#!/bin/sh
## FOR USE/TESTED WITH DEBIAN 11 ##
echo "Checking for Updates"
sudo apt update
echo "Applying Updates"
sudo apt upgrade -y
echo "Installing needed packages"
sudo apt -y install apt-transport-https ca-certificates curl wget gnupg2 software-properties-common
echo "Adding Repositories"
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
sudo add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/debian \
$(lsb_release -cs) \
stable"
deb [arch=amd64] https://download.docker.com/linux/debian buster stable
echo "Installing Docker and Docker-Compose"
sudo apt update
sudo apt install -y docker docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
newgrp docker
sudo curl -s https://api.github.com/repos/docker/compose/releases/latest | grep browser_download_url  | grep docker-compose-linux-x86_64 | cut -d '"' -f 4 | wget -qi -
sudo chmod +x docker-compose-linux-x86_64
sudo mv docker-compose-linux-x86_64 /usr/local/bin/docker-compose
sudo curl -L https://raw.githubusercontent.com/docker/compose/master/contrib/completion/bash/docker-compose -o /etc/bash_completion.d/docker-compose
source /etc/bash_completion.d/docker-compose
exit
echo "Install Complete!"
