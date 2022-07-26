# Instawork project backend by: - Pooja Vijayan
emailId: - poojanair388@gmail.com
#Developed using djang_rest_framework.

Build and run application: -
Build: -
1.Export project from git, Install python, virtual environment (python -m venv <virtual env name>), django, djnago_rest_framework.
2. Virtual environment folder and project will be imported from git.
3.Then, run command for windows devices <source path>\instaWork_rest\.venv\Scripts\activate or source ./django_env/bin/activate for mac  to activate virtual environment, this has to be done from project (teams folder) root path.
5.Run python manage.py runserver command from terminal to run application.
6.If set up fails, please do follow up steps to migrate and reconfigure project
   a) run python manage.py migrate
   b)run python manage.py createsuperuser to attain admin privilages (optional steps)
   c) Run python manage.py makemigrations and python manage.py migrate
   d)Then run python manage.py runserver command.

Testing: -
We can use postman to test the API's, we get postman extension from chrome or can install the .exe for postman.
1.Listing team members in Get method-  http://127.0.0.1:8000/getTeammates
2.Adding team member in Post method-  http://127.0.0.1:8000/getTeammates/
  post request body: -
   {
    "firstName": "pooja",
    "lastName": "Nair",
    "email": "pv@gmail.com",
    "role": "admin"
 }
 3.Updating team member in Put Method-  http://127.0.0.1:8000/editTeam/<id> (for )
  put method body: -
   {
      "id": 3,
      "firstName": "nanthu",
      "lastName": "vijayan",
      "email": "nv@gmail.com",
      "role": "regular"
    }
 4. Removing team member in Delete method-  http://127.0.0.1:8000/editTeam/<id>
 
 
 
 


