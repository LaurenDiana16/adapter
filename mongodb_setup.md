1. Launch and configure EC2 instance, choose a Linux instance (Amazon Linux 2023) and select a security group that allows inbound SSH access to port 22 and inbound access to the MongoDB port 27017

2. Connect to your EC2 instance using your key pair

> ssh -i /path/to/your/key.pem ec2-user@your-instance-public-ip

3. Update the package manager

> sudo dnf upgrade -y

4. Add the MongoDB repository to your system's package sources

> sudo nano /etc/yum.repos.d/mongodb-org-7.0.repo

[mongodb-org-7.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/amazon/2023/mongodb-org/7.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/server-7.0.asc

5. Install the MongoDB package using your package manager

> sudo dnf install -y mongodb-org

6. Edit the MongoDB configuration file at /etc/mongod.conf and modify the bindIp to be 0.0.0.0

> sudo nano /etc/mongod.conf

7. Start and enable MongoDB, status should show running

> sudo systemctl start mongod
> sudo systemctl enable mongod
> sudo systemctl status mongod 
