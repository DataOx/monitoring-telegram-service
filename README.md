### **General information**

A bot for monitoring community activity in Telegram channels.\
One of the projects currently being monitored is [here](https://t.me/mizar_ai).

### ******The purpose of creating a bot****** 

To track activity/participation in Telegram, based on the data received, participants will be rewarded for activity on the client platform.\
The data will be obtained using our tool (bot).\
The bot will constantly track activity in the Telegram channel.

### **Communities must be**

* Monitoring, including messages sent
* Quality of messages
* Days of activity in the channel

### **Bot requirements**

The bot will record the collected data in a data.json file, which will be stored on the server.\
Bot will be configured through a web interface or API.\
The process needs to be automated so that the data is collected on the client platform automatically.   

### **Used libs** 
* psycopg2-binary
* aiogram
* redis
* django

**Project architecture**

![Project architecture](images/project.png "Title")


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




