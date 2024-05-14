# blog-api
Blog API Assignment from 9AI

## FastAPI App with MongoDB

This repository contains a FastAPI Blog application integrated with MongoDB for storing data. Below are the instructions for setting up the project locally.

## Local Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/manojbhavvan/blog-api.git
   cd your-repository
   ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

4. Create a .env file in the root directory of the project with the following content:

    ```text
    MONGODB_URI="mongodb+srv://username:password@clustername.mongodb.net/dbname?retryWrites=true&w=majority"
    ```

5. Replace username, password, clustername, and dbname with your actual MongoDB credentials and database name.

6. Start the FastAPI server:

    ```bash
    uvicorn app.main:app --reload
    ```

## MongoDB URI Configuration
The MongoDB URI in the .env file should follow this format:
 
    MONGODB_URI="mongodb+srv://username:password@clustername.mongodb.net/dbname?retryWrites=true&w=majority"
    

Replace the placeholders with your actual MongoDB credentials and database name.

## Postman Collections
You can find the Postman collection containing requests and their details [here](https://documenter.getpostman.com/view/23687971/2sA3JQ4zHD).

Feel free to customize the README.md further to fit your project's specific details and requirements.