from django.db import models

class Post (models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

class Report(models.Model):
    ldap_login = models.CharField(max_length=50, blank=True, unique=True)
    github_login = models.CharField(max_length=100, blank=True)
    checked = models.CharField(default='NONE', max_length=6) 
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ldap_login