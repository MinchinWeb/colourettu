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


def read_requirements(*parts):
    """
    Given a requirements.txt (or similar style file), returns a list of
    requirements.
    Assumes anything after a single '#' on a line is a comment, and ignores
    empty lines.
    """
    requirements = []
    for line in read(*parts).splitlines():
        new_line = re.sub('(\s*)?#.*$',  # the space immediately before the
                                         # hash mark, the hash mark, and
                                         # anything that follows it
                          '',  # replace with a blank string
                          line)
        new_line = re.sub('(\s*)?-r.*$',  # we also can't reference other
                                          # requirement files
                          '',  # replace with a blank string
                          line)
        if new_line:  # i.e. we have a non-zero-length string
            requirements.append(new_line)
    return requirements


##############################################################################
#                          PACKAGE METADATA                                  #
##############################################################################
META_PATH = ['colourettu', '__init__.py']

NAME         = find_meta(*META_PATH, meta_key='title').lower()
VERSION      = find_meta(*META_PATH, meta_key='version')
SHORT_DESC   = find_meta(*META_PATH, meta_key='description')
LONG_DESC    = read('readme.rst')
AUTHOR       = find_meta(*META_PATH, meta_key='author')
AUTHOR_EMAIL = find_meta(*META_PATH, meta_key='email')
URL          = find_meta(*META_PATH, meta_key='url')
LICENSE      = find_meta(*META_PATH, meta_key='license')

PACKAGES     = setuptools.find_packages()

INSTALL_REQUIRES = [
    'pillow >= 8.3.2'
]

EXTRA_REQUIRES = {
    'build': read_requirements('.requirements/build.in'),
    'docs': read_requirements('.requirements/docs.in'),
    'test': read_requirements('.requirements/test.in'),
}

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

# add 'all' key to EXTRA_REQUIRES
all_requires = []
for k, v in EXTRA_REQUIRES.items():
    all_requires.extend(v)
EXTRA_REQUIRES['all'] = all_requires


setuptools.setup(
    name=NAME,
    version=VERSION,
    url=URL,
    license=LICENSE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=SHORT_DESC,
    long_description=LONG_DESC,
    packages=PACKAGES,
    package_data={'': ['readme.rst', 'LICENSE']},
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRA_REQUIRES,
    platforms='any',
    classifiers=CLASSIFIERS,
)
