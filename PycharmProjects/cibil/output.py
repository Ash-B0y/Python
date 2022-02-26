import json
main_stru ={}
with open("Video_marker.json") as file:
    json_file = json.loads(file.read())
    print(json_file)
    for  i in json_file['video_markers']:
        inner_most_list = []
        for  j in i['items']:
            inner_most_stru ={}
            inner_id = j['id']
            inner_most_stru['inner_id'] = inner_id
            inner_most_list.append(inner_most_stru)
            break
    