from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.shortcuts import render

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import math


def home(request):
    return render(request,'index.html', {})

def blog(request):
    return render(request,'blog.html', {})

def booking(request):
    return render(request,'booking.html', {})

def packages(request):
    return render(request,'package-offer.html', {})

def UserForm(request):
    return render(request,'UserForm.html', {})





def UserForm(request):
    df = pd.read_csv(r'static/TravelChoices.csv')
    df['Education'].replace(['Bachelor\t'],['Bachelor'], inplace= True)
    df['Gender_cat'] = pd.factorize(df.Gender)[0]
    df['City_cat'] = pd.factorize(df.City)[0]
    df['FavoriteTourismDest_india_cat'] = pd.factorize(df.FavoriteTourismDest_india)[0]
    df['Education_cat'] = pd.factorize(df.Education)[0]

    a = df.FavoriteTourismDest_india.value_counts()
    b = df.FavoriteTourismDest_india_cat.value_counts()
    ftdl = a.to_dict()
    ftdlk = ftdl.keys()
    ftdcl = b.to_dict()
    ftdclk = ftdcl.keys()
    ftdlkl = list(ftdlk)
    ftdclkl = list(ftdclk)
    res = {}
    for key in ftdlkl:
        for value in ftdclkl:
            res[key] = value
            ftdclkl.remove(value)
            break

    x = df[['Age','Gender_cat','City_cat','Education_cat']]
    y = df['FavoriteTourismDest_india_cat']
    reg = linear_model.LinearRegression()
    reg.fit(x,y)



# @app.route('/', methods = {'POST'})

    def getvalue():
        if request.method == 'POST':
            age = request.POST['age']
            gender = request.POST['gender']
            cityliving = request.POST['city']
            education = request.POST['education']

        # gender
            if(gender=='male'):
                gender = 1

            elif(gender=='female'):
                gender = 0
            
            # education
            if(education=='Bachelor'):
                education = 0
            elif(education=='Masters'):
                education=1
            elif(education=='Phd'):
                education=2
            elif(education=='Job'):
                education=3
            elif(education=='Retired'):
                education=4
            
            
            # city
            if(cityliving=='NewDelhi'):
                cityliving=4
            elif(cityliving=='Bangalore'):
                cityliving=3
            elif(cityliving=='Mumbai'):
                cityliving=2
            elif(cityliving=='Chennai'):
                cityliving=0
            elif(cityliving=='Pune'):
                cityliving=1
            elif(cityliving=='Jaipur'):
                cityliving=5
            elif(cityliving=='Bhopal'):
                cityliving=6
            elif(cityliving=='Assam'):
                cityliving=8
            elif(cityliving=='Delhi'):
                cityliving=10
            elif(cityliving=='Mizoram'):
                cityliving=9
            elif(cityliving=='Kerala'):
                cityliving=12
            elif(cityliving=='UP'):
                cityliving=11
            z = reg.predict([[age,gender,cityliving,education]])
            z = math.floor(z)
            for name, value in res.items():
                if value==z:
                    # return render_template('home.html', n = f'Recommended state for you : {name}')
                    return f'Recommended state for you : {name}'
    return render(request, 'UserForm.html',{'n':getvalue})