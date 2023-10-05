# Import the 'sniff' function from the Scapy library
from scapy.all import sniff

# Function to handle packets
def packet_callback(packet):
    # Check if the packet has an IP layer
    if packet.haslayer('IP'):
        # Check if it's TCP
        if packet.haslayer('TCP'):
            # Print a message for blocked TCP packets
            print(f"Blocked TCP packet from {packet['IP'].src}")
        else:
            # Print a message for allowed packets (non-TCP)
            print(f"Allowed packet from {packet['IP'].src}")

# Main function
def main():
    # Sniff packets
    print("Listening for packets...")
    # Call the 'sniff' function with a callback function 'packet_callback'
    # 'store=0' ensures that packets are not stored in memory, improving efficiency
    sniff(prn=packet_callback, store=0)

# Entry point of the program
if __name__ == "__main__":
    main()
