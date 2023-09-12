import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="DockerExec",
    version="1.0",
    author="",
    author_email="",
    description="Docker Compose Exec",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Abvgdejg/DockerExec-Python",
    packages=['DockerExec'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
