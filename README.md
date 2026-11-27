# Catálogo de Series API (SeriesHub)

**Somos dos estudiantes y este es un proyecto básico** creado para aprender y practicar el desarrollo de una API REST con FastAPI y PostgreSQL, junto con un frontend en React.

> ⚠️ Estado: proyecto básico / en desarrollo. Está pensado como ejercicio de aprendizaje, no como una aplicación lista para producción. (por ahora)

![FastAPI](https://img.shields.io/badge/backend-FastAPI-009688)
![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-336791)
![Python](https://img.shields.io/badge/Python-3.15-yellow)
![React](https://img.shields.io/badge/frontend-React%2019-61DAFB)
![Vite](https://img.shields.io/badge/build-Vite%208-646CFF)

## 📌 ¿Qué hace?

Expone una API REST para gestionar un catálogo de series: listar, buscar por ID, crear, actualizar y eliminar. Cada serie guarda título, año de estreno, temporadas, género, plataforma, estado, sinopsis y URL de imagen.

El frontend (`frontend/`) está actualmente en la plantilla inicial de Vite + React (pantalla de bienvenida y contador); todavía **no consume la API**.

## 🛠️ Tecnologías

**Backend**

- FastAPI (API y documentación automática en `/docs`)
- Pydantic (validación de datos de entrada)
- psycopg 3 (conexión directa a PostgreSQL)
- python-dotenv (lectura de variables de entorno)
- uvicorn (servidor ASGI)

**Frontend**

- React 19 + Vite 8
- ESLint

## 📁 Estructura

```text
catalogo-series-api/
├── backend/
│   ├── main.py                 # App FastAPI, CORS y endpoint raíz
│   ├── database.py             # Conexión a PostgreSQL con psycopg
│   ├── schemas.py              # Modelos Pydantic (SerieCreate / SerieUpdate)
│   ├── models.py               # Vacío (reservado para modelos)
│   ├── routers/
│   │   └── series.py           # Endpoints /series
│   ├── services/
│   │   └── series_services.py  # Consultas SQL (CRUD)
│   ├── requirements.txt
│   └── .python-version         # Python 3.15
├── frontend/                   # Plantilla React + Vite (sin conectar a la API aún)
│   ├── src/
│   ├── package.json
│   └── vite.config.js
├── .env.example                # Ejemplo de DATABASE_URL
├── package-lock.json
└── README.md
```

## ✅ Requisitos previos

- Python 3.15 (según `backend/.python-version`)
- PostgreSQL en funcionamiento
- Node.js y npm (para el frontend)

## 🚀 Puesta en marcha

### 1. Clonar el repositorio

```bash
git clone https://github.com/BrennanDzz/catalogo-series-api.git
cd catalogo-series-api
```

### 2. Backend

```bash
cd backend
python -m venv .venv
```

Activa el entorno virtual:

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Crea un archivo `.env` en `backend/` a partir de `.env.example`:

```env
DATABASE_URL=postgresql://USUARIO:CONTRASEÑA@HOST:5432/postgres
```

> La aplicación lanza un error si `DATABASE_URL` no está definida.

**Crear la tabla `series`:** el repositorio aún no incluye migraciones ni scripts para crearla, así que hay que crearla manualmente en PostgreSQL. Ejemplo:

```sql
CREATE TABLE series (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    anio_estreno INTEGER NOT NULL CHECK (anio_estreno BETWEEN 1900 AND 2030),
    temporadas INTEGER NOT NULL CHECK (temporadas BETWEEN 1 AND 20),
    genero TEXT NOT NULL,
    plataforma TEXT NOT NULL,
    estado VARCHAR(20) NOT NULL CHECK (estado IN ('En emisión', 'Finalizada')),
    sinopsis TEXT NOT NULL,
    imagen_url TEXT NOT NULL
);
```

Arranca la API:

```bash
uvicorn main:app --reload
```

- API: <http://127.0.0.1:8000>
- Documentación interactiva (Swagger): <http://127.0.0.1:8000/docs>

### 3. Frontend

```bash
cd frontend
npm install
npm run dev
```

Abra la URL que indica Vite (normalmente <http://127.0.0.1:5173>).

Otros comandos:

```bash
npm run build   # genera la versión de producción
npm run lint    # ejecuta ESLint
npm run preview # previsualiza el build
```

## 📡 Endpoints de la API

| Método | Ruta        | Descripción                         | Respuesta |
|--------|-------------|-------------------------------------|-----------|
| `GET`  | `/`         | Mensaje de comprobación de la API   | `200` |
| `GET`  | `/series`   | Lista todas las series (por ID)     | `200` |
| `GET`  | `/series/{id}` | Busca una serie por su ID        | `200` / `404` |
| `POST` | `/series`   | Crea una serie                      | `201` |
| `PUT`  | `/series/{id}` | Actualiza estado, imagen y temporadas | `200` / `404` |
| `DELETE` | `/series/{id}` | Elimina una serie                 | `204` / `404` |

### Ejemplo de `POST /series`

```json
{
  "titulo": "Breaking Bad",
  "anio_estreno": 2008,
  "temporadas": 5,
  "genero": "Drama",
  "plataforma": "Netflix",
  "estado": "Finalizada",
  "sinopsis": "Un profesor de química se convierte en fabricante de metanfetamina.",
  "imagen_url": "https://ejemplo.com/breaking-bad.jpg"
}
```

### Ejemplo de `PUT /series/{id}`

```json
{
  "estado": "En emisión",
  "imagen_url": "https://ejemplo.com/nueva-imagen.jpg",
  "temporadas": 6
}
```

### Validaciones

- `titulo`: de 1 a 100 caracteres (se eliminan espacios sobrantes).
- `anio_estreno`: entre 1900 y 2030.
- `temporadas`: entre 1 y 20.
- `estado`: solo `"En emisión"` o `"Finalizada"`.
- El resto de campos son obligatorios y se validan con Pydantic.

### Ejemplos con `curl`

```bash
curl http://127.0.0.1:8000/series

curl -X POST http://127.0.0.1:8000/series \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Breaking Bad","anio_estreno":2008,"temporadas":5,"genero":"Drama","plataforma":"Netflix","estado":"Finalizada","sinopsis":"Sinopsis de ejemplo","imagen_url":"https://ejemplo.com/img.jpg"}'

curl -X DELETE http://127.0.0.1:8000/series/1
```

## 👥 Autores

Proyecto realizado por **dos estudiantes** como proyecto básico de aprendizaje.

- BrennanDzz — <https://github.com/BrennanDzz>
- ilmwmd — <https://github.com/ilmwmd>
