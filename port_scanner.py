
# Royall-Researchers

import socket
print("Port-Scanner By")
print( '''  
 ____                   _ _ 
|  _ \ ___  _   _  __ _| | |
| |_) / _ \| | | |/ _` | | |
|  _ < (_) | |_| | (_| | | |
|_| \_\___/ \__, |\__,_|_|_|
            |___/           
 ____                               _                   
|  _ \ ___  ___  ___  __ _ _ __ ___| |__   ___ _ __ ___ 
| |_) / _ \/ __|/ _ \/ _` | '__/ __| '_ \ / _ \ '__/ __|
|  _ <  __/\__ \  __/ (_| | | | (__| | | |  __/ |  \__ \ 
|_| \_\___||___/\___|\__,_|_|  \___|_| |_|\___|_|  |___/
 
''')

def scan_ports(target_host, start_port, end_port):
    print(f"Scanning ports on {target_host}...\n")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target_host, port))

        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")

        sock.close()

if __name__ == "__main__":
    target_host = input("Enter the target host: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    scan_ports(target_host, start_port, end_port)
