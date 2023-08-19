import os

from alchemy_sdk_py import Alchemy

ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY")
CHAIN_ID = 1
MY_ADDRESS = "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9"  # Aave token on ETH Mainnet


def main():
    alchemy = Alchemy(network=CHAIN_ID)
    transfers = alchemy.get_asset_transfers(to_address=MY_ADDRESS)
    # this is a paginated version, we could add  `get_all_flag=True` but we'd make a LOT of API calls!
    print(transfers)


if __name__ == "__main__":
    main()
