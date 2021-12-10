from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Business
import os
from api.models import Review
from django.core.exceptions import ObjectDoesNotExist


myHeaders = {'Authorization' :  'Bearer pO6GuQayXawfmMhK_h_FUJgj67BXZUFYe0kcBhLmLxYUNu6tJxF_AXJyTSejnKpxfcjrcpwTuw22iAMw7u8ng5xc6gGyaf6hBkZd-IE7h3epMY7cdogc8r_j2l9XYXYx'}
url = "https://api.yelp.com/v3/businesses/"

# /yelp/businesses/{location}
#return businesses within specified vicinity
#TODO change lines 31-33 for mysql databse in prod
def businesses(request, location):

    parameters = {
        'location':location,
        'radius':40000
        }

    try:    
        response = requests.get(url=url + "search", headers=myHeaders, params=parameters)
        data = response.json()

        #text used to display entire json object
        text = json.dumps(data, sort_keys=True, indent=5)
        return HttpResponse(text)

        return(data['businesses'])
        
    except requests.exceptions.HTTPError as error:
        print(error)

# /yelp/business/{id}
#return json object for requested business
#example business id WavvLdfdP6g8aZTtbBQHTw
def business(request, id):
    try:    
        response = requests.get(url=url + id, headers=myHeaders)
        data = response.json()
        
        #text used to display entire json object
        text = json.dumps(data, sort_keys=True, indent=5)
        return HttpResponse(text)
        
        #return data
        
    except requests.exceptions.HTTPError as error:
        print(error)

# /yelp/reviews/{id}
#return json object of reviews for requested business
#example business id WavvLdfdP6g8aZTtbBQHTw
def reviews(request, id):
    print(url + id + "/reviews/")
    try:    
        response = requests.get(url=url + id + "/reviews", headers=myHeaders)
        data = response.json()
        i = 0
        for review in data['reviews']:
            try:
                reviewObj = Review.objects.get(yelp_review_id=review['id'])
                data['reviews'][i]['numVotes'] = (reviewObj.get_downvotes() + reviewObj.get_upvotes())
    
            except ObjectDoesNotExist:
                data['reviews'][i]['numVotes'] = 0

            i = i + 1

        data['reviews'].sort(key= lambda x : x['numVotes'], reverse = True)
            
        #text used to display entire json object
        text = json.dumps(data, sort_keys=True, indent=5)
        return HttpResponse(text)

        #return data
        
    except requests.exceptions.HTTPError as error:
        print(error)
