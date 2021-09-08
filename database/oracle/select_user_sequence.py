# @Author ZhangGJ
# @Date 2021/09/01 11:18

import cx_Oracle

user_list = ['HIFM_CENTER', 'JJCCB', 'HIFM_NACOS', 'HIFM_XXL_JOB', 'HIFM_FLOWABLE']

oracle_conn = cx_Oracle.connect("root", "123456", "localhost")
oracle_curs = oracle_conn.cursor()

with open('sequence.sql', 'a') as f:
    f.write('-- SEQUENCE')
    f.write('\n')
    for user in user_list:
        select_sequence = f"SELECT \
        	'create sequence ' \
        	|| '{user}' || '.' || sequence_name || ' minvalue ' \
        	|| min_value || ' maxvalue ' \
        	|| max_value || ' start with ' \
        	|| last_number || ' increment by ' \
        	|| increment_by || ( CASE WHEN cache_size = 0 THEN ' nocache' ELSE ' cache ' || cache_size END ) || ';' \
        FROM \
        	dba_sequences \
        WHERE \
        	sequence_owner = '{user}'"
        oracle_curs.execute(select_sequence)
        sequence_rows = oracle_curs.fetchall()
        print(f'-- ---------------------------{user} sequence--------------------------')
        f.write(f'-- ---------------------------{user} sequence--------------------------\n')
        for sequence in sequence_rows:
            str_sequence = sequence[0]
            f.write(str_sequence)
            f.write('\n')

oracle_curs.close()
oracle_conn.commit()
oracle_conn.close()
