# Stores REST API

A simple RESTful API for managing stores and items, built with Python Flask.

## Features

- Create, retrieve, update, and delete stores
- Create, retrieve, update, and delete items
- Data validation with Marshmallow schemas
- Interactive API documentation via Swagger UI

## Project Structure

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
- `GET /item` — List all items
- `POST /item` — Create a new item
- `GET /store/<store_id>` — Get a store by ID
- `DELETE /item/<item_id>` — Delete an item by ID

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
