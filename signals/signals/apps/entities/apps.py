from django.apps import AppConfig
#from django.conf import settings
#from django.db.models.signals import post_save


class EntitiesConfig(AppConfig):
    name ='entities'

#    def ready(self):
#        import entities.signals
#        from .signals import user_create_profile
#        from django.apps.authentication import User
#        post_save.connect(user_create_profile, sender=User)
