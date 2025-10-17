# VetPathogen Pipeline

<details open>
  <summary>🇬🇧 English</summary>
A mock backend workflow that powers the VetPathogen platform. This project ingests
isolate metadata, applies simple pathogen classification rules, assigns antimicrobial
resistance (AMR) risk scores, and exports a consolidated report. It demonstrates how
sequence analysis components connect inside the eventual VetPathogen product.

## Project Highlights

- **Input**: CSV file of veterinary isolates with species labels and short DNA sequences.
- **Classification**: Rule-based identification of likely pathogen species.
- **Resistance prediction**: Randomized risk tiers that imitate downstream AMR analysis.
- **Reporting**: Aggregated results saved back to `data/report.csv`.
- **Notebook demo**: Reproducible end-to-end run for exploratory inspection.

## Repository Layout

```
vetpathogen-pipeline/
├── data/
│   ├── isolates.csv          # Sample input dataset
│   └── report.csv            # Generated output report
├── notebooks/
│   └── pipeline_demo.ipynb   # Interactive demonstration of the pipeline
├── pipeline/
│   ├── classify_pathogen.py  # Species classification logic
│   ├── resistance_predictor.py # Mock resistance risk assignment
│   └── report.py             # Orchestrates pipeline + CSV export
├── requirements.txt          # Project dependencies
└── README.md                 # Final documentation
```

## Installation

```powershell
git clone https://github.com/mehdikhedi/vetpathogen-pipeline.git
cd vetpathogen-pipeline

python -m venv .venv
.venv\Scripts\Activate.ps1   # PowerShell (Windows)
# source .venv/bin/activate  # macOS / Linux

pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

### Command Line

Generate the consolidated pipeline report:

```powershell
python -m pipeline.report --seed 42
```

Arguments:
- `--input`: path to the isolates CSV (default `data/isolates.csv`)
- `--output`: path for the generated report (default `data/report.csv`)
- `--seed`: optional random seed to produce deterministic resistance tiers

### Notebook

1. Launch Jupyter: `jupyter notebook` or `jupyter lab`.
2. Open `notebooks/pipeline_demo.ipynb`.
3. Select the `.venv` interpreter.
4. Run all cells to generate and display the final DataFrame.

## Example Output

```text
   id                 species              predicted_species resistance_risk
0  A1   Staphylococcus_aureus   Staphylococcus_aureus        High
1  A2        Escherichia_coli        Escherichia_coli        Low
2  A3  Pseudomonas_aeruginosa  Pseudomonas_aeruginosa        Low
```

## Future Enhancements

- Replace random resistance scoring with actual genome-based risk assessment.
- Integrate outputs from the Sequence Analysis and AMR Detection modules.
- Add provenance tracking (e.g., timestamps, upload IDs) to the report.
- Expose the pipeline via API endpoints for the VetPathogen web interface.

## Credits

Developed by Mehdi Khedi as part of the VetPathogen prototype plan. Contributions,
feedback, and ideas are welcome.
</details>


<details> 
  <summary>🇫🇷 Français</summary>

Un flux backend simulé pour la plateforme VetPathogen. Ce projet ingère des métadonnées
d’isolats, applique un jeu de règles de classification des agents pathogènes, attribue des
niveaux de risque d’antibiorésistance (AMR) et exporte un rapport consolidé. Il illustre
comment les modules d’analyse de séquences s’articulent dans le produit VetPathogen.

## Points forts

- **Entrée** : fichier CSV contenant les isolats vétérinaires avec espèces et séquences ADN.
- **Classification** : identification basée sur des motifs simples.
- **Prédiction AMR** : niveaux de risque aléatoires pour simuler une analyse ultérieure.
- **Rapport** : résultats combinés enregistrés dans `data/report.csv`.
- **Notebook** : démonstration reproductible pour inspection interactive.

## Organisation du dépôt

```
vetpathogen-pipeline/
├── data/
│   ├── isolates.csv          # Jeu de données d’entrée
│   └── report.csv            # Rapport généré
├── notebooks/
│   └── pipeline_demo.ipynb   # Démonstration interactive du pipeline
├── pipeline/
│   ├── classify_pathogen.py  # Logique de classification
│   ├── resistance_predictor.py # Attribution du risque AMR
│   └── report.py             # Orchestration et export CSV
├── requirements.txt          # Dépendances du projet
└── README.md                 # Documentation finale
```

## Installation

```powershell
git clone https://github.com/mehdikhedi/vetpathogen-pipeline.git
cd vetpathogen-pipeline

python -m venv .venv
.venv\Scripts\Activate.ps1   # PowerShell (Windows)
# source .venv/bin/activate  # macOS / Linux

pip install --upgrade pip
pip install -r requirements.txt
```

## Utilisation

### Ligne de commande

Générer le rapport complet :

```powershell
python -m pipeline.report --seed 42
```

Arguments :
- `--input` : chemin vers le CSV des isolats (défaut `data/isolates.csv`)
- `--output` : chemin du rapport généré (défaut `data/report.csv`)
- `--seed` : graine aléatoire facultative pour des résultats déterministes

### Notebook

1. Lancer Jupyter : `jupyter notebook` ou `jupyter lab`.
2. Ouvrir `notebooks/pipeline_demo.ipynb`.
3. Sélectionner l’interpréteur `.venv`.
4. Exécuter toutes les cellules pour générer et afficher le DataFrame final.

## Exemple de sortie

```text
   id                 species              predicted_species resistance_risk
0  A1   Staphylococcus_aureus   Staphylococcus_aureus        High
1  A2        Escherichia_coli        Escherichia_coli        Low
2  A3  Pseudomonas_aeruginosa  Pseudomonas_aeruginosa        Low
```

## Pistes d’évolution

- Remplacer l’aléatoire par une évaluation génomique réelle du risque AMR.
- Intégrer les résultats des modules « Sequence Analysis » et « AMR Detection ».
- Ajouter une traçabilité (horodatage, identifiants d’upload) au rapport.
- Exposer le pipeline via une API pour l’interface web VetPathogen.

## Crédits

Développé par Mehdi Khedi dans le cadre du prototype VetPathogen. Les retours,
suggestions et contributions sont bienvenus.
</details>
