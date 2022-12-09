**Deploy**

Step 1. Install docker and docker-compose
- `sudo apt update -y`
- `sudo apt upgrade`
- `sudo apt install apt-transport-https ca-certificates curl software-properties-common`
- `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
- `sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"`
- `sudo apt update`
- `sudo apt install docker-ce`
- `sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`
- `sudo chmod +x /usr/local/bin/docker-compose`

Step 2. Project deploy

NOTE: Execute commands in the project folder!
- **up project**: `docker-compose -f deploy.yml up --build -d`
- **down project:** `docker-compose -f deploy.yml up down`
