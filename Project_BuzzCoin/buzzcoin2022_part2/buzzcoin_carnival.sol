pragma solidity >= 0.5.0 < 0.6.0;

/*
 ________  ___  ___  ________  ________  ________  ________  ___  ________      
|\   __  \|\  \|\  \|\_____  \|\_____  \|\   ____\|\   __  \|\  \|\   ___  \    
\ \  \|\ /\ \  \\\  \\|___/  /|\|___/  /\ \  \___|\ \  \|\  \ \  \ \  \\ \  \   
 \ \   __  \ \  \\\  \   /  / /    /  / /\ \  \    \ \  \\\  \ \  \ \  \\ \  \  
  \ \  \|\  \ \  \\\  \ /  /_/__  /  /_/__\ \  \____\ \  \\\  \ \  \ \  \\ \  \ 
   \ \_______\ \_______\\________\\________\ \_______\ \_______\ \__\ \__\\ \__\
    \|_______|\|_______|\|_______|\|_______|\|_______|\|_______|\|__|\|__| \|__|
________  ________  ________  ________   ___  ___      ___ ________  ___          
|\   ____\|\   __  \|\   __  \|\   ___  \|\  \|\  \    /  /|\   __  \|\  \         
\ \  \___|\ \  \|\  \ \  \|\  \ \  \\ \  \ \  \ \  \  /  / | \  \|\  \ \  \        
 \ \  \    \ \   __  \ \   _  _\ \  \\ \  \ \  \ \  \/  / / \ \   __  \ \  \       
  \ \  \____\ \  \ \  \ \  \\  \\ \  \\ \  \ \  \ \    / /   \ \  \ \  \ \  \____  
   \ \_______\ \__\ \__\ \__\\ _\\ \__\\ \__\ \__\ \__/ /     \ \__\ \__\ \_______\
    \|_______|\|__|\|__|\|__|\|__|\|__| \|__|\|__|\|__|/       \|__|\|__|\|_______|
                                                                                                                                                                   
*/

