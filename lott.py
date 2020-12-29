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

    def get_latest_id(self):
        id = self.db.select('ssq_history', 'MAX(id)')
        if id is not None and len(id) == 1:
            return id[0]
        return None

    def get_date_by_id(self, id):
        date = self.db.select('ssq_history', 'date', ['id = "%s"' % id])
        if date is not None and len(date) == 1:
            return date[0]
        return None

    def add_ssq_detail(self, sdata):
        self.db.insert('ssq_history', sdata)

if __name__ == '__main__':
    sq = LottSsq()
    sq.load_db_config()
    t = sq.get_latest_id()
    d = sq.get_date_by_id(t)
    hist = SsqHistory()
    sqdetail = hist.get_next_term(t, d)
    if sqdetail is not None:
        sq.add_ssq_detail(sqdetail)
    blueball = sq.get_blue_balls()
    print(blueball[0:20])
    b = get_random_blue_number(blueball)
    print(b)
