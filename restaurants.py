from googleplaces import GooglePlaces, types, lang
import json
import time
import requests

YOUR_API_KEY = 'AIzaSyBvRBItDA78x85dWOo0uGFom4zeK-PjlHw'

google_places = GooglePlaces(YOUR_API_KEY)

result_array = []

def main(lat_long_dict, srch_location):
    #lat_long_dict = {'lat':37.956821, 'lng':-122.549118}
    try:
        query_result = google_places.nearby_search(
                location=srch_location, keyword='restaurant',
                radius=12000, lat_lng=lat_long_dict, types=[types.TYPE_FOOD])
    except(error):
        print('error her2e')
        print(error)
        return result_array
    # If types param contains only 1 item the request to Google Places API
    # will be send as type param to fullfil:


    for place in query_result.places:
        # Returned places from a query are place summaries.
        place.get_details()

        print(place.name)
        result_array.append({'name': place.name, 'phone': place.local_phone_number, 'place_id': place.place_id, 'website': place.website})


        # The following method has to make a further API call.
        # Referencing any of the attributes below, prior to making a call to
        # get_details() will raise a googleplaces.GooglePlacesAttributeError.
        # print place.details # A dict matching the JSON response from Google.
    if not query_result.has_next_page_token:
        print("HERE")
        return result_array

    while query_result.has_next_page_token:
        try:
            query_result = google_places.nearby_search(location=srch_location, keyword='restaurant',
            radius=12000, lat_lng=lat_long_dict,
                    pagetoken=query_result.next_page_token)
        except:
            print('error he3re')
            return result_array
        for place in query_result.places:
            place.get_details()
            # Returned places from a query are place summaries.
            print(place.name)
            result_array.append({'name': place.name, 'phone': place.local_phone_number, 'place_id': place.place_id, 'website': place.website})
    return result_array
