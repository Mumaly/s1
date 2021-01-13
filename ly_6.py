import requests
import json
import unittest


class Zxgl(unittest.TestCase):
  def test06_xxlbss(self):#输入物流码全名搜索
    url = "http://123.57.140.190/manage/list_box.php"
    payload = {"txm":"2568739591fdsfsd223"}
    payload1 = json.dumps(payload)
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'PHPSESSID=n4co3ftdoocb4hlkl706upb6u7'
    }
    print("第六条跑成功 ")
    response = requests.post(url, headers=headers, json=payload1).text
    self.assertIn("9446366686697",response,msg="断言失败")

if __name__ == '__main__':
    unittest.main()
