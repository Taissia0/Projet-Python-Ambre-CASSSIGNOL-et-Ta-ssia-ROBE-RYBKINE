# Projet-Python-Ambre-CASSSIGNOL-et-Taissia-ROBE-RYBKINE
Projet en Biomodélisation Préing 2 BTC

Le fichier 'data_real.csv' a des mesures de quantités de bactéries vivantes dans les selles de souris et dans le microbiote instestinal de souris au niveau de l'iliéon et du caecum. Certaines souris ont été traitées avec un cocktail d'antibiotique 'ABX' et d'autres ont eu un placebo.
Ce fichier se trouve dans le dossier 'Input'.


Le code 'Code Ambre CASSIGNOL et Taïssia ROBE-RYBKINE' est utilisé pour traiter des données du fichier 'data_real.csv'.
Le code va ouvrir à 3 reprises le fichier 'data_real.csv' pour séparer les données des catégories 'fecal' puis 'cecal' et enfin 'ileal' afin de les répartir dans 3 fichiers 'seperateFecal.csv', 'separateCecal.csv' et 'seperateIleal.csv'.
Ces fichiers se trouvent dans le dossier 'Output'.
Après avoir séparé les données, le code va ouvrir chaque fichier 'seperate' et générer un graphique illustrant les résultats de l'expérience. 
Ces graphiques se trouvent dans le dossier 'Images'.



Nous n'avons pas réussi à mettre des couleurs pour bien distinguer les placebo des ABX sur les courbes des graphiques malgré l'utilisation de set_face_color ou de fonctions de matplotlib.
La légende des graphiques n'est pas bien représentée de part le manque de couleur sur les graphiques. 
Nous précisons pour le 'fecal graph' que les courbes représentées en haut du graphique correspondent aux souris placebo et que les courbes du bas représentent les souris avec l'antibiotique.
Nous précisions aussi que pour les 'Cecal graph' et 'Ileal graph', les violons à gauche représentent les données des souris sous antibiotiques et les vilons à droite les données des souris témoins/placebo.


Nous avons aussi essayé d'améliorer le code en utilisant des fonctions, mais nous n'avons pas réussi. Les fonctions ne sont donc pas présentes dans le code.
