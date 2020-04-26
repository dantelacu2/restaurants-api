from googleplaces import GooglePlaces, types, lang
import json
import time
import requests

YOUR_API_KEY = 'AIzaSyBvRBItDA78x85dWOo0uGFom4zeK-PjlHw'

google_places = GooglePlaces(YOUR_API_KEY)

result_array = []

def main():
    query_result = google_places.nearby_search(
            location='Novato, California', keyword='restaurant',
            radius=12000, types=[types.TYPE_FOOD])
    # If types param contains only 1 item the request to Google Places API
    # will be send as type param to fullfil:


    for place in query_result.places:
        # Returned places from a query are place summaries.
        print(place.name)
        result_array.append(place.name)


        # The following method has to make a further API call.
        place.get_details()
        # Referencing any of the attributes below, prior to making a call to
        # get_details() will raise a googleplaces.GooglePlacesAttributeError.
        # print place.details # A dict matching the JSON response from Google.

    while query_result.has_next_page_token:
        for place in query_result.places:
            # Returned places from a query are place summaries.
            print(place.name)
            result_array.append(place.name)

        query_result = google_places.nearby_search(
                pagetoken=query_result.next_page_token)
    return result_array

main()
