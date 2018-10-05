from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='packed_project',
    version='0.1',
    description='The funniest joke in the world',
    long_description=readme(),
    url='https://github.com/johncornelius091/packed_project',
    author='John Chornelius',
    author_email='John Chornelius',
    license='MIT',
    packages=['packed_project'],
    install_requires=[
      'markdown', 'pytest', 'logger', 'xlrd'
    ],
    tests_require=['pytest'],
    setup_requires=['pytest-runner'],
    extras_require={
        'testing': ['pytest', 'pytest-timeout'],
    },
    dependency_links=[''],
    zip_safe=False
)
