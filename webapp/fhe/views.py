from django.shortcuts import render
from django.http import HttpResponse
from practice.models import Contacts
from django.http import JsonResponse

# Create your views here.

def fhe(request):
    if True is True: # displaying alternate html page templates based on conditions
        # return HttpResponse("Hello world!")
        # values = {"message" : "Welcome to the list!", "count" : 100}
        values = {} # create dictionary

        if request.method == "POST": # if submitting the form...
            # get name and apt from the form
            new_name = request.POST["name"]
            new_apt = request.POST["apt"]

            new_contact = Contacts(name = new_name,
                                apt = new_apt)
            new_contact.save()

            # populate the dictionary with a message string
            values["message"] = f"Welcome, {new_name}!"

        values["count"] = Contacts.objects.count()
        
        return render(request, "fhe.html", values)


    else:
        return render(request, "_____.html", {})

def fhe_json(request): # formatting the contact data

    data = Contacts.objects.all() # get all of the data from the table
    json_data = {"request" : "signup"} # one fixed key by default

    contact_list = [] # create an array
    for row in data:
        contact = { # make a dictionary of key:value pairs
            "name" : row.name,
            "apt" : row.apt
        }
        contact_list.append(contact) # add the dictionary to the array

    json_data["names"] = contact_list # add a list of names to the dictionary

    return JsonResponse(json_data)


# Perhaps it needs to not be its own html but just its own submission type.
# I could maybe do a switch case within the if statement for the different submission boxes.
def fhe_ideas(request):
    # return HttpResponse("Hello world!")
    # values = {"message" : "Welcome to the list!", "count" : 100}
    ideas = {} # create dictionary

    if request.method == "POST": # if submitting the form...
        # get name and apt from the form
        new_idea = request.POST["idea"]

        # new_idea = Ideas(name = new_idea)
        #                     #   apt = new_apt)
        # new_contact.save()
        new_idea.save()

        # populate the dictionary with a message string
        ideas["message"] = f"Welcome, {new_idea}!"

    ideas["count"] = Contacts.objects.count()
    
    # return render(request, "fhe/ideas.html", ideas)
    return render(request, "fhe.html", ideas)