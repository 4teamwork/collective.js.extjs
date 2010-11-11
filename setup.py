from setuptools import setup, find_packages
import os

version = open('collective/js/extjs/version.txt').read().strip()
maintainer = 'Victor baumann'

setup(name='collective.js.extjs',
      version=version,
      description="Ext JS Cross-Browser Rich Internet Application Framework \
        (Maintainer: %s)" % maintainer,
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='%s, 4teamwork GmbH'  % maintainer,
      author_email='mailto:info@4teamwork.ch',
      maintainer=maintainer,
      url='http://www.sencha.com/products/js/',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
