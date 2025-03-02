import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 8080         # Port to listen on

# Dictionary to log client IP and request count
request_count = {}

# Lock for thread-safe operations on request_count
lock = threading.Lock()

def handle_client(conn, addr):
    print(f"[INFO] New connection from {addr}")
    with conn:
        while True:
            try:
                data = conn.recv(1024)  # Receive data from client
                if not data:
                    break
                # Log the request
                with lock:
                    request_count[addr] = request_count.get(addr, 0) + 1
                # print(f"[REQUEST] From {addr}: {data.decode('utf-8')}")
                conn.sendall(b"Server received your message")  # Send response back to client
            except ConnectionResetError:
                break
    print(f"[INFO] Connection closed for {addr}")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"[START] Server listening on {HOST}:{PORT}")
        
        while True:
            conn, addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    start_server()
