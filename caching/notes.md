# Caching

## Types of caching
1. Caching the whole app/site
2. Caching a view
3. Caching fragment of the template
4. Low level caching (caching an object)

## Storing Cached data
1. Database
    - works best if you’ve got a fast, well-indexed database server.
    - stores in your database
   ```python
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.db.DatabaseCache",
            "LOCATION": "my_cache_table",
        }
    }

- we have to run a command to create the cache table in our database
      ``` 
     python manage.py createcachetable

2. File system
    - The file-based backend serializes and stores each cache value as a separate file. 
   ```python
    CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "c:/foo/bar",
    }
}

   
3. Memcached:
    - entirely memory-based cache server
    - used by sites such as Facebook and Wikipedia to reduce database access and dramatically increase site performance.

4. Redis 
    - in-memory database
    - you’ll need a Redis server running either locally or on a remote machine.
    - ```python
    CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}
   