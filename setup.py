from setuptools import setup, find_packages

setup_args = dict(
    name='manyq',
    version='0.0.0',
    description='Fast quantum computer simulator for QML',
    license='MIT',
    packages=find_packages(),
    author='Joaquin Keller',
    author_email='joaquin@entropicalabs.io',
    keywords=['qubit', 'quantum'],
    url='https://entropicalabs.com'
)

install_requires = [
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
