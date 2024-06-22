#!/bin/sh

ssh root@161.35.110.213 <<EOF
  cd jenkins
  git pull 
  source env/bin/activate
  ./manage.py migrate
  sudo systemctl restart nginx
  sudo service gunicorn restart
  sudo service nginx restart
  exit
EOF