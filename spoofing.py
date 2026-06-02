# Import necessary modules
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

    # Input validation: ensure user enters a valid option (1, 2, or 3)
    try:
        captureInput = int(
            input("masukan pilihan anda (default: 1) : ")
        )  # Capturing Input User
        if captureInput not in [1, 2, 3]:
            print("Please check again your input!!")
            return
    except ValueError:
        # Handle non-numeric input gracefully
        print("Invalid input! Please enter a number (1, 2, or 3).")
        return

    # Define network command syntax for target identification and scanning
    grepingTargetName = "nmcli -t -f NAME,STATE,TYPE connection show --active | head -n 1 | cut -d ':' -f 1"
    grepingTargetType = "nmcli -t -f NAME,STATE,TYPE connection show --active | head -n 1 | cut -d ':' -f 3"
    scanSyntax = "nmcli --colors yes connection show --active"

    # Scanning - performed once and shared across all spoofing options
    try:
        print(f"{BIRU}scanning..{RESET}")
        scan = subprocess.run(
            scanSyntax, shell=True, capture_output=True, text=True, check=True
        )
        time.sleep(0.5)
        outputScanTarget = scan.stdout.strip()
        print(outputScanTarget, "\n")
    except subprocess.CalledProcessError as e:
        # Handle errors during network scanning
        print(f"{MERAH}Error scanning network: {e}{RESET}")
        return

    # Extract the main active network interface name (target) from scan results
    try:
        print("Choosing main internet device....")
        time.sleep(0.5)
        grepingTarget = subprocess.run(
            grepingTargetName,
            shell=True,
            capture_output=True,
            text=True,
            check=True,
        )
        TARGET = grepingTarget.stdout.strip()
        if not TARGET:
            print(f"{MERAH}No active connection found!{RESET}")
            return
        print(f"{HIJAU}Target connection = {TARGET}{RESET}\n")
    except subprocess.CalledProcessError as e:
        # Handle errors during target identification
        print(f"{MERAH}Error getting target: {e}{RESET}")
        return

    # Construct common command to restart the network connection (used by all options)
    resettingNetwork = (
        f'nmcli connection down "{TARGET}" && nmcli connection up "{TARGET}"'
    )

    # Main logic execution based on validated user input
    if captureInput == 1:
        # Option 1: Spoof both IP and MAC addresses
        try:
            # Construct command to set static IP configuration (IPv4)
            spoofingIPTarget = f'nmcli connection modify "{TARGET}" ipv4.method manual ipv4.addresses 192.168.1.100/24 ipv4.gateway 192.168.1.1 ipv4.dns 1.1.1.1'
            # Execute IP address spoofing command
            print("Starting Spoofing IP...")
            time.sleep(0.5)
            startingSpoof = subprocess.run(
                spoofingIPTarget, shell=True, capture_output=True, text=True, check=True
            )
            print(f"{HIJAU}IP configuration applied.{RESET}")

            # Construct and execute MAC address spoofing command (using connection modify)
            if "wireless" in grepingTargetType:
                spoofingMACTarget = f'nmcli connection modify "{TARGET}" 802-11-wireless.cloned-mac-address 00:11:22:33:44:55'
                print("Starting spoofing MAC...")
                time.sleep(0.5)
                startingSpoofMac = subprocess.run(
                    spoofingMACTarget,
                    shell=True,
                    capture_output=True,
                    text=True,
                    check=True,
                )
                print(f"{HIJAU}MAC address spoofing applied.{RESET}")
            elif "ethernet" in grepingTargetType:
                spoofingMACTarget = f'nmcli connection modify "{TARGET}" 802-11-ethernet.cloned-mac-address 00:11:22:33:44:55'
                print("Starting spoofing MAC...")
                time.sleep(0.5)
                startingSpoofMac = subprocess.run(
                    spoofingMACTarget,
                    shell=True,
                    capture_output=True,
                    text=True,
                    check=True,
                )
                print(f"{HIJAU}MAC address spoofing applied.{RESET}")

            # Execute network reset to apply all changes
            print("Restarting network connection...")
            startResetting = subprocess.run(
                resettingNetwork, shell=True, capture_output=True, text=True, check=True
            )
            print(f"{HIJAU}Network restarted successfully.{RESET}")
            # Display outputs for debugging (optional)
            # print(startingSpoof.stdout.strip(), "\n", startResetting.stdout.strip())
        except subprocess.CalledProcessError as e:
            print(f"{MERAH}Error during IP+MAC spoofing: {e}{RESET}")
            # Print stderr for more details
            if e.stderr:
                print(f"Details: {e.stderr}")
            return

    elif captureInput == 2:
        # Option 2: Spoof IP address only
        try:
            # Construct command to set static IP configuration (IPv4)
            spoofingIPTarget = f'nmcli connection modify "{TARGET}" ipv4.method manual ipv4.addresses 192.168.1.100/24 ipv4.gateway 192.168.1.1 ipv4.dns 1.1.1.1'

            # Execute IP address spoofing command
            print("Starting Spoofing IP only...")
            time.sleep(0.5)
            startingSpoof = subprocess.run(
                spoofingIPTarget, shell=True, capture_output=True, text=True, check=True
            )
            print(f"{HIJAU}IP configuration applied.{RESET}")

            # Execute network reset to apply changes
            print("Restarting network connection...")
            startResetting = subprocess.run(
                resettingNetwork, shell=True, capture_output=True, text=True, check=True
            )
            print(f"{HIJAU}Network restarted successfully.{RESET}")
        except subprocess.CalledProcessError as e:
            print(f"{MERAH}Error during IP spoofing: {e}{RESET}")
            if e.stderr:
                print(f"Details: {e.stderr}")
            return

    elif captureInput == 3:
        # Option 3: Spoof MAC address only
        try:
            # Construct and execute MAC address spoofing command
            spoofingMACTarget = f'nmcli connection modify "{TARGET}" 802-11-wireless.cloned-mac-address 00:11:22:33:44:55'
            print("Starting spoofing MAC only...")
            time.sleep(0.5)
            startingSpoofMac = subprocess.run(
                spoofingMACTarget,
                shell=True,
                capture_output=True,
                text=True,
                check=True,
            )
            print(f"{HIJAU}MAC address spoofing applied.{RESET}")

            # Execute network reset to apply changes
            print("Restarting network connection...")
            startResetting = subprocess.run(
                resettingNetwork, shell=True, capture_output=True, text=True, check=True
            )
            print(f"{HIJAU}Network restarted successfully.{RESET}")
        except subprocess.CalledProcessError as e:
            print(f"{MERAH}Error during MAC spoofing: {e}{RESET}")
            if e.stderr:
                print(f"Details: {e.stderr}")
            return


