[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/CiscoSE/duo_django_dashboard)

# Duo Django Dashboard Demo

In this Demo you will go through an example of how to add multi-factor authentication to a web app. This is a good example of a Cisco App-First Security use case. Please follow the instructions below to get started!

## Setup Instructions
1. Git clone the application repository.
```
	git clone https://github.com/ciscose/duo_django_dashboard.git
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

* DUO_IKEY = Integration key
* DUO_SKEY = Secret Key
* DUO_HOST = API Host  

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

14. Create 2 users that will authenticate in the Django web app.  The users created are:

* Username: user1 
* Password: Cisco12345

* Username: user2
* Password: C1sco12345

```
python create_users.py
```

15. Now you are ready to start the Django Web App. Run the following command.
```
	python manage.py runserver
```

16. Open a browser and go to http://127.0.0.1:8000 and login using user1.

17. After you login you will see the non-Duo protected dashboard.  Click on the the dashboard “DB Configuration” button and follow the Duo prompts to setup user1 with 2 factor authentication.

18. Experiment with the dashboard navigation buttons to see how the dashboard database configuration is protected by 2FA.

# Additional Resources
* [Duo's Wed SDK in 6 Minutes Video](https://duo.com/resources/videos/set-up-two-factor-authentication-with-duo-s-web-sdk)
* [Duo Web SDK's](https://github.com/duosecurity)
* [Duo Web Two-Factor Authentication for Your Web Application](https://duo.com/docs/duoweb)
