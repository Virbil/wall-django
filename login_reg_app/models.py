from django.db import models
import datetime as dt
import bcrypt

class User_Manager(models.Manager):
    def age_of_user(self, birth_year):
        date_today = dt.date.today().year
        age = date_today - birth_year
        
        return int(age)

    def sign_in_validator(self, post_data):
        errors = {}
        if len(post_data["email"]) < 2:
            errors["email"] = "Please provide a longer email"
        try:
            user = User.objects.filter(email = post_data["email"])
            if not user:
                errors["email"] = "Invalid email. Please try again"
        except:
            errors["email"] = "Invalid email. Please try again"

        if len(post_data["password"]) < 5:
            errors["password"] = "Invalid password. Please try again"

        return errors
    
    def reg_validator(self, post_data):
        errors = {}

        if len(post_data["first_name"]) < 2:
            errors["first_name"] = "First name must be at least 2 characters"
        
        if len(post_data["last_name"]) < 2:
            errors["last_name"] = "Last name must be at least 2 characters"
        
        if len(post_data["birthday"]) < 1:
            errors["birthday"] = "Please select or enter a birthday"
        if post_data["birthday"].isalpha() == True:
            errors["birthday"] = "Birthday must be a valid date"
        if len(post_data["birthday"]) > 0:
            date_entered = dt.datetime.strptime(post_data["birthday"], "%m/%d/%Y")
            if date_entered > dt.datetime.now():
                errors["birthday"] = 'Birthday should be in the past'
            if self.age_of_user(date_entered.year) < 13:
                errors["birthday"] = "Must be 13 years or older to Register"

        if len(post_data["password"]) < 8:
            errors["password"] = "Password must be at least 8 characters"
        if post_data["confirm_pass"] != post_data["password"]:
            errors["confirm_pass"] = "Passwords do not match, please try again"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    birthday = models.DateField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = User_Manager()
    # message_by_user - OTM
    # comment_by_user - OTM

    def __repr__(self):
        return f"<user {self.id}, name: {self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}, email: {self.email}"