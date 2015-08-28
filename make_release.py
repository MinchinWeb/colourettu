'''Eventaully, this file will execute the necessary steps.
For now, it just prints what they are.'''

import re
import subprocess
from sys import exit

import colorama
from colorama import Fore, Style
from minchin import text

# also requires:
# isort
# git on commandline

__version__ = "0.1.0"

version_re = re.compile(r"__version__ = [\"\']{1,3}(?P<major>\d+)\.(?P<minor>\d+)(.(?P<bug>\d+))?[-\.\w\s]*[\"\']{1,3}")


def source_directory():
    return("colourettu")


def test_directory():
    return('tests')


def version_file():
    return(source_directory() + "\\__init__.py")


def main():
    colorama.init()
    text.title("Minchin Make Release v{}".format(__version__))

    """Check for uncomitted changes"""
    git_status = subprocess.check_output(['git', 'status', '--porcelain'])
    if len(git_status) is 0:
        print(Fore.GREEN + 'All changes committed' + Style.RESET_ALL)
    else:
        exit(Fore.RED + 'Please commit all files to continue')

    """Sort Imports"""
    import_status = subprocess.check_output(['isort', '-rc', source_directory()])
    print('{}{}'.format(" "*4, import_status.decode('ascii')))

    """Run tests"""
    test_status = subprocess.check_call(['green', test_directory(), '-vv'])
    if test_status is not 0:
        exit(Fore.RED + 'Please make all tests pass to continue')

    """Update version number"""
    with open(version_file(), 'r') as f:
        print(f)
    current_version = ''

    print('Update version number in __init__.py')  # use `bumpversion` ?? -- https://pypi.python.org/pypi/bumpversion

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

if __name__ == '__main__':
    main()
