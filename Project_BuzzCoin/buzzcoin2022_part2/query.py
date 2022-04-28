from audioop import add
import web3, json, os, time
from eth_abi import encode_abi
from web3 import Web3, EthereumTesterProvider
from eth_account import Account

w3 = Web3(web3.HTTPProvider('http://143.215.130.235:8545'))

address = 0xD067b2D14db99AaA872f8B41378F3BE0E310Eb47
address_str = ('0xD067b2D14db99AaA872f8B41378F3BE0E310Eb47')
contract_addr = '0xF975EF8385D2Afa83C940e4fe4Fa14e10005E9C4'
abi = [{"inputs":[],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"payable":True,"stateMutability":"payable","type":"fallback"},{"constant":False,"inputs":[],"name":"KOTH_coup","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"KOTH_withdraw","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"coup_block","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"donate","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"duel1v1","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"duel_highroller","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"nonce","type":"uint256"}],"name":"guess_the_number","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"mayor_voting","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":True,"inputs":[],"name":"most_sent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"d","type":"uint256"}],"name":"pay_to_mine","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":True,"inputs":[],"name":"richest","outputs":[{"internalType":"address payable","name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"}]

greeter = w3.eth.contract(address=contract_addr,abi=abi)
nonce = w3.eth.get_transaction_count(address_str)
block_num = int(w3.eth.get_block('latest')['number'])
block_info = {}
with open('UTC--2022-03-06T02-25-09.339111541Z--d067b2d14db99aaa872f8b41378f3be0e310eb47') as keyfile:
    encrypted_key = keyfile.read()
    private_key = w3.eth.account.decrypt(encrypted_key, 'buzz')
# print ('block_num: %d' % block_num)
# print ('Nonce: %d' % nonce)
# print (greeter.all_functions())
#fwrite = open("record.txt", 'a')

def refresh_lastest_block(block_info):
    block_num = int(w3.eth.get_block('latest')['number'])
    block_info['block_num'] = block_num
    print ('block_num: %d' % block_num)
def restore_block_info(block_info, filename = "block_info.json"):
    block_info['count'] = 1
    if os.path.exists(filename):
        f = open(filename)
        block_info = json.load(f)
        f.close()
    block_info['block_num'] = int(w3.eth.get_block('latest')['number'])
    return block_info
def dump_block_info(block_info, filename = "block_info.json"):
    with open(filename, 'w') as json_file:
        json.dump(block_info, json_file, indent=4)

def update_block_info(block_info):
    update = False
    cur_block = block_info['count']
    refresh_lastest_block(block_info)
    while cur_block <= block_info['block_num']:
        update |= process_block(block_info, cur_block)
        cur_block += 1
    block_info['count'] = cur_block
    return update
def process_block(block_info, i):
    update = False
    if i % 1000 == 0:
        print (i)
    if 'duel_count' not in block_info:
        block_info['duel_count'] = 0
        block_info['last_duel_address'] = ""
        block_info['duelv2_count'] = 0
        block_info['last_duelv2_address'] = ""
    block = w3.eth.get_block(i)
    for tx in block['transactions']:
        update = True
        print (Web3.toHex(tx))
        tran = w3.eth.get_transaction(tx)
        input = tran['input']
        if (input == '0x9b831805'):
            block_info['duel_count'] += 1
            block_info['last_duel_address'] = tran['from']
            print ("duel: " + tran['from'] + ", " + str(tran['blockNumber']))
        if (input == '0x622cfe47'):
            block_info['duelv2_count'] += 1
            block_info['last_duelv2_address'] = tran['from']
            print ("duelv2: " + tran['from'] + ", " + str(tran['blockNumber']))
    return update
def make_transaction(txn):
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
    txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    return w3.eth.wait_for_transaction_receipt(txn_hash)
def get_account_balance():
    return w3.eth.get_balance(address_str) / (10**18)
def encode(msg):
    types = ['uint256'] * len(msg)
    abi_msg = encode_abi(types, msg)
    return Web3.keccak(abi_msg)
def guess_number():
    '''
        assert(gtm[msg.sender] <= 20);
        assert(msg.value == 1 ether);
        assert(nonce <= 100);
        uint256 temp = uint256(keccak256(abi.encode(msg.sender)));
        temp = uint256(keccak256(abi.encode(temp, block.number)));
        temp = uint256(keccak256(abi.encode(temp, temp)));
        temp = temp % 100;
        if (nonce == temp) {
            gtm[msg.sender]++;
            msg.sender.transfer(5 ether);
        }
    '''
    block_num = int(w3.eth.get_block('latest')['number'])
    nonce = w3.eth.get_transaction_count(address_str)

    temp = Web3.toInt(encode([address]))
    temp = Web3.toInt(encode([temp, block_num+1]))
    temp = Web3.toInt(encode([temp, temp]))
    temp = temp % 100
    print ('nonce: %d' % temp)
    transcation = {'value':w3.toWei(1, "ether"), "chainId": 9090, 'nonce': nonce, 'gas': 200000,'gasPrice': 1000000000}
    txn = greeter.functions.guess_the_number(temp).buildTransaction(transcation)
    make_transaction(txn)
    return temp
def duel1v1(p1):
    if p1.lower() == address_str.lower():
        print ("Last transaction is mine duel1v1")
        return 
    opponent = Web3.toInt(hexstr=p1)
    winner = Web3.toInt(encode([address, opponent])) % 2
   
    if winner == 0:
        print ("I will win duel1v1:" + str(p1))
        nonce = w3.eth.get_transaction_count(address_str)
        transcation = {'value':w3.toWei(1, "ether"), "chainId": 9090, 'nonce': nonce, 'gas': 200000,'gasPrice': 1000000000}
        txn = greeter.functions.duel1v1().buildTransaction(transcation)
        receipt = make_transaction(txn)
        return receipt
    else:
        print ("Duel exist, but I will lose duel1v1:" + str(p1))
        return 0
