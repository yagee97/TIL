## blockchain Consensus
blockchain의 합의 알고리즘에 대해 다룹니다.

<br>

#### Q. 새로운 block 들이 동시에 생성되었을 때, 어떤 block이 최종적으로 선택되어야 할까?

### 1. 합의(Consensus)

    1. mining을 통해 새 block을 생성한 후, block chain network에 전파(propagation)을 한다.
    2. 전파받은 block의 "유효성"을 검증한다.
    3. blockchain을 조립하고 선택한다.

<br>

### 2. Validating a new block in detail (유효성 검증)

    1. block chain structure가 잘 구성되었는지 확인.
    2. block header의 hash 값을 체크한다.
       => POW를 체크하는 것. hash 값이 target의 difficulty보다 작아야 한다.
    3. block의 timestamp는 미래로 2시간까지 허용된다.
        => 머신끼리의 시간이 일치하지 않을 수 있기 때문.
    4. block size가 1MB의 기준을 충족하는지 확인.
    5. 첫번째 거래가 coinbase를 생성하는 거래인지 확인
        => block contents의 제일 첫번째 거래 기록이 "coinbase"여야 한다.
        
###### coinbase는 mining 했을 때, **이 block이 보상을 받았다** 라는 거래기록 이다.

<br>

### 3. block chain forks
![blockchain](https://user-images.githubusercontent.com/19389288/49688858-d17c9a80-fb5b-11e8-9e8c-d3cfe0be4faf.PNG)
> 101-A와 101-B가 동시에 생성되었는 데, 101-A가 102번 block을 먼저 생성하여 전파했다. <br>
> 이 때, 102번 block을 생성하고 있던 101-B는 자신을 버리고 101-A가 만든 102 block을 받아들인다.

##### 이것을 `select the longest chain`이라고 하며, `greatest cumulative difficulty chain` 이라고 하기도 한다.

<br>

### Q. 왜 select the longest chain을 사용할까?
    1. 다음 block을 만들기 위해 가장 긴 chain을 고르는 것이 좋기 때문이다.
    2. 개인과 전체의 이익이 일치(coincide)하기 때문이다.
    개인: 새로운 노드를 계속 만드는 것보다, 긴 chain을 선택하는 게 더 이롭다.
    전체: 전체적인 chain이나 block의 양이 줄어, overhead가 줄어든다.
    
<br>
    
### Q. 자기자신을 버리고 다른 block을 사용하면 어떻게 되는가?
* A-1. transaction에 영향을 주지는 않는다. 
###### (다른 block에 자기가 담고 있던 transaction들이 포함될 수 있기 때문)
* A-2. 짧은 block chain에 있던 transaction들은 miner들에 의해 검증된다.


<br>

### * Coinbase transaction(reward bitcoin)이 영향을 받을 수는 있다.
> * coin-based transaction은 100개의 추가 block을 생성한 후 사용할 수 있도록 정의된다.
###### coinbase에 담긴 UTXO는 최소 100 block 동안 사용이 불가능 하다.

> * 17 시간 후 (10분당 block 1개) <br>
> * 이 시간동안, generation 된 block이 채택되었는 지 확인할 수 있다.

###### block chain fork 후 낡은 것(버려지는 block) 이라고 판명될 수 있는 block으로부터의 보상을 차단한다.
    



