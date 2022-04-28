import web3
from web3 import Web3, eth
from eth_abi import encode_abi

w3 = Web3(web3.HTTPProvider('http://143.215.130.235:8545'))
address = 0xD067b2D14db99AaA872f8B41378F3BE0E310Eb47
address_str = '0xD067b2D14db99AaA872f8B41378F3BE0E310Eb47'
abi = [{"inputs":[],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"payable":True,"stateMutability":"payable","type":"fallback"},{"constant":False,"inputs":[],"name":"donate","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":True,"inputs":[],"name":"logmask","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"mask","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"problem1","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"nonce","type":"uint256"}],"name":"problem2","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"problem3","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[],"name":"problem4","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":False,"inputs":[{"internalType":"uint256","name":"nonce","type":"uint256"}],"name":"problem5","outputs":[],"payable":True,"stateMutability":"payable","type":"function"}]
def encode(types, msg):
    abi_msg = encode_abi(types, msg)
    return Web3.keccak(abi_msg)
def p2(mask, log_mask):
    '''
    uint256 hash = uint256(keccak256(abi.encode(nonce,msg.sender)));
        uint256 temp = hash % mask;
        if(temp == 0) {
            msg.sender.transfer(30 ether);
            p2[msg.sender] = true;
            if(logmask < 35) {
                mask = mask<<1;
                logmask += 1;
            }
        }
    '''
    for nonce in range(100000000):
        
        hashbyte = encode(['uint256','uint256'], [nonce, address])
        hash = int(hashbyte.hex() ,16)
        temp = hash % mask
        if temp == 0:
            print (nonce)
            break
        if nonce % 50000 == 0:
            print ('try:' + str(nonce))
#p2(34359738368,35)
def p3():
    '''
    function problem3() external payable {
        assert(block.number != last_block[msg.sender]);
        uint dice = uint(keccak256(abi.encode(msg.sender,block.number,now))) %6;
        last_block[msg.sender] = block.number;
        if(dice == 0){
            msg.sender.transfer(10 ether);
            p3[msg.sender] = true;
        }
    }
    '''
def p5():
    '''
        uint256 hash = uint256(keccak256(abi.encode(nonce)));
        uint256 doggy = 0x1C0139BB37A6598130C27861C8E8EB3EFB094D0962C0DCB2C31710B3A04F0CFE;
        if(hash == doggy){
            msg.sender.transfer(30 ether);
            p5[msg.sender] = true;
        }
    '''
    doggy = 0x1C0139BB37A6598130C27861C8E8EB3EFB094D0962C0DCB2C31710B3A04F0CFE
    nonce = 201695
    for nonce in range(2**200):
        hashbyte = encode(['uint256'], [nonce])
        hash = hashbyte.hex()
        if nonce % 50000 == 0:
            print ('try:' + str(nonce))
        if hash == doggy:
            print (nonce)
            break
def find():
    f = open("cryptolab.gtisc.gatech.edu.html","r")
    lines = f.readlines()
    seen = set()
    for line in lines:
        if 'input' in line:
            seen.add(line.split(':')[1].split('"')[1][:10])
    print (seen)
find()
#print (encode(['uint256'], [0x68747470733a2f2f6c616468612e6d652f612e706e670a]).hex())
#counter = w3.eth.contract(address=address_str, abi=abi)
#print (counter.getBlock())
#print (counter.functions.__dict__)