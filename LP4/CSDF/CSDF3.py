from scapy.all import *
import os

# Set the Wi-Fi interface to monitor mode
wifi_interface = "wlan0mon"  # Change this to your Wi-Fi interface in monitor mode

# Dictionary to track failed attempts by MAC address
failed_attempts = {}

# Threshold for blocking an IP (e.g., 5 failed attempts)
threshold = 5


def detect_brute_force(pkt):
    # Check if the packet is an authentication packet
    if pkt.haslayer(Dot11Auth):
        source_mac = pkt.addr2  # Get the source MAC address (device trying to authenticate)

        # Check if the packet is an authentication failure
        if pkt[Dot11Auth].status != 0:  # Status != 0 indicates failure
            print(f"Authentication failed from: {source_mac}")
            if source_mac in failed_attempts:
                failed_attempts[source_mac] += 1
            else:
                failed_attempts[source_mac] = 1

            # Block the device if it exceeds the threshold of failed attempts
            if failed_attempts[source_mac] > threshold:
                block_device(source_mac)


def block_device(mac):
    print(f"Blocking device with MAC: {mac}")

    # Block by MAC address using iptables
    os.system(f"sudo iptables -A INPUT -m mac --mac-source {mac} -j DROP")

    # Optionally, de-authenticate the device (disconnect it from the Wi-Fi)
    # This command may vary based on your system and network setup
    os.system(f"sudo aireplay-ng -0 1 -a <AP_MAC_ADDRESS> -c {mac} {wifi_interface}")


if __name__ == "__main__":
    print(f"Monitoring Wi-Fi for authentication failures on {wifi_interface}...")

    # Sniff packets and apply the detect_brute_force function on each packet
    sniff(iface=wifi_interface, prn=detect_brute_force)
