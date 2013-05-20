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

pcreate -s pyramid_locmako projectname

At the end you will be asked which languages you want to initialize.

After you have initialized your project, you will of course do the
familiar
  cd projectname
  python setup.py develop
For the initial database creation there is a conveniencescript 
instelled in scripts:
  initialize_projectname_db

