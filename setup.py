from setuptools import setup, find_packages

long_description = open('README.md').read()
setup(
    name="pyGinit",
    version="0.2.2",
    description="a simple cli tools for automation git repository creation",
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    long_description_content_type='text/markdown',
    url='https://github.com/AlphaBeta1906/pyGinit',
    download_url=(
        'https://github.com/AlphaBeta1906/pyGinit/archive/refs/tags/0.2.2.tar.gz'
    ),
    author="fariz",
    author_email="farizi1906@gmail.com",
    license="MIT",
    py_modules=["main"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='automation,tools ,cli,git,github,development',
    install_requires=["Click", "PyInquirer", "Gitpython", "pyGithub", "Colorama"],
    entry_points="""
        [console_scripts]
        pyginit= pyGinit.main:pyginit
    """,
    python_requires='>=3.7',
)
