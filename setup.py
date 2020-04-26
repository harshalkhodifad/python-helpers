import setuptools
#with open("README.md", "r") as fh:
#    long_description = fh.read()
setuptools.setup(
     name='hello',  
     version='0.3',
     scripts=[] ,
     author="Harshal K",
     author_email="harshalvkhodifad@gmail.com",
     description="Just for fun",
     long_description="# For Fun",
   long_description_content_type="text/markdown",
     url="https://github.com/harshalkhodifad",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: Self Approved :: No License",
         "Operating System :: OS Independent",
     ],
 )
