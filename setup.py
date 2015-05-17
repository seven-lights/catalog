import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires=['pyramid>=1.4', 'pyramid_jinja2', 'jinja2','sqlalchemy','waitress','pyramid_tm','pyramid_debugtoolbar','zope.sqlalchemy']

setup(name='catalog',
      version='0.0',
      description='catalog',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="catalog",
      entry_points = """\
      [paste.app_factory]
      main = catalog:main
      """,
      paster_plugins=['pyramid'],
      )
