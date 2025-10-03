# Stores REST API

A RESTful API for managing stores, items, tags, and users, built with Python Flask, Flask-Smorest, SQLAlchemy, and Marshmallow.

## Features

- CRUD operations for stores, items, tags, and users
- JWT authentication and admin privileges
- Data validation using Marshmallow schemas
- SQLAlchemy ORM for database management
- Interactive API documentation via Swagger UI
- Docker support for easy deployment
- Well-commented API endpoints for maintainability

## Project Structure

```
.
├── app.py                # Main Flask app factory (fully commented)
├── db.py                 # SQLAlchemy database instance
├── models/               # SQLAlchemy models
│   ├── __init__.py
│   ├── item.py
│   ├── store.py
│   ├── tag.py
│   ├── item_tags.py
│   └── user.py
├── resources/            # API endpoints (blueprints, fully commented)
│   ├── item.py
│   ├── store.py
│   ├── tag.py
│   └── user.py
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
- `GET /tag/<tag_id>` — Get a tag by ID
- `DELETE /tag/<tag_id>` — Delete a tag (if not assigned to any items)
- `POST /register` — Register a new user
- `POST /login` — Login and get JWT token
- `POST /logout` — Logout and revoke JWT token
- `GET /user/<user_id>` — Get a user by ID
- `DELETE /user/<user_id>` — Delete a user by ID

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

**Register User**

```json
{
  "username": "testuser",
  "password": "testpass"
}
```

## Code Documentation

All API endpoints in [`resources/item.py`](resources/item.py), [`resources/store.py`](resources/store.py), [`resources/tag.py`](resources/tag.py), [`resources/user.py`](resources/user.py), and the main app in [`app.py`](app.py) are now fully commented to explain their purpose and usage, making the codebase easier to understand and maintain.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
