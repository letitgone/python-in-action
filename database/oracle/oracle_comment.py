# @Author ZhangGJ
# @Date 2021/07/14 11:37
import cx_Oracle

oracle_conn = cx_Oracle.connect("root", "123456", "127.0.0.1")
oracle_curs = oracle_conn.cursor()

user_list = ['HIFM_CENTER', 'JJCCB', 'HIFM_NACOS', 'HIFM_XXL_JOB', 'HIFM_FLOWABLE']

for user in user_list:
    # 查询用户下所有表
    oracle_tables = f"select table_name from all_tables where owner='{user}'"
    oracle_curs.execute(oracle_tables)
    oracle_tables_rows = oracle_curs.fetchall()
    for row in oracle_tables_rows:
        table = row[0]
        # 查询表注释
        oracle_table_comments = f"SELECT comments FROM all_tab_comments WHERE table_name = '{table}' AND owner = '{user}' "
        oracle_curs.execute(oracle_table_comments)
        oracle_table_comments_rows = oracle_curs.fetchone()
        if oracle_table_comments_rows[0] is None:
            try:
                update_comment = f"COMMENT ON TABLE {user}.{table} IS '{table}'"
                oracle_curs.execute(update_comment)
            except Exception:
                continue
            print(f'Update table comment: {table}')

        # 查询表下所有字段
        oracle_columns = f"SELECT COLUMN_NAME, COMMENTS FROM ALL_COL_COMMENTS WHERE TABLE_NAME='{table}'"
        oracle_curs.execute(oracle_columns)
        oracle_columns_rows = oracle_curs.fetchall()
        for column_row in oracle_columns_rows:
            column = column_row[0]
            comment = column_row[1]
            if comment is None:
                try:
                    update_comment = f"COMMENT ON COLUMN {user}.{table}.{column} IS '{column}'"
                    oracle_curs.execute(update_comment)
                except Exception:
                    continue
                print(f'Update table column comment: {table}.{column}')
        print()

oracle_curs.close()
oracle_conn.commit()
oracle_conn.close()
