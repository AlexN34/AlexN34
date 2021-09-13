Title: Docker Compose 
Date: 2018-3-25 09:15
Tags: docker, compose, cheatsheets
Slug: docker-compose
Category: cheatsheets
Author: Alex Nguyen
Summary: Continuing experimentation with Docker using Docker-compose

## Magical scriptable `docker run` commands
I originally picked up Docker as a last ditch attempt to install a contained Python 3.4 environmenfor a work project after the usual approaches of `pyenv` etc were just not working that day. After being impressed by the performance of containerisation I've been keen to stretch into bringing more of my environment into containers in hope of one day achieving a cross-platform setup.

This weekend I made a start compiling some run configs and docker files [here](https://github.com/alexnguyennn/dockerfiles)

I haven't found an ideal way to abstract out system dependent filepaths or test whether these yaml files work the same on both Windows/MacOS/Linux) yet, but for now I'm using predefined environment variables to store mounted volumes.

### Command Lookup
- `docker-compose up <docker-compose.yml>` to spin up instance of container
- `docker-compose down <docker-compose.yml>` for teardown
