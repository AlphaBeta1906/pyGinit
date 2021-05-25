from setuptools import setup

setup(
    name="pyGinit",
    version="0.3.1",
    author="fariz",
    license="MIT",
    py_modules=["main"],
    install_requires=["Click", "PyInquirer", "pyGithub"],
    entry_points="""
        [console_scripts]
        pyGinit= pyGinit.main:pyGinit
    """,
)
