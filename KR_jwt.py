from justwatch import JustWatch

just_watch = JustWatch(country='KR')

results = []

for num in range(1, 31):

    result_by_multiple = just_watch.search_for_item(
        providers=['nfx'],
        content_types=['movie'],
        page = num,
    )
    
    results.append(result_by_multiple)

print(results)
