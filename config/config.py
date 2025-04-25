from web3 import Web3

RPC_URL='https://carrot.megaeth.com/rpc'
ROUTER_ADDRESS = Web3.to_checksum_address("0xa6b579684e943f7d00d616a48cf99b5147fc57a5")
BASE_TOKEN = "ETH"

ERC20_ABI = '[{"constant":true,"inputs":[{"name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"amount","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"type":"function"}]'

ROUTER_ABI = '[{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"}]'

GTE_TOKENS = {
    "MegaETH": {"address": Web3.to_checksum_address("0x10a6be7d23989D00d528E68cF8051d095f741145"), "decimals": 18},
    "WETH": {"address": Web3.to_checksum_address("0x776401b9BC8aAe31A685731B7147D4445fD9FB19"), "decimals": 18},
    "GTE": {"address": Web3.to_checksum_address("0x9629684df53db9E4484697D0a50C442B2BFa80A8"), "decimals": 18},
    "USDC": {"address": Web3.to_checksum_address("0x8D635C4702bA38B1f1735E8e784C7265dcc0B623"), "decimals": 6},
    "tkUSDC": {"address": Web3.to_checksum_address("0xfAf334E157175fF676911aDcF0964D7f54F2c424"), "decimals": 6},
    "Kimchizuki": {"address": Web3.to_checksum_address("0xA626F15D10F2b30AF1fb0d017F20a579500B5029"), "decimals": 18},
    "five": {"address": Web3.to_checksum_address("0xF512886BC6877B0740E8Ca0B3c12bb4cA602B530"), "decimals": 18},
    "gte pepe": {"address": Web3.to_checksum_address("0xBBA08CF5ECE0cC21e1DEB5168746c001B123A756"), "decimals": 18},
    "Enzo": {"address": Web3.to_checksum_address("0x9cd3a7b840464d83bee643bc9064d246375b07a3"), "decimals": 18},
    "Nazdaq": {"address": Web3.to_checksum_address("0xd0ed4c2af51bb08c58a808b9b407508261a87f25"), "decimals": 18},
    "Toast": {"address": Web3.to_checksum_address("0xc49ae2a62e7c18b7ddcab67617a63bf5182b08de"), "decimals": 18},
    "Fast": {"address": Web3.to_checksum_address("0xca6d9311918a89cb57b2b399314e2facccc98ca4"), "decimals": 18},
    "ETH": {"address": None, "decimals": 18},
}