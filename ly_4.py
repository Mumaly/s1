import requests
import json
import unittest


class Zxgl(unittest.TestCase):
  def test04_xxlbss(self):#通过产品物流码模糊搜索
    url = "http://123.57.140.190/manage/list_box.php"
    payload = 'txm=5512'
    payload1 = json.dumps(payload)
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'PHPSESSID=n4co3ftdoocb4hlkl706upb6u7'
    }
    print("第四条跑成功 ")
    response = requests.post(url, headers=headers, data=payload1).text
    self.assertIn("EKD1IUE6EQXUSR1GUG",response,msg="断言失败")

if __name__ == '__main__':
    unittest.main()

