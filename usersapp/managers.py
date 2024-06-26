from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """This overrides the base manager class to use email authentication"""
    def create_user(self, email, first_name, last_name, password=None):
        """For creating regular users"""
        if not email:
            raise ValueError("Email mustn't be blank.")
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self, email, first_name, last_name, password):
        """The cli for creating superuser"""
        user = self.create_user(email, first_name, last_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 
    