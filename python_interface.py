# Test implementation of c++ to .py sockets
import sys
import socket
import threading

def main():
    num_args = len(sys.argv)
    if num_args < 3:
        print ("python_interface.py <Hostname> <Port>")
        sys.exit(1)

    host = sys.argv[1]
    #host = '127.0.0.1'
    port = int(sys.argv[2])

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(("Register_Request").encode(), (host,port)) 
            while True:
                data, addr = s.recvfrom(1024)
                value = (data.decode())
                break


if __name__ == "__main__":
    main()