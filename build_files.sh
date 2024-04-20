sudo apt-get install --reinstall python-pkg-resources
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade distribute 
python3 -m pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py collectstatic