try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

CONFIG = {
    'description': 'Skeleton for Python Packages',
    'author': 'Joel Tannas',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'jtannas@gmail.com',
    'version': '0.1',
    'install_requires': [
        'docutils',
        'pytest',
        'virtualenvwrapper',
        'yapf',
    ],
    'packages': ['py_skeleton'],
    'scripts': ['bin/hello'],
    'name': 'py_skeleton',
}

setup(**CONFIG)
