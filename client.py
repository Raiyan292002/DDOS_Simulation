import socket
import time
import csv

# Server configuration (same as above)
HOST = '127.0.0.1'  # Localhost
PORT = 8080         # Port to connect to

def log_response_time(start_time, end_time):
    response_time = end_time - start_time
    with open('response_times.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([response_time])

def simulate_bot():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            # print("[CONNECTED] Bot connected to the server")
            while True:
                # Record the start time before sending
                start_time = time.time()

                s.sendall(b"Bot request to server")  # Send request
                data = s.recv(1024)  # Receive server response

                # Check for empty response
                if not data:
                    break  # Exit the loop if the server is unresponsive

                # Record the end time after receiving
                end_time = time.time()

                # Log the response time
                log_response_time(start_time, end_time)

                print(f"[RESPONSE] Server: {data.decode('utf-8')}")
                time.sleep(0.5)  # Adjust delay to control request rate
    except Exception:
        pass

if __name__ == "__main__":
    simulate_bot()
