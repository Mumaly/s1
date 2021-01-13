import requests
import json
import unittest


class Zxgl(unittest.TestCase):
  def test02_xxlbss(self):#通过小箱条码全名搜索
    url = "http://123.57.140.190/manage/list_box.php"
    payload = 'box=KQ12UULMTMTYTYEN15'
    payload1 = json.dumps(payload)
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'PHPSESSID=n4co3ftdoocb4hlkl706upb6u7'
    }
    print("第二条跑成功 ")
    response = requests.post(url, headers=headers, data=payload1).text
    self.assertIn("KQ12UULMTMTYTYEN15",response,msg="断言失败")

if __name__ == '__main__':
    unittest.main()

