# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['passd']

package_data = \
{'': ['*']}

install_requires = \
['dmenu>=0.2.1,<0.3.0',
 'pypass @ git+https://github.com/aviau/python-pass.git@master',
 'pyperclip>=1.8.2,<2.0.0']

entry_points = \
{'console_scripts': ['passd = passd.cli:run']}

setup_kwargs = {
    'name': 'passd',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Max Campbell',
    'author_email': 'me@0m.ax',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

