from justwatch import JustWatch
import json

just_watch = JustWatch(country='US')

results = just_watch.search_for_item(providers=['nfx'])

for result in results:

    movie_id = result['id']
    title = ''
    if 'title' in result:
        title = result['title']

    short_description
    if 'short_description' in result:
    	short_description = result['short_description']
    original_release_year = result['original_release_year']
    object_type = result['object_type']
    original_title = result['original_title']
    original_language = result['original_language']
    max_season_number = result['max_season_number']
    age_certification = result['age_certification']
