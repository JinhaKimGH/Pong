from setuptools import setup

APP = ['PongGame.py']
DATA_FILES = []
OPTIONS = {
 'iconfile':'pong.icns',
 'argv_emulation': True,
 'packages': ['certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)