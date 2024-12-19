from django.shortcuts import render
from django.http import HttpResponse
from practice.models import Contacts
from django.http import JsonResponse

# Create your views here.

def practice(request):
    # return HttpResponse("Hello world!")
    # values = {"message" : "Welcome to the list!", "count" : 100}
    values = {} # create dictionary

    if request.method == "POST": # if submitting the form...
        # get name and email from the form
        new_name = request.POST["name"]
        new_email = request.POST["email"]

        new_contact = Contacts(name = new_name,
                              email = new_email)
        new_contact.save()

        # populate the dictionary with a message string
        values["message"] = f"Welcome, {new_name}!"

    values["count"] = Contacts.objects.count()
    
    return render(request, "practice.html", values)

def practice_json(request): # formatting the contact data

    data = Contacts.objects.all() # get all of the data from the table
    json_data = {"request" : "signup"} # one fixed key by default

    contact_list = [] # create an array
    for row in data:
        contact = { # make a dictionary of key:value pairs
            "name" : row.name,
            "email" : row.email
        }
        contact_list.append(contact) # add the dictionary to the array

    json_data["names"] = contact_list # add a list of names to the dictionary

    return JsonResponse(json_data)