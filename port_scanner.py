import socket
from datetime import datetime

print("=" * 50)
print("         ADVANCED PORT SCANNER")
print("=" * 50)

target = input("Enter Website or IP Address: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid Hostname")
    exit()

print(f"\nTarget: {target}")
print(f"IP Address: {target_ip}")

start_port = int(input("\nEnter Starting Port: "))
end_port = int(input("Enter Ending Port: "))

print("\nScanning Started...")
start_time = datetime.now()

open_ports = []

for port in range(start_port, end_port + 1):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)

    result = scanner.connect_ex((target_ip, port))

    if result == 0:

        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown Service"

        print(f"Port {port} OPEN ({service})")
        open_ports.append(port)

    scanner.close()

end_time = datetime.now()

print("\n" + "=" * 50)
print("SCAN SUMMARY")
print("=" * 50)

print(f"Target IP      : {target_ip}")
print(f"Ports Scanned  : {end_port - start_port + 1}")
print(f"Open Ports     : {len(open_ports)}")

if open_ports:
    print("Open Port List :", open_ports)
else:
    print("No Open Ports Found")

print(f"Scan Duration  : {end_time - start_time}")

print("\nScan Completed Successfully")