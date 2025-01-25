from django.shortcuts import render

# Create your views here.
from joblib import load
# import numpy as np
model=load('./Real Estate Model.joblib')

def predict(request):
    if request.method=='POST':
        CRIM=request.POST['CRIM']
        ZN=request.POST['ZN']
        INDUS=request.POST['INDUS']
        CHAS=request.POST['CHAS']
        NOX=request.POST['NOX']
        RM=request.POST['RM']
        AGE=request.POST['AGE']
        DIS=request.POST['DIS']
        RAD=request.POST['RAD']
        TAX=request.POST['TAX']
        PTRATIO=request.POST['PTRATIO']
        B=request.POST['B']
        LSTAT=request.POST['LSTAT']
        y_pred=model.predict([[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]])
        x=y_pred*10000
        return render(request,'main.html',{'result':x})
    return render(request,'main.html')
