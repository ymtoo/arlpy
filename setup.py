from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('VERSION') as f:
    version = f.read().replace('\n', '')

setup(
    name='arlpy',
    version=version,
    description='ARL Python Tools',
    long_description=readme,
    author='Mandar Chitre',
    author_email='mandar@arl.nus.edu.sg',
    url='https://github.com/org-arl/arlpy',
    license='BSD (3-clause)',
    keywords='underwater acoustics signal processing communication'
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'numpy>=1.11',
        'scipy>=0.18',
        'utm>=0.4'
    ]
)
