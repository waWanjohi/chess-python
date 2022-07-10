from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Model definition for User
    ---

    Empty for now as there are no users required

    In case we need to change anything later.    
    AbstractUser will allow for that to happen.

    """

    pass 