def duel_highroller(p1):
    if p1.lower() == address_str.lower():
        print ("Last transaction is mine")
        return 
    opponent = Web3.toInt(hexstr=p1)
    winner = Web3.toInt(encode([address, opponent])) % 2
    if winner == 0:
        print ("I will win duel_highroller: " + str(p1))
        nonce = w3.eth.get_transaction_count(address_str)
        transcation = {'value':w3.toWei(5, "ether"), "chainId": 9090, 'nonce': nonce, 'gas': 200000,'gasPrice': 1000000000}
        txn = greeter.functions.duel_highroller().buildTransaction(transcation)
        receipt = make_transaction(txn)
        return receipt
    else:
        print ("Duel_highroller exist, but I will lose duel_highroller:" + str(p1))
        return 0
def pay_to_mine(d):
    '''
        assert(d >= 32);
        assert(d > previous_max[msg.sender]);
        uint256 hash = uint256(keccak256(abi.encode(nonce,msg.sender)));
        uint mask = 1<<d;
        if (hash % mask == 0) {
            previous_max[msg.sender] = d;
            uint amt = 1<<(d-32);
            msg.sender.transfer(amt * 10 ** 18);
        }
    '''
    mask = 1 << d
    for n in range(1, 10**d):
        hash = Web3.toInt(encode([n, address]))
        if n % 10**8 == 0:
            print (n)
        if hash % mask == 0:
            print ("Find nonce: %d" % n)
            break
def listen_to_duel_request():
    while 1:
        if update_block_info(block_info):
            if block_info['duel_count'] % 2 == 1:
                receipt = duel1v1(block_info['last_duel_address'])
                if receipt:
                    with open('record.txt', 'a') as f:
                        f.write("DUEL with: " + block_info['last_duel_address'] + ", blockNumber: " + str(receipt['blockNumber'])+ "\n")
            if block_info['duelv2_count'] % 2 == 1:
                receipt = duel_highroller(block_info['last_duelv2_address'])
                if receipt:
                    with open('record.txt', 'a') as f:
                        f.write("DUEL_HIGH with: " + block_info['last_duelv2_address'] + ", blockNumber: " + str(receipt['blockNumber'])+ "\n")
            print("My balance: %.3f buzz" % get_account_balance())
            dump_block_info(block_info)
        time.sleep(10)
def listen_to_duel_v2():
    while 1:
        opponent = w3.toHex(w3.toInt(w3.eth.get_storage_at("0xF975EF8385D2Afa83C940e4fe4Fa14e10005E9C4", 99)))
        if opponent != 0 or opponent != "0x0":
            receipt = duel1v1(opponent)
            if receipt:
                print (receipt)
                with open('record.txt', 'a') as f:
                    f.write("DUEL with: " + opponent + ", blockNumber: " + str(receipt['blockNumber'])+ "\n")
        opponent = w3.toHex(w3.toInt(w3.eth.get_storage_at("0xF975EF8385D2Afa83C940e4fe4Fa14e10005E9C4", 101)))
        if opponent != 0 or opponent != "0x0":
            receipt = duel_highroller(opponent)
            if receipt:
                print (receipt)
                with open('record.txt', 'a') as f:
                        f.write("DUEL_HIGH with: " + opponent + ", blockNumber: " + str(receipt['blockNumber'])+ "\n")
        time.sleep(10)
def print_all_transaction():
    max_block = int(w3.eth.get_block('latest')['number'])
    for i in range(210900, max_block):
        block = w3.eth.get_block(i)
        for tx in block['transactions']:
            tran = w3.eth.get_transaction(tx)
            if tran['from'] == address_str:
                print (Web3.toHex(tx))
def find():
    f = open("cryptolab.gtisc.gatech.edu.html","r")
    lines = f.readlines()
    seen = set()
    for line in lines:
        if 'input' in line:
            seen.add(line.split(':')[1].split('"')[1][:10])
    print (seen)
def check_storage():
    p1 = "0xacda94a203ccd8d46538ce9caf3c0a4cd62d45bd"
    for i in range(250):
        opponent = w3.toHex(w3.toInt(w3.eth.get_storage_at("0xF975EF8385D2Afa83C940e4fe4Fa14e10005E9C4", i)))
        print (i, opponent)
        if (opponent.lower()) == p1.lower() or opponent.lower() == address_str.lower():
            print ("-------------------------------")
            print (i, opponent)

#pay_to_mine(32)
#for i in range(13):
#    guess_number()
#hash = Web3.toInt(encode([1, address]))
#print (hash)
#transcation = {'value':w3.toWei(0, "ether"), "chainId": 9090, 'nonce': nonce, 'gas': 200000,'gasPrice': 1000000000}
#txn = greeter.functions.mayor_voting().buildTransaction(transcation)
#print (txn)
print("My balance: %.3f buzz" % get_account_balance())
p1 = 0x9c638860cd0d60a0c5d12bd5dec0b4090938c8c5
winner = Web3.toInt(encode([address, p1])) % 2
#print (winner)
winner = Web3.toInt(encode([p1, address])) % 2
#print (winner)
#opponent = w3.toHex(w3.toInt(w3.eth.get_storage_at("0xF975EF8385D2Afa83C940e4fe4Fa14e10005E9C4", 101)))
#block_info = restore_block_info(block_info)

#listen_to_duel_v2()
#check_storage()
print_all_transaction()
'''
update_block_info(block_info)

listen_to_duel_request()

update_block_info(block_info)
dump_block_info(block_info)
'''
