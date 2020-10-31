import setuptools

setuptools.setup(
    name="lib",
    version="0.1",
    license="MIT",
    author="Sean Collings",
    author_email="sean@seanrcollings.com",
    packages=setuptools.find_packages("."),
    package_dir={"": "."},
    python_requires=">=3.8",
)
