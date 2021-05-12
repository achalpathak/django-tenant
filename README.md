Project Setup:
1. python manage.py migrate
2. python manage.py createsuperuser
3. run python manage.py runserver django.tenant:8000
4. visit http://django.tenant:8000/admin/login/?next=/admin/ and create tenant as tenant1 and tenant2 from admin panel
5. add the following enteries to host file so that tenant1.django.tenant and tenant2.django.tenant can redirect to local host and can act as a different tenants
6. python manage.py migrate_schema
7. python manage.py runserver django.tenant:8000

Now you can visit any of the below url to create, list products based on the tenants
http://tenant1.django.tenant:8000/api/v1/products/
http://tenant2.django.tenant:8000/api/v1/products/

visit below url for update and delete.
http://tenant1.django.tenant:8000/api/v1/products/1
http://tenant2.django.tenant:8000/api/v1/products/1
