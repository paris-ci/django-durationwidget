import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-durationwidget",
    version="1.0.13",
    author="Devang Padhiyar + paris-ci",
    author_email="devangpadhiyar700@gmail.com",
    description="Django Duration field widget to handle duration field in the form",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paris-ci/django-durationwidget",
    packages=setuptools.find_packages(),
    install_requires=[
        'Django>=4.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
