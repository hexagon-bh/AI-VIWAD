from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_socket_io_get_request():
    data = request.args.get('data')  # Get the 'data' query parameter from the GET request
    if data:
        # Do something with the received data (e.g., print it)
        print("Received data:", data)
        return "Data received successfully\n"
    else:
        return "No data received\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)