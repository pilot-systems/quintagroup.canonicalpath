# -*- coding: utf-8 -*-
"""
This module contains the tool of quintagroup.seoptimizer
"""
import os

from setuptools import find_packages, setup

version = '0.8'

setup(name='quintagroup.seoptimizer',
      version=version,
      description="Quintagroup Search Engine Optimization Tool",
      long_description="",

      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Framework :: Plone :: 5.2",
          "Framework :: Zope2",
          "Framework :: Zope3",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
          "Operating System :: OS Independent",
          "Development Status :: 5 - Production/Stable",
      ],
      keywords='web zope plone seo search optimization',
      author='Myroslav Opyr, Volodymyr Romaniuk, Mykola Kharechko, '
             'Vitaliy Podoba, Volodymyr Cherepanyak, Taras Melnychuk, '
             'Vitaliy Stepanov, Andriy Mylenkyy',
      author_email='support@quintagroup.com',
      url='http://quintagroup.com/services/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['quintagroup'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
