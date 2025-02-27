# practice_fastapi_docker

### Step 1: Install Required Libraries
First, install the necessary dependencies:

bash
pip install fastapi uvicorn scikit-learn joblib numpy pandas

### Step 2: Train and Save the Logistic Regression Model
Create a script train_model.py to train and save the model:


Run the script:

bash
python train_model.py

### Step 3: Create a FastAPI App
Create a new file app.py:

### Step 4: Run FastAPI Locally
Run the FastAPI app using Uvicorn:
uvicorn main:app --reload

### Step 5: Create a Dockerfile
Create a Dockerfile in the project directory:
name : dockerfile (a docker menu pop-up at bottom of vscode

Use an official Python runtime as base image
FROM python:3.9

Set the working directory
WORKDIR /app

Copy files to the container
COPY . /app

Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn scikit-learn joblib numpy pydantic

Expose port
EXPOSE 8000

Run the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

Step 6: Build and Run the Docker Container
Build the Docker Image
bash
docker build -t fastapi-logistic-regression .

Run the Container
bash
docker run -p 8000:8000 fastapi-logistic-regression

#### FastAPI automatically generates API documentation at:

Swagger UI:
👉 http://127.0.0.1:8000/docs
ReDoc:
👉 http://127.0.0.1:8000/redoc
