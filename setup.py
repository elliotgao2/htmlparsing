from setuptools import setup, find_packages

setup(
    name="htmlparsing",
    version="0.1.4",
    description="Pure HTML parsing library.",
    author="Jiuli Gao",
    author_email="gaojiuli@gmail.com",
    url='https://github.com/gaojiuli/htmlparsing',
    py_modules=['htmlparsing'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'parse',
        'lxml',
        'html2text'
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
