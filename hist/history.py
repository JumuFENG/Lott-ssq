# Python 3
# -*- coding: utf-8 -*-

import requests
import re
from datetime import datetime,timedelta,date

class SsqHistory(object):
    def get_request(self, url):
        headers = {
            'Host': 'www.17500.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
        params=None
        proxies=None

        rsp = requests.get(url, headers=headers, params=params, proxies=proxies)
        rsp.raise_for_status()
        return rsp.text

    def get_http_rsp(self):
        with open('text.txt','r', encoding='utf-8') as f:
            return f.read()

    def get_ssq_details(self, id):
        url = 'https://www.17500.cn/ssq/details.php?issue=%s' % id
        ssq_details = self.get_request(url)
        #ssq_details = self.get_http_rsp()
        #print(ssq_details)
        tbls = re.findall(r"<TABLE.*?>(.*?)</TABLE>", ssq_details, re.DOTALL|re.I)
        if not len(tbls) == 6:
            print("html content do not contains 6 tables, check the response!")
            return

        ssq = {}
        ssq['id'] = str(id)

        date = tbls[2]
        date = re.findall(r"<td align=\"right\">(.*?)开奖</td></tr>", date)
        if date is None or not len(date) == 1:
            print('date info error: \n', tbls[2])
            return
        ssq['date'] = date[0]

        redblue = tbls[3]
        red = re.findall(r"red>(.*?)</font>", redblue)
        if not len(red) == 6:
            print('red blue not correct:\n', redblue)
            return
        ssq['red_all'] = ''
        for r in red:
            ssq['red_all'] += r

        blue = re.findall(r"blue>(.*?)</font>", redblue)
        if not len(blue) == 1:
            print('red blue not correct:\n', redblue)
            return
        ssq['blue'] = blue[0]

        awards = tbls[4]
        awards = re.findall(r".*?等奖.*?align=center>(.*?)</TD>.*?align=center>(.*?)</TD>", awards, re.DOTALL)
        if awards is None or not len(awards) == 6:
            print('award info error:\n', tbls[4])
            return

        for i in range(0, 6):
            ssq['award' + str(i+1) + '_count'] = awards[i][0].replace(',', '')
            ssq['award' + str(i+1) + '_money'] = awards[i][1].replace(',', '')
        
        extra_info = tbls[5]
        extra_info = re.findall(r"投注总额为：(.*?)元<br>奖池金额为：(.*?)元.*?出球顺序：(.*?)。。", extra_info, re.DOTALL)
        if extra_info is None or not len(extra_info[0]) == 3:
            print('extra info error:\n', tbls[5])
            return

        extra_info = extra_info[0]
        ssq['total_buy'] = extra_info[0].replace(',', '')
        ssq['remained'] = extra_info[1].replace(',', '')
        red_order = extra_info[2].split('+')[0].strip().split()
        for i in range(0,6):
            ssq['red_' + str(i+1)] = red_order[i]

        return ssq

    def get_next_term(self, lastid, lastdate = None):
        if lastdate is None:
            return self.get_ssq_details(int(lastid) + 1)
        if isinstance(lastdate, str):
            lastdate = datetime.strptime(lastdate, '%Y-%m-%d').date()
        if not isinstance(lastdate, date):
            print('error argument lastdate: %s, %s' % (lastdate, type(lastdate)))
            
        today = datetime.today().date()
        nextdate = lastdate + timedelta(days = 1)
        while True:
            if nextdate.weekday() == 1 or nextdate.weekday() == 3 or nextdate.weekday() == 6:
                break;
            nextdate = nextdate + timedelta(days = 1)

        if (today - nextdate).days < 0:
            print('date not match. today = %s, next term = %s' % (today, nextdate))
            return None

        if (today - nextdate).days == 0:
            now = datetime.now()
            if now.hour < 21:
                print('the result will declare after 21:15.')
                return None
            if now.hour == 21 and now.minute < 16:
                print('the result will declare after 21:15.')
                return None

        nextid = int(lastid) + 1
        if not nextdate.year == lastdate.year:
            nextid = nextdate.year * 1000 + 1
        return self.get_ssq_details(nextid)

if __name__ == '__main__':
    hist = SsqHistory()
    hist.get_ssq_details(2020131)
