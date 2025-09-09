import requests
import re
import openpyxl
def get_station():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9350'
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Mobile Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    # print(resp.text)
    stations = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', resp.text)
    return stations
def save(lst):
    wb = openpyxl.Workbook()
    ws = wb.active
    for item in lst:
        ws.append(item)
    # 修正：文件扩展名应该是 .xlsx
    wb.save('车站代码.xlsx')
    print("数据已保存到 车站代码.xlsx")
if __name__ == '__main__':
    lst = get_station()
    save(lst)