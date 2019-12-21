#!/usr/bin/env python3
import connexion
from flask import redirect

application = connexion.App(__name__, specification_dir='./')
application.add_api('specification.yml')


@application.route('/')
def home():
  return redirect('senseapi/v1/ui/')


if __name__ == '__main__':
  application.run(host='0.0.0.0')
