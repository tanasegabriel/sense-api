FROM balenalib/rpi-raspbian
LABEL maintainer="Gabriel Tanase <tanase.gabriel91@gmail.com>"

# Installing system dependencies
RUN install_packages\
    python3 python3-pip libatlas-base-dev libopenjp2-7 libtiff5

# Setting up the app
ADD . / sense-api/
WORKDIR /sense-api
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "senseapi"]
