import os
from setuptools import setup
from setuptools import find_packages


def get_version():
    """
    Read version from package __version__ file.
    In setup.py anything from the package itself musn't be imported.
    """
    with open(
        os.path.join('src', 'pypokedexx', '__version__.py'),
        encoding='utf-8'
    ) as version_file:
        for line in version_file:
            if line.startswith('__version__'):
                _, _, version = line.replace("'", '').split()
                return version


setup(
    name='pypokedexx',
    version=get_version(),
    description='Pokédex CLI',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'pypokedexx = pypokedexx.cli:main',
        ]
    },
)
