from sync_voice_over.json_queries import dir_access, json_query

key='urls'
json_file = dir_access(key)
links = json_query(json_file)[key]

print(links)