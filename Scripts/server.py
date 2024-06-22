import socket
import math

def evaluate_expression(expression):
    try:
        # Split the expression using regular expressions to handle multiple operators and spaces
        import re
        parts = re.split(r'(\+|\-|\*|\/|\%)', expression)
        
        # Remove any empty strings from the parts list
        parts = [part.strip() for part in parts if part.strip()]
        
        # Initialize the result with the first number
        result = float(parts[0])
        
        # Iterate over the remaining parts in pairs (operator, operand)
        i = 1
        while i < len(parts) - 1:
            operator = parts[i]
            operand = float(parts[i + 1])
            
            if operator == '+':
                result += operand
            elif operator == '-':
                result -= operand
            elif operator == '*':
                result *= operand
            elif operator == '/':
                if operand != 0:
                    result /= operand
                else:
                    raise ArithmeticError("Division by zero")
            elif operator == '%':
                result %= operand
            else:
                raise ValueError("Invalid operator: " + operator)
            
            i += 2  # Move to the next operator/operand pair
        
        return result
    
    except (ValueError, ArithmeticError) as e:
        print(e)
        return float('nan')  # Return NaN for any value errors or division by zero
    except Exception as e:
        print(e)
        return float('nan')  # Return NaN for any other exceptions

def main():
    print("Waiting for clients operation:")
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(('127.0.0.1', 8000))
            server_socket.listen()
            
            while True:
                client_socket, addr = server_socket.accept()
                with client_socket:
                    print("Connection Established:")
                    
                    client_operation = client_socket.recv(1024).decode()
                    print("Operation received from client:", client_operation)
                    
                    if client_operation.lower() == "exit":
                        print("Disconnected")
                        break
                    
                    result = evaluate_expression(client_operation)
                    
                    if not math.isnan(result):
                        response = "Answer: " + str(result)
                    else:
                        response = "Error: Invalid operation format"
                    
                    client_socket.sendall(response.encode())
    
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
