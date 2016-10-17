'''Eventaully, this file will execute the necessary steps.
For now, it just prints what they are.'''

import os
import re
import shutil
import subprocess
from pathlib import Path
from sys import exit

import colorama
import semantic_version
from semantic_version import Version
from colorama import Fore, Style
from isort import SortImports
from minchin import text
from datetime import datetime

# also requires:
# - green
# - pip
# - setuptools
# - wheel
#
# assumes:
# - git on commandline
# - tests written for green
# - green available on command line
# - a valid `.pypirc` file with credentials for TestPyPI and PyPI
# - your project is already registered on TestPyPi and PyPI

__version__ = "0.1.0"

version_re = re.compile(r"__version__ = [\"\']{1,3}(?P<major>\d+)\.(?P<minor>\d+).(?P<patch>\d+)(?:-(?P<prerelease>[0-9A-Za-z\.]+))?(?:\+[0-9A-Za-z-\.]+)?[\"\']{1,3}")
bare_version_re = re.compile(r"__version__ = [\"\']{1,3}([\.\dA-Za-z+-]*)[\"\']{1,3}")
list_match_re = re.compile(r"(?P<leading>[ \t]*)(?P<mark>[-\*+]) +:\w+:")


def here_directory():
    return(Path.cwd())


def module_name():
    return("colourettu")


def source_directory():
    return(here_directory() / module_name())


def test_directory():
    return(here_directory() / 'tests')


def doc_directory():
    return(here_directory() / 'docs')


def dist_directory():
    return(here_directory() / 'dist')


def version_file():
    return(source_directory() / "__version__.py")


def changelog_file():
    return(here_directory() / 'docs' / "changelog.rst")


def other_dependancies(server, environment):
    """Installs things that need to be in place before installing the main package"""
    server = server.lower()
    # Pillow is not on TestPyPI
    if server is "local":
        pass
    elif server in ["testpypi", "pypitest"]:
        print("  **Install Pillow**")
        subprocess.call([environment + '\\Scripts\\pip.exe', 'install', 'Pillow'], shell=True)
    elif server is "pypi":
        pass
    else:
        print("  **Nothing more to install**")


def server_url(server_name):
    server_name = server_name.lower()
    if server_name in ["testpypi", "pypitest"]:
        return(r"https://testpypi.python.org/pypi")
    elif server_name in ["pypi", ]:
        return(r"https://pypi.python.org/pypi")
    else:
        # we really should throw an error here...
        return()

# //-------------------------------------------------------------------------//


def git_check():
    """Check for uncomitted changes"""
    git_status = subprocess.check_output(['git', 'status', '--porcelain'])
    if len(git_status) is 0:
        print(Fore.GREEN + 'All changes committed' + Style.RESET_ALL)
    else:
        exit(Fore.RED + 'Please commit all files to continue')


def sort_imports(my_dir):
    """Sort Imports

    Assumes `my_dir` is a Pathlib object"""

    for f in my_dir.glob('**/*.py'):
        SortImports(str(f))


def run_tests():
    """Run tests"""
    test_status = subprocess.check_call(['green', str(test_directory()), '-vv'])
    if test_status is not 0:
        exit(Fore.RED + 'Please make all tests pass to continue')


def update_version_number(update_level='patch'):
    """Update version number

    Returns a semantic_version object"""

    """Find current version"""
    temp_file = version_file().parent / ("~" + version_file().name)
    with open(str(temp_file), 'w') as g:
        with open(str(version_file()), 'r') as f:
            for line in f:
                version_matches = bare_version_re.match(line)
                if version_matches:
                    bare_version_str = version_matches.groups(0)[0]
                    if semantic_version.validate(bare_version_str):
                        current_version = Version(bare_version_str)
                        print("{}Current version is {}".format(" "*4, current_version))
                    else:
                        current_version = Version.coerce(bare_version_str)
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
                            current_version = current_version.next_patch()
                            current_version.prerelease = ('dev', )
                    else:
                        exit(Fore.RED + 'Cannot update version in {} mode'.format(update_level))

                    print("{}New version is     {}".format(" "*4, current_version))

                    """Update version number"""
                    line = '__version__ = "{}"'.format(current_version)
                print(line, file=g, end="")
        print('', file=g)  # add a blank line at the end of the file
    shutil.copyfile(str(temp_file), str(version_file()))
    os.remove(str(temp_file))
    return(current_version)


def add_release_to_changelog(version):
    """Add release line at the top of the first list it finds

    Assumes your changelog in managed with `releases`"""
    temp_file = changelog_file().parent / ("~" + changelog_file().name)
    now = datetime.today()
    release_added = False
    with open(str(temp_file), 'w') as g:
        with open(str(changelog_file()), 'r') as f:
            for line in f:
                list_match = list_match_re.match(line)
                if list_match and not release_added:
                    release_line = "{}{} :release:`{} <{}-{:02}-{:02}>`".format(
                                        list_match.group("leading"),
                                        list_match.group("mark"),
                                        version, now.year, now.month, now.day)
                    print(release_line, file=g)
                    release_added = True
                print(line, file=g, end="")
            if not release_added:
                release_line = "{}{} :release:`{} <{}-{:02}-{:02}>`".format(
                                " ", "-", version, now.year, now.month, now.day)
                print(release_line, file=g)
        print('', file=g)  # add a blank line at the end of the file
    shutil.copyfile(str(temp_file), str(changelog_file()))
    os.remove(str(temp_file))


