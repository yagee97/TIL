## Blockchain Mining
blockchain의 mining에 대해서 다룹니다.

<br>

## 1. 채굴 (Mining)
##### mining이란, `transaction`과 `이전 block`을 가지고 새로운 block을 만들어내는 것을 말한다.
이 과정에서, nonce값을 넣고 나온 hash 값이 block이 되는 조건에 부합하는가를 봐야한다.

<br>
    
**mining에 성공하는 조건은 두가지가 있다.** 
    
    1. block이 되는 조건에 만족해야한다.
    2. 생성한 block을 자신이 속한 blockchain network에 전파시켜 block으로써 인정을 받아야한다.
    
    
###### 위의 조건들을 모두 만족시켜야 mining에 따른 **보상** 을 받을 수 있다.

<br>

##### block은 얼마나 자주 생성될까?
> + 10분마다 한번씩 생성이 된다.<br> 
> + 10분보다 더 빠르게 생성이 된다면, POW(작업증명)이 약화된다. <br> 
> + 10분보다 더 오래걸리면, transaction들이 제 시간에 blockchain에 담기지 못하기 때문에, 비효율적일 수 있다.

<br>

## 2. 난이도 조정 (Difficulty adjustment)
+ hash 값의 + nBits (to be zeros) 개수를 조정한다. <br>
###### nBis: SHA hash function으로 계산되었을 때, 몇자리가 0이 나와야 하는가? <br>

+ 2016개의 block이 쌓일 때마다 체크된다. <br>
###### 여기서의 2016은, 6(1시간에 6개) x 24(하루) x **14(2주)** = 2016) 2주마다 체크를 하게 된다는 것이다.

<br>

#### 2주마다 block의 개수를 체크하는 데, 
+ 2016개의 block을 만드는 시간이 20160 min 보다 적게 걸렸다면, nBits를 늘려야한다. 
=> 난이도가 쉬워 더 많은 block을 만들었다는 것이기 때문.

+ 2016개의 block을 만드는 시간이 20160 min 보다 더 오래걸렸다면, nBits를 줄여야한다.
=> 난이도가 어려워 더 적은 block을 만들었다는 것이기 때문.

<br>

#### * nBis: SHA hash function으로 계산되었을 때, 몇자리가 0이 나와야 하는가?

<br>

> **First byte** <br>
> : Bytes to compare (비교를 위해 사용되는 bytes) <br>
> nBits = total bits - Byte to compare <br>
> **Other 3 bytes** <br>
> First bits of bytes to compare (24 bits)

<br>

#### * Difficulty analysis
`388648495`(hash 값) => `0x172A4E2F` (16진수)
<br>

![mining](https://user-images.githubusercontent.com/19389288/49686040-f9570880-fb31-11e8-9566-d75ba8ef00ae.PNG)

##### 첫번째 byte는 0이 아닌 byte의 수다. (Bits to compare)
###### 23(decimal of 17)(byte) x 8 = 184 (bits)
###### 2A4E2F: 001010100100111000101111 (binary)

![mining2](https://user-images.githubusercontent.com/19389288/49686044-083dbb00-fb32-11e8-901d-2e8d3ac9d9a5.PNG)

##### 이 예제에서, 0이여야 하는 bit 수는 `256(전체 bit 수) - 184 (비교를 해야하는 bit 수) = 72bit`이다.
##### 하지만, 비교를 해야하는 bit의 수에서 앞의 두자리가 현재 0이기 때문에 `nBits`는 `74`가 된다.

###### hash 값은 byte값이기 때문에, 1byte만 증가해도 8bit가 추가된다. 17이 18이 되거나, 16이 되어버리면,
###### 8bit 씩 움직여야 하기 때문에 뒤의 남은 bit들을 통해 난이도 조정을 하는 것이다.

 
