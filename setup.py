import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DroneBlocksTelloSimulator",
    version="0.0.5",
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
    install_requires=['paho-mqtt>=1.6.1'],
    python_requires=">=3.6"
)

# python3 -m venv venv
# source venv/bin/activate
# python -m pip install --upgrade build
# python -m build
# python -m pip install --upgrade twine
# python -m twine upload dist/*