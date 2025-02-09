from flask import Flask, render_template_string
import pandas as pd
import plotly.graph_objects as go

app = Flask(__name__)

# Charger les données
try:
    df = pd.read_csv("GlobalLandTemperaturesByCountry.csv")
except FileNotFoundError:
    raise Exception("Le fichier 'GlobalLandTemperaturesByCountry.csv' est introuvable.")

# Convertir la date
df['dt'] = pd.to_datetime(df['dt'])

# Filtrer les données pour la France et extraire l'année
df_france = df[df['Country'] == 'France']
df_france['Year'] = df_france['dt'].dt.year

# Moyenne annuelle des températures pour la France
df_france = df_france.groupby('Year')['AverageTemperature'].mean().reset_index()

# Ne garder que les années de 1800 à 2020
df_france = df_france[(df_france['Year'] >= 1800) & (df_france['Year'] <= 2020)]

# Calculer la normale 1961-1990 pour la France
df_normale = df_france[(df_france['Year'] >= 1961) & (df_france['Year'] <= 1990)]
normale_1961_1990 = df_normale['AverageTemperature'].mean()

# Calculer la moyenne de température globale de la France
moyenne_globale = df_france['AverageTemperature'].mean()

# Calculer l'écart de température par rapport à la moyenne globale
df_france['Ecart_temperature'] = df_france['AverageTemperature'] - moyenne_globale

# Déterminer les températures min et max pour normaliser la couleur
temp_min = df_france['AverageTemperature'].min()
temp_max = df_france['AverageTemperature'].max()

# Création du premier graphique avec dégradé de couleurs
fig1 = go.Figure()

fig1.add_trace(go.Bar(
    x=df_france['Year'],
    y=df_france['AverageTemperature'],
    marker=dict(
        color=df_france['AverageTemperature'],  # Utilisation des valeurs pour la couleur
        colorscale="RdBu_r",  # Dégradé du bleu (froid) au rouge (chaud)
        cmin=temp_min,  # Échelle min
        cmax=temp_max,  # Échelle max
        colorbar=dict(title="Température (°C)")
    ),
    name=""
))

# Ajouter la ligne de référence 1961-1990
fig1.add_trace(go.Scatter(
    x=df_france['Year'],
    y=[normale_1961_1990] * len(df_france),
    mode='lines',
    line=dict(color='black', dash='dash'),
    name=""
))

# Mise en forme du premier graphique
fig1.update_layout(
    title="Température moyenne annuelle en France depuis 1800<br>Comparée à la normale 1961-1990",
    xaxis_title="Année",
    yaxis_title="Température moyenne (°C)",
    template="plotly_white",
    width=1200,  # Largeur du graphique
    height=700,  # Hauteur du graphique
)

# Création du second graphique pour l'écart de température
fig2 = go.Figure()

fig2.add_trace(go.Bar(
    x=df_france['Year'],
    y=df_france['Ecart_temperature'],
    marker=dict(
        color=df_france['Ecart_temperature'],  # Utilisation des valeurs pour la couleur
        colorscale="RdBu_r",  # Dégradé inversé du rouge (positif) au bleu (négatif)
        colorbar=dict(title="Écart de température (°C)")
    ),
    name="Écart de température"
))

# Mise en forme du deuxième graphique
fig2.update_layout(
    title="Écart de température par rapport à la moyenne globale (1800-2020)",
    xaxis_title="Année",
    yaxis_title="Écart de température (°C)",
    template="plotly_white",
    width=1200,  # Largeur du graphique
    height=700,  # Hauteur du graphique
)

# Convertir les graphiques en HTML
graph_html1 = fig1.to_html(full_html=False)
graph_html2 = fig2.to_html(full_html=False)

# Template HTML pour afficher les graphiques avec une mise en page améliorée
html_template = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Températures en France</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
            background-color: #f0f0f0;
        }
        h1 {
            color: #333;
            font-size: 2em;
            margin-bottom: 20px;
        }
        p {
            color: #555;
            font-size: 1.1em;
            margin-bottom: 30px;
        }
        #graph-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
            flex-direction: column;
        }
        .graph {
            margin-bottom: 40px;
            width: 100%;
        }
        h2 {
            color: #333;
            font-size: 1.5em;
            margin-bottom: 15px;
            text-align: center;  /* Centrer les titres des graphiques */
        }
    </style>
</head>
<body>
    <h1>Température moyenne annuelle en France depuis 1800</h1>
    <p>Dégradé de couleur du bleu (froid) au rouge (chaud), avec une ligne de référence 1961-1990.</p>
    
    <div id="graph-container" class="graph">
        <h2>Températures moyennes comparées à la normale 1961-1990</h2>
        {{ graph_html1 | safe }}
    </div>

    <div id="graph-container" class="graph">
        <h2>Écart de température par rapport à la moyenne globale (1800-2020)</h2>
        {{ graph_html2 | safe }}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template, graph_html1=graph_html1, graph_html2=graph_html2)

if __name__ == '__main__':
    app.run(debug=True, port=5000)