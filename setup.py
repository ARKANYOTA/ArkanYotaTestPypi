from distutils.core import setup
setup(
  name = 'ArkanYotaTestPypi',         # How you named your package folder (MyLib)
  packages = ['ArkanYotaTestPypi'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Test Pypi',   # Give a short description about your library
  author = 'ARKANYOTA',                   # Type in your name
  author_email = 'lesarktime@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/ARKANYOTA',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ARKANYOTA/ArkanYotaTestPypi/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Test', 'Upload', 'Pypi'],   # Keywords that define your package best
  install_requires=[''],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
