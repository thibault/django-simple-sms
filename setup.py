import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-simple-sms',
    version='1.0.0',
    packages=['djsms'],
    include_package_data=True,
    license='MIT',
    description='Easily send text messages from your Django project.',
    long_description=README,
    url='https://github.com/thibault/django-simple-sms',
    author='Thibault Jouannic',
    author_email='thibault@miximum.fr',
    setup_requires=('setuptools'),
    install_requires=[
        'libnexmo',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
