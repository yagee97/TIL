# Transparent_donation
프론트엔드와 백엔드를 개발하여, 서로 연동한 후, 프론트엔드에서 계정을 생성하여 송금하는 방법
<br><br><br>
### 1. Geth 설치 경로 확인
> 사용자마다 geth 경로가 다를 수 있으므로, 본인의 geth 설치 경로를 파악해두어야 한다.
    
    $ which geth
    /usr/bin/geth

<br>

### 2. 사설망에서 geth 실행
> 사설망에서 geth를 실행하기 위해 **첫번째 블록**인 `genesis.json`을 만들어야 한다.
  위 geth의 경로에 `private_net`이라는 폴더를 생성한 후, 이곳에 `genesis.json`을 저장한다.

    $ cd /usr/bin/
    $ sudo mkdir private_net
    $ //genesis.json 파일생성 (gedit 또는 vim으로)

###### (genesis.json파일은 따로 첨부하지 않는다.)

<br>

### 3. geth 초기화
    
    $ geth --datadir /usr/bin/private_net/ init /usr/bin/private_net/genesis.json
    
<br>

### 4. geth console 실행

    $ sudo geth --networkid "10" --nodiscover --datadir /usr/bin/private_net --rpc --rpcaddr "localhost" 
    --rpcport "8545" --rpccorsdomain "*" --rpcapi "eth, net, web3, personal" --targetgaslimit "20000000"
    console2>> sudo /usr/bin/private_net/error.log
    
command line 실행 후, **Welcome to the Geth Javascript console!** 이라고 출력되면 성공이다.

<br>

### 5-1. 외부계정 주소 만들기

    > personal.newAccount("<비밀번호>")
    "0xf5------------------ (계정 주소)" -> 계정 주소가 생성된다.

> `personal.newAccount`를 두번 실행하여, 계정을 두개 만들었다.

<br>

### 5-2. 외부 계정 주소 확인

    > eth.accounts
    [ "계정1", "계정2" ]
    
    //index를 사용하여 계정 주소를 확인할 수도 있다.
    > eth.accounts[0]
    "계정1"
 
<br>

### 6. 코인 베이스 계정 주소 확인
> 코인 베이스 계정 주소는 블록을 생성하려고 채굴을 했을 때, 보상을 받는 계정 주소이다.

    > eth.coinbase
    "계정1" -> 기본적으로 0번 인덱스에 있는 계정이 coinbase로 등록 되어있다.
    
    //코인 베이스의 계정 주소를 변경할 수도 있다.
    > miner.setEtherbase(eth.accounts[1])
    true
    > eth.coinbase
    "계정2"

<br>

### 7. 채굴 시작

    > miner.start(1)
    null
    > eth.mining
    true

<br>

### 8. 코인 베이스 잔액 확인 (이더기준)

    > web3.fromWei(eth.getBalance(eth.account[0]),"ether")
    
<br>

### 9. 채굴 중지

    > miner.stop()
    true
    > eth.mining
    false
    
<br>

### 10. 프론트 엔드 실행

    $ cd ~/project
    $ node app.js

### 11. localhost:8080 접속
![default](https://user-images.githubusercontent.com/19389288/48009120-5b50d680-e15e-11e8-851f-b455a4df46a3.PNG)

### 12. 송금
**Generate New Seed** 버튼 클릭하여 새로운 seed를 받는다. 또한, 새로 생성할 계정의 개수도 적는다.

> From에 이미 ether를 가지고 있는 계정을 적고, to에 ether를 받을 계정을 적는다. 
이 때, 새로 생성된 계정을 사용해서 적어도 되지만, from에 적힐 계정에는 이미 ether가 들어있는 상태여야 한다.

> terminal의 geth console 에서 새로 생성된 계정하나를 `coinbase` 로 지정한 후, `mining` 을 하여 ether를 얻을 수 있다.

> from과 to에 알맞은 계정을 적은 후, **Send Ether** 버튼을 누르면, 
위의 하늘색 박스에 `transaction hash` 값이 나타난다. 이 값을 가지고 다시 geth console로 돌아간 후,
`mining`을 시켜 이 거래에 대한 블록을 생성한 후, `eth.getTransaction("transaction hash")` 를 하면, 거래가 성사되어 있는 것을 확인할 수 있다.

eth.getTransaction의 결과값에 blockNumber가 null 이라면, 그 거래는 성사되지 않았다는 것을 뜻한다.

    $ miner.start(1)
    null
    $ eth.mining
    true
    $ eth.getTransaction("transaction hash")

<br>

### 13. 송금 완료 확인

    $  web3.fromWei(eth.getBalance( "from계정" ),"ether")
    $  web3.fromWei(eth.getBalance( "to계정" ),"ether")
    
송금 이벤트가 발생하기 전과 후의 ether 수를 비교하여, 송금이 완료되었는지 알 수 있다.


    

