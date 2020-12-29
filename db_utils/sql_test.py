# Python 3
# -*- coding: utf-8 -*-

from sql_helper import SqlHelper
import json

def load_db_config():
    with open('db.config', 'r', encoding='utf-8') as fp:
        db_config = json.load(fp=fp)
        return db_config

def get_ssq_history(sf):
    ssqdata = []
    with open(sf, 'r', encoding='utf-8') as f:
        data = f.readlines()
        for line in data:
            l = line.strip()
            row = line.split(',')
            r = {}
            r['id'] = row[0]
            r['date'] = row[1]
            all_red = ''
            for i in range(2, 8):
                all_red += str(row[i]).zfill(2)
            r['red_all'] = all_red
            r['blue'] = row[8]
            for i in range(1,7):
                r['red_' + str(i)] = row[8+i]
            r['total_buy'] = row[15]
            r['remained'] = row[16]
            r['award1_count'] = row[17]
            r['award1_money'] = row[18]
            r['award2_count'] = row[19]
            r['award2_money'] = row[20]
            r['award3_count'] = row[21]
            if not int(row[22]) == 0:
                r['award3_money'] = row[22]
            r['award4_count'] = row[23]
            if not int(row[24]) == 0:
                r['award4_money'] = row[24]
            r['award5_count'] = row[25]
            if not int(row[26]) == 0:
                r['award5_money'] = row[26]
            r['award6_count'] = row[27]
            if not int(row[28]) == 0:
                r['award6_money'] = row[28]
            ssqdata.append(r)
    return ssqdata

if __name__ == '__main__':
    db_config = load_db_config()
    db = SqlHelper(db_config['Host'], db_config['User'], db_config['Password'], database=db_config['DB'])
    #db.delete_table('ssq_history')
    if not db.is_exist_table('ssq_history'):
        db.execute_sql_file('ssq.sql')
    # ssqdata = get_ssq_history('ssq.csv')
    # db.insert_many('ssq_history', datalist = ssqdata)
    t = db.select('ssq_history', 'blue')
    # t = db.is_exist_table('ssq_history')
    print(t)
    # t = db.is_exist_table('ssqq')
    # print(t)