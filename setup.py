"""pyramid_mongodb installation script.
"""
import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README")).read()
README = README.split("\n\n", 1)[0] + "\n"

requires = [
    "pyramid",
    "mako",
    "Babel", "lingua",
    ]

entry_points = """
    [pyramid.scaffold]
    pyramid_locmako = pyramid_locmako.scaffolds:LocmakoTemplate
"""

setup(name="pyramid_locmako",
      version="0.2",
      description="Pyramid application template with mako and localization.",
      long_description=README,
      #long_description=README + "\n\n" +  CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Pylons",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        ],
      keywords="web wsgi pylons pyramid mako i18n",
      author="Petr Blahos",
      author_email="petrblahos@gmail.com",
      url="https://github.com/petrblahos/pyramid_locmako",
      license="MIT",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      tests_require = requires,
      install_requires = requires,
      test_suite="pyramid_locmako",
      entry_points=entry_points,
      )

