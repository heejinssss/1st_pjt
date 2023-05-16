import sys
from justwatch import JustWatch
import pprint

just_watch = JustWatch(country='KR')

results = []

for num in range(1, 44):

    result_by_multiple = just_watch.search_for_item(
        providers=['dnp'],
        content_types=['movie'],
        page = num,
    )
    
    results.append(result_by_multiple)

sys.stdout = open('myjson.txt', 'w', encoding="UTF-8")    

pprint.pprint(results)

sys.stdout.close()