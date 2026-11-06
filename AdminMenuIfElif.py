print("1) Disk\n2) Users\n3) Ping\nq) Quit")
option = input("> ").strip().lower()

if option == "1":
    used = int(input("Used %: "))
    if used > 90:
        print("CRITICAL: Disk space is almost full!")
    elif used > 80:
        print("WARNING: Disk space is high.")
    else:
        print(f"OK: Disk usage is normal ({used}%).")
elif option == "2":
    print("Connected users: root, admin, student01")
elif option == "3":
    ip = input("Enter IP to ping: ").strip()
    parts = ip.split(".")
    if len(parts) == 4:
        print(f"Pinging {ip}... 4 packets transmitted, 0% packet loss.")
    else:
        print(f"Invalid IP address: '{ip}' must have exactly 4 octets.")
elif option == "q":
    print("Exiting admin menu. Bye!")
else:
    print("Unknown option")