import requests

headers = {
    'Cookie': '_octo=GH1.1.677862355.1577348141; _ga=GA1.2.1528640652.1577348142; _device_id=5a23270379be44969b57aa8bb836cadd; user_session=GhCrjuBA5Ae0EOE_mAxWl4YizoQ7YSd8AQin1Boh6cw9tDgO; __Host-user_session_same_site=GhCrjuBA5Ae0EOE_mAxWl4YizoQ7YSd8AQin1Boh6cw9tDgO; logged_in=yes; dotcom_user=huobingli; tz=Asia%2FShanghai; _gh_sess=88KfwHcl1iBJNOijSQA3jKQcg%2BdCncyM76QWQBrya3X82l3WE%2B9XuzEt59V9Z6qA7iH%2B8wyzr4VeOr5Av%2FXIC%2B1QKsyvWjRDEg%2B2kC9s%2F9FBlzfvAhgL3VerTdJ3%2F3jyrDDaaJe8JmdbeYdQTq87HZDzoMcybGp053ksQ25FxQnRr6nxDCG2LqsUXbPZrLPX--Qo5lb%2BNOVRYjrovm--EHYoEcfpx%2FEAO40ixhjafA%3D%3D',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36 Edg/83.0.461.1'
}
r=requests.get("https://github.com",headers=headers)
print(r.cookies)

res_cookies_dic = requests.utils.dict_from_cookiejar(r.cookies)
print(res_cookies_dic)

print("----------\n")

filename='html.html'
with open(filename, 'a', encoding='utf-8') as f:
    f.write(r.text)

