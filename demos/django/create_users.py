#!/usr/bin/env python3

"""
Copyright (c) 2018 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example_site.settings")
import django
django.setup()
from django.contrib.auth.models import User
user = User.objects.create_user('user1', 'user1@mycompanymail.xyz', 'C1sco12345')
user = User.objects.create_user('user2', 'user2@mycompanymail.xyz', 'C1sco12345')