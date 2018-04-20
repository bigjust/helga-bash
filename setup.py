from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name="helga-bash",
    version=version,
    description=('like hulk-smash, but saves memorable quotes in a db'),
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='irc bot bash',
    author='Justin Caratzas',
    author_email='bigjust@lambdaphil.es',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['helga_bash'],
    zip_safe=True,
    entry_points = dict(
        helga_plugins = [
            'bash = helga_bash:bash',
        ],
    ),
)
