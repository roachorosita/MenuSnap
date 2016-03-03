from locu.api import VenueApiClient, MenuItemApiClient

KEY = '77ca60baa8056bc0c1aa6f422bc525a56ed1443e'

venue_client = VenueApiClient(KEY)

venues = venue_client.search(locality = 'San Francisco')

print venues

menu_item_client = MenuItemApiClient(KEY)
menu_items = menu_item_client.search(locality = 'San Francisco', name = 'espresso')
print menu_items['objects'][0]