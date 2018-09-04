## Requires
1. python3
2. git
3. pip (should have come installed with python)
4. virtualenv (install with `pip install virtualenv`)

## Set up
These instructions are designed for Mac/Linux
1. `git clone` the repo
2. `cd` into the directory you cloned to
3. Create a python virtual environment with `virtualenv venv -p python3`
4. Activate the virtual environment with `source venv/bin/activate` or `venv/Scripts/activate.bat` on Windows
5. Install requirements with `pip install -r blackjack/requirements.txt`
6. Run `cd blackjack` to move into the blackjack folder
7. Run tests with `tox`
8. Go wild!
