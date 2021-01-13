import requests
import json
import unittest


class Zxgl(unittest.TestCase):
  def test09_dxlb(self):#大箱列表管理-输入不存在的大箱条码，搜索
    url = "http://123.57.140.190/manage/list_box_big.php"

    payload = 'box=附加贷款列夫朗道'
    cc=json.dumps(payload)
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'PHPSESSID=n4co3ftdoocb4hlkl706upb6u7'
    }
    print("第九条跑成功 ")
    response = requests.request("POST", url, headers=headers, data=cc).text
    self.assertNotIn("附加贷款列夫朗道",response,msg="断言失败")

if __name__ == '__main__':
    unittest.main()