"""
This module contains the package installer routine.
"""


def main():
    """Package installer routine.

    Install via: pip install <project-root>

    .. code-block:: none

        cd <project-root>
        pip install . <-e for editable mode where you can edit the package contents>

    :Uninstall via: pip uninstall <setup.py:CONFIG['name']>
    """

    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup

    CONFIG = {
        'description': 'Skeleton for Python Packages',
        'author': 'Joel Tannas',
        'url': 'https://github.com/jtannas/python-skeleton',
        'download_url': 'https://goo.gl/jpBQxg',
        'author_email': 'jtannas@gmail.com',
        'version': '0.1',
        'install_requires': ['mypy'],
        'packages': ['app'],
        'scripts': ['bin/hello'],
        'name': 'py_skeleton',
    }

    setup(**CONFIG)


if __name__ == "__main__":
    main()
