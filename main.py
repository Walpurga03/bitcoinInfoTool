import subprocess
import json
import os

# Umgebungsvariablen lesen
BITCOIN_CLI_PATH = os.getenv('BITCOIN_CLI_PATH')
BITCOIN_CONF_PATH = os.getenv('BITCOIN_CONF_PATH')
BITCOIN_DATA_DIR = os.getenv('BITCOIN_DATA_DIR')

def run_bitcoin_cli_command(command):
    # Kompletten Befehl zusammenbauen, inklusive Pfad zu bitcoin-cli, Konfigurationsdatei und Datenverzeichnis
    full_command = f"{BITCOIN_CLI_PATH} -conf={BITCOIN_CONF_PATH} -datadir={BITCOIN_DATA_DIR} {command}"
    result = subprocess.run(full_command.split(), capture_output=True, text=True)
    if result.stdout:
        return json.loads(result.stdout)
    elif result.stderr:
        return "Fehler: " + result.stderr
    else:
        return "Unbekannter Fehler"

def get_blockchain_info():
    return run_bitcoin_cli_command("getblockchaininfo")

def get_block_count():
    return run_bitcoin_cli_command("getblockcount")

def get_best_block_hash():
    return run_bitcoin_cli_command("getbestblockhash")

def get_block(blockhash):
    return run_bitcoin_cli_command(f"getblock {blockhash}")

def get_transaction(txid):
    return run_bitcoin_cli_command(f"gettransaction {txid}")

def get_new_address():
    return run_bitcoin_cli_command("getnewaddress")

def send_to_address(bitcoinaddress, amount):
    return run_bitcoin_cli_command(f"sendtoaddress {bitcoinaddress} {amount}")

def list_unspent():
    return run_bitcoin_cli_command("listunspent")

def get_wallet_info():
    return run_bitcoin_cli_command("getwalletinfo")

def get_peer_info():
    return run_bitcoin_cli_command("getpeerinfo")

def main():
    while True:
        print("\nWählen Sie eine Option:")
        print(" 1 - Blockchain Info")
        print(" 2 - Blockchain Count")
        print(" 3 - Best Block Hash")
        print(" 4 - Block nach Hash")
        print(" 5 - Transaction nach ID")
        print(" 6 - Neue Adresse generieren")
        print(" 7 - Senden an Adresse")
        print(" 8 - List Unspent")
        print(" 9 - Wallet Info")
        print("10 - Peer Info")
        print(" 0 - Beenden")
        
        choice = input("Ihre Wahl: ")
        
        if choice == "1":
            print("Blockchain Info:\n", get_blockchain_info())
        elif choice == "2":
            print("Blockchain Count:\n", get_block_count())
        elif choice == "3":
            print("Best Block Hash:\n", get_best_block_hash())
        elif choice == "4":
            blockhash = input("Blockhash eingeben: ")
            print("Block:\n", get_block(blockhash))
        elif choice == "5":
            txid = input("Transaction ID eingeben: ")
            print("Transaction:\n", get_transaction(txid))
        elif choice == "6":
            print("Neue Adresse:\n", get_new_address())
        elif choice == "7":
            bitcoinaddress = input("Bitcoin Adresse eingeben: ")
            amount = input("Betrag eingeben: ")
            print("Senden:\n", send_to_address(bitcoinaddress, amount))
        elif choice == "8":
            print("List Unspent:\n", list_unspent())
        elif choice == "9":
            print("Wallet Info:\n", get_wallet_info())
        elif choice == "10":
            print("Peer Info:\n", get_peer_info())
        elif choice == "0":
            print("Programm wird beendet...")
            break
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()
