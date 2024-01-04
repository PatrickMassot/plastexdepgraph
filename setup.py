import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plastexdepgraph",
    version="0.0.1",
    author="Patrick Massot",
    description="Dependency graph plasTeX plugin.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_data={'plastexdepgraph': ['static/*', 'templates/*', 'Packages/*',
                                    'Packages/renderer_templates/*']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"],
    python_requires='>=3.7',
    install_requires=['plasTeX>=3.0', 'pygraphviz']
)
