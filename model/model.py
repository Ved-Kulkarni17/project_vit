import pandas as pd
from sklearn.preprocessing import LabelEncoder
from pyod.models.iforest import IForest
import numpy as np

df = pd.read_csv('conn.csv')
df = df.drop(columns=[c for c in ['ts', 'uid', 'label', 'history'] if c in df.columns])

df = df.replace('-', np.nan)

for col in ['id.orig_h', 'id.resp_h', 'proto', 'service', 'conn_state']:
    if col in df.columns:
        df[col] = df[col].fillna('missing')
        df[col] = LabelEncoder().fit_transform(df[col].astype(str))

for col in df.columns:
    if df[col].dtype == object:
        df[col] = df[col].replace({'F': 0, 'T': 1})

df = df.fillna(0)

X = df.values
clf = IForest()
clf.fit(X)
df['anomaly'] = clf.labels_
df['anomaly_score'] = clf.decision_scores_
df.to_csv('anomaly_results.csv', index=False)
print(df[['anomaly', 'anomaly_score']].value_counts())
print(df.head())
