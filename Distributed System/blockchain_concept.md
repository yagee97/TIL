## Mining
block chian 개념에 대해 다룹니다.

<br>

## 첫번째 블록(genesis block)
block chain의 각 block들은 <code>contents</code>와 <code>nonce</code>를 가지고 있다.
> - **contents** 에는 의미있는 무언가(거래정보 등) 같은 다양한 값이 들어간다.
> - **nonce** 는 임의의 값인데, 작업증명 (POW)을 하기 위해 존재하는 값이다.
> **nonce** 는 32bit로 구성되어 있다.
<br>

**block이 되기 위한 조건** 은 hash function에 block의 <code>contents</code> 와 <code>nonce</code> 를 더해서 만든 값을 넣고 돌렸을 때 
<br> 나온 hash 값의 **앞 40bits** 가 0이 나와야 한다.
> - 이 때, hash값이 조건을 충족하지 못하면 **임의의 bit(nonce)** 를 변경시켜 hash 값의 앞 40bits가 0이 되도록 계속 시도한다.
> - nonce의 모든 bit(32bit)를 다 시도했는데 불구하고 앞 40bit가 0이 되지 않는 경우에는 contents의 값을 바꿔 <br>
다시 시도한다.

<br>

첫번째 블록인 **genesis block** 은 과거의 값을 이용하지 않지만, 두번째 블록 부터는 과거의 값을 이용해야 한다. 

<br>

## Block Chain(genesis block 이후)
- 모든 block은 **block number** 를 가지고 있다.
- 새로운 block은 이전 block의 **hash 값** 을 포함한다.
- block의 hash 값은 40bit가 0으로 시작되어야 한다.

<br>

> 이전 block의 hash값을 이용하기 때문에 거래내역(contents)를 위변조 하게 되면, 모든 사용자의 block에서의 거래내역 또한 바뀌어야 한다.
> 이로 인해 block chain에서의 거래내역 위변조는 사실상 거의 불가능하다.

<br>

### hash 값을 생성하는 방법
    1. 모든 데이터 뒤에 nonce를 붙여서 hash 값 생성
    2. block header(이전 contents 포함)를 hashing 한 값에 nonce를 더해서 다시 hash 값 생성
    => 보다 더 효율적임.

<br>

### Block header
> - version
> - 이전 block의 hash값
> - merkle root: block안에 있는 transaction들을 가지고 만들어낸 hash 값.
> - timestamp
> - bits: 난이도
> - nonce

<br>

### header만 hashing하면 생기는 장점!
    1. lightweight node
    2. Full node 에는 모든 transaction 기록이 존재하기 때문에 무거워진다.
    3. 반면에, lightweight node는 오직 header값만 사용하기 때문에 가볍다.
    => 여기에서, 이전 transaction의 검증은 어떻게 가능할까?

: contents(transactions 기록)들이 block header안에 있는 **merkle root** 에 있기 때문에 검증이 가능하다.

### Merkle Tree
: 바이너리 트리. 각각의 데이터에 hash값을 구해서 구한 hash값들을 또 다시 두개씩 묶어서 더한 후,<br>
다시 hashing해서 트리를 구성하는 것이다.<br>

    암호화 되어 있기 때문에, 값만 보고 어떤 transaction인지 알 수 없다.
    거래가 하나라도 변경이 되면  **전체의 값(merkle tree)** 이 바뀌게 된다.
    header에는 이전 block의 hash값과 현재 block의 contents에 대한 merkle root 값이 들어있다.

<br>

![node](https://user-images.githubusercontent.com/19389288/49415406-ee127e80-f7b9-11e8-88fe-76d44d694a08.PNG)

    위의 그림을 보면, lightweight node에서 header에 merkle root값이 <code>6c0a</code>라는 값을 가졌지만,
    이 아래의 값(이전 transaction)들은 알 수 없다. 하지만, 이 node가 몇번째 node인지는 알고 있기 때문에
    이 node가 유효한 node인지 확인하기 위해 **몇개의 정보**  를 얻게 되면, 아래의 값들 또한 알 수 있다. 

<br>

![node2](https://user-images.githubusercontent.com/19389288/49415583-96284780-f7ba-11e8-8146-eb570d1e9b24.PNG)

    위의 그림에서의 빨간 네모들을 알면, 이전 transaction들을 알 수 있게 된다.
