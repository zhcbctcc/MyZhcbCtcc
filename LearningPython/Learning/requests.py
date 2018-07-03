# #第一个代码
# import requests
# r = requests.get('https://www.douban.com/')
# print(r.status_code)
# print(r.text)

#第二个代码:获取特定的URL
import requests
r = requests.get('https://www.douban.com/search',params={'q':'python','cat':'1001'})
print(r.url)
print(r.encoding)
print(r.content)
