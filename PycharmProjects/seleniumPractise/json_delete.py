# import json
#
# my_json = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
#
# my_list = json.loads(my_json)
#
# for idx, dictionary in enumerate(my_list):
#     if dictionary['id'] == 2:
#         my_list.pop(idx)
#
# # 👇️ [{'id': 1, 'name': 'Alice'}]
# print(my_list)
#
# json_again = json.dumps(my_list)
# print(json_again) # 👉️ '[{"id": 1, "name": "Alice"}]'
import json

# data = ["DisneyPlus", "Netflix", "Peacock"]
# json_string = json.dumps(data)
# print(json_string)

appDict = {
    'name': 'messenger',
    'playstore': True,
    'company': 'Facebook',
    'price': 100
}
app_json = json.dumps(appDict)
print(app_json)
