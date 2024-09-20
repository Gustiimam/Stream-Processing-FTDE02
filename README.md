# Stream Processing Project
This project is designed to process streaming data using Kafka, MongoDB, and Python. The system reads data from a CSV file, sends it to a Kafka topic via a producer script, and a consumer script saves the data to MongoDB. The system also implements deduplication to prevent duplicate entries in MongoDB.

## Table of Contents
1. Tools Used
2. Requirements
3. Project Structure
4. Setup and Usage
   - Kafka Setup
   - MongoDB Setup
   - Producer Script
   - Consumer Script
5. Deduplication in MongoDB
6. Additional Information

# Tools Used
- Kafka: For streaming data using a producer-consumer model.
- MongoDB: For storing the streamed data.
- Docker: To run Kafka, MongoDB, and other services in containers.
- Python: For developing producer and consumer scripts.
- pandas: To handle CSV file processing.
- Kafka-Python: For integrating Kafka into Python scripts.
- PyMongo: To interact with MongoDB from Python.

# Requirements
Ensure the following tools are installed on your machine:

1. Docker: To run Kafka and MongoDB.
2. Python (version 3.8 or higher): Required for running the scripts.
3. Kafka: Ensure Kafka is installed or running in Docker.

# Project Structure
project-root/
│
├── producer.ipynb                # Producer script that sends data to Kafka topic
├── Consumer-Workflow.ipynb         # Consumer script that reads from Kafka and stores in MongoDB
├── requirements.txt                # Required Python libraries
└── README.md                       # Project documentation

# Setup and Usage
1. Kafka Setup
   You need to run Kafka and Zookeeper to handle the message stream. You can use Docker Compose for this setup:
   docker-compose up -d
 
   Ensure your docker-compose.yml includes:
   - Kafka
   - Zookeeper
   - MongoDB
   - Mongo-Express (optional for MongoDB UI).
  
3. MongoDB Setup
   MongoDB can be run as a container in Docker using the following command:
   docker run --name mongodb -d -p 27017:27017 mongo

   To view the MongoDB collections, you can use mongo-express or connect through a client like DBeaver:
   docker run -d -p 8081:8081 --link mongodb:mongo mongo-express

4. Producer Script
   The producer reads data from a CSV file and sends it to a Kafka topic. To run the producer:
   - Open producer.ipynb in your Jupyter notebook.
   - Modify the timeout value and time.sleep() duration based on your needs.
   - Run the script to start sending data to the Kafka topic.

5. Consumer Script
   The consumer listens to the Kafka topic and stores the messages into MongoDB, while ensuring no duplicate data is inserted.
   - Open Consumer-Workflow.ipynb in Jupyter Notebook.
   - Run the consumer script to begin consuming messages and storing them in MongoDB.

6. Deduplication in MongoDB
   To avoid duplicates, a unique index is created on the field that should be unique (e.g., transaction_id). This ensures that only unique records are stored in MongoDB.
   You can create the unique index using:
   db.collection.createIndex({ "transaction_id": 1 }, { unique: true })

   This will prevent any duplicate records with the same transaction_id from being inserted.

# Additional Information
- If the producer script is relaunched, the deduplication mechanism will prevent duplicate data from being stored in MongoDB.
- If you want to adjust the data sending speed, modify the time.sleep() in the producer script.

This project demonstrates how to set up a basic stream processing pipeline using Kafka and MongoDB with deduplication functionality.
Feel free to adjust the parameters to suit your needs!
