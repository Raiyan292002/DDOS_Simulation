Project Overview
This project simulates a Distributed Denial-of-Service (DDoS) attack to assess the server's
response times under high request loads and explore the impact of network-based attacks on
server availability. The simulation consists of a server application that handles client requests
and multiple client bots that simulate simultaneous connection attempts. This approach aligns
with the course objective of fostering a security-oriented mindset by building awareness of how
malicious network traffic can degrade service quality and understanding defensive measures
against such attacks.

How to run
Run ./simulation.sh and 3 different amount of bots to run the simulation with. For example ./simulation.sh 5 50 100 would run the 
simulation with 5, 50 and then 100 bots

Scope and Objectives
1. Develop a DDoS simulation: Create server and client bot applications that
communicate over sockets, with bots periodically sending requests to stress the server.
2. Measure server response: Log response times for each request and calculate averages
to evaluate the performance under load.
3. Analyze and reflect: Report on the simulation’s effectiveness, analyze findings, address
challenges, and document lessons learned.
Background

DDoS Attack Fundamentals
A Distributed Denial-of-Service (DDoS) attack attempts to overwhelm a server by flooding it with
requests, causing it to slow down or crash. DDoS attacks are common and pose a major
security risk, particularly in disrupting services and preventing legitimate access. This project
emulates the effect of DDoS attacks, aiming to observe response patterns and analyze potential
defense strategies.

The project addresses the need for:
1. Understanding the impact of multiple clients connecting and sending requests to a
server.
2. Observing how network bottlenecks affect server response times and connection
stability.
3. Identifying potential issues in the server’s handling of large volumes of requests.
Methodology

Tools and Setup
• Language: Python was chosen for its socket programming capabilities.
• Scripts: Separate scripts for the server (server.py) and client bots (client.py) handle the
core of the simulation. The simulation.sh script orchestrates the overall simulation,
including setting up connections and cleaning up processes.

Simulation Execution Process
1. Server Configuration: A multithreaded server listens on a specified port and spawns
threads for handling each client connection.
2. Bot Clients: Each bot client sends periodic requests to the server and logs response
times to an output file.
3. Data Collection: Response times are logged and later averaged to evaluate server
performance.
4. Server Shutdown and Cleanup: The shell script manages server shutdown and checks
for port conflicts to prevent errors during repeated simulations.
Implementation Details

Server Code Overview (server.py)
The server code employs socket programming and multithreading. Each client connection is
handled in a separate thread, enabling concurrent connections and simulating a real-world
server environment.
• Connection Management: A dictionary tracks each client’s request count.
• Thread Synchronization: The threading.Lock() is used to prevent race conditions when
updating shared data.

Client Code Overview (client.py)
Client bots repeatedly send requests and log response times to a CSV file, recording each
session's duration to help measure server responsiveness.
• Error Handling: The client terminates gracefully if the server disconnects or does not
respond.
• Performance Logging: Response times are calculated and stored, allowing for analysis
of server performance under high load.
Simulation Script (simulation.sh)
The shell script runs the server and client applications, managing port conflicts, and collating
response time data into an output file.
• Port Management: Checks if the port is already in use and terminates existing
processes to prevent conflicts.
• Output Management: Aggregates data into avg_response_times.csv, allowing easy
analysis of performance across multiple simulations.

Results and Findings
Response Time Analysis
Results indicate a correlation between the number of clients and response latency, highlighting
the server's limitations under high load. With an increasing number of clients, response times
worsened, indicating a performance bottleneck at around 40 clients (more than 1ms delay).
Observations on Server Stability
The server exhibited stability for up to approximately 40 connections but showed signs of
overload with further clients. Empty responses from the server were observed towards the end,
indicating that it struggled to manage concurrent connections at peak load.
