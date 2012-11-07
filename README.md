pyramid_locmako
===============

Pyramid scaffolding with Mako and Internationalization

Licensed under MIT License.

Expect things to change!!! Now, the contents of the page has been
taken from pyramid's own starter template. I expect that will
change completely. I also want to add some more templates into 
this package supporting:
* mongodb
* sqlalchemy
* webassets
* ...some other concepts I find useful mainly for myself...

Overview
========

pyramid_locmako is similar to pyramid's starter scaffold, only
it uses mako as a templating engine, initializes internationalization
and makes slightly more complex directory structure:
* Creates a directory views for views
* Creates a directory tests for tests

Installing
==========

Has not been pushed to pypi yet, so your only change is probably
to grab it here at github, unpack, then
  python setup.py install

Usage
=====

pcreate -s pyramid_locmako

At the end you will be asked which languages you want to initialize.


