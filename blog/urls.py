from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import BolgViewSet, BlogModelViewSet, AuthorViewSet # AuthorReadOnlyModelViewSet

router = DefaultRouter()
router.register(r'blog', BolgViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'blog-model-viewset', BlogModelViewSet)
# router.register(r'author-readonly-viewset', AuthorReadOnlyModelViewSet)

# urlpatterns = router.urls  # if we want to register urls on home

urlpatterns = [
    # path('blog/', BolgViewSet.as_view({'get': 'list'}), name='list-viewset'),
    # path('blog/<int:pk>/', BolgViewSet.as_view({'get': 'retrieve'}),
    #      name='retrieve-viewset'),
    path('viewset/', include(router.urls)),
    # authtoken built-in view - exposing an api endpoint for drf authtoken
    # send post request by providing username and password in json format only, to get the token
    path('viewset/authtoken/', views.obtain_auth_token),
]
