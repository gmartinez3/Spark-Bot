#Example searches rooms for "Test Room", finds the id, and then posts a test message "python test message1"

import pyCiscoSpark
import sys


def search (values, searchFor):
    for k in values["items"]:
        print (k["title"])
        if (k["title"] == searchFor) : return k["id"]
    return None

accesstoken="Bearer "+str(sys.argv[1])

rooms_dict=pyCiscoSpark.get_rooms(accesstoken)

roomid = search (rooms_dict, "Test Room")

print (roomid)

resp_dict = pyCiscoSpark.post_message(accesstoken,roomid,"A different test message")

print (resp_dict)


