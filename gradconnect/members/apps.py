from django.apps import AppConfig


# Define the configuration class for the 'members' app
class MembersConfig(AppConfig):
    # Set the default type for auto-incrementing primary keys
    default_auto_field = 'django.db.models.BigAutoField' 
    name = 'members'
    
    def ready(self):
        import members.signals  # Register the signals on app ready