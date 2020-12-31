# Python 3
# -*- coding: utf-8 -*-

import json
from db_utils.sql_helper import SqlHelper
from randgen.rand import get_random_blue_number
from hist.history import SsqHistory

class LottSsq():
    def load_db_config(self):
        self.db = None
        with open('db_utils/db.config', 'r', encoding='utf-8') as fp:
            db_config = json.load(fp=fp)
            self.db = SqlHelper(db_config['Host'], db_config['User'], db_config['Password'], database=db_config['DB'])

    def get_blue_balls(self):
        return self.db.select('ssq_history', 'blue', order=' ORDER BY id DESC')

    def get_latest_id_date(self):
        dd = self.db.select('ssq_history', ['id', 'date'], ['id = ( select MAX(id) from ssq_history )'])
        if dd is not None and len(dd) == 1:
            return dd[0]

    def add_ssq_detail(self, sdata):
        self.db.insert('ssq_history', sdata)

if __name__ == '__main__':
    sq = LottSsq()
    sq.load_db_config()
    td = sq.get_latest_id_date()
    if td is None:
        print("error when get_latest_id_date!")
        exit()
    hist = SsqHistory()
    sqdetail = hist.get_next_term(td['id'], td['date'])
    print(sqdetail)
    if sqdetail is not None:
        sq.add_ssq_detail(sqdetail)
    blueball = sq.get_blue_balls()
    print(blueball[0:20])
    b = get_random_blue_number(blueball)
    print(b)
