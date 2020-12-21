from django.apps import AppConfig


class WorkshopConfig(AppConfig):
    name = 'workshop'
    def ready(self):
      import workshop.signals    
