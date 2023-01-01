# Integrify Technical assignment( django rest framework)
A personal TODO application  api with django rest framework

Backend of: [Localhost](https://127.0.0.1:8000/)

## installation
1. install python3 from <a href="https://www.python.or
g/" target="_blank">here</a> 
1. pip install -r requirements.txt
1. python manage.py migrate
1. python manage.py createsuperuser(insert user name and password)
1. python manage.py runserver
---
# api paths
* [**api/v1/**](#apiv1)
	* [**api/v1/todo/**](#apiv1todo)
		* [**api/v1/todo/add/**](#apiv1todoadd) 
		* [**api/v1/todo/edit/{id}/**](#apiv1editpk)
		* [**api/v1/todo/delete/{id}/**](#apiv1deletepk) 


* [**api/v1/**](#authv1)
	* [**api/v1/signin/**](#authv1login)
		* [**api/v1/signin/refresh/**](#authv1loginrefresh)
	* [**api/v1/signup/**](#authv1register)
	* [**api/v1/changepassword/{pk}/**](#authv1change_passwordpk)



## api/v1/
### api/v1/todo/
**Allowed Methods** : GET
<br>**Access Level** : Authorized users
<br>return array of objects of all todos in the database related to the authorized user.
<br>you can get a specific todo object with passing the id to the end of the path.

### api/v1/todo/add/
**allowed methods** : POST
<br>**Access Level** : Authorized users
<br>**fields :** 'required': {'name'}, 'optional': {"description", "is_active", "status"}
<br>*POST :* The data should include fields available if user authorized.

### api/v1/todo/edit/{id}/
**allowed methods** : PUT
<br>**Access Level** : Authorized users
<br>**fields :** 'required': 'optional': {"title", description", "image", "is_active", "priority", "send_email"}
<br>*POST :* The data should include fields available if user authorized.

### api/v1/todo/delete/{id}/
**allowed methods** : DELETE
<br>**Access Level** : Authorized users
<br>*DELETE :* there is no data to send. you should put the Id of records that are in user you want to delete in the url instead of *{key}*


## api/v1/
### api/v1/signin/
**allowed methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {'username', 'password'}
<br>*POST :* the data you post should include 'username' and 'password' fields if the user was authorized the access token and the refresh token will return as json.[more information about JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#usage)

#### api/v1/signin/refresh/
**allowed methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {'refresh'}
<br>*POST :* the data you post should include 'refresh' and the value of it should be user refresh token that is sent when user login.

### auth/v1/signup/
**allowed methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {'username', 'password1', 'password2', 'email', 'first_name', 'last_name'}
<br>*POST :* should include the 'fields' keys and proper value. errors and exceptions handled , should have a proper place to show them in frontend.

### api/v1/changepassword/{id}/
**allowed methods** : PUT
<br>**Access Level** : Authorized users
<br>**fields :** 'required': {'old_password', 'password1', 'password2'}
<br>*PUT :* should include 'fields' keys with proper values. errors and exceptions handled , should have a proper place to show them in frontend.



### api/v1/logout/
**allowed methods** : POST
<br>**Access Level** : Authorized users
<br>**fields :** 'required': {'refresh_token'}
<br>*POST :* should include the authorized user access token. post user refresh token with 'refresh_token' key to expire the access and refresh token of the given user.
