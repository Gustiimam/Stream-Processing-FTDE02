#!python3

import json
import pandas as pd
from kafka import KafkaProducer
import time

if __name__ == "__main__":

    # Use a relative path to the CSV file
    data = pd.read_csv('C:\Data\Data engineer DigitalSkola\Project 4 - Stream Processing\Data CSV/New_Information.csv')
    json_data = data.to_dict(orient='records')

    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    # producing data from csv with constraint time
    start_time = time.time()  # time start
    timeout = 600  # 600 is equal to 10 minutes

    for record in json_data:
        if time.time() - start_time > timeout:
            print("Timeout reached, stopping producer.")
            break
        producer.send("ftde02-project4", record)
        print(f"Produced: {record}")
        time.sleep(5)

    # message to end producer
    producer.flush()
    producer.close()
    print("Producer selesai mengirim data.")