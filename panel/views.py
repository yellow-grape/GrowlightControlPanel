

from django.shortcuts import render


light = False #will bethe raspberry pi state of the relay 

def homepage(req):
    context = {'light': light}
    if(light == True):
        ToggleLights()
    elif(light == False):
        ToggleLights()
    return render(req, "home.html", context)

def change(req):
    global light
    light = not light
    return homepage(req)


def ToggleLights():
        try:
            #light.state = light
             print("Turn on lugths")
        except:print("Aww man")
        return 
