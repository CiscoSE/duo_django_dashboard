# Duo Django Dashboard Demo
## Setup Instructions
1. Git clone the application repository.
```
	git clone https://github.com/duosecurity/duo_python.git
```

2. Change directory to the cloned folder.
```
	cd duo_django_dashboard
```

3. Create a virtual environment  (duo_env) for the python dependencies.
```
	python3 -m venv duo_env
```

4. Activate the virtual environment.
```
	source duo_env/bin/activate
```

5. Change directory to the Django demo and install all the requirements
```
	cd demos/django
	pip install -r requirements.txt
```

6. [Signup for a Duo account](https://signup.duo.com/) if you don’t already have one.

7. Log in to the  [Duo Admin Panel](https://admin.duosecurity.com/)  and navigate to **Applications**.

8. Click **Protect an Application** and locate **Web SDK** in the applications list. Click **Protect this Application** to get your **integration key**, **secret key**, and **API hostname**. (See  [Getting Started](https://duo.com/docs/getting-started)  for help.)

Make sure the Web SDK application global policy is set as:

**Enabled**.    **New User Policy**.    Prompt unenrolled users to enroll whenever possible.

9. Open up your code editor (e.g. Visual Studio Code), and add the Duo Integration Key, Secret Key and the API Host to _settings.py_ (in the _duo_python_demos_django_example_site/ folder).

DUO_IKEY = Integration key
DUO_SKEY = Secret Key
DUO_HOST = API Host  

10. You are missing one value (the _DUO_AKEY_), which you have to generate yourself and keep secret from Duo. The security of your Duo application is tied to the security of your skey and akey. Treat these pieces of data like a password. They should be stored in a secure manner with limited access, whether that is in a database, a file on disk, or another storage mechanism.

11. Now you will actually generate an akey, which needs to be at least 40 characters long. You can generate a random string in Python by running these two commands.
```
python
    >>> import os, hashlib
    >>> print(hashlib.sha1(os.urandom(32)).hexdigest())
    >>> [generated Akey will be printed here]
    >>> exit()
```

12. Open up your code editor, and fill in the DUO_AKEY in the _settings.py_ file with the generated value.

13. Now we will set up Django. First we need to run the initial database migration, by running these two commands.
``` 
python manage.py makemigrations
python manage.py migrate
```

14. Create 2 users that will authenticate in the Django web app.  The users created are user1 and user2.  Both users have the password set as C1sco12345.
```
python create_users.py
```

15. Now you are ready to start the Django Web App. Run the following command.
```
	python manage.py runserver
```

16. Open a browser and go to http://127.0.0.1:8000 and login using user1.

17. After you login you will see the non-Duo protected dashboard.  Click on the the dashboard “DB Configuration” button and follow the Duo prompts to setup user1 with 2 gator authentication.

18. Experiment with the dashboard navigation buttons to see how the dashboard database configuration is protected by 2FA.
