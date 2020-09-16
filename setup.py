from setuptools import setup

setup(
        name='fix_wrapper',     # package name
        version='1.0',  
        description='This is python package for fix wrapper', 
        url='https://github.com/Joannazhx/FIX_wrapper',  
        author='Joanna',  
        packages=['src'],                 
        install_requires=[
            'numpy==1.19.0',
            'pandas==1.1.1',
            'pep8==1.7.1',
            'pylint==2.6.0'
        ],
        classifiers = [

        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        ]
)