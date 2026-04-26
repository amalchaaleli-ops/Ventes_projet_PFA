import pandas as pd
import matplotlib.pyplot as plt
import os

print("Démarrage de l'automatisation de l'analyse des ventes...")

# Génération du fichier CSV
donnees = {
    'ID': [101, 102, 103, 104, 105],
    'Prix': [15.0, 25.0, 10.0, 50.0, 5.0],
    'Quantite': [3, 2, 5, 1, 10],
    'Remise': [10, 5, 0, 15, 0]
}
df_initial = pd.DataFrame(donnees)
df_initial.to_csv('ventes.csv', index=False)
print("1. Fichier 'ventes.csv' généré avec succès.")

#  Lecture Dynamique (Tailles Différentes)
print("\n--- Début de l'analyse dynamique par blocs ---")
fichier_a_lire = 'ventes.csv'

# Taille du bloc (par exemple, lire 2 lignes par 2 lignes pour tester)
taille_bloc = 2 

ca_total_entreprise = 0
meilleur_produit_id = None
max_benefice = 0
resultats_finaux = [] # Pour stocker les données traitées

# pd.read_csv renvoie ici un itérateur (un lecteur dynamique)
for bloc in pd.read_csv(fichier_a_lire, chunksize=taille_bloc):
    
    bloc['CA_Brut'] = bloc['Prix'] * bloc['Quantite']
    bloc['CA_Net'] = bloc['CA_Brut'] * (1 - bloc['Remise'] / 100)
    bloc['TVA'] = bloc['CA_Net'] * 0.20
    
    # On cumule le CA total au fur et à mesure
    ca_total_entreprise += bloc['CA_Net'].sum()
    
    #On cherche le meilleur produit dans ce bloc
    id_max_bloc = bloc.loc[bloc['CA_Net'].idxmax(), 'ID']
    benefice_max_bloc = bloc['CA_Net'].max()
    
    if benefice_max_bloc > max_benefice:
        max_benefice = benefice_max_bloc
        meilleur_produit_id = id_max_bloc
        
    # On sauvegarde le bloc traité
    resultats_finaux.append(bloc)

# On recolle tous les morceaux à la fin
df_final = pd.concat(resultats_finaux, ignore_index=True)

print(f"2. Le Chiffre d'Affaires Total de l'entreprise est de : {ca_total_entreprise:.2f}")
print(f"3. Le produit ayant généré le plus gros bénéfice est l'ID : {meilleur_produit_id}")

# Exportation finale
df_final.to_csv('resultats_final.csv', index=False)
print("4. Fichier 'resultats_final.csv' exporté avec succès.")

# Visualisation avec Matplotlib
plt.figure(figsize=(8, 5))
plt.bar(df_final['ID'].astype(str), df_final['CA_Net'], color='coral')
plt.title('Chiffre d\'Affaires Net par Produit')
plt.xlabel('ID Produit')
plt.ylabel('CA Net')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig('graphique_CA.png')
print("5. Graphique 'graphique_CA.png' généré et sauvegardé.! 🎉")