"""
SenSante - Exploration du dataset patients_dakar.csv
Lab 1 : Git , Python et Structure Projet
"""
import pandas as pd
import matplotlib.pyplot as plt

# ===== CHARGER LES DONNEES =====
df = pd.read_excel("data/patients_dakar.csv.xlsx")

# ===== PREMIERS A P E R U S =====
print ("=" * 50)
print (" SENSANTE - Exploration du dataset ")
print ("=" * 50)

# Dimensions du dataset
print (f"\nNombre de patients : {len(df)}")
print (f" Nombre de colonnes : {df. shape [1]} ")
print (f" Colonnes : {list(df. columns )}")

# Apercu des 5 premieres lignes
print (f"\n- - - 5 premiers patients ---")
print (df.head ())

# ===== STATISTIQUES DE BASE =====
print (f"\n- - - Statistiques descriptives ---")
print (df.describe().round(2))

# ===== REPARTITION DES DIAGNOSTICS =====
print (f"\n- - - Repartition des diagnostics ---")
diag_counts = df["diagnostic"].value_counts()
for diag , count in diag_counts.items() :
    pct = count / len ( df ) * 100
    print (f" { diag :12s} : { count :3d} patients ({ pct :.1f}%)")

# ===== REPARTITION PAR REGION =====
print ( f"\n- - - Repartition par region ( top 5) ---")
region_counts = df ["region"].value_counts().head(5)
for region , count in region_counts.items() :
    print (f" { region :15s} : { count :3d} patients ")

# ===== TEMPERATURE MOYENNE PAR DIAGNOSTIC =====
print ( f"\n- - - Temperature moyenne par diagnostic ---")
temp_by_diag = df.groupby("diagnostic")["temperature"].mean()
for diag , temp in temp_by_diag.items() :
    print ( f" { diag :12s} : { temp :.1f} C")

print ( f"\n{ '= ' * 50}")
print (" Exploration terminee !")
print (" Prochain lab : entrainer un modele ML")
print (f"{ '= ' * 50}")


# ===== GENERATION DES GRAPHIQUES =====
# --- GRAPHIQUE 1 : Répartition des diagnostics ---
plt.figure(figsize=(8, 6))
# On compte les valeurs et on fait un diagramme en barres
df['diagnostic'].value_counts().plot(kind='bar', color=['#2ecc71', '#e74c3c', '#3498db', '#f39c12'])
plt.title('Répartition des diagnostics')
plt.xlabel('Diagnostic')
plt.ylabel('Nombre de patients')
plt.xticks(rotation=45) # Incliner les noms pour qu'ils soient lisibles
plt.tight_layout() # Ajuste automatiquement les marges
plt.show()

# --- GRAPHIQUE 2 : Température par diagnostic ---
plt.figure(figsize=(10, 8))
# 1. On récupère les données de répartition
diag_counts = df["diagnostic"].value_counts()
# 2. On crée le diagramme circulaire
# autopct='%1.1f%%' sert à afficher les pourcentages automatiquement
diag_counts.plot(
    kind='pie', 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=['#2ecc71', '#e74c3c', '#3498db', '#f39c12'],
)
plt.title('Répartition des Diagnostics - Étude SenSante')
plt.ylabel('') # On enlève le nom de la colonne sur le côté pour que ce soit plus joli
plt.show()

# --- GRAPHIQUE 3 : Top 5 des régions ---
plt.figure(figsize=(8, 6))
top5 = df['region'].value_counts().head(5)
top5.plot(kind='barh', color='teal').invert_yaxis() # barh pour horizontal
plt.title('Top 5 des régions')
plt.xlabel('Nombre de patients')
plt.show()


