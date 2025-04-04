import requests
from lxml import html

# initialize output list
output_list = []

# Proxy details
proxies = {
    "http": "http://ae026b183ea34b3cb19d570e5841eac62f1a191924f@proxy.scrape.do:8080",
    "https": "https://ae026b183ea34b3cb19d570e5841eac62f1a191924f@proxy.scrape.do:8080",
}


cookies = {
    '_rvt': 'cFg73dCSxT5eVQZMXDYg-3U9BeqSvP57Nw9QYknWMyEk0AjUnKjSjxuHfNsNs2YgwULx1mUGAjgq-SmRr75EBwI1QVDXqDKMolRN3fCbpd01',
    'd': 'eaJwxlHi3QFaNzSnWKi2SIH3gFG50MPsI10KrQ2',
    's': 'Qbv8zZO6Wka6edCHJ8uV-2dyXPfFct0I0',
    'auths': '0',
    '_gcl_au': '1.1.682509549.1743694806',
    '_ga': 'GA1.1.571491091.1743694806',
    'bm_lso': '8F46CC5FFB535A292CED1FB78E11998B690D07BC6E78A07B61D94FD08830C086~YAAQBvQwF/0f+vWVAQAA69zN/AMwBQkiKmtNftpY3WLksI4homUBRWR42BQKw1C+9Gqbg+3ZrA4oJejpO43DeqORbLxt+H/+0oD1lX+LRWvTemAnqz6JQS/vzyXE2T+rb3IVstOAKwEa0YbhjdlbBGTa2Iy05pyXe7egxfo2JHFAb+7fcPORyNbTw+ZPe4L5r10RmdQ2jVJ8Ce+oD61N8xIOeerpjnhJ+xP9vyXFv0QbdwB+saYOCxNLwiO7fQpVqq67fBb2OxJoGOY+0G/dhP9/BTUw4gboG5yv5Rhlq6SFKhvso5J8j8SHO2wFAyliO59uaViaKu9jOKGH3u6fxc60PTtJuEDAFqb/AXr58QKsRNzOeGLB9883F7VNewvkWQmhykjwpFbCXtGzeLXCAReiPwRqAbZTY/kDHYuDfVHZN0jpyoIqYYaPYT9cHK2ZQxVdqK8avmrIKRL5mAm6^1743703035447',
    'wsso-session': 'eyJ1bCI6bnVsbCwidXBsIjp7ImN0IjoiVVMiLCJuIjoiRmxvcmlkYSUyMENpdHkiLCJsdCI6MjUuNDQ3ODkwMywibGciOi04MC40NzkyMTk2LCJzcmMiOiJRVUVSWV9QQVJBTSJ9LCJkIjpudWxsLCJydiI6eyJjIjpbXSwiZSI6W10sImwiOltdLCJydGNfdSI6bnVsbCwicnRjX2V0IjoiMjAyNS0wNC0wM1QxNTo0MToxOC4wMzg5MDg5WiJ9LCJmYyI6eyJjIjpbXX0sInAiOltdLCJpZCI6bnVsbH0=',
    'wsso': 'eyJ1bCI6bnVsbCwidXBsIjp7Im4iOm51bGwsInMiOmZhbHNlLCJsZyI6MC4wLCJsdCI6MC4wLCJjdCI6bnVsbCwic3JjIjoiREVWSUNFIiwiZHQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwKzAwOjAwIn0sImQiOnsidHlwZSI6MCwiZGF0ZXMiOnsiZnJvbSI6bnVsbCwidG8iOiI5OTk5LTEyLTMxVDIzOjU5OjU5Ljk5OTk5OTlaIiwiZXhwaXJhdGlvbiI6bnVsbH19LCJydiI6eyJjIjpbXSwiZSI6W3sidCI6IjIwMjUtMDQtMDNUMTg6NDU6MTQuNjI4NjM3NVoiLCJpZCI6MTU0NTc0OTcyfV0sImwiOltdLCJydGNfdSI6bnVsbCwicnRjX2V0IjoiMjAyNS0wNC0wM1QxNTo0MToxOC4wMzg5MDg5WiJ9LCJmYyI6eyJjIjpbXX0sInAiOltdLCJpZCI6bnVsbH0=',
    'bm_s': 'YAAQDfQwF31sDuuVAQAA4734/AOK+aAR7veRHIV93ywkKhyJz+1oTSGWt9M1tmikDNglxtQrkrwjPyLpXmvVRjCm8RmaofSHmM6T9M3YHgcrHOWughqxDZKnkSyWZOIFahmvxPk9WB4T5fsKcHZ3/ICO6kgdn6X2cF8+4Qx5nnaf8fzVwh1rDsx8K87/lyhoHJSB6KtsuajUdzu2EI1mmdriTVjLwTrtxvhf/uTyTW0M2fa+9Inxqv2tvovJ9VDsbVzsD5jukc57dFx0XGfMAr+MuYU2xw9qwJTVJ9sm2kuyVVUnGPjAILlbXTAXeHr02tEEc3bPxhWfi5gS/kNu6NrgTLEygFAGWgWTTJX3+EIEG88v42tOGLN08bhDa/cJQ+XMISRjM2SairHLmg8gww/T7+4bUQZivfcd3Hj0zXElIbjVuCwFaAMMout75/v48DRe/T8Qa+TGb7Lq',
    'bm_so': '856090440562E90A6A5A67BD3B7A0D7C346D61F014A2C90B0E9C780AADE44A27~YAAQDfQwF35sDuuVAQAA4734/ANELBCGTQaevQ4YZW/CDa9YJBy4q9d6KHQ9Hg8pFR2eLZc39Ly2JsQn7EDTrTVb+HuHs7LsIeKq5ThWUC5ypPnP7sMfqfHkX59OTQqe/LtIef0ZZkf87ssWKxn1GquIPrxBig7lGAeK/p6qtFdUO2G9rnIWQjQ8CGKClbS30dkp25dKq5w2xjf6JM2aLLAWhB7aN4fZCUjNqvpO1DDHIG2kD+PJ8joU/PLJrM+xftNkof6DUhlDiIyoZWE4YggCBhtC3GUmTaohvaeEAlbN3e9y50hQ8AH2XiP/JeRae/195tLW+8bobkPxuBnylgxyEfZ208VAfT7REwO/iD2f4EK7BYPqSKv1lJHenmCibIRvlBmXSbqXTeuI4WpFlJVmoEpkK7HTHGzxgCEcj0G/wawll7kfoxyIHMx/DK42ai8EPFzMqzOwTn/6ilXx',
    'ulv-ed-event': '{"154574972":[1743705843820,1743703035782]}',
    '_fbp': 'fb.1.1743705844682.485440210253329850',
    'lastRskxRun': '1743705845300',
    'rskxRunCookie': '0',
    'rCookie': 'oueitxq6esgz2qudilvgmm91pft4o',
    'forterToken': '4c3b6cb3df7c420d9ace2318cee408f4_1743705844003__UDF43-m4_24ck_8Dna8zIAWOM%3D-1795-v2',
    'forterToken': '4c3b6cb3df7c420d9ace2318cee408f4_1743705844003__UDF43-m4_24ck_8Dna8zIAWOM%3D-1795-v2',
    '_uetsid': 'ea76b8f010a111f09a9c619a32f7f7b3',
    '_uetvid': 'ea76d56010a111f09456954236a3a15d',
    '_ga_1686WQLB4Q': 'GS1.1.1743708591.4.1.1743708612.0.0.0',
    'bm_sz': '86F5AC2455B147CD5B540CBA1C2801BB~YAAQNhzFF+1UAPSVAQAAGZAy/ht1Mq/8YCK2WQpHacG/f5VysQGmApvZJSBxGqs/Xy/hjhmqdizaoOXHZkIKHfC87YcGmjHaJBw/M8dO+XtLVmXHVRGc3EjE3M/O5gUN0D7NYTgwIHuNJ280/+GJDoTl3r84qCQjLp2beJ6mtbqoXQNmqOsW+YghpTXDlkoF9Jc4mYRM+fdr0LEFEL6E6G2+PSxjjqpDUCP/5BUi2wKo6VUKvMRCRSA7e93x6dQLNPh9HWUXweqIl/HY14aDO2zF0Lmm5jqmEkPbNJnUg8vQGIoLTONqX+ws7gS34q6n7wUvWov40Nbm0QFQYycYE/O7m60GhL3Bm1CecX7VuMrlGp2B3/AsfQ==~3686722~3360313',
    'akacd_rls': '1743748373~rv=40~id=c089e25584067c9b35674dcfda36678f',
    '_abck': 'F9DB17A5984B12FC97FA8508F17D1E84~0~YAAQDfQwF/vzDuuVAQAANgY3/g1zEW30VLT5Q20DY6MumAWqoJRozvFFYwrkzqFsN9F6XuOTGHK6PthaBjWMluNxFR3qcHkxOVeaUuJqgW129DUlylrayNd7cwvXce4DNVTzxHrUbo2mszSgynJYBNoQeXztPcm8/g9V2RgxrruNTaURBgfqeoUYM/UYquANQYFRSJsRp3LYx+3eCCuqoDFKDZTgmxNVDRcjK2fFWzoeYiFypBdp8ZBYB7/+WE3pShhv0y6zOlamP0+eOFLzm82OQnbZI3bMj2xDWa0ykSfyalhKAF4ZIvaJGwWbBIQPLool6G9bpnoWdBViKsmbevKPs4gYiakktUjBgzZXLk/K0yIjPfiZMej/n7V5SYJXdyKVgZ1hCgwz9cbTg8KULcYiUlWoJ0LmrTEael0n7kFFD7mKom7vT8nPSHMv+hgNDa/6cknAfGgi3HsBRW6B4TQ4Bc/oSkyPtrwD6eu7Midz+EsJoc7lyNToi+RrIGhjbirXYxjf7tS+OjJr6UjElrWRn8KfUCAJ5UsC65N5WdeHpA7XJvduw/nuaDvI9DJj52NzBKJ8sZALD0vsSTDInHenp5Ylz2MXl7UK~-1~||0||~1743709461',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-US;q=0.9,en;q=0.8,mr;q=0.7',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    # 'cookie': '_rvt=cFg73dCSxT5eVQZMXDYg-3U9BeqSvP57Nw9QYknWMyEk0AjUnKjSjxuHfNsNs2YgwULx1mUGAjgq-SmRr75EBwI1QVDXqDKMolRN3fCbpd01; d=eaJwxlHi3QFaNzSnWKi2SIH3gFG50MPsI10KrQ2; s=Qbv8zZO6Wka6edCHJ8uV-2dyXPfFct0I0; auths=0; _gcl_au=1.1.682509549.1743694806; _ga=GA1.1.571491091.1743694806; bm_lso=8F46CC5FFB535A292CED1FB78E11998B690D07BC6E78A07B61D94FD08830C086~YAAQBvQwF/0f+vWVAQAA69zN/AMwBQkiKmtNftpY3WLksI4homUBRWR42BQKw1C+9Gqbg+3ZrA4oJejpO43DeqORbLxt+H/+0oD1lX+LRWvTemAnqz6JQS/vzyXE2T+rb3IVstOAKwEa0YbhjdlbBGTa2Iy05pyXe7egxfo2JHFAb+7fcPORyNbTw+ZPe4L5r10RmdQ2jVJ8Ce+oD61N8xIOeerpjnhJ+xP9vyXFv0QbdwB+saYOCxNLwiO7fQpVqq67fBb2OxJoGOY+0G/dhP9/BTUw4gboG5yv5Rhlq6SFKhvso5J8j8SHO2wFAyliO59uaViaKu9jOKGH3u6fxc60PTtJuEDAFqb/AXr58QKsRNzOeGLB9883F7VNewvkWQmhykjwpFbCXtGzeLXCAReiPwRqAbZTY/kDHYuDfVHZN0jpyoIqYYaPYT9cHK2ZQxVdqK8avmrIKRL5mAm6^1743703035447; wsso-session=eyJ1bCI6bnVsbCwidXBsIjp7ImN0IjoiVVMiLCJuIjoiRmxvcmlkYSUyMENpdHkiLCJsdCI6MjUuNDQ3ODkwMywibGciOi04MC40NzkyMTk2LCJzcmMiOiJRVUVSWV9QQVJBTSJ9LCJkIjpudWxsLCJydiI6eyJjIjpbXSwiZSI6W10sImwiOltdLCJydGNfdSI6bnVsbCwicnRjX2V0IjoiMjAyNS0wNC0wM1QxNTo0MToxOC4wMzg5MDg5WiJ9LCJmYyI6eyJjIjpbXX0sInAiOltdLCJpZCI6bnVsbH0=; wsso=eyJ1bCI6bnVsbCwidXBsIjp7Im4iOm51bGwsInMiOmZhbHNlLCJsZyI6MC4wLCJsdCI6MC4wLCJjdCI6bnVsbCwic3JjIjoiREVWSUNFIiwiZHQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwKzAwOjAwIn0sImQiOnsidHlwZSI6MCwiZGF0ZXMiOnsiZnJvbSI6bnVsbCwidG8iOiI5OTk5LTEyLTMxVDIzOjU5OjU5Ljk5OTk5OTlaIiwiZXhwaXJhdGlvbiI6bnVsbH19LCJydiI6eyJjIjpbXSwiZSI6W3sidCI6IjIwMjUtMDQtMDNUMTg6NDU6MTQuNjI4NjM3NVoiLCJpZCI6MTU0NTc0OTcyfV0sImwiOltdLCJydGNfdSI6bnVsbCwicnRjX2V0IjoiMjAyNS0wNC0wM1QxNTo0MToxOC4wMzg5MDg5WiJ9LCJmYyI6eyJjIjpbXX0sInAiOltdLCJpZCI6bnVsbH0=; bm_s=YAAQDfQwF31sDuuVAQAA4734/AOK+aAR7veRHIV93ywkKhyJz+1oTSGWt9M1tmikDNglxtQrkrwjPyLpXmvVRjCm8RmaofSHmM6T9M3YHgcrHOWughqxDZKnkSyWZOIFahmvxPk9WB4T5fsKcHZ3/ICO6kgdn6X2cF8+4Qx5nnaf8fzVwh1rDsx8K87/lyhoHJSB6KtsuajUdzu2EI1mmdriTVjLwTrtxvhf/uTyTW0M2fa+9Inxqv2tvovJ9VDsbVzsD5jukc57dFx0XGfMAr+MuYU2xw9qwJTVJ9sm2kuyVVUnGPjAILlbXTAXeHr02tEEc3bPxhWfi5gS/kNu6NrgTLEygFAGWgWTTJX3+EIEG88v42tOGLN08bhDa/cJQ+XMISRjM2SairHLmg8gww/T7+4bUQZivfcd3Hj0zXElIbjVuCwFaAMMout75/v48DRe/T8Qa+TGb7Lq; bm_so=856090440562E90A6A5A67BD3B7A0D7C346D61F014A2C90B0E9C780AADE44A27~YAAQDfQwF35sDuuVAQAA4734/ANELBCGTQaevQ4YZW/CDa9YJBy4q9d6KHQ9Hg8pFR2eLZc39Ly2JsQn7EDTrTVb+HuHs7LsIeKq5ThWUC5ypPnP7sMfqfHkX59OTQqe/LtIef0ZZkf87ssWKxn1GquIPrxBig7lGAeK/p6qtFdUO2G9rnIWQjQ8CGKClbS30dkp25dKq5w2xjf6JM2aLLAWhB7aN4fZCUjNqvpO1DDHIG2kD+PJ8joU/PLJrM+xftNkof6DUhlDiIyoZWE4YggCBhtC3GUmTaohvaeEAlbN3e9y50hQ8AH2XiP/JeRae/195tLW+8bobkPxuBnylgxyEfZ208VAfT7REwO/iD2f4EK7BYPqSKv1lJHenmCibIRvlBmXSbqXTeuI4WpFlJVmoEpkK7HTHGzxgCEcj0G/wawll7kfoxyIHMx/DK42ai8EPFzMqzOwTn/6ilXx; ulv-ed-event={"154574972":[1743705843820,1743703035782]}; _fbp=fb.1.1743705844682.485440210253329850; lastRskxRun=1743705845300; rskxRunCookie=0; rCookie=oueitxq6esgz2qudilvgmm91pft4o; forterToken=4c3b6cb3df7c420d9ace2318cee408f4_1743705844003__UDF43-m4_24ck_8Dna8zIAWOM%3D-1795-v2; forterToken=4c3b6cb3df7c420d9ace2318cee408f4_1743705844003__UDF43-m4_24ck_8Dna8zIAWOM%3D-1795-v2; _uetsid=ea76b8f010a111f09a9c619a32f7f7b3; _uetvid=ea76d56010a111f09456954236a3a15d; _ga_1686WQLB4Q=GS1.1.1743708591.4.1.1743708612.0.0.0; bm_sz=86F5AC2455B147CD5B540CBA1C2801BB~YAAQNhzFF+1UAPSVAQAAGZAy/ht1Mq/8YCK2WQpHacG/f5VysQGmApvZJSBxGqs/Xy/hjhmqdizaoOXHZkIKHfC87YcGmjHaJBw/M8dO+XtLVmXHVRGc3EjE3M/O5gUN0D7NYTgwIHuNJ280/+GJDoTl3r84qCQjLp2beJ6mtbqoXQNmqOsW+YghpTXDlkoF9Jc4mYRM+fdr0LEFEL6E6G2+PSxjjqpDUCP/5BUi2wKo6VUKvMRCRSA7e93x6dQLNPh9HWUXweqIl/HY14aDO2zF0Lmm5jqmEkPbNJnUg8vQGIoLTONqX+ws7gS34q6n7wUvWov40Nbm0QFQYycYE/O7m60GhL3Bm1CecX7VuMrlGp2B3/AsfQ==~3686722~3360313; akacd_rls=1743748373~rv=40~id=c089e25584067c9b35674dcfda36678f; _abck=F9DB17A5984B12FC97FA8508F17D1E84~0~YAAQDfQwF/vzDuuVAQAANgY3/g1zEW30VLT5Q20DY6MumAWqoJRozvFFYwrkzqFsN9F6XuOTGHK6PthaBjWMluNxFR3qcHkxOVeaUuJqgW129DUlylrayNd7cwvXce4DNVTzxHrUbo2mszSgynJYBNoQeXztPcm8/g9V2RgxrruNTaURBgfqeoUYM/UYquANQYFRSJsRp3LYx+3eCCuqoDFKDZTgmxNVDRcjK2fFWzoeYiFypBdp8ZBYB7/+WE3pShhv0y6zOlamP0+eOFLzm82OQnbZI3bMj2xDWa0ykSfyalhKAF4ZIvaJGwWbBIQPLool6G9bpnoWdBViKsmbevKPs4gYiakktUjBgzZXLk/K0yIjPfiZMej/n7V5SYJXdyKVgZ1hCgwz9cbTg8KULcYiUlWoJ0LmrTEael0n7kFFD7mKom7vT8nPSHMv+hgNDa/6cknAfGgi3HsBRW6B4TQ4Bc/oSkyPtrwD6eu7Midz+EsJoc7lyNToi+RrIGhjbirXYxjf7tS+OjJr6UjElrWRn8KfUCAJ5UsC65N5WdeHpA7XJvduw/nuaDvI9DJj52NzBKJ8sZALD0vsSTDInHenp5Ylz2MXl7UK~-1~||0||~1743709461',
}

