try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'gesso',
    'author': 'Nick Ephraims',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'nick.ephraims@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['gesso'],
    'scripts': [],
    'name': 'gesso'
}

setup(**config)