import os

import setuptools

from glowing_barnacle import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
    name='glowing-barnacle',
    version=__version__,
    description='A GPS App',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    license="GPL-3",
    author='Maxime Barbier',
    author_email='maxime.barbier1991+glowing-barnacle@gmail.com',
    url="https://github.com/Krozark/glowing-barnacle",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        #"BasicSR @ git+https://github.com/xinntao/BasicSR"
        "torch==1.8.0",
        "torchvision==0.9.0",
        "GitPython",
        "dlib",
        "django==3.1.7",
    ],
    python_requires='>=3.8, <=3.9',
    platforms='unix',
    entry_points='''
        [console_scripts]
        gb-setup=glowing_barnacle.dependencies:main
        gb-manage=manage:main
        gb-runserver=manage:runserver
    '''
)
