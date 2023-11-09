#!/bin/bash

docker volume create --driver local --opt type=none device=./report o=bind myapp
docker compose up --build 