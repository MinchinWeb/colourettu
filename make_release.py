'''Eventaully, this file will execute the necessary steps.
For now, it just prints what they are.'''

print('Commit current changes')
print('Update version number in __init__.py')
print('Test pass?')
print('    run `green test -vv`')
print('Update documenation')
print('    cd docs')
print('    make html')
print('    index.html')
print('    cd ..')
print('Build distribution')
print('    python -m pip install pip -U')
print('    pip install setuptools twine -U')
print('    python setup.py sdist bdist_egg bdist_wheel')
print('Test distribution')
# see https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
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
