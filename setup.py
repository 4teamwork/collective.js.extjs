from setuptools import setup, find_packages
import os

version = '1.3.0'

setup(name='collective.js.extjs',
      version=version,
      description='Ext JS 3.4 integration for Plone.',

      long_description=(
        open('README.rst').read() + '\n' +
        open(os.path.join('docs', 'HISTORY.txt')).read()),

      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Programming Language :: Python',
        'Framework :: Plone',
        'Framework :: Plone :: 4.1',
        'Framework :: Plone :: 4.2',
        ],

      keywords='extjs plone',
      author='4teamwork AG',
      author_email='mailto:info@4teamwork.ch',
      url='https://github.com/4teamwork/collective.js.extjs',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        ],

      entry_points='''
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      ''',
      )
