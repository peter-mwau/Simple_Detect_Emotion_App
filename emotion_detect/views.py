from django.shortcuts import render
import requests, json, urllib
from django.http import JsonResponse
from .forms import EmotionForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from . models import Records_log

# Create your views here.



#get data enetered by user in form and send it to the api
@csrf_exempt
def emotions(request):
    form = EmotionForm(request.POST or None)
    if form.is_valid():
        userInput = form.cleaned_data.get("userInput")
        response = requests.post("https://elitecode-detect-emotions.hf.space/run/predict", json={
        "data": [
            userInput,
        ]
        }).json()
        data = response["data"]
        #decode the json data
        # convert to string
        data = json.dumps(data) 
        # convert to dictionary
        data = json.loads(data)  
        output = data[0]['label']
        formoutput = EmotionForm(initial={'output': output, 'userInput': userInput})
        # print(formoutput)
        form = EmotionForm(request.POST or None)
        r = Records_log(Query=userInput, Emotion=output)
        r.save()
        return render(request, 'home.html', {'form': formoutput})
    return render(request, 'home.html', {'form': form})


#save the data to the database
# def save_data(request):
#     form = EmotionForm(request.POST or None)
#     if form.is_valid():
#         userInput = form.cleaned_data.get("userInput")
#         # output = form.cleaned_data.get("output")
#         # get output value from the data label in the api
#         output = form.cleaned_data.get("output")
#         # print(userInput)
#         # print(output)
#         # print(Records_log.objects.all())
#         # Records_log.objects.create(Query=userInput, emotion=output)
#         r = Records_log(Query=userInput, emotion=output)
#         r.save()
#         return render(request, 'home.html', {'form': form})
#     return render(request, 'home.html', {'form': form})