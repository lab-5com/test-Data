## Technical Test for Data Engineering Position

### Objective
Develop a streaming data processing application that joins two datasets, simulating real-time data streams. This application will serve as a proof of concept for a larger implementation where these datasets will be replaced by continuous streaming sources.

### Scenario
- You are provided with two files: one representing **transaction facts** (e.g., timestamp, product ID, quantity) and the other containing **product details** (e.g., product ID, product name, price).
- Your tasks is 
  - **Implement a streaming application** that joins these datasets on the product ID, outputting a combined dataset with transaction details enriched by product information.
  - **Compute Gross Turnover**: In a streaming fashion, compute the gross turnover by products (product ID, product name, total sales amount), and the total gross turnover across all products. This state should be stored in a persistent store (e.g., a database, a stateful service, or a file) and updated in real-time as new transactions are processed.

### Requirements
- **Streaming Technology**: You may choose any streaming technology you prefer, with a preference for Spark Streaming, Kafka Streams, FS2, Akka Streams, or Apache Beam.
- **Programming Language**: While you may use any programming language, Scala is preferred.
- **Output**: The application should output the joined dataset and the computed gross turnovers in real-time, simulating a continuous stream. Output format can be to a console, file, or any mock sink of your choice.
- **Testing**: Implement tests to validate your streaming logic, data integrity, and correctness of the computed turnovers.

### Deliverables
1. Source code for the streaming application, including any configuration files.
2. A brief documentation explaining your solution, choice of technology, how to run your application and tests, and how the gross turnover calculations are implemented and stored.
3. Test cases.
