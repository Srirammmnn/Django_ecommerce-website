from django.urls import path
from .views import chatbot_response, chatbot_widget
from . import views

urlpatterns = [
   path('chatbot-response/',views.chatbot_response, name='chatbot_response'),
   path('chatbot/', chatbot_widget, name='chatbox_page'),  # Optional: to load as a standalone page
]
