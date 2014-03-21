from setuptools import setup
 
setup(
    name = 'jsonxmlconverter',
    packages = ['jsonxmlconverter'],
    version = '0.0.1',
    description = 'Converts JSON file into XML',
    author='Sreejith Sreekantan',
    author_email='krssreejith@gmail.com',
    url='https://github.com/sreejithsreekantan/jsonxmlconverter',
    license='LICENSE.txt',
    long_description=open('README.txt').read(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    install_requires=[
        "sys",
        "getopt",
        "json"
    ]
)
