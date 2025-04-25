from colorama import Fore, Style

def log_info(message):
    print(f"{Fore.CYAN}{Style.NORMAL}[INFO] {message}{Style.RESET_ALL}")

def log_success(message):
    print(f"{Fore.GREEN}{Style.NORMAL}[SUCCESS] {message}{Style.RESET_ALL}")

def log_warning(message):
    print(f"{Fore.YELLOW}{Style.NORMAL}[WARNING] {message}{Style.RESET_ALL}")

def log_error(message):
    print(f"{Fore.RED}{Style.NORMAL}[ERROR] {message}{Style.RESET_ALL}")

def log_debug(message):
    print(f"{Fore.MAGENTA}{Style.NORMAL}[DEBUG] {message}{Style.RESET_ALL}")
