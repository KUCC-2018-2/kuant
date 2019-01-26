from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import UserViewSet, WriteViewSet, ScrapViewSet, MessageViewSet

userRouter = DefaultRouter()
userRouter.register('user', UserViewSet)

writeRouter = DefaultRouter()
userRouter.register('write', WriteViewSet)

scrapRouter = DefaultRouter()
scrapRouter.register('scrap', ScrapViewSet)

messageRouter = DefaultRouter()
messageRouter.register('message', MessageViewSet)

urlpatterns = [
    path('', include(writeRouter.urls)),
    path('', include(userRouter.urls)),
    path('', include(scrapRouter.urls)),
    path('', include(messageRouter.urls)),
]