def run_sphinx():
    """Runs Sphinx via it's `make html` command"""
    old_dir = here_directory()
    os.chdir(str(doc_directory()))
    doc_status = subprocess.check_call(['make', 'html'], shell=True)
    os.chdir(str(old_dir))  # go back to former working directory
    if doc_status is not 0:
        exit(Fore.RED + 'Something broke generating your documentation...')


def build_distribution():
    build_status = subprocess.check_call(['python', 'setup.py', 'sdist', 'bdist_egg', 'bdist_wheel'])
    if build_status is not 0:
        exit(Fore.RED + 'Something broke tyring to package your code...')


def check_local_install(version, ext, server="local"):
    all_files = list(dist_directory().glob('*.{}'.format(ext)))
    the_file = all_files[0]
    for f in all_files[1:]:
        if f.stat().st_mtime > the_file.stat().st_mtime:
            the_file = f

    environment = 'env-{}-{}-{}'.format(version, ext, server)
    if server == "local":
        pass
    else:
        # upload to server
        print("  **Uploading**")
        subprocess.call(['twine', 'upload', str(the_file), '-r', server])

    if (here_directory() / environment).exists():
        shutil.rmtree(environment)  # remove directory if it exists
    subprocess.call(['virtualenv', environment])
    if server == "local":
        subprocess.call([environment + '\\Scripts\\pip.exe', 'install', str(the_file)], shell=True)
    else:
        other_dependancies(server, environment)
        print("  **Install from server**")
        subprocess.call([environment + '\\Scripts\\pip.exe', 'install', '-i', server_url(server), module_name() + "==" + str(version)], shell=True)
    print("  **Test version of install package**")
    test_version = subprocess.check_output([environment + '\\Scripts\\python.exe', '-c', "exec(\"\"\"import {0}\\nprint({0}.__version__)\\n\"\"\")".format(module_name())], shell=True)
    test_version = test_version.decode('ascii').strip()
    # print(test_version, type(test_version), type(expected_version))
    if (Version(test_version) == version):
        print('{}{} install {} works!{}'.format(Fore.GREEN, server, ext, Style.RESET_ALL))
    else:
        exit('{}{} install {} broken{}'.format(Fore.RED, server, ext, Style.RESET_ALL))


def print_all_steps():
    # see https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
    print('Tag release')
    print('   tag v(version number)')
    print('   push tag')
    print('Push new documentation')
    print('    cd ..\colourettu-gh-pages')
    print('   (copy changes)')
    print('   git add -a')
    print('   git commit -m "Documentation updated!"')
    print('   cd ..\colourettu')
    print('Push to git repo, including tags')

    # swtich to twine  https://pypi.python.org/pypi/twine/
    # twine upload dist/*

# //-------------------------------------------------------------------------//


def main():
    colorama.init()
    text.title("Minchin 'Make Release' for Python v{}".format(__version__))
    print()
    text.subtitle("Configuration")
    print("base dir     -> {}".format(here_directory()))
    print("source       -> .\{}\\".format(source_directory().relative_to(here_directory())))
    print("test dir     -> .\{}\\".format(test_directory().relative_to(here_directory())))
    print("doc dir      -> .\{}\\".format(doc_directory().relative_to(here_directory())))
    print("version file -> .\{}".format(version_file().relative_to(here_directory())))
    print()

    print()
    text.subtitle("Git -- Clean directory?")
    # git_check()

    print()
    text.subtitle("Sort Import Statements")
    # sort_imports(source_directory())
    # sort_imports(test_directory())

    print()
    text.subtitle("Run Tests")
    # run_tests()

    print()
    text.subtitle("Update Version Number")
    # new_version = update_version_number('patch')
    new_version = update_version_number('prerelease')

    print()
    text.subtitle("Add Release to Changelog")
    # add_release_to_changelog(new_version)

    print()
    text.subtitle("Build Documentation")
    # run_sphinx()

    print()
    text.subtitle("Build Distributions")
    build_distribution()

    # for server in ["local", "testpypi", "pypi"]:
    for server in ["testpypi"]:
        for file_format in ["zip", "whl"]:
            print()
            text.subtitle("Test {} Build {}".format(file_format, server))
            check_local_install(new_version, file_format, server)
    # tests will pass if the local version of colourettu can be imported
    # source files should be moved to a 'src' directory, but this will require
    #    the module to be properly installed to run tests, generate docs, etc.
    #
    # uploads -- you cannot upload a file with the same name. Consider adding
    #    build information to version number to allow retries updating...
    #
    # registering -- does not attempt

    # after everything is done
    # update_version_number('prerelease')

if __name__ == '__main__':
    main()
