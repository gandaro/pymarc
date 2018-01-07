version = '3.1.7'

from setuptools import setup

classifiers = """
Intended Audience :: Education
Intended Audience :: Developers
Intended Audience :: Information Technology
License :: OSI Approved :: BSD License
Programming Language :: Python
Topic :: Text Processing :: General
"""

setup(
    name='pymarc',
    version=version,
    url='http://github.com/edsu/pymarc',
    author='Ed Summers',
    author_email='ehs@pobox.com',
    license='http://www.opensource.org/licenses/bsd-license.php',
    packages=['pymarc'],
    install_requires=['six>=1.11.0'],
    description='read, write and modify MARC bibliographic data',
    classifiers=list(filter(None, classifiers.split('\n'))),
    test_suite='test',
)
