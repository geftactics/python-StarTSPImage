from setuptools import setup, find_packages

version = '0.2.3'

setup(
    name='StarTSPImage',
    version=version,
    packages=find_packages(),
    license='MIT',
    description='Creates Star graphics mode raster images for use with Star TSP series thermal printers',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=['Pillow'],
    url='https://github.com/geftactics/python-StarTSPImage',
    download_url = 'https://github.com/geftactics/python-StarTSPImage/archive/' + version + '.tar.gz',
    author='Geoff Kendal',
    author_email='Geoff@squiggle.org'
)
