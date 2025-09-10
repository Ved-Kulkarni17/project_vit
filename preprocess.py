import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('conn.csv')

le_orig_h = LabelEncoder()
le_resp_h = LabelEncoder()

df['id.orig_h'] = le_orig_h.fit_transform(df['id.orig_h'])
df['id.resp_h'] = le_resp_h.fit_transform(df['id.resp_h'])

