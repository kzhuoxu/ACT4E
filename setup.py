from setuptools import find_packages, setup

setup(
name='ACT4E-MySolutions',
version="0.1",
package_dir={'': 'src'},
packages=find_packages('src'),
entry_points={},
extras_require={},
install_requires=['ACT4E-exercises'],
)