contract Buzzcoin {
    mapping (address => bool) private perm;
    address[95] private users;
    address owner;
    function () external payable {}
    function donate() external payable {}
    constructor() public{
        owner = msg.sender;
        users = [0xF796Ed91E8077e46b0D7F4e753730Eb944b49C34,0xa2381530922EBeA1d9cA903e69e9c39488939e0d,0x0d5505d1f34D94E466ed75c2A889b0B2f9a58001,0x050279A9Cfb2db2738dC2DB92f532265694ae022,0xae283e6C4020d7a9759da9ccd910f0B5aF60454a,0x108261789D8FcB5E7b91dE56f4391b0C7Ea9a756,0xDd6d3e2a2B5A050a06c4a0494e5F1401a66594B1,0xE6864A2B2352Ee57D51F157D1ea3377340b961bc,0xec8a3A132D69F286C60ba0f9F2ab0c50F7CB45d1,0xb60646aCc01C742544f43339d03D759bf8a6050f,0xaa4B4A21B447120b25b8D8627C67bbE16dcD2297,0x5E23Ad055A17184B71be7460389eA5EB27429237,0xEc3A1AFa53bF6b58e7F52129A68860551aFdec85,0x5Eafc7DcC8dbDA41EB405FB1E544Cb3027aaAF8b,0xf2186f4f2798a9c1b0c269d1f39B7600A1c2F27F,0x12Af2fbeB51183fCEe7b03E0D4885b7567ef8cA9,0x15aBd174867c0355075c2c26AE44F5e58469E5B5,0x61446015D70a78769fa3B37c48A4Ad9BF93b97F0,0x1CF6b379b2411d26c0caEF2BD68DC3c23D9C464F,0x29cb9Afe61d928d887682a6DBe30652b51F20C5a,0x8b8899f0163bb40C05737D45DE75f9CB36B0979f,0x1BB706288028FA8Cc623cAf16dDAc85eA84E430E,0x47D803F9f48888702Be306DD6E287c2302CC1A05,0xf32fa30e2bfC68D83633388Bf4b2550250376Df9,0x02824BDDF2D999368Ab5FE5bE7B284c056ea56Df,0x28B058081F308d0148404b66c49267EadfBdDB97,0x9939c2eDEfFc9352a58F3039770D2c3Ec4C9cF3e,0x2E6794056531610bAB2185bf5af625eA035BAFB7,0x83072Bc42F85e401DDB0d7798072D2C3Af5805a4,0xc28a56C1C6dd3Dd19E7911Fb8a1d9795C585b805,0xCb067A62eDc7EB0daE6c739BbCC96dF1A74a9EFc,0x8024012343B12F6a17089480C602612B60E54448,0x854E642690033A65478f2FF95dc123f37D2d3508,0x37fD455819737AC867D3474B06E197a32c84269e,0xfD0B2Bf664EfB799Df77935eF1539a3981DA6829,0x7Faeafa67dDd99CE4e31f3DD75C88852AcA4acde,0xd13197025053171d22375e3aF70B94C51a9148db,0xf60A00204bD0076c1c30d00B418004C3B1c4F369,0xBe12E6dC89811111fcbC2f272c4dEE1418c2741B,0x67f287606E1366B629ce364C461a1e69a9080CF2,0xb2300D0f86AA0a01c8dEbF077d63b0Ca4aC9F935,0xaCDA94A203cCD8D46538CE9cAf3C0a4CD62d45BD,0x0D5E4A5838FC2B0166c62FF442B7531877b100AD,0xAF0aE19C8b2E5364e1B62Cc017c91F38B2ab1131,0xe1a92eCeD9cfbbB928584499aE1dC2792009C3D3,0xD067b2D14db99AaA872f8B41378F3BE0E310Eb47,0x4a7f19e95861Cbd05102c1Fa45d40b28F88319Ac,0x25cd92916A913f0722E29Aa354291c8D266e2C3B,0x07E79c68d0De37593b6eD4d5b134182E5E7611B6,0x7C30a9612005F1cC204Cc0E34d09A1171cc50D23,0x83393dc26Bc5207b9ce0482EdFe81032c05a11B2,0x5711AA72Ec6715C04240d66b1E6bfe022770901D,0x75D51B3a0639664E459DEF567596AF0738c8f521,0xb38305C0a605e746940A7f4F9e24CCF8C5F1c953,0xA5eFfF5891e4A54E45845cAA528655f110639674,0x93322E31a8340862a3c5018fC5816eEF519518D4,0xf7f74d8735536C45B202a3aF7b7f0FeF2a63315A,0x17b07139CcaB6011Fe76FDfb7855044BF883f3d8,0xB7e43Ec0b024a896932A46029466b101c4A0f4D4,0xe7aD9543A4324231Ee9e106dce3e7c5d839E7881,0x8d8F7f8740465Df9d53F1F8B567B3DcAf2CED86d,0x85FCF8cfB9be90d29d8ffD04f0Ac5ACA25e3cbEc,0x4112F49a6684195e57c831199FC3F0de59941747,0x4C659664c2ec0d3C933752Ab07d52e2Cc810026f,0xc633E3dc80fF7297509617EE3b064eeB80232320,0xa112fFF5EAE14A3593A18161441c0Af729b4fC6C,0xa1519EB0945B6Ba793F211b39Eaf6f43d9566F5C,0x2F2c50aB1874778E7B445A0fcCcF155A994C9CAc,0x57dd6A825DF69593337583cb4302DEBc9837727b,0xddC012A4a24A4aaD3CA20148AbB2cA196Da98869,0x4C4E82D2e1AC67B7e31EFC57Edb95CC1a2267C17,0xAA4CE52685E0d0617E31b1072b04BbB4E910b09C,0x65597Bf80563fC53c0Cbe61fAe697C393179feAe,0xeeE3A917842CBf10662B9C8692A8b73B60696aD2,0x2308AD6a4ECE67269062D197A313d4Afd9B7E8df,0x4752778f53566953853942E93332b9a0abae9Ed3,0x3886d352a6659C38DB807f4542726D263AF33c43,0x82869bA6F714EEA1Fad1708f281485000c7A9A14,0xc32566929AEf004C6f40c158203Ce498cdA3EEbd,0x4ce89E352CBf2F1D6Ccc2224E4Ba4faC9369cF16,0x91F3468D48c65650832Fd87c082225E675C36891,0x24Cd97f3D6B0602E8b39B22F0385a5bA545D44c5,0x437df6e889119Ac8C4a36E671aFDaA23Fe4Bc238,0xe2a2a000204a9dc01D83eF6BDec5C6f93540d778,0x61c5f05e62996FfCb1F65C6687346F7C56056Cc7,0x89127D8895655A649F52536F64a6bB4C570497BB,0x866A6b06c366fAb984eA88ADA77182C7589c13B5,0x383A6D32a857f333151ABDac4611F45a1d214de7,0x9C638860cd0D60A0C5d12Bd5dEC0B4090938C8C5,0xFfC700D98f75a6612De3B4FF731b16e50F726D02,0x4924C5646E5b42Ce1A1CC0Ef680a814473d992f8,0xefe02d3a350286Ed3672572Bd1574907e97902C5,0x41fAb123F143F5477A2edf68f8892D84143665F6,0xD270129a3884e3785213aFf5C12CF0A75773A7D3,0xe751B2bE388b046f0cC03407B8c70C79Ffe91211];
        for(uint i = 0; i < users.length; i++){
            perm[users[i]] = true;
        }
    }

/*
"Ho ho ho wizard noises. If you can guess the number, you win a prize <|:)"
            ,    _
           /|   | |
         _/_\_  >_<
        .-\-/.   |
       /  | | \_ |
       \ \| |\__(/
       /(`---')  |
      / /     \  |
   _.'  \'-'  /  |
   `----'`=-='   '

*/
    mapping (address => uint) gtm;
    function guess_the_number(uint nonce) external payable {
        assert(perm[msg.sender]);
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

    }


/*
Maim your friends

     o      _o
    <|\,/ /` |>
 ___/_>_____<_\___

*/
    mapping (address => uint) duel;
    address payable private p1;
    uint256 private dplays;
    function duel1v1() external payable {
        assert(perm[msg.sender]);
        assert(duel[msg.sender] <= 30);
        assert(msg.value == 1 ether);
        assert(p1 != msg.sender);
        duel[msg.sender]++;
        if(dplays == 0){
            p1 = msg.sender;
            dplays = 1;
        }
        else {
            uint winner =  uint256(keccak256(abi.encode(msg.sender,p1))) %2;
            if(winner == 0){
                msg.sender.transfer(5 ether);
            }
            else {
                p1.transfer(6 ether);
            }
            delete dplays;
            delete p1;
        }
    }


/*
higher stakes :OOO !!

           \ /
       |_O  X  O_\
        /`-/ \-'\
       | \     / |
______/___\____|_\____

*/
    address payable private p1h;
    uint256 dhplays;
    function duel_highroller() external payable {
        assert(perm[msg.sender]);
        assert(duel[msg.sender] <= 30);
        assert(msg.value == 5 ether);
        assert(p1h != msg.sender);
        duel[msg.sender]++;
        if(dhplays == 0){
            p1h = msg.sender;
            dhplays = 1;
        }
        else {
            uint winner =  uint256(keccak256(abi.encode(msg.sender,p1h))) %2;
            if(winner == 0){
                msg.sender.transfer(10 ether);
            }
            else {
                p1h.transfer(12 ether);
            }
            delete dhplays;
            delete p1h;
        }
    }



/*
I will pay you to mine. The faster you can mine, the more you get paid. 
Your speedups will not really come from hardware, but from implmentation
How much faster would this be in a systems language like C++ or Rust? 
What about a GPU solution? Pay off is exponential.

                             ___
                     /======/
            ____    //      \___       ,/
             | \\  //           :,   ./
     |_______|__|_//            ;:; /
    _L_____________\o           ;;;/
____(CCCCCCCCCCCCCC)____________-/_____________

*/
    mapping (address => uint256) previous_max;
     
    function pay_to_mine(uint nonce, uint d) external payable {
        assert(msg.value == 1 ether);
        assert(d >= 32);
        assert(d > previous_max[msg.sender]);
        uint256 hash = uint256(keccak256(abi.encode(nonce,msg.sender)));
        uint mask = 1<<d;
        if (hash % mask == 0) {
            previous_max[msg.sender] = d;
            uint amt = 1<<(d-32);
            msg.sender.transfer(amt * 10 ** 18);
        }
    }



/*
King of the Hill. Coup the current king by paying them off 
                 
                 |ZZzzz
                 |
                 |
    |ZZzzz      /^\            |ZZzzz
    |          |~~~|           |
    |        |^^^^^^^|        / \
   /^\       |[]+    |       |~~~|
|^^^^^^^|    |    +[]|       |   |
|    +[]|/\/\/\/\^/\/\/\/\/|^^^^^^^|
|+[]+   |~~~~~~~~~~~~~~~~~~|    +[]|
|       |  []   /^\   []   |+[]+   |
|   +[]+|  []  || ||  []   |   +[]+|
|[]+    |      || ||       |[]+    |
|_______|------------------|_______|

*/
    address payable public richest;
    uint256 public most_sent;
    uint256 public coup_block;
    mapping (address => uint256) pending_withdrawals;

    function KOTH_coup() public payable returns (bool) {
        if (msg.value > most_sent) {
            if(coup_block == 0){
                coup_block = block.number;
            }
            pending_withdrawals[richest] += msg.value;
            uint amount = block.number - coup_block;
            amount = amount>>3;
            amount = amount;
            richest.transfer(amount * (1 ether));
            richest = msg.sender;
            coup_block = block.number;
            most_sent = msg.value;
            return true;
        } else {
            return false;
        }
    }
    function KOTH_withdraw() public {
        uint256 amt = pending_withdrawals[msg.sender];
        pending_withdrawals[msg.sender] = 0;
        msg.sender.transfer(amt);
    }


 
/*
https://www.vice.com/en/article/4agdwg/pete-buttigieg-would-really-like-you-to-forget-about-that-wine-cavei
         __             _,-"~^"-.
       _// )      _,-"~`         `.
     ." ( /`"-,-"`                 ;
    / 6                             ;
   /           ,             ,-"     ;
  (,__.--.      \           /        ;
   //'   /`-.\   |          |        `._________
     _.-'_/`  )  )--...,,,___\     \-----------,)
   ((("~` _.-'.-'           __`-.   )         //
         ((("`             (((---~"`         //
                                            ((________________
                                            `----""""~~~~^^^```
*/
    uint256 private plays = 0;
    uint256 private total = 0;
    uint256[101] private counter;
    address payable[101] private identity;
    address payable[5] private already_played;

    mapping (address => uint) mayor;

    function mayor_voting() external payable {
        if(msg.value  % (1 ether) != 0 || msg.value == 0 || msg.value > (100 ether)){
            revert();
        }
        assert(perm[msg.sender]);
        assert(mayor[msg.sender] <= 30);
        uint256 val = msg.value / (1 ether);

        for(uint i = 0; i < 5; i++){
            if(already_played[i] == msg.sender) {
                revert();
            }
        }

        mayor[msg.sender]++;
        already_played[plays] = msg.sender;
        plays++;
        counter[val]++;
        identity[val] = msg.sender;
        total += msg.value;

        if (plays == 5) {
            bool paid = false;
            for (uint i = 0; i < 101; i++) {
                if(counter[i] == 1 && !paid){
                    identity[i].transfer(total + (5 ether));
                    paid = true;
                }
                delete counter[i];
                delete identity[i];
            }
            plays = 0;
            total = 0;

            for (uint i = 0; i < 5; i++)
                delete already_played[i];
        }
    }
}
