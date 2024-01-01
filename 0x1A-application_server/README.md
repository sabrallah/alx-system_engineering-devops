Application Server Project
This project sets up an application server to serve a Flask application.

Description
The application server is configured using Gunicorn and serves a simple Flask application on port 5000. Nginx is configured as a reverse proxy to route requests from port 80 to the Gunicorn application server.

Contents
0-hello_route.py: Simple Flask application that returns "Hello HBNB"
1-install_gunicorn.sh: Bash script to install Gunicorn
2-run_gunicorn.sh: Bash script to run Gunicorn server
3-nginx_config: Nginx configuration file to proxy requests to Gunicorn
Setup
Install required packages:
Copy code

sudo apt-get update
sudo apt-get install nginx gunicorn python3-flask
Clone this repo:
Copy code

git clone https://github.com/username/application_server.git
Run the Gunicorn server:
Copy code

./2-run_gunicorn.sh
Configure Nginx to proxy requests
Try it out! Make requests to localhost
Author
SABRALLAH YOUSSEF THE GREATEST OF ALL TIMES

Let me know if you would like me to expand or modify the README further. I tried to cover the key points concisely.
