from django.db import models

# User Model (For user_db)
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'
        managed = False  # This ensures Django won't manage the table

    def __str__(self):
        return self.username


# Admin Model (For admin_db)
class Admin(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'admin'
        managed = False  # This ensures Django won't manage the table

    def __str__(self):
        return self.email

# accounts/models.py

# class App(models.Model):
#     name = models.CharField(max_length=255)
#     url = models.URLField()
#     category = models.CharField(max_length=100)
#     sub_category = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='app_images/')

#     class Meta:
#         db_table = 'App'  # This specifies the table name in the database
#         managed = False  # Let Django not manage the table creation

#     def __str__(self):
#         return self.name

class App(models.Model):
    app_name = models.CharField(max_length=255)
    app_link = models.URLField()
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    app_image = models.ImageField(upload_to='app_images/')
    points = models.IntegerField() 
    screenshot = models.ImageField(upload_to='screenshots/', blank=True, null=True)

    class Meta:
        db_table = 'App'  # This specifies the table name in the database
        managed = False  # Let Django not manage the table creation

    def __str__(self):
        return self.app_name
