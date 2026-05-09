# BCSS
Clasificador de sistemas estelares (Borg)

## Proyecto Big Data - Manual de Instalación y Manual de Uso

Bienvenido al repositorio del proyecto BCSS.  
Este entorno ha sido diseñado para facilitar la puesta en marcha tanto en entorno local como mediante GitHub Codespaces, utilizando contenedores Docker para garantizar una instalación rápida, reproducible y consistente.

---

## Tecnologías utilizadas

- Docker & Docker Compose
- Python
- PostgreSQL
- Grafana
- FastAPI
- GitHub Codespaces

---

## Estructura del proyecto

```text
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
├── grafana/
│   ├── dashboards/                     # Ficheros de configuracion dashboard .json 
│   ├── provisioning/                 
│       ├── dashboard/dafoult.yaml      # Configurar rutas dashboard a contenedor grafana
│       └── datasources/postgres.yaml   # Configurar conexion Base de datos a grafana
├── notebook/                           # Descatalogado con script main.py
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
├── .gitignore
├── LICENSE
├── main.py                         # Orquestador principal del pipeline
├── README.md
└── requirements.txt                # Requerimientos de librerias y utilidades para todo el sistema
```

---

### 1. Instalación del proyecto

- Acceder al directorio .devcontainer
Tanto si trabajamos en local como en Codespaces, el primer paso será movernos desde la terminal a la carpeta .devcontainer.
    
'cd .devcontainer'

### 2. Levantar los contenedores Docker

Ejecutamos el siguiente comando:

'docker-compose up'

Este proceso puede tardar varios minutos la primera vez, ya que Docker debe:

    * Descargar imágenes
    * Instalar dependencias
    * Crear contenedores
    * Configurar servicios
    * Inicializar Grafana y la base de datos

Cuando finalice, veremos varios puertos abiertos en la pestaña Ports y los servicios estarán operativos.

![Contenedores operativos](img/Fig18Manualpuertos.png)

---

### Tabla de comandos útiles

| Comando                           | Descripción                                   |
| --------------------------------- | --------------------------------------------- |
| `cd .devcontainer`                | Acceder al directorio de configuración Docker |
| `docker-compose up`               | Levantar todos los contenedores               |
| `docker-compose down`             | Detener los contenedores                      |
| `docker-compose down -v`          | Eliminar contenedores y volúmenes             |
| `docker ps`                       | Ver contenedores activos                      |
| `docker logs <contenedor>`        | Ver logs de un contenedor                     |
| `docker restart <contenedor>`     | Reiniciar un contenedor                       |
| `docker images`                   | Ver imágenes Docker instaladas                |
| `py main.py`                      | Ejecutar el proyecto en Windows               |
| `python main.py`                  | Ejecutar el proyecto en Linux/Codespaces      |
| `pip install -r requirements.txt` | Instalar dependencias manualmente             |
| `git status`                      | Ver estado del repositorio                    |
| `git pull`                        | Actualizar el proyecto                        |
| `git clone <url>`                 | Clonar el repositorio                         |

---

