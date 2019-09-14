[![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/tanasegabriel/sense-api.svg)](https://hub.docker.com/r/tanasegabriel/sense-api/builds)
[![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/tanasegabriel/sense-api.svg)](https://hub.docker.com/r/tanasegabriel/sense-api)
[![Commit SHA](https://images.microbadger.com/badges/commit/tanasegabriel/sense-api.svg)](https://github.com/tanasegabriel/sense-api/commits/master)
[![Size & Layers](https://images.microbadger.com/badges/image/tanasegabriel/sense-api.svg)](https://hub.docker.com/r/tanasegabriel/sense-api/tags)
[![Docker Pulls](https://img.shields.io/docker/pulls/tanasegabriel/sense-api.svg?color=yellowgreen)](https://hub.docker.com/r/tanasegabriel/sense-api)
[![Hardware](https://img.shields.io/badge/hardware-Raspberry_Pi-purple)](https://www.raspberrypi.org/)

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
