import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DroneBlocksTelloSimulator",
    version="0.0.1",
    author="Dennis Baldwin",
    author_email="db@droneblocks.io",
    description="Program a drone with the DroneBlocks Simulator and then deploy to Tello",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dbaldwin/DroneBlocks-Python-Simulator",
    project_urls={
        "Bug Tracker": "https://github.com/dbaldwin/DroneBlocks-Python-Simulator/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)