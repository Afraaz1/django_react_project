
# INITIAL STEPS
1. Clone this repository: `gh repo clone Afraaz1/django_react_project`.

# INSTALLATION FOR DJANGO
1. `cd` into `api`:
2. Install [pyenv](https://github.com/yyuu/pyenv#installation).
3. Install [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv#installation).
4. Install Python 3.10.0: `pyenv install 3.10.0`.
5. Create a new virtualenv called `env`: `pyenv virtualenv 3.10.0 env`.
6. Start virtual enviroment using `env\scripts\activate` if your using command prompt or `env\scripts\activate.ps1` if you use powershell
7. Install all dependancies from requirements.txt using `pip install -r /path/to/requirements.txt`
8. Run command Python manage.py runserver

# INSTALLATION FOR REACT

1. `cd` into `frontend`
2. Install dependencies using `npm install`
3. Run server via `npm start`