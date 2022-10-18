from setuptools import setup

setup(name="pip-example",
      version="1.0.0",
      license='MIT',
      url='https://github.com/ahmed91abbas/pip-example',
      # install_requires=['requests'],
      packages=['domain'],
      package_dir={'domain': 'src/domain'},
)
