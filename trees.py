#/usr/bin/python3
# encoding: utf-8
import dbutils

class Trees():

    _db = ''

    def __init__(self):
        self._db = dbutils.DBUtils()

    def get(self, id):
        return self._db.get('select id, parent_id, name, lft, rght from trees where id = "%d" ' % id)

    def get_by_name(self, name):
        return self._db.get('select id, parent_id, name, lft, rght from trees where name = "%s" ' % name)

    def add(self, p_name, name):

        p_id = 0
        p_lft = 0
        p_rght = 0

        n_lft = 1

        if p_name is not None:
            p = self.get_by_name(p_name)
            p_id = p['id']
            p_lft = p['lft']
            p_rght = p['rght']

            n_lft = p_rght
        else:
            max_rght = self._db.get('SELECT IFNULL(MAX(RGHT), 0) AS MAX_RGHT FROM trees')
            max_rght = max_rght['MAX_RGHT']

            n_lft = max_rght + 1

        n_rght = n_lft + 1

        # 父节点:rght + 2
        params = [ p_lft, p_rght ]
        self._db.save('UPDATE trees SET RGHT = RGHT + 2 WHERE LFT <= %s AND RGHT >= %s', params)

        # 其他节点:lft + 2, rght + 2
        params = [ n_lft, p_rght ]
        self._db.save('UPDATE trees SET LFT = LFT + 2, RGHT = RGHT + 2 WHERE LFT > %s AND RGHT > %s', params)

        # 添加
        params = [ p_id, name, n_lft, n_rght ]
        self._db.save('INSERT INTO trees(PARENT_ID, NAME, LFT, RGHT) values (%s, %s, %s, %s)', params)

    def remove(self, name):

        n = self.get_by_name(name)

        p_id = n['parent_id']
        n_id = n['id']
        n_lft = n['lft']
        n_rght = n['rght']

        params = [ n_lft, n_rght]

        # 父节点:rght - 1
        self._db.save('UPDATE trees SET RGHT = RGHT - 2 WHERE LFT < %s AND RGHT > %s', params)

        # 其他节点:lft - 2, rght - 2
        self._db.save('UPDATE trees SET LFT = LFT - 2, RGHT = RGHT - 2 WHERE LFT > %s AND RGHT > %s', params)

        # 子节点 parent_id, lft - 1, rght - 1
        params = [ p_id, n_lft, n_rght]
        self._db.save('UPDATE trees SET PARENT_ID = %s, LFT = LFT - 1, RGHT = RGHT - 1 WHERE LFT > %s AND RGHT < %s', params)

        # 删除自己
        params = [ n_id ]
        self._db.save('DELETE FROM trees WHERE ID = %s', params)
