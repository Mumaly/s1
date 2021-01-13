import requests
import json
import unittest


class Zxgl(unittest.TestCase):
  def test01_xxlbss(self):#通过小箱条码模糊搜索
    url = "http://123.57.140.190/manage/list_box.php"
    payload = 'box=S9HZ'
    payload1 = json.dumps(payload)
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'PHPSESSID=n4co3ftdoocb4hlkl706upb6u7'
    }
    print("第一条跑成功 ")
    response = requests.post(url, headers=headers, data=payload1).text
    self.assertIn("T1KPLI",response,msg="断言失败")

if __name__ == '__main__':
    unittest.main()

