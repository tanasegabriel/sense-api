FROM balenalib/rpi-raspbian

# Installing system dependencies
RUN install_packages \
    python3 python3-pip libatlas-base-dev libopenjp2-7 libtiff5

# Installing requirements
WORKDIR /sense-api
ADD requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Setting up the app
ADD . .
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "senseapi"]

# Setting up labels
ARG BUILD_DATE
ARG VCS_REF

LABEL maintainer="Gabriel Tanase <tanase.gabriel91@gmail.com>" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="SenseAPI" \
      org.label-schema.description="A simple RESTful service built on top of the SenseHAT Python API module, that runs on Docker" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/tanasegabriel/sense-api" \
      org.label-schema.schema-version="1.0"
