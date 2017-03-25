import os
import re
import subprocess
import sys
from setuptools import setup

APP = ['inqry.py']
DATA_FILES = []
OPTIONS = {}

VERSION_PY = os.path.join(os.path.dirname(__file__), 'version.py')


def version_getter():
    try:
        pattern = re.compile(r'(v\d+\.\d+\.?\d?).*', re.UNICODE)
        tag = subprocess.check_output(["git", "describe", "--tags"]).rstrip().decode("utf-8")
        return re.findall(pattern, tag)[0]
    except:
        with open(VERSION_PY, 'r') as f:
            return f.read().strip().split('=')[-1].replace('"', '')


def version_writer():
    message = "#  Do not edit this file. Pipeline versioning is governed by git tags."
    with open(VERSION_PY, 'w') as f:
        return f.write(message + os.linesep + "__version__ = '{ver}'".format(ver=version_getter()) + '\n')


def windows_only():
    return ['wmi', 'pypiwin32'] if sys.platform == 'win32' else []


version_writer()

setup(app=APP,
      author=['OXO Hub Lab', 'Eric Hanko', 'Jacob Zaval'],
      author_email='apxlab@microsoft.com',
      data_files=DATA_FILES,
      description='Gets machine specs and generates a QR code containing them',
      install_requires=['qrcode', 'PyYAML', 'Pillow'] + windows_only(),
      license='MIT',
      long_description=open('README.md').read(),
      name='InQRy',
      options={'py2app': OPTIONS},
      packages=['inqry', "inqry.system_specs"],
      setup_requires=['py2app'],
      tests_require=['pytest'],
      url="https://office.visualstudio.com/APEX/Lab-Projects/_git/lab_inventory",
      version="{ver}".format(ver=version_getter()),
      )
