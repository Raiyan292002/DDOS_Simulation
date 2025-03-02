#!/bin/bash

# Clear any previous output file
rm -rf avg_response_times.csv

# Script that runs DDoS simulation and logs average response time
output_file="avg_response_times.csv"

# Create a file with headings if it doesn't exist
if [ ! -f "$output_file" ]; then
    echo "Number of Bots, Avg Response Time (ms)" > "$output_file"
fi

# Function to run the simulation for a specific number of bots
run_simulation() {
    rm -rf response_times.csv
    num_bots=$1
    echo "Running simulation with $num_bots bots..."

    # Check if there's an existing server process using the specified port and kill it
    existing_pid=$(lsof -t -i:8080)
    if [ -n "$existing_pid" ]; then
        kill -9 "$existing_pid"
        sleep 1  # Allow time for the port to be freed
    fi

    # Start the server in the background
    python3 server.py & 
    server_pid=$!
    sleep 2  # Wait for the server to start

    # Launch the specified number of bot clients
    for ((i=1; i<=num_bots; i++)); do
        python3 client.py &
    done

    # Run the simulation for a specific duration
    sleep 10

    # Kill the server after the simulation
    kill -9 $server_pid
    wait $server_pid 2>/dev/null
    sleep 1  # Allow time for the port to free up

    # Calculate the average response time from response_times.csv
    avg_response_time=$(awk '{sum += $1 * 1000} END {print sum / NR}' response_times.csv)

    # Log the number of bots and average response time to the output file
    echo "$num_bots, $avg_response_time" >> "$output_file"
    echo "Average response time for $num_bots bots: $avg_response_time s"
}

# Run simulations for each argument (number of bots)
run_simulation $1
run_simulation $2
run_simulation $3

# Display the results file
cat "$output_file"
