## Adding swagger UI to our project
1. `pip install drf_spectacular` 
2. Make below changes in `settings.py` file
    ```
   INSTALLED_APPS = [
            ...
            'drf_spectacular',
        ]
    
   REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    }
3. Add below urls in `urls.py`
    ```
   from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
   
   urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),  # It downloads yaml file
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
   ]
   ```