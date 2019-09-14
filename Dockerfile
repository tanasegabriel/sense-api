FROM balenalib/rpi-raspbian
LABEL maintainer="Gabriel Tanase <tanase.gabriel91@gmail.com>"

# Installing system dependencies
RUN install_packages\
    python3 python3-virtualenv libatlas-base-dev libopenjp2-7 libtiff5

# Setting up the virtualenv
ENV VIRTUAL_ENV=/sense-api
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ADD . / sense-api/

# Installing dependencies and setting up gunicorn
WORKDIR /sense-api
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "senseapi"]
