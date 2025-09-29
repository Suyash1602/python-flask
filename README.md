# Stores REST API

A RESTful API for managing stores and items, built with Python Flask, Flask-Smorest, SQLAlchemy, and Marshmallow.

## Features

- CRUD operations for stores and items
- Data validation using Marshmallow schemas
- SQLAlchemy ORM for database management
- Interactive API documentation via Swagger UI
- Docker support for easy deployment

## Project Structure

```
.
├── app.py                # Main Flask app factory
├── db.py                 # SQLAlchemy database instance
├── models/               # SQLAlchemy models
│   ├── __init__.py
│   ├── item.py
│   └── store.py
├── resources/            # API endpoints (blueprints)
│   ├── item.py
│   └── store.py
├── schemas.py            # Marshmallow schemas
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker image definition
├── docker-compose.yml    # Docker Compose config
├── .flaskenv             # Flask environment variables
├── instance/
│   └── data.db           # SQLite database file
├── README.md             # Project documentation
└── .vscode/
    └── settings.json
```

## Getting Started

### Prerequisites

- Python 3.13+
- [pip](https://pip.pypa.io/en/stable/)
- [Docker](https://www.docker.com/) (optional)

### Installation

1. Clone the repository:

   ```sh
   git clone <your-repo-url>
   cd REST-API_pyton
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Run the application:

   ```sh
   flask run
   ```

   Or with Docker:

   ```sh
   docker-compose up --build
   ```

### API Documentation

Once running, visit [http://localhost:5000/swagger-ui](http://localhost:5000/swagger-ui) for interactive API docs.

## Example Endpoints

- `GET /store` — List all stores
- `POST /store` — Create a new store
- `GET /store/<store_id>` — Get a store by ID
- `DELETE /store/<store_id>` — Delete a store by ID
- `GET /item` — List all items
- `POST /item` — Create a new item
- `GET /item/<item_id>` — Get an item by ID
- `PUT /item/<item_id>` — Update an item by ID
- `DELETE /item/<item_id>` — Delete an item by ID

## Example Payloads

**Create Item**

```json
{
  "name": "New Item",
  "price": 101,
  "store_id": 1
}
```

**Create Store**

```json
{
  "name": "New Store"
}
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
