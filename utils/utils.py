from web3 import Web3
from config import config
from display import loging
import time
import random
from datetime import datetime, timedelta


def wait_until_next_day():
    now = datetime.now()

    # Random waktu antara jam 14:00 sampai 17:00
    random_hour = random.randint(14, 17)
    random_minute = random.randint(0, 59)
    random_second = random.randint(0, 59)

    next_run_time = datetime(now.year, now.month, now.day, random_hour, random_minute, random_second)

    # Cek apakah waktu sekarang > next_run_time atau selisihnya < 8 jam
    if now > next_run_time or (next_run_time - now).total_seconds() < 8 * 60 * 60:
        next_run_time += timedelta(days=1)

    # Log jadwal berikutnya menggunakan f-string
    loging.log_info(f"Next run scheduled at {next_run_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    while True:
        now = datetime.now()
        time_remaining = next_run_time - now

        if time_remaining.total_seconds() <= 0:
            break

        # Tampilkan countdown menggunakan print karena logging tidak mendukung end='\r'
        countdown = str(time_remaining).split('.')[0]
        print(f"Countdown: {countdown}", end='\r')
        time.sleep(1)

    # Newline dan pesan sukses menggunakan logging
    print
    loging.log_info(f"('It is now time to run the next transaction!'")

def check_connection(web3):
    try:
        # Check if connected
        if web3.is_connected():
            loging.log_success("Connected to MegaETH node")
            return True
        else:
            loging.log_error("Failed to connect to MegaETH node")
            return False
    except Exception as e:
        loging.log_error(f"Error checking connection: {e}")
        return False

def is_valid_address(address):
    return Web3.is_checksum_address(address)
import logging

def check_token_balance(address, web3, token=None):
    try:
        if not web3.is_address(address):
            raise ValueError("Invalid Ethereum address")

        address = web3.to_checksum_address(address)

        if token:
            token_data = config.GTE_TOKENS.get(token)
         
            if not token_data:
                raise ValueError(f"Token '{token}' not found in config")

            token_contract = web3.eth.contract(address=web3.to_checksum_address(token_data["address"]), abi=config.ERC20_ABI)
            raw_balance = token_contract.functions.balanceOf(address).call()
            decimals = token_data.get("decimals", 18)
            balance = raw_balance / 10**decimals
            return balance
        
        decimals= config.GTE_TOKENS["ETH"]["decimals"]
        raw_eth_balance = web3.eth.get_balance(address)
        eth_balance = raw_eth_balance / 10**decimals
        return eth_balance

    except Exception as e:
        logging.error(f"Error checking balance: {e}")
        return None

    
def show_balance(address, web3, token=None):
    if token and token != "ETH":
        balance = check_token_balance(address, web3, token)
        if balance is not None:
            loging.log_info(f"{token} Balance: {balance:.18f} {token}")
           
    else:
        balance = check_token_balance(address, web3)
        loging.log_info(f"ETH Balance: {balance:.18f} ETH".rstrip('0').rstrip('.'))
        


def approve(web3, account, token_address, amount):
    contract = web3.eth.contract(address=Web3.to_checksum_address(token_address), abi=config.ERC20_ABI)
    tx = contract.functions.approve(config.ROUTER_ADDRESS, amount).build_transaction({
        'from': account.address,
        'nonce': web3.eth.get_transaction_count(account.address),
        'gas': 100000,
        'gasPrice': int(web3.eth.gas_price * 1.2)
    })
    signed = account.sign_transaction(tx)
    tx_hash = web3.eth.send_raw_transaction(signed.raw_transaction)
    web3.eth.wait_for_transaction_receipt(tx_hash)

def swap(web3, account, router, token_in, token_out, amount_decimal):
    token_in_data = config.GTE_TOKENS[token_in]
    token_out_data = config.GTE_TOKENS[token_out]
    deadline = int(time.time()) + 1800
    amount_in = int(amount_decimal * (10 ** token_in_data["decimals"]))
    amount_out_min = 0
    
    max_retries = 3
    retry_count = 0
    while retry_count < max_retries:
        try:
            nonce = web3.eth.get_transaction_count(account.address, 'pending')
            if retry_count > 0:
                nonce += 1

            if token_in == config.BASE_TOKEN:
                path = [
                    Web3.to_checksum_address(config.GTE_TOKENS["WETH"]["address"]),
                    Web3.to_checksum_address(token_out_data["address"])
                ]
                tx = router.functions.swapExactETHForTokens(
                    amount_out_min,
                    path,
                    account.address,
                    deadline
                ).build_transaction({
                    'from': account.address,
                    'value': amount_in,
                    'gas': 300000,
                    'gasPrice': int(web3.eth.gas_price * 1.2),
                    'nonce': nonce
                })
            elif token_out == config.BASE_TOKEN:
                approve(web3, account, token_in_data["address"], amount_in)
                path = [
                    Web3.to_checksum_address(token_in_data["address"]),
                    Web3.to_checksum_address(config.GTE_TOKENS["WETH"]["address"])
                ]
                tx = router.functions.swapExactTokensForETH(
                    amount_in,
                    amount_out_min,
                    path,
                    account.address,
                    deadline
                ).build_transaction({
                    'from': account.address,
                    'gas': 300000,
                    'gasPrice': int(web3.eth.gas_price * 1.2),
                    'nonce': nonce
                })
            else:
                approve(web3, account, token_in_data["address"], amount_in)
                path = [
                    Web3.to_checksum_address(token_in_data["address"]),
                    Web3.to_checksum_address(config.GTE_TOKENS["WETH"]["address"]),
                    Web3.to_checksum_address(token_out_data["address"])
                ]
                tx = router.functions.swapExactTokensForTokens(
                    amount_in,
                    amount_out_min,
                    path,
                    account.address,
                    deadline
                ).build_transaction({
                    'from': account.address,
                    'gas': 300000,
                    'gasPrice': int(web3.eth.gas_price * 1.2),
                    'nonce': nonce
                })

            signed = account.sign_transaction(tx)
            tx_hash = web3.eth.send_raw_transaction(signed.raw_transaction)
            loging.log_debug(f"[→] SWAP {token_in} → {token_out} = {amount_decimal:.6f} {token_in}")
            receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
            return receipt
        except Exception as e:
            if "nonce too low" in str(e).lower() or "already known" in str(e).lower():
                retry_count += 1
                time.sleep(2)
                
                continue
            loging.log_error(f"[!] Error: {str(e)}")
            raise e
    
    raise Exception("Max retries exceeded for transaction")
        


    
