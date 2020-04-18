
from dbfread import DBF
from pandas import DataFrame
#dbf = DBF('/home/arif/aarzeon/ab_kopf.dbf',ignore_missing_memofile=True)
dbf = DBF('/home/arif/aarzeon/dopadr.dbf',ignore_missing_memofile=True)

frame = DataFrame(iter(dbf))

#instant=frame.loc[frame['ABK_AUF'] == 3.0]

#print(instant['ABK_KNA'].values[0])
print(frame)
