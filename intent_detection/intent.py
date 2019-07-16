#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#load data from google sheet 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import fasttext 

def Train_model(): # ham lay data tu google sheet va train tra ve gia tri la model
    scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds=ServiceAccountCredentials.from_json_keyfile_name('/home/dung/Downloads/dungnguyendinh1052000-intent_detection_chatbot-master/intent_detection/Quickstart-a774cbf2c9a1.json',scope)
    client=gspread.authorize(creds)
    sheet=client.open("data chatbot").sheet1
    prin=sheet.get_all_records()
    for i in range(12):
        prin[i]["Data"]=prin[i]["Data"].split("\n")
        a=prin[i]["Data"].count('')
        for j in range(a):
            prin[i]["Data"].remove('')
            
    file=open("data.txt",'w') # tao file .txt va luu data duoi dang fasttext doc duoc
    for i in range(12):
        for j in prin[i]["Data"]:
            prin[i]['Topic']=prin[i]['Topic'].split(' ')
            prin[i]['Topic']="-".join(prin[i]['Topic'])
            file.write('__label__'+prin[i]['Topic']+' '+j+'\n')
    file.close() 
    # train model
    classifier = fasttext.train_supervised("data.txt",lr=0.5, dim=100, ws=5, epoch=30, minCount=1, minCountLabel=0, minn=0, maxn=0, neg=5, wordNgrams=2, loss='softmax', bucket=2000000, thread=3, lrUpdateRate=100, t=0.0001, label='__label__')
    
    return classifier 


def load_model(): # hàm load model 
    model_path = "intent_detection_chatbot/intent_detection/intent_model.bin"
    classifier = fasttext.load_model(model_path)
    return classifier




def get_intent(input_Str):  #hàm nhập vào input xuất ra ouput là nhãn
    input_Str=input_Str.lower()
    print(load_model().predict(input_Str)[0][0].split("__label__")[1]) # su dung ham load_model() dung model da train
                                                                       # hoac thay bang Train_model() de train model
    







