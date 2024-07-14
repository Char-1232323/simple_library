from setuptools import setup, find_packages

setup(
    name='simple_library',
    version='0.1.0',
    author='Zha Fei',
    author_email='2164242181@qq.com',
    packages=find_packages(),
    description='A simple example library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Char-1232323/simple_library',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)