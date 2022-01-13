import setuptools
from distutils.core import setup

with open('README.md', encoding="utf-8") as f:
    readme = f.read()

setup(
    name="sarveillance",
    version="0.0.1",
    description="Sentinel-1 SAR time series analysis for OSINT use",
    long_description=readme,
    long_description_content_type='text/markdown',
    url="https://github.com/MJCruickshank/SARveillance",
    author="MJCruickshank",
    license="MIT",
    classifiers=["Development Status :: 2 - Pre-Alpha",
                 "Programming Language :: Python :: 3"],
    keywords="sattelite, surveillance, SAR, radar, remote sensing",
    project_urls={
        "Documentation": "https://github.com/MJCruickshank/SARveillance/blob/main/README.md",
        "Source": "https://github.com/MJCruickshank/SARveillance",
        "Tracker": "https://github.com/MJCruickshank/SARveillance/issues",
    },
    packages=["sarveillance"],
    python_requires=">=3.9",
    setup_requires=["wheel"],
    install_requires=[
        "scipy",
        "pyproj>=3.2.1",
        "numpy>=1.22.0",
        "geemap>=0.11.0",
        "pandas>=1.3.5",
        "shapely",   # --no-binary shapely
        "streamlit",    
    ],
    entry_points={
        "console_scripts": [
            # command = package.module:function
            "sarveillance = sarveillance.cli:main",
        ],
    },
    package_data={"sarveillance": [
        "bases_df.csv",
    ]},
)
