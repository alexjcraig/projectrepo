from setuptools import setup

setup(name='ajcproject',
      version='1.0.',
      description='s23 final project',
      maintainer='Alex Craig',
      maintainer_email='acraig2@andrew.cmu.edu',
      license='MIT',
      packages=['ajcproject'],
      entry_points={'console_scripts': ['oa = ajcproject.main:main']},
      long_description='''This is my final project for the s23 mini 2''')
