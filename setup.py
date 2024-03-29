import os
import setuptools

# from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

version = os.environ.get('MODULE_VERSION', '0.0.0')

setuptools.setup(
    name='django-ubigeo',
    version=version,
    packages=setuptools.find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to validate peru ubigeo',
    long_description=README,
    url='https://www.softlabperu.com/',
    author='Jason lazolock',
    author_email='jlazolock@softlabperu.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: X.Y',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
