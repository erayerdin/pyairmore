try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import pyairmore

with open("README.md", "r") as f:
    README = f.read()

with open("requirements.txt", "r") as f:
    DEPS = f.readlines()

setup(
    name="pyairmore",
    version=pyairmore.__version__,
    description="PyAirmore is a communication layer between an Android Airmore server and the client.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/erayerdin/pyairmore",
    download_url="https://github.com/erayerdin/exceptive/archive/master.zip",
    packages=["pyairmore"],
    include_package_data=True,
    keywords="python android airmore pyairmore",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development",
        "Topic :: System :: Networking :: Monitoring",
    ],
    author=pyairmore.__author__,
    author_email="eraygezer.94@gmail.com",
    license="Apache License 2.0",
    tests_require=["nose", "tox", "coverage"],
    install_requires=DEPS,
    zip_safe=False
)
