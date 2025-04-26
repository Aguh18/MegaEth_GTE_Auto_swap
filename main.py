from web3 import Web3
from utils.utils import check_connection
from utils.utils import is_valid_address
from display import loging
from utils.utils import show_balance
from eth_account import Account
from config import config
from utils.utils import swap
from utils.utils import check_token_balance
from utils.utils import wait_until_next_day
from dotenv import load_dotenv
from display import appearance
import os

load_dotenv()

def main():
    
    print(appearance.ASCII_ART)
    print(appearance.CREDIT)
    
    PRIVATE_KEY = os.getenv("PRIVATE_KEY") 
    account = Account.from_key('0x' + PRIVATE_KEY)
    address = account.address
    web3 = Web3(Web3.HTTPProvider(config.RPC_URL))
    router = web3.eth.contract(address=config.ROUTER_ADDRESS, abi=config.ROUTER_ABI)
    
    loging.log_info(f"Account Address: {address}")

    if not check_connection(web3):
        return

    print("\n=== BALANCE CHECK ===")
    print("-" * 50)
    for token in config.GTE_TOKENS.keys():
        show_balance(address, web3, token=token)
    print("-" * 50)
    

    swap_type  = False
    while True:
            # Minta input dari user
            swap_method = input("Do you want to auto run swap automatically or once? (auto/once): ").strip().lower()

            # Cek apakah input adalah "auto" atau "once"
            if swap_method == "auto":
                swap_type = True
                break
            elif swap_method == "once":
                swap_type = False
                break
            else:
                loging.log_warning("❌ Invalid input. Please enter 'auto' or 'once'.")
                continue
                
    while True:
        try:
            swap_count = int(input("How much swapping do you want to do? : "))
            break  
        except ValueError:
            loging.log_warning("Invalid input. Please enter a number.")
            continue
        
    while True:
        try:
            swap_percent = float(input("How much percent do you want to swap? (1-100): "))
            swap_percent = swap_percent / 100
            break  
        except ValueError:
            loging.log_warning("Invalid input. Please enter a number.")
            continue
    
    
    while True:
        for i in range(swap_count):
            for item in config.GTE_TOKENS.keys():
                if item == "ETH":
                    continue
                else:
                    amt = check_token_balance(address, web3)
                    swap(web3, account, router, config.BASE_TOKEN, item, amt * swap_percent)
                    
            loging.log_info("Swap back to eth")
            
            for item in config.GTE_TOKENS.keys():
                if item == "ETH":
                    continue
                else:
                    amt = check_token_balance(address, web3, item)
                    swap(web3, account, router, item, config.BASE_TOKEN, amt )
                    
            loging.log_success(f"Swap {i+1} completed.")
                    
            loging.log_info("\n=== BALANCE CHECK ===")
            print("-" * 50)
            for token in config.GTE_TOKENS.keys():
                show_balance(address, web3, token=token)
            print("-" * 50)
            loging.log_info("Waiting for next swap...")
        if swap_type:
            loging.log_info("Waiting for next swap...")
            wait_until_next_day()
            continue
        else:
            loging.log_info("Swap completed.")
            break
        


    
if __name__ == "__main__":
    try:
        
        main()
    except KeyboardInterrupt:
        loging.log_warning("Program interrupted by user.")


