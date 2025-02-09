# 📊 Visualisation des Températures en France (1800-2020)

Ce projet est une application **Flask** permettant de visualiser l'évolution des températures moyennes annuelles en **France** de **1800 à 2020**. Deux graphiques interactifs générés avec **Plotly** permettent d'analyser ces tendances et l'écart par rapport à la moyenne globale.

---

## 🚀 Fonctionnalités

- 📈 **Graphique des températures moyennes** avec un dégradé de couleur indiquant les variations.
- 📊 **Graphique de l'écart des températures** par rapport à la moyenne globale.
- 🔥 Comparaison avec la normale climatique **1961-1990**.
- 🌍 Données issues du dataset **GlobalLandTemperaturesByCountry.csv**.
- 🎨 Interface web simple et responsive.

---

## 🛠️ Installation et Exécution

### 1️⃣ Prérequis

Assurez-vous d'avoir **Python 3.7+** et **pip** installés.

### 2️⃣ Cloner le projet

```bash
git clone https://github.com/ri2az/Temperature-Visualization.git
cd Temperature-Vizualization
```

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4️⃣ Lancer l'application Flask

```bash
python app.py
```

L'application sera disponible sur : `http://127.0.0.1:5000/`

---

## 📂 Structure du projet

```
📁 Temperature-Vizualization/
├── 📄 app.py                # Code principal Flask
├── 📄 requirements.txt      # Dépendances Python
├── 📄 README.md             # Documentation
├── 📂 static/               # (Optionnel) Fichiers statiques CSS/JS
├── 📂 templates/            # (Optionnel) Templates HTML (si utilisés)
└── 📄 .gitignore            # Fichiers à ignorer par Git
```

---

## 📌 Améliorations futures

- ✅ Ajouter une **sélection de pays** pour visualiser d'autres régions.
- ✅ Permettre le **téléchargement des graphiques**.
- ✅ Héberger l'application sur **Render, Railway ou Heroku**.

---

## 🤝 Contribuer

Les contributions sont **les bienvenues** !

1. **Fork** le projet 🍴
2. **Crée** une nouvelle branche (`git checkout -b feature-nom`)
3. **Fais tes modifications** et commit (`git commit -m 'Ajout de feature'`)
4. **Pousse** les changements (`git push origin feature-nom`)
5. **Ouvre une Pull Request**

---

## 📜 Licence

Ce projet est sous licence **MIT**. Vous êtes libre de l'utiliser, le modifier et le partager !

📬 Pour toute question, contactez-moi sur **GitHub**. 😊

---

## 📄 .gitignore

Ajoutez un fichier `.gitignore` contenant :

```
__pycache__/
*.pyc
*.pyo
.env
.DS_Store
.vscode/
.idea/
*.sqlite3
```

