from setuptools import setup, find_packages

long_description = (
    open("README.rst", encoding="utf-8").read()
    + "\n\n"
    + open("CHANGES.rst", encoding="utf-8").read()
)

setup(
    name="more.jsonschema",
    version="0.3.dev0",
    description="JSON Schema support for Morepath",
    long_description=long_description,
    author="Henri Hulski",
    author_email="henri.hulski@gazeta.pl",
    keywords="morepath validation",
    license="BSD",
    url="https://github.com/morepath/more.jsonschema",
    namespace_packages=["more"],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    install_requires=["morepath >= 0.19", "jsonschema >= 3.2.0"],
    extras_require=dict(
        test=["pytest >= 2.9.1", "pytest-remove-stale-bytecode", "webtest"],
        coverage=["pytest-cov"],
    ),
)
