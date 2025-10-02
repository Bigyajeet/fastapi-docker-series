



This repository is a **progressive learning series** focused on mastering the modern Python API stack. It contains multiple example projects that demonstrate how to build robust, high-performance web services using the following core technologies:

  * **FastAPI:** For building asynchronous web APIs with automatic documentation.
  * **Pydantic:** For powerful, declarative data validation, configuration management, and serialization.
  * **Docker:** For packaging applications into isolated, portable containers for easy deployment.

Each directory represents a step or concept in the development process, suitable for beginners looking to build a strong foundational portfolio.

### 📚 Contents and Modules

| Folder | Focus | Key Concepts Covered |
| :--- | :--- | :--- |
| `InstallationAndDemo/` | **FastAPI Basics** | Setting up a basic FastAPI app, defining a simple route, and running with Uvicorn. |
| `Pydantic/` | **Data Modeling** | In-depth look at **Pydantic V2** models, field validation, nested models, computed fields, and data serialization. |
| `FastApiProject/` | **Full API Project** | Integrating Pydantic into FastAPI routes, defining request/response schemas, and handling basic CRUD (Create, Read, Update, Delete) operations. |
| `Docker/` | **Containerization** | Creating a production-ready `Dockerfile`, managing application dependencies, and setting up multi-container local environments using `docker-compose.yml`. |

### 🚀 Getting Started

To clone this repository and run the examples, follow these steps.

#### 1\. Clone the Repository

```bash
git clone https://github.com/Bigyajeet/fastapi-docker-series.git
cd fastapi-docker-series
```

#### 2\. Running the Docker Example (Recommended)

The best way to run this series is by using Docker, as it encapsulates the environment.

1.  Navigate to the Docker example directory:
    ```bash
    cd Docker
    ```
2.  Build the Docker image:
    ```bash
    docker build -t fastapi-series-app .
    ```
3.  Run the container on port $\texttt{8000}$:
    ```bash
    docker run -d --name fastapi-demo -p 8000:8000 fastapi-series-app
    ```
4.  Access the API documentation in your browser:
      * **Swagger UI:** `http://localhost:8000/docs`
      * **ReDoc:** `http://localhost:8000/redoc`

#### 3\. Running Locally (Python)

If you prefer to run the applications directly:

1.  (Assuming you have Python 3.11+ installed) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On Linux/Mac
    ```
2.  Install dependencies for a specific folder (e.g., the main project):
    ```bash
    pip install -r FastApiProject/requirement.txt
    ```
3.  Run the application:
    ```bash
    uvicorn FastApiProject.main:app --reload
    ```

### 🤝 Contribution

If you have suggestions for new topics to cover in the series or find an issue, feel free to open a pull request or an issue\!

