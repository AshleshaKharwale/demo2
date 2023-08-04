from django.shortcuts import render

# Create your views here.


# to create cachetable -  python manage.py createcachetable
# it creates my_cache_table

def fragment_cache(request):
    return render(request, 'fragment_cache.html')


def low_level_cache(request):
    pass
