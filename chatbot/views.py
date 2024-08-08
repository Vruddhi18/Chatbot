from django.shortcuts import render
from django.http import JsonResponse
import openai

# from django.contrib import auth

openai_api_key='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'
openai.api_key = openai_api_key


def ask_openai(message):
    response = openai.Completion.create(
        model = 'text-davinci-003',
        prompt = message,
        max_tokens = 150,
        n = 1,
        stop = None,
        temperature = 0.7,
    )
    # print(response)
    answer = response.choices[0].text.strip()
    return answer

# Create your views here.
def chatbot(request):
    if request.method=='POST':
        message=request.POST.get('message')
        response=ask_openai(message)
        return JsonResponse ({'message':message,'response':response})
    return render (request,'chatbot.html')


# def login(request):
#     return render(request,'login.html')

# def register(request):
#     return render(request,'register.html')

# def logout(request):
#     auth.logout(request)
