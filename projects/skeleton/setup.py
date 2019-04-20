try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'LPTHW',
	'author': 'Michelle',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'Bausager.m@live.dk',
	'version': '0.1',
	'install_requists': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'}

setup(**config)
