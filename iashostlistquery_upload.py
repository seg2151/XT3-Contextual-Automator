# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:46:15 2017

@author: SGarcia
"""

from impala.dbapi import connect
from impala.util import as_pandas

SAMPLE_SIZE = 100000
START_DATE = '2017-03-27'
END_DATE = '2017-03-28'
query = '''
SELECT host, extpublisherid, extplacementid

FROM thirdparty.iasdata

WHERE day between '{}' and '{}'
--and cast(sadscore as float) = 1.0

GROUP BY 1,2,3

limit {}
'''.format(START_DATE, END_DATE, SAMPLE_SIZE)

print('Connecting to host...')
conn = connect(host = , port = )
print('Connected')
cursor = conn.cursor()
print('Executing sql script...')
cursor.execute(query)
print('Creating dataframe and running web script...')
df_cursor = as_pandas(cursor)

df = df_cursor.copy()



       
