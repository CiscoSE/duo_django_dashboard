import os
import django
from django.contrib.auth.models import User

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example_site.settings")
django.setup()
user = User.objects.create_user('user1', 'user1@mycompanymail.xyz', 'C1sco12345')
user = User.objects.create_user('user2', 'user2@mycompanymail.xyz', 'C1sco12345')