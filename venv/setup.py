from setuptools import setup

setup(name='packed_project',
      version='0.1',
      description='The funniest joke in the world',
      url='https://github.com/johncornelius091/packed_project',
      author='John Chornelius',
      author_email='John Chornelius',
      license='MIT',
      packages=['packed_project'],
      install_requires=[
          'markdown', 'pytest', 'logger'
      ],
      dependency_links=[''],
      zip_safe=False)
