#/usr/bin/python3
# encoding: utf-8
import dbutils

class Trees():

    SQL_INSERT = 'insert into trees(parent_id, name, lft, rght) values (%s, %s, %s, %s)'

    _db = ''
    def __init__(self):
        self._db = dbutils.DBUtils()

    def get(self, id):
        return self._db.get('select id, parent_id, name, lft, rght from trees where id = "%d" ' % id)

    def get_by_name(self, name):
        return self._db.get('select id, parent_id, name, lft, rght from trees where name = "%s" ' % name)

    def add(self, p_name, name):

        p_id = 0
        p_rght = 0

        if p_name is not None:

            p = self.get_by_name(p_name)
            p_id = p['id']
            p_rght = p['rght']

            tmp_p_id = p_id

            while True:
                params = [ tmp_p_id ]
                self._db.save('update trees set rght = rght + 2 where id = %s', params)
                p = self.get(tmp_p_id)

                if p is None:
                    break

                tmp_p_id = p['parent_id']
        else:
            max_rght = self._db.get('SELECT MAX(RGHT) AS rght FROM trees')['rght']

            if max_rght is not None:
                p_rght = max_rght
        # 
        params = [ p_rght ]
        self._db.save('UPDATE trees SET LFT = LFT + 2, RGHT = RGHT + 2 WHERE LFT > %s', params)

        entity = []
        entity.append(p_id)
        entity.append(name)

        if p_name is not None:
            entity.append(p_rght + 0)
            entity.append(p_rght + 1)
        else:
            entity.append(p_rght + 1)
            entity.append(p_rght + 2)

        self._db.save(self.SQL_INSERT, entity)
