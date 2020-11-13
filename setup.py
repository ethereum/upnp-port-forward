#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)

extras_require = {
    'test': [
        "pytest>=6.0.1",
        "pytest-xdist==2.1.0",
        "tox==3.19.0",
    ],
    'lint': [
        "black==19.10b0",
        "flake8==3.8.3",
        "isort>=4.2.15,<5",
        "mypy==0.770",
        "pydocstyle>=3.0.0,<4",
    ],
    'doc': [
        "Sphinx>=1.6.5,<2",
        "sphinx_rtd_theme>=0.1.9",
        "towncrier>=19.2.0, <20",
    ],
    'dev': [
        "bumpversion>=0.5.3,<1",
        "pytest-watch>=4.1.0,<5",
        "wheel",
        "twine",
        "ipython",
    ],
}

extras_require['dev'] = (
    extras_require['dev'] +  # noqa: W504
    extras_require['test'] +  # noqa: W504
    extras_require['lint'] +  # noqa: W504
    extras_require['doc']
)


with open('./README.md') as readme:
    long_description = readme.read()


setup(
    name='upnp-port-forward',
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version='0.1.2',
    description="""upnp-port-forward: UPnP port forwarding for humans""",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='The Ethereum Foundation',
    author_email='snakecharmers@ethereum.org',
    url='https://github.com/ethereum/upnp-port-forward',
    include_package_data=True,
    install_requires=[
        "netifaces>=0.10.9,<0.11",
        "upnpclient>=0.0.8,<1",
    ],
    python_requires='>=3.6, <4',
    extras_require=extras_require,
    py_modules=['upnp_port_forward'],
    license="MIT",
    zip_safe=False,
    keywords='ethereum',
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={'upnp_port_forward': ['py.typed']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
