pyramid_locmako
===============

Pyramid scaffolding with Mako, Internationalization and SQLAlchemy.

Licensed under MIT License.

Overview
========

pyramid_locmako is similar to pyramid's starter scaffold, only
it uses mako as a templating engine, initializes internationalization
and makes slightly more complex directory structure:
* Creates directories for views, models, tests

The distinction to the original alchemy scaffolding is adding 
the request property db for accessing the database session,
which is effectively eliminating the global variable DBSession.

Installing
==========

Has not been pushed to pypi yet, so your only change is probably
to grab it here at github, unpack, then
  python setup.py install

Usage
=====

# before we start:
virtualenv MYENV
cd MYENV
. bin/activate.sh
easy_install pyramid
git clone https://github.com/petrblahos/pyramid_locmako.git
cd pyramid_locmako
python setup.py install
cd ..

# now finally
pcreate -s pyramid_locmako PLM1
# At the end you will be asked which languages you want to initialize.
cd PLM1
python setup.py develop
../bin/initialize_PLM1_db development.ini
pserve development.ini

What now? It is just a pyramid project. If lost head into narrative
documentation at http://pyramid.readthedocs.org/en/latest/


