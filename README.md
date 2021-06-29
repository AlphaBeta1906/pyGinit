[![Python package](https://github.com/AlphaBeta1906/pyGinit/actions/workflows/python-package.yml/badge.svg)](https://github.com/AlphaBeta1906/pyGinit/actions/workflows/python-package.yml)
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
from this repository :
```bash
git clone  https://github.com/AlphaBeta1906/pyGinit.git
cd path/to/pyGinit
pip install --editable . # install it globally so you can use it everywhere
```

## Usage

### authetincation :
You need to add token,username and password of your github account using :

```
pyGinit set-auth <YOUR_GITHUB_TOKEN> <YOUR_GITHUB_USERNAME> <YOUR_GITHUB_PASSWORD>
```
use the same command to change your auth value

### repository initalization : 

go to your porject directory where you want to create local and remote repository for it. and then type :
```
pyGinit init
```
_Note: make sure the directory is not a local git repository_




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/AlphaBeta1906/pyGinit/blob/master/LICENSE)

## Development status :
[v0.1.9](https://github.com/AlphaBeta1906/pyGinit/releases/tag/v0.1.9)  
[v0.1.7](https://github.com/AlphaBeta1906/pyGinit/releases/tag/V0.1.7)  
[v0.1.6-beta](https://github.com/AlphaBeta1906/pyGinit/releases/tag/v0.1.6-beta)    
[v0.1.5-beta](https://github.com/AlphaBeta1906/pyGinit/releases/tag/v0.1.5-beta)   
[v0.1.3-alpha](https://github.com/AlphaBeta1906/pyGinit/releases/tag/v0.1.3-alpha)   

