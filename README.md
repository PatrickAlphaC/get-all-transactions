# Get all transactions from an address

We look at some techniques to get all transactions from an address, as well as get certain events. You can read my full blog on this here.

# Getting Started

## Requirements 

- [Python](https://www.python.org/downloads/) 3.7 or higher
    - You'll know you've done it right if you can run `python3 --version` in your terminal and see something like `Python 3.10.6`

## Installation

```bash
git clone https://github.com/PatrickAlphaC/get-all-transactions 
cd get-all-transactions
pip install -r requirements.txt
```

To use the `alchemy` prefixed scripts, you'll need to set the `ALCHEMY_API_KEY` environment variable to your Alchemy API key.  

For using any other python script, you'll need an `RPC_URL` environment variable set to your RPC URL.

## Use

```
python3 alchemy_get_events.py
```

Or call any other python script. Feel free to edit the scripts for your needs. 
