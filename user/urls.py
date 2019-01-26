from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import UserViewSet, WriteViewSet, ScrapViewSet, MessageViewSet, CommentViewSet

userRouter = DefaultRouter()
userRouter.register('user', UserViewSet)

writeRouter = DefaultRouter()
userRouter.register('write', WriteViewSet)

scrapRouter = DefaultRouter()
scrapRouter.register('scrap', ScrapViewSet)

messageRouter = DefaultRouter()
messageRouter.register('message', MessageViewSet)

commentRouter = DefaultRouter()
commentRouter.register('comment', CommentViewSet)

urlpatterns = [
    path('', include(writeRouter.urls)),
    path('', include(userRouter.urls)),
    path('', include(scrapRouter.urls)),
    path('', include(messageRouter.urls)),
    path('', include(commentRouter.urls)),
]