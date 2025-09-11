<<<<<<< Updated upstream
class ThreatModel:
    def __init__(self):
        print("[Model] ThreatModel initialized.")

    def predict(self, data):
        return {"prediction": "threat", "input": data}
=======
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from pyod.models.iforest import IForest
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score


df = pd.read_csv('conn.csv')  

df = df.replace('-', np.nan)

df['id.orig_h'] = df['id.orig_h'].apply(lambda x: np.nan if isinstance(x, str) and x.strip() == '::' else x)
df = df.fillna(0)



for col in ['id.orig_h', 'id.orig_p', 'id.resp_h', 'proto', 'conn_state']:
    if col in df.columns:
        df[col] = df[col].fillna('missing')
        df[col] = LabelEncoder().fit_transform(df[col].astype(str))




df.to_csv('conn_encoded.csv', index=False)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X = scaler.fit_transform(df.values)


clf = IForest(contamination=0.01)
clf.fit(X)

df['anomaly'] = clf.labels_
df['anomaly_score'] = clf.decision_scores_

df.to_csv('results.csv', index=False)

df_pred = pd.read_csv('results.csv')
df_true = pd.read_csv('../conn.csv')

df_pred['row_idx'] = df_pred.index
df_true['row_idx'] = df_true.index

df = pd.merge(df_pred, df_true[['row_idx', 'label']], on='row_idx')

accuracy = accuracy_score(df['label'], df['anomaly'])

print("Accuracy:", accuracy)


>>>>>>> Stashed changes
