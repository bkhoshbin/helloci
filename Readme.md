
caprover deploy --appToken <YOUR_APP_TOKEN_HERE> --caproverUrl https://captain.magellon.org --imageName khoshbin/magellon-demo01 --appName demo01

docker build -t flask-app .

sudo docker run -it -p3000:5000 flask-app
sudo docker run -d -p3000:5000 flask-app

run command line pytest




docker run -p 80:80 -p 443:443 -p 3000:3000 -v /var/run/docker.sock:/var/run/docker.sock -v /captain:/captain caprover/caprover

caprover deploy --appToken 28e1a156f2810859 --caproverUrl https://captain.magellon.org --imageName khoshbin/magellon-demo01 --appName demo01

caprover login
docker pull khoshbin/magellon-demo01
caprover deploy -n demo01 -i khoshbin/magellon-demo01
caprover ps

Your identification has been saved in circleci
Your public key has been saved in circleci.pub
The key fingerprint is:
SHA256:IOZsUMiWzSXjwueYg5gfIxdq+wYT+Gd575skJUnidYQ

cat ~/.ssh/circleci.pub

To get the private key and fingerprint from your remote server for use in your CircleCI config file, you can follow these steps:

    Log in to your remote server using SSH.

    Use the following command to generate an SSH key if you don't already have one: ssh-keygen -t rsa -b 4096

    Follow the prompts to set a name for the key (such as "circleci"), choose a password (or leave it blank if you don't want to use one), and save the key in the default location (usually ~/.ssh/id_rsa).

    Once the key is generated, you can use the following command to display the public key: cat ~/.ssh/id_rsa.pub. Copy the entire contents of the file to your clipboard.

    Go to your CircleCI project settings and click on "SSH Permissions" in the sidebar.

    Click the "Add SSH Key" button and paste the public key you copied in step 4 into the "Hostname" field.

    Choose a name for the key (such as "remote-server"), and click "Add SSH Key".

    The private key will now be available in your CircleCI job as an environment variable named SSH_KEY_<name>_PRIVATE, where <name> is the name you gave the key in step 7.

    To use the private key in your config.yml file, you can add the add_ssh_keys step to your job, as shown in the example in my previous answer. In the fingerprints field, you can include the fingerprint of the private key (which is also displayed in the CircleCI web interface) to ensure that only authorized keys are used to connect to your server.

Note: Be sure to keep your private key secure and do not share it with others. You should also take appropriate security measures to protect your remote server, such as configuring your firewall and using strong passwords.


MySql:

sudo docker run -d --name=mysql2 -e MYSQL_ROOT_PASSWORD=behd1d2 -e MYSQL_USER=behdad -e MYSQL_PASSWORD=behd1d2 -e MYSQL_DATABASE=magellon01 -v /tmp/mysql/data:/var/lib/mysql -p 3306:3306 mysql:latest

mysql as graphql 

ssh-keygen -t ed25519 -C "b.khoshbin@gmail.com"
