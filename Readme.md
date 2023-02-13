
caprover deploy --appToken <YOUR_APP_TOKEN_HERE> --caproverUrl https://captain.magellon.org --imageName khoshbin/magellon-demo01 --appName demo01

docker build -t flask-app .

sudo docker run -it -p3000:5000 flask-app
sudo docker run -d -p3000:5000 flask-app

run command line pytest




docker run -p 80:80 -p 443:443 -p 3000:3000 -v /var/run/docker.sock:/var/run/docker.sock -v /captain:/captain caprover/caprover

