from setuptools import setup, find_packages


setup(
    name='rison',
    version='0.0.1',
    description='A Python rison encoder/decoder',
    long_description='A Python rison encoder/decoder',
    url='https://github.com/pifantastic/python-rison',
    author='Aaron Forsander',
    author_email='aaron.forsander@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Encoding',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='rison',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    extras_require={
        'test': ['nose'],
    }
)