params = {
    'lat': 'MjUuNDQ3ODkwMw==',
    'lon': 'LTgwLjQ3OTIxOTY=',
    'to': '253402300799999',
    'tlcId': '2',
}

# Send request using proxy
try:
    response = requests.get('https://www.stubhub.com/explore', params=params, cookies=cookies, headers=headers,proxies=proxies, timeout=10)
    if response.status_code ==200:  # check response 
        html_content = response.text
except:
    print("Proxy didnt provide proper response... Using raw html")
    with open("response.html", "r", encoding="utf-8") as file:
        html_content = file.read()  # if not getting data with/without proxy,  directly used raw html data from url 
    

# Parse HTML
tree = html.fromstring(html_content)

# Extract elements
elements = tree.xpath('//ul[@class="sc-13546f91-1 bDlbkX"]')


# Extract details from each element
for i in elements:
    title_list = i.xpath("//p[@class='sc-9b60a1e0-6 hvVHAU']/text()")  #Extracts the title.
    datetime_list = i.xpath("//p[@class='sc-9b60a1e0-8 haloEs'][1]/text()") #Extracts the first occurrence of the date/time.
    location_list = i.xpath("//p[@class='sc-9b60a1e0-8 haloEs'][2]/text()") # Extracts the second occurrence of the date/time.
    image_list = i.xpath("//div[@class='sc-9b60a1e0-1 kIZVBw']//img/@src")  #Extracts image_url
    
    
#manipulate  extracted data into json data
for title,date_time,location,image_url in zip(title_list,datetime_list,location_list,image_list):
    output_list.append({
        "title": title,
        "datetime": date_time,
        "location": location,
        "image_url" : image_url
    })

print(output_list)   


