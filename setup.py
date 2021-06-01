from setuptools import setup
long_description = ('README.md')
setup(
    name="pyGinit",
    version="0.1.3",
    description = "a simple cli tools for automation git repository creation",
    long_description = long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AlphaBeta1906/pyGinit',
    author="fariz",
    author_email = "farizi1906@gmail.com",
    license="MIT",
    py_modules=["main"],
    classifiers=[ 
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='automation,tools ,cli,git,github,development',
    install_requires=["Click", "PyInquirer", "pyGithub","Colorama","GitPython"],
    entry_points="""
        [console_scripts]
        pyGinit= pyGinit.main:pyGinit
    """,
    python_requires='>=3.7'
)
