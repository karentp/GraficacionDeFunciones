#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Karen Dayana Tovar Parra",
    author_email='tovarparrakaren@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Pequeño proyecto en Python para graficar funciones y sus derivadas hasta de segundo orden. ",
    entry_points={
        'console_scripts': [
            'graficacion_de_funciones_en_python=graficacion_de_funciones_en_python.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='graficacion_de_funciones_en_python',
    name='graficacion_de_funciones_en_python',
    packages=find_packages(include=['graficacion_de_funciones_en_python', 'graficacion_de_funciones_en_python.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/karentp/graficacion_de_funciones_en_python',
    version='0.1.0',
    zip_safe=False,
)
