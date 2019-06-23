#!/usr/bin/env python3
import atexit
import pytest
import subprocess

sense_emulator = subprocess.Popen(["sense_play", "tests/sense_fixture.hat"])
atexit.register(sense_emulator.terminate)

gunicorn = subprocess.Popen(["gunicorn", "-b", "127.0.0.1:8000", "senseapi", "emulation"])
atexit.register(gunicorn.terminate)

pytest.main(["tests/test_senseapi.tavern.yaml"])
