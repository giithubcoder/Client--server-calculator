import socket

def main():
    print("CalculatorClient Started")

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
                soc.connect(("127.0.0.1", 8000))

                operation = input("Enter your Operations (e.g., '1 + 2' or 'sqrt 4', 'exit' to disconnect from server): ")

                if operation.lower() == "exit":
                    print("Connection disconnected.")
                    break
                elif operation.lower() == "disconnect":
                    print("Disconnecting from server...")
                    break

                soc.sendall(operation.encode())

                result = soc.recv(1024).decode()
                print("Result:", result)

        except ConnectionRefusedError:
            print("Connection refused. Ensure the server is running.")
            break
        except Exception as e:
            print(e)
            break

if __name__ == "__main__":
    main()
