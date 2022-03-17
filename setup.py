from distutils.core import setup
from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Create ACOPOStrak resources for training, meetings, mappView widgets, etc...'

setup(
  name = 'PyAcpTrak',
  version = VERSION,
  license='MIT',
  description = DESCRIPTION,
  packages = find_packages(),
  author = 'HeytalePazguato (Jorge Centeno)',
  author_email = 'Heytale.Pazguato@gmail.com',
  url = 'https://github.com/HeytalePazguato/PyAcpTrak',
  download_url = 'https://github.com/HeytalePazguato/PyAcpTrak/archive/refs/tags/v0_0_2.tar.gz',    # I explain this later on
  keywords = ['ACOPOStrak', 'ACPTrak', 'PyAcpTrak', 'python'],
  install_requires=[
          'svgutils',
          'numpy',
          'IPython',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9',
    'Operating System :: Microsoft :: Windows',
  ],
)
