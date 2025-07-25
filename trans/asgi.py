import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import myhome.routing  # 🔁 your app's routing.py for WebSockets

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trans.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            myhome.routing.websocket_urlpatterns  # 🔁 this needs to be defined
        )
    ),
})
