import socket


def convert_volume(number, from_unit, to_unit):
    conversion_factors = {
        ("літр", "мілілітр"): 1000,
        ("літр", "кубічний метр"): 0.001,
        ("мілілітр", "літр"): 0.001,
    }

    if (from_unit, to_unit) in conversion_factors:
        factor = conversion_factors[(from_unit, to_unit)]
        result = number * factor
        return result
    elif (to_unit, from_unit) in conversion_factors:
        factor = conversion_factors[(to_unit, from_unit)]
        result = number / factor
        return result
    else:
        return None

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))
server_socket.listen(1)

print("Server is running...")

conn, addr = server_socket.accept()
print(f"Connection from: {addr}")

while True:
    try:
        data = conn.recv(1024)
        if not data:
            print("Server is closing...")
            break

        decoding = data.decode()
        print(f"Received data: {decoding}")

        try:
            number, from_unit, to_unit = decoding.split("|")
            number = float(number)

            result = convert_volume(number, from_unit.strip(), to_unit.strip())

            if result is not None:
                response = f"{number} {from_unit} is equal to {result} {to_unit}"
            else:
                response = "Conversion not possible for the selected units."

        except Exception as e:
            response = f"Error processing data: {e}"

        conn.send(response.encode())

    except Exception as e:
        print(f"Error: {e}")
        break

conn.close()
server_socket.close()