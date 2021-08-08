![GitHub](https://img.shields.io/github/license/AlphaBeta1906/pyGinit?style=flat-square)
# pyGinit

pyGinit is a command line tools that help you to initialize your current project a local git repo and remote repo

## Requirements
Requirements before install pyGinit:
1. a github account and it's personal acces token
2. git 1.70 or newer
3. python >= 3.7

## Installation
using pip :
```bash
pip install pyGinit
```
from this repository(maybe not stable) :
```bash
git clone  https://github.com/AlphaBeta1906/pyGinit.git
cd path/to/pyGinit
pip install --editable . # install it globally so you can use it everywhere
```

## Usage

### Authentication :
You need to add token and username of your github account using :

```bash
pyginit set-auth <YOUR_GITHUB_TOKEN> <YOUR_GITHUB_USERNAME>
```
use the same command to change your auth value

if you dont know how to get your github token, you can see [this](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)

all your token are save in `.pyGinitconfig.ini` at home path, so you will be secure

### repository initalization : 

go to your project directory where you want to create local and remote repository for it. and then type :
```bash
pyginit init
```
all you need is to fill out inquirer by `pyInquirer` and let `pyGinit` do the rest, from creating local repository,remote github repository, and push your directory to github   
_Note: make sure the directory is not a local git repository_




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://github.com/AlphaBeta1906/pyGinit/blob/master/LICENSE)

## Development status :
[v0.2.1](https://github.com/AlphaBeta1906/pyGinit/releases/tag/v0.2.1)  
[v0.2.0](https://github.com/AlphaBeta1906/pyGinit/releases/tag/v0.2.0)  
[v0.1.9](https://github.com/AlphaBeta1906/pyGinit/releases/tag/v0.1.9)  
[v0.1.7](https://github.com/AlphaBeta1906/pyGinit/releases/tag/V0.1.7)  
[v0.1.6-beta](https://github.com/AlphaBeta1906/pyGinit/releases/tag/v0.1.6-beta)    
[v0.1.5-beta](https://github.com/AlphaBeta1906/pyGinit/releases/tag/v0.1.5-beta)   
[v0.1.3-alpha](https://github.com/AlphaBeta1906/pyGinit/releases/tag/v0.1.3-alpha)   

