import requests
import json
""" 
# Using an open Movies Public API (http://www.omdbapi.com) to make a simple Command line 
# to allow its users to search for a movie by movie title and year was acted
"""
url="http://www.omdbapi.com"

name_of_movie= input("Enter name of the movie: \n")
year_of_act= input("Enter the year movie was acted: \n")

if name_of_movie and year_of_act:#Ensure User Enters Movie Name and Year
    if year_of_act.isdigit():
        
        if (int(year_of_act)<=2017 and int(year_of_act)>=1970):
            print("Wait a moment----")
            payload={'t':name_of_movie,'y':year_of_act,'plot':'full'}
            request=requests.get(url,params=payload)

            respo=request.json()
            #print request.status_code
            if (responce['Response']=="True"):
                print(responce['Response']) 
                print(responce['Title']+"\n")

                print("Description.\n"+responce['Plot']+"\nYear of release: "+responce['Year']+"\n"+"Actors\n"+responce['Actors']+"\nWritten By \n"+responce['Writer'])
            else:
                print(responce['Sorry error occurred!'])
        else:
            print("Sorry.We only have movies  from 1990-2017")
    else:
        print("Invalid year")

else:
    print("Name of the movie and year movie was acted are both required")
