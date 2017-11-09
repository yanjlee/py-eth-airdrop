from web3 import *
import time

## Replace "example_file.txt" with file that contains 1 address per line
addressList = "example_file.txt"
addressListRead = open(path1, 'r', encoding='utf8')

## Must be running a local node that can connect via IPC e.g Geth
web3_obj = Web3(IPCProvider())

## Standard ERC20 ABI
ERC20_abi = [{"constant":False,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"anonymous":False,"inputs":[{"indexed":True,"name":"_from","type":"address"},{"indexed":True,"name":"_to","type":"address"},{"indexed":False,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},
            {"anonymous":False,"inputs":[{"indexed":True,"name":"_owner","type":"address"},{"indexed":True,"name":"_spender","type":"address"},{"indexed":False,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]


##Replace with the address of your contract
token_contract = web3_obj.eth.contract(abi=ERC20_abi, address="<token_contract_address>")
##Replace with the password of the default account for your local node
web3_obj.personal.unlockAccount(web3_obj.eth.accounts[0], '<password>')

##Replace with the amount of tokens you want to drop
airdrop_amount = 50

##Change this to the decimal value of the token
token_decimals = 5

count = 0

for address in addressListRead:
    if len(address) > 0:
        address = address.strip()
        amount_to_send = airdrop_amount*(10**token_decimals)
        if web3_obj.isAddress(address):
            print("TX: " + str(count) + " to: " + address + " returned TX Hash: " + sendTransaction(address, amount_to_send))
        else:                                                                                   
            print("Invalid wallet address provided: " + address)
    count += 1

def sendTransaction(address, amount_to_send):
    token_contract.transact({'from':web3_obj.eth.accounts[1], 'gasPrice': 1000000000}).transfer(address, amount_to_send)
