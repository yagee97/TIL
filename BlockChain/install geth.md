# Install geth
우분투 환경에서 geth를 설치하는 방법 정리

### 1. git 설치

    $ sudo apt-get install git

### 2. ethereum 설치

    $ git clone https://github.com/ethereum/go-ethereum.git
    
### 3. Go & C compiler install

    $ sudo apt-get install -y bulid-essential libgmp3-dev golang git tree

### 4. cd go-ethereum
go-ethereum 디렉토리로 이동
   
    $ make geth
    
### 5. geth version check

    $ /build/bin/geth version
    
### 6. geth copy(location : go-ethereum)
  
    $ sudo cp build/bin/geth /usr/local/bin/
    
### 7. path setting check

    $ which geth
    
/usr/local/bin/geth

<br>
-----------------------------<br>


위 방법대로 geth를 설치한 후, geth를 구동하여 사용할 수 있다.<br>

**geth 구동과 사용법**  보러가기 => https://github.com/yagee97/TIL/blob/master/BlockChain/transaction.md
