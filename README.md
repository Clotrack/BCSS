# BCSS
Clasificador de sistemas estelares (Borg)

### Estructura del proyecto
BCSS/
├── .devcontainer/
│   └── docker-compose.yml          # Creacion de los contenedores de Docker
├── api/
│   ├── Dockerfile
│   ├── main.py                     # API!!!!! archivo de inicio de la API!!!
│   └── requirements.txt
├── data/
│   ├── curated/                    # Datos finales listos para análisis
│   ├── processed/                  # Datos tras gaia_clean y nasa_clean
│   ├── raw/                        # Archivos CSV originales (sin procesar)
│   ├── createBBDD_estructure.py    # Crear estructura Base de datos 
│   ├── charge_curated.py
│   ├── charge_gaia.py
│   ├── charge_match.py
│   ├── charge_nasa.py
│   └── create_view.py
├── notebook/                       # Descatalogado con script main.py
│   ├── gaia_clean.ipynb
│   ├── nasa_clean.ipynb
│   ├── planets_eda.ipynb
│   └── stars_eda.ipynb
├── script/
│   ├── download_nasa.py
│   ├── gaia_clean.py
│   ├── nasa_clean.py
│   ├── planets_eda.py
│   └── stars_eda.py
├── test/                           # Pruebas unitarias del sistema
│   └── gaia_clean_test.ipynb
│   
├── .gitignore
├── LICENSE
├── main.py                         # Orquestador principal del pipeline
├── README.md
└── requirements.txt                # Requerimientos de librerias y utilidades para todo el sistema
