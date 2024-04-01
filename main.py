import subprocess
import json

def run_bitcoin_cli_command(command):
    # Kompletten Befehl zusammenbauen, inklusive Pfad zu bitcoin-cli und Konfigurationsdatei
    full_command = f"/usr/local/bin/bitcoin-cli -conf=/home/alex/.bitcoin/bitcoin.conf -datadir=/mnt/bitcoin_data {command}"
    result = subprocess.run(full_command.split(), capture_output=True, text=True)
    if result.stdout:
        return json.loads(result.stdout)
    else:
        return "Fehler: " + result.stderr

def get_blockchain_info():
    return run_bitcoin_cli_command("getblockchaininfo")

def get_block_count():
    return run_bitcoin_cli_command("getblockcount")

def main():
    while True:
        print("\nWählen Sie eine Option:")
        print("1 - Blockchain Info")
        print("2 - Blockchain Count")
        print("0 - Beenden")
        
        choice = input("Ihre Wahl: ")
        
        if choice == "1":
            print("Blockchain Info:\n", get_blockchain_info())
        elif choice == "2":
            print("Blockchain Count:\n", get_block_count())
        elif choice == "0":
            print("Programm wird beendet...")
            break
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()
