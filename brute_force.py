import os

from web3 import Web3

START_BLOCK = 17950195
END_BLOCK = 17950197

MY_ADDRESS = "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9"  # Aave token on ETH Mainnet


def main():
    w3 = Web3(Web3.HTTPProvider(os.getenv("RPC_URL")))
    for block in range(START_BLOCK, END_BLOCK):
        block = w3.eth.get_block(block, full_transactions=True)
        for transaction in block.transactions:
            if MY_ADDRESS in transaction["from"] or MY_ADDRESS in transaction["to"]:
                print(transaction)


if __name__ == "__main__":
    main()
