from setuptools import find_packages, setup

setup(
    name="htmlparsing",
    version="0.0.1",
    description="Pure HTML parsing library.",
    author="Jiuli Gao",
    author_email="gaojiuli@gmail.com",
    url='https://github.com/gaojiuli/htmlparsing',
    install_requires=[
        'lxml',
        'html2text',
        'parse'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    license='MIT',
    packages=find_packages(),
    py_modules=['htmlparsing'],
    include_package_data=True,
    zip_safe=False,
)
