from setuptools import setup, find_packages

setup_args = dict(
    name='manyq',
    version='0.0.2',
    description='Fast quantum computer simulator for Quantum Machine Learning',
    license='Apache 2.0',
    packages=find_packages(),
    author='Joaquin Keller',
    author_email='joaquin.keller@gmail.com',
    keywords=['qubit', 'quantum'],
    url='https://github.com/JoaquinKeller/manyQ',
    classifiers=[
        'Development Status :: 4 - Beta', 'License :: OSI Approved :: Apache Software License','Programming Language :: Python :: 3'
    ]
)

install_requires = [
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
