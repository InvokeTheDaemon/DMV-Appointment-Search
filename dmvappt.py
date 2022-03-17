import requests, time, beepy
import _thread

# Usage: python3 dmvappt.py

# This tool just watches for Nevada DMV appointment cancelations. Useful when everything is booked and you need to get in ASAP. Plays an alert tone and quits the loop if an opening is found

# pip install beepy

# To generate URLs:
# 1. Open https://dmvapp.nv.gov/qmaticwebbooking/#/
# 2. Pull up dev tools (CTRL+SHIFT+I) and go to the network tab
# 3. For each location select service and copy the URL for the request starting with "dates;servicePu...."

# URLs to json requests
url = 'location 1 url'
url2 = 'location 2 url'
url3 = 'location 3 url'

# Infinite loop until an appointment is found
continue_loop = True

#String to match in for dates. If you want a specific date just use YYYY-MM-DD as the format
search_string = "2022-03-"


while continue_loop:
    #Request json from DMV
    r = requests.get(url)
    data = r.json()

    for i in data:
        #Check if there are any appointments for this month
        if search_string in i['date']:
            print("[*] APPOINTMENT FOUND AT [LOCATION 1] ON " + i['date'])
            #Break the loop - date found
            continue_loop = False
            #Play a sound - Thread because beepy is broken and freezes the program
            _thread.start_new_thread(beepy.beep,('sound=1',))

    #Request json from DMV
    r = requests.get(url2)
    data = r.json()

    for i in data:
        #Check if there are any appointments for this month
        if search_string in i['date']:
            print("[*] APPOINTMENT FOUND AT [LOCATION 2] ON " + i['date'])
            #Break the loop - date found
            continue_loop = False
            #Play a sound - Thread because beepy is broken and freezes the program
            _thread.start_new_thread(beepy.beep,('sound=1',))

    #Request json from DMV
    r = requests.get(url3)
    data = r.json()

    for i in data:
        #Check if there are any appointments for this month
        if search_string in i['date']:
            print("[*] APPOINTMENT FOUND AT [LOCATION 3] ON " + i['date'])
            #Break the loop - date found
            continue_loop = False
            #Play a sound - Thread because beepy is broken and freezes the program
            _thread.start_new_thread(beepy.beep,('sound=1',))

                            
    # Sleep for 30 seconds to not DoS the DMV
    time.sleep(30)