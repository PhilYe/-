import requests

url = 'https://fanyi.baidu.com/basetrans'
data = {
  'from':'zh','to':'en','query':'人生苦短',
'transtype':'translang',
'simple_means_flag':'3',
'sign':'822331.552714',
'token':'3f5c12d4c9dfa3460a91984955ff4629'
}
headers = {
  'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
  #'referer':'https://fanyi.baidu.com/?aldtype=16047',
  #'x-requested-with':'XMLHttpRequest',
  #'dnt':'1',
  #'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
  #'content-length':'154',
  #'accept-language':'zh-CN,zh;q=0.9',
  #'accept-encoding':'gzip, deflate, br',
  #'accept':'*/*',
  'cookie':'BAIDUID=E47C3A64E1D3BD53D94181E0251332F6:FG=1; BIDUPSID=E47C3A64E1D3BD53D94181E0251332F6; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; PSTM=1560260002; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; yjs_js_security_passport=44caf966a9c5172c117fc894f4637c6cdafb0c86_1560566313_js; H_PS_PSSID=26523_1426_21081_29135_29237_28518_29098_29369_28838_29221_26350_22157; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1560566284,1560566314,1560580343,1560581097; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1560581097; locale=zh'
}
response = requests.post(url, data = data, headers = headers)
print(response.content.decode())
#2019年测试

