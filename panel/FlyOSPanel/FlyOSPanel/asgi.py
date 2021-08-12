"""
<<<<<<< HEAD
ASGI config for 飞屎OS-batePanel project.
=======
ASGI config for FlyOSPanel project.
>>>>>>> parent of aeeb25f (✨ feat(震撼发布): Fly OS -> 惊喜不只是飞)

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '飞屎OS-batePanel.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FlyOSPanel.settings')
>>>>>>> parent of aeeb25f (✨ feat(震撼发布): Fly OS -> 惊喜不只是飞)

application = get_asgi_application()
