from db_con import *

select ="select *from tbl_mhs"
select1 ="select *from tbl_sinkronisasi"

cursor_db.execute(select)

results =cursor_db.fetchall()

cursor_db.execute(select1)
results1 = cursor_db.fetchall()
test=0
for row in results:
    for row1 in results1:
        if (row[1] == row1[1]):
            test=test+1
    if test=1:
        print()


