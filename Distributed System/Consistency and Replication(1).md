## Consistency and Replication
Distributed System ch6. Consistency and Replication

<br>

#### 1. Replication
   : 데이터 또는 서비스의 여러 복사본 생성 및 사용
   동일한 데이터가 여러 storage device들에 저장된 경우이며, 데이터 복제를 말한다.
   ex) Web site mirror, browser, cache, DNS 등

<br>

#### 2. 왜 Replication을 사용하는가?
##### (1) Improve Reliability 
	Data survival, availability, confidence

<br>

##### (2) Improve performane (scalability)
	- Number of users increases: Divide the work by multiple servers
	- Geographcal area increases: Reduce access times to improbe proximity

<br>

##### If Replication is so good, why not just use it?
많은 복사본을 가지고 있다는 것은 복제본 또한 업데이트 해야한다는 뜻이다.
이때, **consistency problem** 이 생긴다.

<br>

##### * Solution?
	(1) local replication을 금지하자
	(2) 웹 서버에서 캐시된 복사본들을 평가한다
	(3) conditional HTTP GET을 사용하자

<br>
#### 3. Conditional GET
browser가 server에 GET 요청을 보낼 때, 요청하는 정보가 이미 캐시되어있다면,
browser는 이 data에 변경이 있는지 여부를 확인하는 요청을 보내게 된다.

	server는 요청데이터가 변경되지 않았을 경우에 응답 코드로 304를 리턴.
	캐시됐던 데이터에 변경이 있다면, 변경된 데이터를 응답으로 보낸다.

<br>

#### 4. Tight Consistency
여러 복사본을 일관되게 유지하는 것은 **scalability** 문제의 영향을 받을 수 있다.
복사복이 많으면 성능이 좋아야 하는데, 복사본이 많을수록 한 복사본의 업데이트 후 
**consistency**를 유지하는 것은 **overhead**가 크기 때문이다.

<br>

> ##### (1) 어떤 복사본이든 "Read" 작업이 동일한 결과를 반환해야한다.
> ##### (2) 따라서, 한 복사본의 "Update" 작업은 다른 작업이 수행되기 전에 모든 복사본으로 전파되어야 한다.

<br>

=> 이것을 **Tight Consistency**라고 한다.
update는 single atomic operation으로 모든 복사본에서 수행된다.

<br>

#### 5. Consistency vs. Overhead
##### * Dilemma
	(1) 복제 또는 캐싱을 적용하여 확장성 문제를 완화함으로써 성능을 향상한다.
	(2) 이러한 복제된 복사본을 일관되게 유지하려면, 일반적으로 동기화가 필요하며 이것은 비용이 많이 든다.
	(3) 복제나 캐싱을 사용해서 확장성의 문제를 완화시켰지만, 이 복제를 동기화시키려면 비용이 많이 들기 때문에 딜레마다.
	
##### * Loosen the Consistency
	(1) 즉시 동기화되는 업데이트 요구사항을 완화한다
	=> 복사본은 모든 곳에서 같지 않을 수도 있다.
	(2) 어느정도까지 일관성을 유지할 수 있을까?
	=> 복제된 데이터의 접근 및 업데이트 패턴에 따라 달라진다.



