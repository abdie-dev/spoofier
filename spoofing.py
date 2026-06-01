from re import sub
import subprocess
import time


MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"  # Reset warna ke default terminal


def autoConfiguration():
    print("1. IP and MAC ( +DNS cloudflare ) \n2. IP only\n3. MAC only")

    captureInput = int(
        input("masukan pilihan anda (default: 1) : ")
    )  # Capturing Input User

    # Syntax Library
    grepingTargetName = "nmcli -t -f NAME,STATE,TYPE connection show --active | head -n 1 | cut -d ':' -f 1"
    scanSyntax = "nmcli --colors yes connection show --active"

    # Logic for Code execution
    if captureInput == 1:
        # Scanning
        print(f"{BIRU}scanning..{RESET}")
        scan = subprocess.run(scanSyntax, shell=True, capture_output=True, text=True)
        time.sleep(0.5)
        outputScanTarget = scan.stdout.strip()
        print(outputScanTarget, "\n")

        # Grepping Main Target ( Main internet )
        print("Choosing main internet device....")
        time.sleep(0.5)
        grepingTarget = subprocess.run(
            grepingTargetName,
            shell=True,
            capture_output=True,
            text=True,
        )
        outputGrepingTarget = grepingTarget.stdout.strip()
        print(f"{HIJAU}Target = {outputGrepingTarget}{RESET}\n")

        spoofingMACTarget = f"nmcli connection modify {outputGrepingTarget} ipv4.method manual \\ ipv4.addresses 192.168.1.100/24 \\ ipv4.gateway 192.168.1.1 \\ ipv4.dns 1.1.1.1"
        resettingNetwork = f'nmcli connection down "{outputGrepingTarget}" && nmcli connection up "{outputGrepingTarget}" '
        # Main spoofing
        print("Starting Spoofing IP...")
        time.sleep(0.5)
        startingSpoof = subprocess.run(
            spoofingMACTarget, shell=True, capture_output=True, text=True
        )
        startResetting = subprocess.run(
            resettingNetwork, shell=True, capture_output=True, text=True
        )
        print(startingSpoof.stdout.strip(), "\n", startResetting.stdout.strip())

        pass
    elif captureInput == 2:
        pass
    elif captureInput == 3:
        pass
    else:
        print("Please check again your input!!")


def manualConfiguration():
    pass


def scanNetwork():
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
