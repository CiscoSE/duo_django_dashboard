import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example_site.settings")
import django
django.setup()
from django.contrib.auth.models import User
user = User.objects.create_user('user1', 'user1@mycompanymail.xyz', 'C1sco12345')
user = User.objects.create_user('user2', 'user2@mycompanymail.xyz', 'C1sco12345')