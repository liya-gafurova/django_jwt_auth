from django.urls import include, path

users_urlpatterns = [
    path('register/', include('dj_rest_auth.registration.urls')),
    path('auth/', include('dj_rest_auth.urls'))
]