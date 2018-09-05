#!/usr/bin/env bash
cd /root/liveinconcert
docker-compose exec django /code/manage.py spotify
docker-compose exec django /code/manage.py songkick
docker-compose exec django /code/manage.py update_rsvp
