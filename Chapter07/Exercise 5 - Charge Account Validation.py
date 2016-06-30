__author__ = 'ccarp_000'
#reads file into a list
#enter charge account number
# destermine whether valid by searching it in list
#if number is valid give valid message if invalid give invalid mesage

def main():
    infile = open('charge_accounts.txt', 'r')
    charge_accounts = infile.readlines()
    infile.close()
    print(charge_accounts)

main()