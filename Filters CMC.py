import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Charger les données
data1 = pd.read_csv('/Users/eugenedupas/Desktop/40deg2528kg1_data_00008.csv')
data2 = pd.read_csv('/Users/eugenedupas/Desktop/40deg2528kgsuite_data_00008.csv')

# Enlever les espaces supplémentaires dans les noms de colonnes
data1.columns = data1.columns.str.strip()
data2.columns = data2.columns.str.strip()

# Concaténer les données au lieu de les additionner
t = pd.concat([data1['t(s)'], data2['t(s)']]).reset_index(drop=True)
chan0 = pd.concat([data1['chan0'], data2['chan0']]).reset_index(drop=True)

# Calculer la déformation
deformation = chan0 * 5/100

# Appliquer un filtre passe-bas Butterworth pour enlever le bruit
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y

# Paramètres du filtre
order = 5
fs = 1 / np.mean(np.diff(t))  # Fréquence d'échantillonnage
cutoff = 0.1  # Fréquence de coupure

# Nettoyer les données avant le filtrage
deformation_clean = deformation.replace([np.inf, -np.inf], np.nan).dropna()

# Filtrer les données de déformation
deformation_filtered = lowpass_filter(deformation_clean, cutoff, fs, order)

# Calculer la contrainte variable en fonction de la déformation filtrée
contrainte = (100+100*deformation_filtered)*10**(-3)* 1830*10**(-3) * 9.81/(5.5*10**(-7))

# Calculer la vitesse de déformation (dérivée de la déformation filtrée)
vitesse_deformation = np.gradient(deformation_filtered, t[:len(deformation_filtered)])

# Filtrer les valeurs non positives (nécessaires pour le log-log)
positive_indices = (contrainte > 0) & (vitesse_deformation > 0)
contrainte_positive = contrainte[positive_indices]
vitesse_deformation_positive = vitesse_deformation[positive_indices]

# Tracer le graphique en échelle logarithmique
plt.figure(figsize=(10, 6))
plt.loglog(contrainte_positive, vitesse_deformation_positive, label='Vitesse de déformation (en s-1)')
plt.xlabel('Contrainte (en Pa)')
plt.ylabel('Vitesse de déformation (en s-1)')
plt.title('Vitesse de déformation en fonction de la contrainte (échelle log-log) 2528 kg')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()
