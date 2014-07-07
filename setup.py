from setuptools import setup

setup(
    name='hello',
    packages=['hello'],
    include_package_data=True,
    install_requires=[
    'flask',
    ],
)