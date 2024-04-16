python3.9 -m venv blogapienv
source blogapienv/bin/activate
pip install -r requirements.txt 
python3.9 manage.py collectstatic
pip install -r requirements.txt 
python3.9 manage.py collectstatic
