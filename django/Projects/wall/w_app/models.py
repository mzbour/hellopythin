from urllib import request
from django.db import models
# from __future__ import unicode_literals
from tkinter import CASCADE
import bcrypt
import re
from django.shortcuts import render, redirect

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def reg_validation(self, postData):
        errors = {}
        if len(postData['first_name']) <3:
            errors["fname"] = "The first name must be larger than two characters"
        if not NAME_REGEX.match(request.POST['first_name']):
            errors["fname"] = "The name must not contain any symbols"
        if len(postData['last_name'])<3:
            errors["lname"] = "The last name must be larger than two characters"
        if not NAME_REGEX.match(request.POST['first_name']):
            errors["lname"] = "The last name must not contain any symbols"
        if not EMAIL_REGEX.match(request.POST['email']):
            errors['email']="The email syntax is in error form! "
        if len(request.POST['password']) < 8 :
            errors['password']="The password must be larger than the "
        if request.POST['password'] != request.POST['confirm_password']:
            errors['password']="the confirm password not matched!!?"
        return errors
        

    def log_validation(self, postData):
        errors = {}
        try:
            user = User.objects.get(email_address = postData['email'])
        except:
            errors['email'] = f"Email address {postData['email']} is not registered in our database!"
            return errors
        if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
            errors['pword'] = "Password does not match our database!"
        return errors
        
    

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email_address = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    message_text = models.TextField()
    user = models.ForeignKey(User, related_name='messages',on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment_text = models.TextField()
    user = models.ForeignKey(User, related_name='comments',on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments',on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

