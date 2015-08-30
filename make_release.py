'''Eventaully, this file will execute the necessary steps.
For now, it just prints what they are.'''

import re
import subprocess
from sys import exit

import colorama
from colorama import Fore, Style
from minchin import text
from pathlib import Path
import os
import semantic_version

# also requires:
# isort
# git on commandline

__version__ = "0.1.0"

version_re = re.compile(r"__version__ = [\"\']{1,3}(?P<major>\d+)\.(?P<minor>\d+).(?P<patch>\d+)(?:-(?P<prerelease>[0-9A-Za-z\.]+))?(?:\+[0-9A-Za-z-\.]+)?[\"\']{1,3}")
bare_version_re = re.compile(r"__version__ = [\"\']{1,3}([\.\dA-Za-z+-]*)[\"\']{1,3}")


def here_directory():
    return(Path(os.getcwd()))


def source_directory():
    return(here_directory() / "colourettu")


def test_directory():
    return(here_directory() / 'tests')


def version_file():
    return(source_directory() / "__init__.py")


def git_check():
    """Check for uncomitted changes"""
    git_status = subprocess.check_output(['git', 'status', '--porcelain'])
    if len(git_status) is 0:
        print(Fore.GREEN + 'All changes committed' + Style.RESET_ALL)
    else:
        exit(Fore.RED + 'Please commit all files to continue')


def sort_imports(my_dir):
    """Sort Imports"""

    import_status = subprocess.check_output(['isort', '-rc', my_dir])
    print('{}{}'.format(" "*4, import_status.decode('ascii')))


def run_tests():
    """Run tests"""
    text.clock_on_right('Run tests')
    test_status = subprocess.check_call(['green', str(test_directory()), '-vv'])
    if test_status is not 0:
        exit(Fore.RED + 'Please make all tests pass to continue')


def update_version_number(update_level='patch'):
    """Update version number"""
    text.clock_on_right('Update version number')

    """Find current version"""
    with open(str(version_file()), 'r') as f:
        for line in f:
            version_matches = bare_version_re.match(line)
            if version_matches:
                bare_version_str = version_matches.groups(0)[0]
                if semantic_version.validate(bare_version_str):
                    current_version = semantic_version.Version(bare_version_str)
                    print("{}Current version is {}".format(" "*4, current_version))
                else:
                    current_version = semantic_version.Version.coerce(bare_version_str)
                    if not text.query_yes_quit("{}I think the version is {}. Use it?".format(" "*4, current_version), default="yes"):
                        exit(Fore.RED + 'Please set an initial version number to continue')

    """Determine new version number"""
    if update_level is 'major':
        current_version = current_version.next_major()
    elif update_level is 'minor':
        current_version = current_version.next_minor()
    elif update_level is 'patch':
        current_version = current_version.next_patch()
    elif update_level is 'prerelease':
        if not current_version.prerelease:
            current_version.prerelease = ('dev', )
    else:
        exit(Fore.RED + 'Cannot update version in {} mode'.format(update_level))

    print("{}New version is {}".format(" "*4, current_version))

    """Update version number"""


def print_all_steps():
    print('Update documenation')
    print('    cd docs')
    print('    make html')
    print('    index.html')
    print('    cd ..')
    print('Build distribution')
    print('    python -m pip install pip -U')
    print('    pip install setuptools wheel twine -U')
    print('    python setup.py sdist bdist_egg bdist_wheel')
    print('Test distribution')
    # see https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
    # use `vex` for virtual envs?
    print('Push new documentation')
    print('    cd ..\colourettu-gh-pages')
    print('   (copy changes)')
    print('   git add -a')
    print('   git commit -m "Documentation updated!"')
    print('   cd ..\colourettu')
    print('Push to test PyPI')
    print('    python setup.py sdist upload -r pypitest')
    print('    pip install -i https://testpypi.python.org/pypi [package-name]')
    print('    everything working?')
    print('Push to real PyPI')
    print('    python setup.py sdist upload -r pypi')
    print('    python setup.py bdist_wheel upload -r pypi')
    print('    everything working??')
    print('Tag release')
    print('   tag v(version number)')
    print('   push tag')

    # swtich to twine  https://pypi.python.org/pypi/twine/
    # twine upload dist/*


def main():
    colorama.init()
    text.title("Minchin 'Make Release' for Python v{}".format(__version__))
    print("base dir     -> {}".format(here_directory()))
    print("source       -> .\{}\\".format(source_directory().relative_to(here_directory())))
    print("test dir     -> .\{}\\".format(test_directory().relative_to(here_directory())))
    print("version file -> .\{}".format(version_file().relative_to(here_directory())))
    print()

    # git_check()
    # text.clock_on_right('Sort import statements')
    # sort_imports(str(source_directory()))
    # sort_imports(str(test_directory()))
    # run_tests()
    update_version_number('patch')

    # after everything is done
    update_version_number('prerelease')

if __name__ == '__main__':
    main()
