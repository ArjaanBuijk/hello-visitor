This code is published as part of the [corresponding blog article](https://www.toptal.com/django/optimize-your-environment-for-development-and-production-a-pydantic-tutorial-part-2) at the Toptal Engineering Blog.

Visit https://www.toptal.com/blog and subscribe to our newsletter to read great articles!

* * *

# Hello-Visitor

I built this demonstration Django app to highlight the benefits of pydantic settings management. To explore these benefits, we can try out the following two scenarios:

1. **Missing a required setting**

   In the file `hello-visitor/src/.env` , out comment DATABASE_URL:

   ```bash
   # file: hello-visitor/src/.env
   # DATABASE_URL=postgres://
   ```

   When we try to start Django, pydantic will raise a clear exception, that the required field DATABASE_URL  is not defined:

   ```bash
   # in `src` folder
   $ python manage.py runserver
   Traceback (most recent call last):
   ...    
   "../hello-visitor/src/hello_visitor/settings.py", line 51, in <module>
       config = SettingsFromEnvironment()
   ...
   pydantic.error_wrappers.ValidationError: 1 validation error for SettingsFromEnvironment
   DATABASE_URL
     field required (type=value_error.missing)
   ```



2. **Wrong format for a setting**

   In the file `hello-visitor/src/.env` we will define the DATABASE_URL, but with a wrong format:

   ```bash
   # file: hello-visitor/src/.env
   DATABASE_URL=just-some-random-string
   ```

   When we try to start Django, pydantic will again raise a clear exception, that the value is incorrect:

   ```bash
   # in `src` folder
   $ python manage.py runserver
   Traceback (most recent call last):
   ...    
   "../hello-visitor/src/hello_visitor/settings.py", line 51, in <module>
       config = SettingsFromEnvironment()
   ...  
   pydantic.error_wrappers.ValidationError: 1 validation error for SettingsFromEnvironment
   DATABASE_URL
     invalid or missing URL scheme (type=value_error.url.scheme)
   ```

   

We clearly see the power of pydantic’s runtime validation. We would need to write quite a bit of custom code to achieve the same type of error checking and logging.

