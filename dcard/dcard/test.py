import json,codecs
global false, null, true
false = null = true = ""

result = []
with open('data.json',encoding='utf-8') as f:
    data = f.readline()
    while data:
        data_detail = json.loads(data)
        for article in data_detail:
            if int(article['likeCount']) > 500:
                result.append(article)
                print("id:",article['id'])
                print("title:",article['title'])
                print("media:",article['media'])
                print("likeCount:",article['likeCount'])
        data = f.readline()

f = codecs.open('result.json')
the_result = json.dumps(result)
print(the_result,type(the_result))
f.write(the_result)
f.close()