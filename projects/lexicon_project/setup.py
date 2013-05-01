try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup 

config = {
	'description': 'exercise 48 lexicon project',
	'author': 'Sean Shields',
	'url': 'URL to get it at.',
	'download_url': "Where to download it.",
	'author_email': 'sean@dmgctrl.com'
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex48'],
	'scripts': [],
	'name': 'ex48_lexicon_project'
}

setup(**config)