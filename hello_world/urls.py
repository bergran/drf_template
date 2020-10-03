from django.urls import path

from hello_world.views.hello_world import HelloWorldAPIView


urlpatterns = [
    path("api/v1/hello-world", HelloWorldAPIView.as_view(), name="hello-world")
]
