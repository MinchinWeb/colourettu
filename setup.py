import codecs
import os
import re

import setuptools


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_meta(*meta_file_parts, meta_key):
    """
    Extract __*meta*__ from meta_file
    """
    meta_file = read(*meta_file_parts)
    meta_match = re.search(r"^__{}__ = ['\"]([^'\"]*)['\"]".format(meta_key),
                           meta_file, re.M)
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{}__ string.".format(meta_key))


##############################################################################
#                          PACKAGE METADATA                                  #
##############################################################################
META_PATH = ['colourettu', '__init__.py']

NAME         = find_meta(*META_PATH, meta_key='title')
VERSION      = find_meta(*META_PATH, meta_key='version')
SHORT_DESC   = find_meta(*META_PATH, meta_key='description')
LONG_DESC    = read('readme.rst')
AUTHOR       = find_meta(*META_PATH, meta_key='author')
AUTHOR_EMAIL = find_meta(*META_PATH, meta_key='email')
URL          = find_meta(*META_PATH, meta_key='url')
LICENSE      = find_meta(*META_PATH, meta_key='license')

PACKAGES     = setuptools.find_packages()

INSTALL_REQUIRES = [
    'Pillow'
]

# full list of Classifiers at
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    #   having an unknown classifier should keep PyPI from accepting the
    #   package as an upload
    # 'Private :: Do Not Upload',

    # 'Development Status :: 1 - Planning',
    # 'Development Status :: 2 - Pre-Alpha',
    # 'Development Status :: 3 - Alpha',
    # 'Development Status :: 4 - Beta',
    'Development Status :: 5 - Production/Stable',
    # 'Development Status :: 6 - Mature',
    # 'Development Status :: 7 - Inactive',

    # 'Programming Language :: Python :: 2',
    # 'Programming Language :: Python :: 2.6',
    # 'Programming Language :: Python :: 2.7',
    # 'Programming Language :: Python :: 2 :: Only',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    # 'Programming Language :: Python :: 3 :: Only',

    'Natural Language :: English',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Multimedia :: Graphics',
]
##############################################################################

if LICENSE in ['MIT License']:
    CLASSIFIERS += ['License :: OSI Approved :: {}'.format(LICENSE)]


setuptools.setup(
    name=NAME,
    version=VERSION,
    url=URL,
    license=LICENSE,
    author=AUTHOR,
    install_requires=INSTALL_REQUIRES,
    author_email=AUTHOR_EMAIL,
    description=SHORT_DESC,
    long_description=LONG_DESC,
    packages=PACKAGES,
    package_data={'': ['readme.rst', 'LICENSE']},
    include_package_data=True,
    platforms='any',
    classifiers=CLASSIFIERS,
)
