from setuptools import setup

setup(
   name='witokit_new',
   version='0.1.5',
   description='Re-implementation of part of witokit package',
   author='Tomas Mlynar',
   author_email='tomas@mlynar.ml',
   packages=['witokit_new', 'witokit_new.utils'],  #same as name
   #install_requires=['tqdm', 'bs4', 'bz2'], #external packages as dependencies
)
