import requests
import re
# r = requests.get('https://static1.scrape.cuiqingcai.com/')
# pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
# r.status_code
# titles = re.findall(pattern, r.text)

# print(titles)

# 
"""
<RequestsCookieJar[<Cookie _octo=GH1.1.320366172.1585402952 for .github.com/>, <Cookie logged_in=no for .github.com/>, <Cookie _gh_sess=OiVp6NnAg2w3Nt3Go7cCspSNLdggENinlTO3EdRbpQQGpQpLSws1MEi47mfeHoTtdHCnzBw%2FNuK6Q91mb55tEqDkr%2BB%2FXbozXFXV7DMNZ5MHMiOJOcXFlP8T2R7CFd8sBk7Ku5FHe9CySSFUSl%2FYUoWwrCRVvp4l8A5BkvUmnad4G3wwg5JDuzzXbYhQQpkwEA4mq6qAqUufkCQ9ZwzBF3tSzH85GbQa5%2FajI1XtmiOdS2LyA7O0aop4%2F3LNoCzZ9nlg7EIV6AIFjvIYP2YAgQ%3D%3D--3pRpoept0JcvExD8--O1M%2BRpAMDd0C6FsoZT7G8w%3D%3D for github.com/>]>
"""
# r = requests.get("https://github.com")
# print(r.text)


# cookie 模拟登陆
"""
<RequestsCookieJar[<Cookie _octo=GH1.1.71532192.1585403244 for .github.com/>, <Cookie logged_in=no for .github.com/>, <Cookie _gh_sess=4bg7wShQkU02utA5ekV%2FrQD48W1vXKbBG4c3t9JsC78abRsjDHl0PBQ%2BULkgeIVD8iUh44OVHyk0NmQ%2BgzNTu%2BzEzPxK8bLvYawswAD4TY5NJtA5wIY0HVZS%2FVuSfdn2aXWKbsD6pNNSlij87ZpDZ1jbKtuLjW52N4IN2HUnvcjGGmx5ZwrgV%2BLIRZs9tN%2F%2FuN3Z%2FJ5TjeNLbVFl5Q%2Bvz%2B55iCj63ni6NPRSvEv9My2wblFtAySd%2Fs8BXgT9CwABM6LEX0W8UwuUmH5XydZ2iQ%3D%3D--T5x3GriDnWcimJmm--htRdF16dUU2kP8rn%2B3oI9Q%3D%3D for github.com/>]>
"""
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36 Edg/83.0.461.1'
# }
# r = requests.get("https://github.com/", headers=headers)

# # print(r.cookies)

# f = open("html2.html","w", encoding='utf-8')
# f.write(r.text)
# f.close()


# session 维持
"""
{
  "cookies": {}
}
"""
# requests.get("http://httpbin.org/cookies/set/number/123456789")
# r = requests.get("http://httpbin.org/cookies")
# print(r.text)

# s = requests.Session()
# s.get("http://httpbin.org/cookies/set/number/123456789")
# r = s.get("http://httpbin.org/cookies")
# print(r.text)


# ssl 证书验证

response = requests.get("http://static2.scrape.cuiqingcai.com/", verify=False)
print(response.status_code)