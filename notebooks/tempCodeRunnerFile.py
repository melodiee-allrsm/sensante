import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Charger le dataset
df = pd.read_csv("data/patients_dakar.csv")

# Vérifier les dimensions
print(f"Dataset : {df.shape[0]} patients, {df.shape[1]} colonnes")

# Afficher les colonnes
print(f"\nColonnes : {list(df.columns)}")

# Afficher la répartition des diagnostics
print(f"\nDiagnostics :\n{df['diagnostic'].value_counts()}")


# Encoder les variables catégoriques en nombres
# Le modèle ne comprend que des nombres !
le_sexe = LabelEncoder()
le_region = LabelEncoder()

df['sexe_encoded'] = le_sexe.fit_transform(df['sexe'])
df['region_encoded'] = le_region.fit_transform(df['region'])

# Définir les features (X) et la cible (y)
feature_cols = [
    'age','sexe_encoded','temperature','tension_sys',
    'toux','fatigue','maux_tete','region_encoded'
]

X = df[feature_cols]
y = df['diagnostic']

# Afficher les dimensions
print(f"Features : {X.shape}")   # ex: (500, 8)
print(f"Cible : {y.shape}")     # ex: (500,)