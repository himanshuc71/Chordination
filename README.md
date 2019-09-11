# Chordination
Chordination will help directors and choreographers to refine the beautiful artistry known as dance


Demo video: https://youtu.be/UnY9-GNlZ-E

Medium article on the whole design process: https://medium.com/@sophie2220/cs-160-final-project-chordination-36b51fb78059

Tech used: Python, Django, Django databases, HTML, CSS, Javascript, jQuery, Paper.js, Adobe Illustrator (For Logo design)

![](final-project%20image.png)

To run: 

pip3 install websockets django channels channels_redis

To run redis server: 
sudo apt-get install redis-server

sudo systemctl enable redis-server.service

redis-cli

To run the server: 
python3 manage.py runserver 0.0.0.0:3000

django db cmds:

Create user to make changes with django UI: python manage.py createsuperuser

Reset db: python manage.py reset_db (from django_extensions)

