import  requests
import json
import unittest


class Zxgl(unittest.TestCase):

  def test03_xxlbss(self):#输入不存在的小箱条码，搜索
    url = "http://123.57.140.190/manage/list_box.php"
    payload = 'box=sdasdadsadasdadada'
    payload1 = json.dumps(payload)
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'PHPSESSID=n4co3ftdoocb4hlkl706upb6u7'
    }
    print("第三条跑成功 ")
    response = requests.post(url, headers=headers, data=payload1).text
    self.assertNotIn("sdasdadsadasdadada",response,msg="断言失败")

if __name__ == '__main__':
    unittest.main()

