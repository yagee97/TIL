### Jupyter 설치

window 10 + Python 3.7 환경에서 Jypyter 설치하기

---------------------------------------------------------



#### 1) Jupyter 설치 (cmd)

```
C:\Users\예지> pip install jupyter
```



#### 2) profile 생성하기

```
C:\Users\예지> ipython profile create
```



#### 3) 파일 수정하기

생성된 profile은 `C:\Users\예지\.ipython\profile_default` 에 위치.

여기에서 `ipython_config.py` 라는 **파일 수정**.

```
c.InteractiveShellApp.matplotlib = 'inline'
c.InteractiveShellApp.pylab = 'inline'
```

( 위의 코드가 주석처리 되어 있는 것을 풀고, none을 **inline**으로 수정 )



#### 4) 작업 폴더 생성

Jupyter 파일을 관리할 작업 폴더 생성

```
C:\Users\예지> mkdir myworks
C:\Users\예지> cd myworks
```



#### 5) Jupyter 실행

위의 최종 경로에서 Jupyter 실행

```
C:\Users\예지> jupyter notebook
```



#### 6) 완료

Jupyter를 실행한 후 나온 localhost:8888/... 에 접속하고,

아래와 같은 화면이 보이면 **Jupyter 설치 성공**

![](C:\Users\예지\Desktop\TIL할꺼\주피터.PNG)