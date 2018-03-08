from setuptools import setup, find_packages

setup(
    name='optionsGame',
    version='0.1.0',
    author='LAMFO',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    url='https://github.com/lamfo-unb/optionsGame',
    license='LICENSE.txt',
    install_requires=['numpy', 'keras', 'asciimatics', 'pytest'],
    include_package_data=True,
    description=''
)