def manualConfiguration():
    # Placeholder for manual network configuration function
    # TODO: Implement manual IP/MAC configuration based on user input
    print(f"{KUNING}Manual configuration not yet implemented.{RESET}")


def scanNetwork():
    # Execute resolvectl status command to display DNS and network configuration
    try:
        scan = subprocess.run(
            ["resolvectl", "status"], capture_output=True, text=True, check=False
        )
        print("\n" + "=" * 50)
        print("DNS & Network Status")
        print("=" * 50)
        print(scan.stdout)
        if scan.stderr:
            print(f"{KUNING}Stderr: {scan.stderr}{RESET}")
    except FileNotFoundError:
        print(
            f"{MERAH}resolvectl command not found. Try using 'systemd-resolve --status' instead.{RESET}"
        )


if __name__ == "__main__":
    print("Welcome to Spoofing by biww\n")
    print("1. Auto Configure\n2. Manual Configure\n3. Reset\n4. Scan")
    try:
        captureInput = int(input("masukan pilihan anda: "))
    except ValueError:
        print(f"{MERAH}Invalid input! Please enter a number.{RESET}")
        exit(1)

    match captureInput:
        case 1:
            autoConfiguration()
        case 2:
            manualConfiguration()
        case 3:
            print(
                f"{KUNING}Reset feature not yet implemented. Use 'nmcli connection down/up' manually.{RESET}"
            )
        case 4:
            scanNetwork()
        case _:
            print(f"{MERAH}Invalid choice.{RESET}")
