from django.db import models
# from flask_migrate import Migrate
class User(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    email = models.CharField(max_length = 100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)



# newly_created_user1 = User.objects.create(first_name="Mohamamd",last_name="alBzour",email="m.albzour99@gmail.com" ,age=22,created_at="2010-09-25",updated_at="2013-05-06")
# newly_created_user2 = User.objects.create(first_name="Ahmad",last_name="qalalwi",email="A.ql33@gmail.com" ,age=28,created_at="2011-09-25",updated_at="2016-07-06")
# newly_created_user3 = User.objects.create(first_name="Ali",last_name="hasson",email="aliB99@gmail.com" ,age=21,created_at="2009-02-23",updated_at="2014-02-06")

# # Query: Retrieve all the users
# allusers=User.objects.all()
# # Query: Retrieve the last user
# lastuser=User.objects.last()
# # Query: Retrieve the first user
# fuser=User.objects.first()
# # Query: Change the user with id=3 so their last name is Pancakes.
# g=User.objects.get(id=3)
# g.first_name="Pancakes"
# g.save()
# # Query: Delete the user with id=2 from the database
# c = User.objects.get(id=2)
# c.delete()
# # Query: Get all the users, sorted by their first name
# orderusers=User.objects.all().order_by("first_name")
# # BONUS Query: Get all the users, sorted by their first name in descending order
# orderusers=User.objects.all().order_by("-first_name")
# # Submit your .txt file that contains all the queries you ran in the shell
