# MegaEth GTE Auto Swap Bot

## Overview
The **MegaEth GTE Auto Swap Bot** is a Python-based automation tool designed to interact with the MegaEth protocol on the MegaEth testnet. It automates back-and-forth token swaps between ETH and other configured tokens (e.g., GTE tokens) on a decentralized exchange (DEX). The bot supports one-time or daily automated swaps with customizable swap percentages and counts, performing swaps in both directions (e.g., GTE to ETH and ETH back to GTE) within each cycle. It includes balance monitoring and logging for transparency.

---

## Features
- **Back-and-Forth Swaps**: Automatically swaps tokens (e.g., GTE to ETH and back to GTE) in each cycle for configured tokens.
- **Balance Monitoring**: Displays real-time balances for ETH and configured tokens before and after swaps.
- **One-Time or Daily Automation**: Run swaps once or schedule daily execution (VPS required for automation).
- **Customizable Swap Parameters**: Set the number of swap cycles and percentage of token balance to swap via user input.
- **Single Wallet Support**: Operates with one Ethereum wallet on the MegaEth testnet.

---

## Prerequisites
Before setting up the bot, ensure you have the following:

- **Python 3.8+**: Required to run the bot.
- **pip**: Python package manager for installing dependencies.
- **Git**: For cloning the repository.
- **Ethereum Wallet**: A wallet with:
  - MegaEth testnet ETH for gas fees.
---

## Installation

### 1. Clone the Repository
Clone the project to your local machine:

```bash
git clone https://github.com/Aguh18/MegaEth_GTE_Auto_swap.git
cd MegaEth_GTE_Auto_swap
```

### 2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```



### 4. Configure Environment File
Create a `.env` file in the project root and add your wallet's private key:

```env
PRIVATE_KEY=your_private_key
```

- **PRIVATE_KEY**: Your Ethereum wallet's private key for the MegaEth testnet (without `0x` prefix). Example:
  ```env
  PRIVATE_KEY=abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
  ```
- **Warning**: Keep your `.env` file private and add it to `.gitignore` to prevent accidental exposure. To ensure this, create or update a `.gitignore` file with:
  ```gitignore
  .env
  ```
### 5. Acquire Testnet Funds

- **MegaEth ETH**:  
  Get testnet ETH from the [MegaETH Testnet Faucet](https://testnet.megaeth.com/) to cover gas fees.  
  Simply visit the site, enter your wallet address, and claim. You'll instantly receive **0.005 ETH per day**.

---

## Usage

### 1. Prepare Funds
Ensure your wallet has:
- Sufficient MegaEth testnet ETH for gas fees.
- GTE tokens or other configured tokens for swapping.

### 2. Start the Bot
Run the bot with:

```bash
python main.py
```

### 3. Interact with Prompts
- **Select Execution Mode**:
  - `once`: Run swaps once and exit.
  - `auto`: Run swaps daily (requires a VPS for continuous operation).
- **Set Swap Count**: Enter the number of swap cycles to perform.
- **Set Swap Percentage**: Specify the percentage of token balance to swap (1–100).

### 4. Bot Execution
The bot will:
- Display initial balances for ETH and configured tokens.
- For each cycle and each token (excluding ETH):
  - Swap a percentage of the token balance to ETH.
  - Swap the resulting ETH back to the original token (back-and-forth).
- Log transaction statuses and update balances after each cycle.
- Wait until the next day for automated mode (if selected).






## Security Notes
- **Protect Private Keys**: Never use mainnet wallets for testnet operations. Keep your private key secure.
- **Verify Contracts**: The bot uses preconfigured contract addresses. If you suspect issues, confirm addresses against official MegaEth sources.
- **Testnet Only**: This bot is designed for the MegaEth testnet. Do not adapt for mainnet without thorough review.
- **Review Code**: Inspect the code before running with sensitive data like private keys.

---


## Disclaimer
This bot is intended for educational and testing purposes on the MegaEth testnet. Use it at your own risk. The developers are not liable for any financial losses or issues arising from its use.

---

## License
MIT License


## Community

Join us on Telegram: [AutoDropz](https://t.me/+V_JQTTMVZVU3YTM9)
