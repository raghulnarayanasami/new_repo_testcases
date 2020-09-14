#!/bin/bash
cd /root
source env/bin/activate
kill -9 $(lsof -ti :8001)
nohup python manage.py runserver 0.0.0.0:8000 >> /root/demoproject/event.log &
echo 'Done'
echo 'Done'
