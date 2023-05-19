import json

movies_json = open('json_data/my_netflix.json', encoding='utf-8')
movies_list = json.load(movies_json)

try:
    lst = []
    for dict_lst in movies_list: # 페이지당
        for num in range(30): # 페이지 내에서 30번씩 (page size = 30)
            for type in ((dict_lst["items"])[num])["scoring"]:
                if type["provider_type"] == "tmdb:id":
                    lst.append(type["value"])
    print(lst)
except:
    print(lst)

# -------------------------------------------------------------------------------

# ott별 tmdb id 값 list로 저장
ott_id_dict = {"nfx": "", "dnp": "", "wac": "", "wav": "", "apt": "", "ply": ""}

ott_list = ['nfx', 'dnp', 'wac', 'wav', 'apt', 'ply']
for ott in ott_list:
    list_file = [line.split(', ') for line in open(f'{ott}_tmdb.txt', 'r')]
    ott_id_dict[ott] = list_file[0]

# + 추가해야 할 것
# 모든 tmdb id를 중복 없이 합친 하나의 리스트가 필요
# 그 리스트를 기준으로 json을 구축해야 함

# ott_id_dict = {"nfx": [], "dnp": [], "wac": [], "wav": [], "apt": [], "ply": []}