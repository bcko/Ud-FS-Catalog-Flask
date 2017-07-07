from setuptools import setup

setup(
    name='catalog_app',
    packages=['catalog_app'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)