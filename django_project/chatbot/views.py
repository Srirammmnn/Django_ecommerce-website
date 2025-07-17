from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import openai


openai.api_key =""

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        # Dummy response
        reply = f"You said: {user_message}. I'm currently offline but will respond soon!"
        return JsonResponse({"reply": reply})



def chatbot_widget(request):
    return render(request, 'chatbot/chatbox.html')
