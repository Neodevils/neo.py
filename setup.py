import setuptools

with open("README.md", "r") as fh:
    # README.md dosyasını oku
    long_description = fh.read()

setuptools.setup(
    name="neopy",
    version="0.0.1",
    author="Neodevils",
    description="discord.py için Türkçe kaynak kodları içeren bir kütüphane",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["neopy"],
    package_dir={'': 'neopy/kaynak-kodlar'},
    install_requires=[]
)
