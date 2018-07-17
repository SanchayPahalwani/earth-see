### 1 Install Python 3.5/3.6 and Django Framework 2.0
 
 [Python version 3.5.x/3.6.x](https://www.python.org/downloads/)
 
 [Django version 2.0.x](https://docs.djangoproject.com/en/2.0/intro/install/) or up.
 

### 2 Clone the repository
 
 via HTTPS
 
     git clone https://github.com/SanchayPahalwani/earth-see.git

 
### 3 Python environment setup
 Upgrade virtualenv

     pip install --upgrade virtualenv 
     virtualenv -p python3 env 
     source env/bin/activate
 

### 4 Install dependencies
 Install the file named `requirements.txt`:
 
     pip install -U -r requirements.txt
 
 
### 5 Database migrations
 After connecting the database, remember to apply the project migrations.
 
     python manage.py makemigrations 
     python manage.py makemigrations position 
     python manage.py migrate

### 6 Create superuser(admin)

     python manage.py createsuperuser

 
### 7 Run

     python manage.py runserver
