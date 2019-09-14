[![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/tanasegabriel/sense-api.svg?style=popout)](https://hub.docker.com/r/tanasegabriel/sense-api)
[![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/tanasegabriel/sense-api.svg?style=popout)](https://hub.docker.com/r/tanasegabriel/sense-api/builds)
[![Docker Pulls](https://img.shields.io/docker/pulls/tanasegabriel/sense-api.svg?color=yellowgreen&style=popout)](https://hub.docker.com/r/tanasegabriel/sense-api)
[![Docker Image Size](https://img.shields.io/microbadger/image-size/tanasegabriel/sense-api?color=blueviolet&style=popout)](https://hub.docker.com/r/tanasegabriel/sense-api/tags)
[![Hardware](https://img.shields.io/badge/hardware-Raspberry_Pi-orange?style=popout)](https://www.raspberrypi.org/)


# SenseAPI
A simple RESTful service built on top of the [SenseHAT Python API module](https://pythonhosted.org/sense-hat/), that runs on Docker.

## Installation

**Before installing** make sure that the Sense Hat is attached to your Raspberry and that I2C is enabled:

`sudo raspi-config` -> `Interfacing options` -> `I2C`

**Setting up the container:**
```bash
docker run -d -p 8000:8000 --privileged --name sense-api --restart on-failure tanasegabriel/sense-api
```

## Usage
Access `http://localhost:8000` in your browser:
![homepage](https://i.imgur.com/0sLC54b.png)


You can use the UI to understand how the API works and to test it out, but programatic requests should be issued on `http://localhost:8000/senseapi/v1/<endpoint>`.
