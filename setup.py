from setuptools import setup

setup(
    name="pyGinit",
    version="0.1.3",
    author="fariz",
    license="MIT",
    py_modules=["main"],
    install_requires=["Click", "PyInquirer", "pyGithub","Colorama"],
    entry_points="""
        [console_scripts]
        pyGinit= pyGinit.main:pyGinit
    """,
)
