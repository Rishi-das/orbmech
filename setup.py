from setuptools import setup, find_packages

setup(
    name='orbmech',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
     author='Rishita Das',
    author_email='rishita2002das@gmail.com',
    description='A Python package for simulating and analyzing orbital mechanics',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Rishi-das/orbmech',
)
