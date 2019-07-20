FROM balenalib/rpi-raspbian as intermediate

# Cloning the RTIMUlib repository
RUN apt-get update -y && apt-get install -y git
RUN git clone https://github.com/RPi-Distro/RTIMULib

FROM balenalib/rpi-raspbian
LABEL maintainer="Gabriel Tanase <tanase.gabriel91@gmail.com>"

# Installing system dependencies
RUN apt-get update &&\
    apt-get install -y --no-install-recommends\
    python3 python3-dev python3-virtualenv g++ gcc-arm-linux-gnueabihf libatlas-base-dev libopenjp2-7 libtiff5

# Setting up the virtualenv
ENV VIRTUAL_ENV=/sense-api
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ADD . / sense-api/

# Installing RTIMUlib
COPY --from=intermediate /RTIMULib /RTIMULib
WORKDIR /RTIMULib/Linux/python/
RUN python setup.py build &&\
    python setup.py install
RUN rm -rf /RTIMULib

# Installing dependencies and setting up gunicorn
WORKDIR /sense-api
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "senseapi"]
