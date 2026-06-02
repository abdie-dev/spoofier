# Import necessary modules
from re import sub  # For string substitution (currently unused)
import subprocess  # For executing shell commands
import time  # For adding delays


# Define color codes for terminal output
MERAH = "\033[91m"  # Red color
HIJAU = "\033[92m"  # Green color
KUNING = "\033[93m"  # Yellow color
BIRU = "\033[94m"  # Blue color
CYAN = "\033[96m"  # Cyan color
RESET = "\033[0m"  # Reset color to default terminal


def autoConfiguration():
    # Display configuration options to user
    print("1. IP and MAC ( +DNS cloudflare ) \n2. IP only\n3. MAC only")

    # Get user input for configuration choice (default to option 1)
    captureInput = int(
        input("masukan pilihan anda (default: 1) : ")
    )  # Capturing Input User

    # Define network command syntax for target identification and scanning
    grepingTargetName = "nmcli -t -f NAME,STATE,TYPE connection show --active | head -n 1 | cut -d ':' -f 1"
    scanSyntax = "nmcli --colors yes connection show --active"

    # Main logic execution based on user input
    if captureInput == 1:
        # Perform network scan to identify active connections
        print(f"{BIRU}scanning..{RESET}")
        scan = subprocess.run(scanSyntax, shell=True, capture_output=True, text=True)
        time.sleep(0.5)
        outputScanTarget = scan.stdout.strip()
        print(outputScanTarget, "\n")

        # Extract the main active network interface name (target) from scan results
        print("Choosing main internet device....")
        time.sleep(0.5)
        grepingTarget = subprocess.run(
            grepingTargetName,
            shell=True,
            capture_output=True,
            text=True,
        )
        TARGET = grepingTarget.stdout.strip()
        print(f"{HIJAU}Target = {TARGET}{RESET}\n")

        # Construct command to set static IP configuration (IPv4) for the target interface
        spoofingIPTarget = f"nmcli connection modify {TARGET} ipv4.method manual ipv4.addresses 192.168.1.100/24 ipv4.gateway 192.168.1.1 ipv4.dns 1.1.1.1"
        # Construct command to restart the network connection to apply changes
        resettingNetwork = (
            f'nmcli connection down "{TARGET}" && nmcli connection up "{TARGET}" '
        )

        # Proceed with IP and MAC address spoofing operations

        # Execute IP address spoofing command on the target interface
        print("Starting Spoofing IP...")
        time.sleep(0.5)
        startingSpoof = subprocess.run(
            spoofingIPTarget, shell=True, capture_output=True, text=True
        )

        # Execute MAC address spoofing command on the target interface
        print("Starting spoofing MAC...")
        time.sleep(0.5)
        spoofingMACTarget = (
            f"nmcli device modify {TARGET} cloned-mac-address 00:11:22:33:44:55"
        )
        startingSpoofMac = subprocess.run(
            spoofingMACTarget, shell=True, capture_output=True, text=True
        )

        # Display the output of MAC spoofing operation
        print(startingSpoofMac.stdout.strip())
        # Execute network reset command to apply all changes
        startResetting = subprocess.run(
            resettingNetwork, shell=True, capture_output=True, text=True
        )
        # Display outputs of both IP spoofing and network reset operations
        print(startingSpoof.stdout.strip(), "\n", startResetting.stdout.strip())

    elif captureInput == 2:
        # Perform network scan to identify active connections
        print(f"{BIRU}scanning..{RESET}")
        scan = subprocess.run(scanSyntax, shell=True, capture_output=True, text=True)
        time.sleep(0.5)
        outputScanTarget = scan.stdout.strip()
        print(outputScanTarget, "\n")

        # Extract the main active network interface name (target) from scan results
        print("Choosing main internet device....")
        time.sleep(0.5)
        grepingTarget = subprocess.run(
            grepingTargetName,
            shell=True,
            capture_output=True,
            text=True,
        )
        TARGET = grepingTarget.stdout.strip()
        print(f"{HIJAU}Target = {TARGET}{RESET}\n")

        # Construct command to set static IP configuration (IPv4) for the target interface
        spoofingIPTarget = f"nmcli connection modify {TARGET} ipv4.method manual ipv4.addresses 192.168.1.100/24 ipv4.gateway 192.168.1.1 ipv4.dns 1.1.1.1"
        # Construct command to restart the network connection to apply changes
        resettingNetwork = (
            f'nmcli connection down "{TARGET}" && nmcli connection up "{TARGET}" '
        )

        # Proceed with IP address spoofing only

        # Execute IP address spoofing command on the target interface
        print("Starting Spoofing IP only...")
        time.sleep(0.5)
        startingSpoof = subprocess.run(
            spoofingIPTarget, shell=True, capture_output=True, text=True
        )

        # Execute network reset command to apply changes
        startResetting = subprocess.run(
            resettingNetwork, shell=True, capture_output=True, text=True
        )
        # Display outputs of IP spoofing and network reset operations
        print(startingSpoof.stdout.strip(), "\n", startResetting.stdout.strip())
    elif captureInput == 3:
        # Perform network scan to identify active connections
        print(f"{BIRU}scanning..{RESET}")
        scan = subprocess.run(scanSyntax, shell=True, capture_output=True, text=True)
        time.sleep(0.5)
        outputScanTarget = scan.stdout.strip()
        print(outputScanTarget, "\n")

        # Extract the main active network interface name (target) from scan results
        print("Choosing main internet device....")
        time.sleep(0.5)
        grepingTarget = subprocess.run(
            grepingTargetName,
            shell=True,
            capture_output=True,
            text=True,
        )
        TARGET = grepingTarget.stdout.strip()
        print(f"{HIJAU}Target = {TARGET}{RESET}\n")

        # Construct command to restart the network connection to apply changes
        resettingNetwork = (
            f'nmcli connection down "{TARGET}" && nmcli connection up "{TARGET}" '
        )

        # Proceed with MAC address spoofing only

        spoofingMACTarget = (
            f"nmcli device modify {TARGET} cloned-mac-address 00:11:22:33:44:55"
        )
        # Execute MAC address spoofing command on the target interface
        print("Starting spoofing MAC only...")
        time.sleep(0.5)
        startingSpoofMac = subprocess.run(
            spoofingMACTarget, shell=True, capture_output=True, text=True
        )

        # Execute network reset command to apply changes
        startResetting = subprocess.run(
            resettingNetwork, shell=True, capture_output=True, text=True
        )
        # Display outputs of MAC spoofing and network reset operations
        print(startingSpoofMac.stdout.strip(), "\n", startResetting.stdout.strip())
    else:
        print("Please check again your input!!")


def manualConfiguration():
    # Placeholder for manual network configuration function
    # TODO: Implement manual IP/MAC configuration based on user input
    pass


def scanNetwork():
    # Execute resolvectl status command to display DNS and network configuration
    scan = subprocess.run(["resolvectl", "status"], capture_output=True, text=True)
    print("\nStdout:", scan.stdout)  # Output: Hello World
    return


if __name__ == "__main__":
    print("Welcome to Spoofing by biww\n")
    print("1. Auto Configure\n2. Manual Configure\n3. Reset\n4. Scan")
    captureInput = int(input("masukan pilihan anda: "))
    match captureInput:
        case 1:
            autoConfiguration()
        case 2:
            manualConfiguration()
        case 3:
            pass
        case 4:
            scanNetwork()
    pass
