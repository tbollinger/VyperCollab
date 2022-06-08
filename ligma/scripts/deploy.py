from brownie import Token, accounts

def main():
    acct = accounts.load('local')
    Token.deploy(acct, {'from': acct})