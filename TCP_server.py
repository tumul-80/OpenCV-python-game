'''
This code basically achieves the purpose of creating and accepting connections from TCP clients
and writes the message and time whenever a new conncection is made. 

Created by: Tumul Kumar. 
'''

import socket
from datetime import datetime


class TCPServer:
    # to write out the initial hell_message 
    with open('out.txt', 'w') as output:  # truncating file and writing default
        output.write('Hello\n')

    def __init__(self, host, TCP_port):
        self.host = host
        self.TCP_port = TCP_port  # non-privileged port
        self.sock = None
    # to print the message on the console output with the current date and time
    def print_msg(self, msg):
        current_date_time = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        print(current_date_time+ ' JST ' + msg)
        with open('out.txt', 'a') as output:  # truncating file and writing default
            output.write(current_date_time + msg)

    def config(self):
        self.print_msg(' Creating socket \n')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.print_msg(' Socket created\n')
        self.sock.bind((self.host, self.TCP_port))
        self.print_msg(' Server binded to ' + self.host + ':' + str(self.TCP_port)+'\n')

    def wait_for_client(self):
        self.print_msg('Listening for incoming connections \n')
        self.sock.listen(3)

        client_conn, client_addr = self.sock.accept()
        client_address = ':'.join(map(str, client_addr))
        self.print_msg(' Connected by: ' + client_address + '\n')

        self.handle_client(client_conn, client_address)

    def handle_client(self, client_conn, client_address:str):
        try:
            while True:
                data = client_conn.recv(1024)
                if not data: break
                name = data.decode()
                self.print_msg('\nRequest from ' + client_address+'\n')
                print('\n' + name + '\n')
                client_conn.sendall(data)
                self.print_msg(' Connection\n')
                if name == "exit":
                    raise KeyboardInterrupt("\nExit command entered\m")

        except OSError as err:
            self.print_msg(err)

        except KeyboardInterrupt:
            self.shutdown()

        except NameError:
            self.shutdown()

        finally:
            client_conn.close()
            self.print_msg('\n Closing client socket for ' + client_address)

    def shutdown(self):
        self.print_msg('\n Shutting down server')

def main():
    tcp_server = TCPServer('localhost', 9999)
    tcp_server.config()
    tcp_server.wait_for_client()


if __name__ == '__main__':
    main()

    
