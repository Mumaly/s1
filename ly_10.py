import requests
import json
import unittest


class Zxgl(unittest.TestCase):
  def test10_dxlb(self):#大箱列表管理-小箱条码模糊搜索
    url = "http://123.57.140.190/manage/list_box_big.php"

    payload = 'txm=W1ZAZIMIDS'
    cc=json.dumps(payload)
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'PHPSESSID=n4co3ftdoocb4hlkl706upb6u7'
    }
    print("第十条跑成功 ")
    response = requests.request("POST", url, headers=headers, data=cc).text
    self.assertIn("W1ZAZIMIDS",response,msg="断言失败")

if __name__ == '__main__':
    unittest.main()