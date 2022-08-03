#!/usr/bin/env python
# coding: utf-8

# In[7]:


pip install pywhatkit


# In[50]:


import pywhatkit
pywhatkit.playonyt("https://www.youtube.com/c/2SourceFort")


# In[9]:


pip install wikipedia


# In[10]:


import wikipedia
result = wikipedia.summary("Microsoft CEO")
print(result)


# In[11]:


#Text To Speech: pyttsx3

pip install pyttsx3


# In[49]:


import pyttsx3
engine = pyttsx3.init()
engine.say("Welcome to Machine Learning Tutorials")
engine.runAndWait()


# In[ ]:





# In[ ]:





# In[17]:


pip install datetime


# In[51]:


import datetime
time = datetime.datetime.now().strftime('%I:%m %p')
print(time)


# In[25]:


import datetime
date = datetime.datetime.now().strftime('%d %b %Y')
print(date)


# In[27]:


#Read Today's News

pip install requests


# In[28]:


pip install json


# In[34]:


import requests
import json
a=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=9fe4be099c6c417a8c00b56ee67f9db5") 
b=json.loads(a.text)
for i in range(10):
    my_data=b['articles'][i]['title']
    print ("Title:",i+1,my_data)


# In[38]:


# Crack Jokes
pip install pyjokes


# In[39]:


import pyjokes
j = pyjokes.get_joke()
print(j)


# In[46]:


import requests
import wikipedia
import pyaudio
import speech_recognition as sr 
import requests
import json
import pywhatkit
import datetime
import pyjokes

api_key = "e226a2eaa720614632c86b91ec9868ee"
base_url = "https://api.openweathermap.org/data/2.5/weather?"

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    a = r.recognize_google(audio)
    a=a.lower()
    print("Check: "+a)

if 'play' in a: 
    a = a[5:]
    pywhatkit.playonyt(a)
    
elif 'news' in a:
    a=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=9fe4be099c6c417a8c00b56ee67f9db5") 
    b=json.loads(a.text)
    for i in range(10):
        my_data=b['articles'][i]['title']
        print ("Title:",i+1,my_data)

elif 'name' in a:
    print("My name is Itronix Solutions")

elif 'date' in a:
    date = datetime.datetime.now().strftime('%d %b %Y')
    print(date)

elif 'time' in a:
    time = datetime.datetime.now().strftime('%I:%m %p')
    print(time)

elif 'joke':
    j = pyjokes.get_joke()
    print(j)

elif 'tell' in a:
    a=a.split()
    a=a[4:]
    search=' '.join(a)
    print (wikipedia.summary(search))

elif 'temperature' in a:
    city_name=str(a.split()[-1:][0])
    print(city_name)
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key
    response = requests.get(complete_url) 

    x = response.json() 
    if x["cod"] != "404": 
        y = x["main"] 
        current_temperature = y["temp"] 
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"] 
        z = x["weather"] 
        weather_description = z[0]["description"] 
        print(" Temperature (in Celcius unit) = " +
                        str(int(current_temperature)-273.15) + 
              "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
              "\n humidity (in percentage) = " +
                        str(current_humidiy) +
              "\n description = " +
                        str(weather_description)) 
    else: 
        print(" City Not Found ") 
else:
    print("Itronix Assistant Couldn't Understand")


# In[48]:


api_key = "e226a2eaa720614632c86b91ec9868ee"
base_url = "https://api.openweathermap.org/data/2.5/weather?"

city_name="jaffna"
print(city_name)

complete_url = base_url + "q=" + city_name + "&appid=" + api_key
response = requests.get(complete_url) 

x = response.json() 
if x["cod"] != "404": 
    y = x["main"] 
    current_temperature = y["temp"] 
    current_pressure = y["pressure"] 
    current_humidiy = y["humidity"] 
    z = x["weather"] 
    weather_description = z[0]["description"] 
    print(" Temperature (in Celcius unit) = " +
                    str(int(current_temperature)-273.15) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description)) 
else: 
    print(" City Not Found ") 


# In[53]:


pip install SpeechRecognition


# In[ ]:





# In[ ]:





# In[ ]:





# In[54]:


pip install pyAudio


# In[55]:


import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something:")
    audio = r.listen(source)
    text = r.recognize_google(audio)
print("You Said:",text)


# In[ ]:




