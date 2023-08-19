import os

from alchemy_sdk_py import Alchemy

ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY")
CHAIN_ID = 1
MY_ADDRESS = "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9"  # Aave token on ETH Mainnet


def main():
    alchemy = Alchemy(network=CHAIN_ID)
    upgraded_events = alchemy.get_logs(
        contract_address=MY_ADDRESS,
        topics=["0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b"],
    )
    print(upgraded_events)


if __name__ == "__main__":
    main()
