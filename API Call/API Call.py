from yelpapi import YelpAPI

consumer_key = '7ot7QyUcVY_0Cs5J3FplOw'
consumer_secret = 'WWbFcQqRRRvpidzMwPpoWzJcI9o'
token = 'NP9DZXZEThhAk-ms1JBc8s77mqjLHZGq'
token_secret = 'PWrNPbxe-Q0NgjZApehwXslHQwQ'


yelp_api = YelpAPI(consumer_key, consumer_secret, token, token_secret)
search_results = yelp_api.search_query(term='ice cream', location='pomona, ca', limit='5')
print(search_results)
#business_results = yelp_api.business_query(id=business_id, other_args)
#phone_search_results = yelp_api.phone_search_query(phone=phone_number, other_args)
