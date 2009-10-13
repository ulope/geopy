from setuptools import setup, find_packages

setup(name='geopy',
      version='0.93-f1',
      description='Python Geocoding Toolbox',
      author='Brian Beck',
      author_email='exogen@gmail.com',
      url='http://github.com/ulope/geopy',
      download_url='git://github.com/ulope/geopy.git',
      packages=find_packages(),
      license='MIT',
      keywords='geocode geocoding gis geographical maps earth distance',
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "Intended Audience :: Science/Research",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Scientific/Engineering :: GIS",
                   "Topic :: Software Development :: Libraries :: Python Modules"
                   ],
     )
