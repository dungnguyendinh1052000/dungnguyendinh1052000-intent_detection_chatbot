#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#load data from google sheet 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds=ServiceAccountCredentials.from_json_keyfile_name('Quickstart-a774cbf2c9a1.json',scope)
client=gspread.authorize(creds)
sheet=client.open("data chatbot").sheet1
prin=sheet.get_all_records()
for i in range(12):
    prin[i]["Data"]=prin[i]["Data"].split("\n")
    a=prin[i]["Data"].count('')
    for j in range(a):
        prin[i]["Data"].remove('')
#print(prin)
file=open("data.txt",'w')
for i in range(12):
    for j in prin[i]["Data"]:
        prin[i]['Topic']=prin[i]['Topic'].split(' ')
        prin[i]['Topic']="-".join(prin[i]['Topic'])
        file.write('__label__'+prin[i]['Topic']+' '+j+'\n')
file.close()  


# In[1]:

import fastText 

def load_model(): # hàm load model 
    model_path = "intent_detection_chatbot/intent_detection/intent_model.bin"
    classifier = fastText.FastText.load_model(model_path)
    return classifier
classifier=load_model() # gán biến classifier thành biến chưa model đã load 
def get_intent(input_Str):  #hàm nhập vào input xuất ra ouput là nhãn
    input_Str=input_Str.lower()
    print(classifier.predict(input_Str)[0][0].split("__label__")[1])
    







