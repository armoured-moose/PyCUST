import setuptools

setuptools.setup(
    name="PyCUST",
    version="0.0.1",
    packages=setuptools.find_packages(where="PyCUST"),
    package_dir={"": "PyCUST",},
    url="https://github.com/armoured-moose/PyCUST",
    author="Samuel Ward",
    author_email="samuel.ward@york.ac.uk",
    description="Python LOCUST actor for IMAS"
    # long_description=open('README.md').read(),
    # install_requires=['']
)