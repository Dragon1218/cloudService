# setup.py

from setuptools import setup, find_packages

setup(
    name='cloudService',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
    entry_points={
        'console_scripts': [
            'cloudService=cloudService.app:main',
        ],
    },
    author='Zivan Stanojevic',
    author_email='flyhorse0329@gmail.com',
    description='A simple Flask Hello World app packaged as a Python package',
    url='https://github.com/Dragon1218/cloudService',  # Replace with your GitHub repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
