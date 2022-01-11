# Network
- [HTTP란 무엇인가요?](#http란-무엇인가요)
- [HTTPS란 무엇인가요? (SSL, 비대칭키 암호화)](#https란-무엇인가요-ssl-비대칭키-암호화)
- [URL과 URI의 차이점을 알고있나요?](#url과-uri의-차이점을-알고있나요)

<br>

## HTTP란 무엇인가요?
> 웹 서비스에서 클라이언트(웹 브라우저)와 웹 서버간에 정보를 주고 받기 위해 사용되는 네트워크 프로토콜이다.
> 인터넷에서 데이터를 주고 받을 수 있도록 하는 통신규약이다.  
> 클라이언트에서 브라우저를 통해서 요청을 하면 서버에서 응답해주는 형태로 동작한다.

### HTTP 특징
- TCP/IP를 이용하는 응용 프로토콜이다.
- HTTP는 연결 상태를 유지하지 않는 비연결성 프로토콜이다.(stateless)
- HTTP는 연결을 유지하지 않는 프로토콜이기 때문에 요청/응답 방식으로 동작한다.
- 평문통신이기 때문에 도청이 가능하다.  
  **보완방법**
  1) 통신자체를 암호화 프로토콜(SSL/TLS)와 조합해서 통신내용을 암호화
  2) 콘텐츠를 암호화

<br>

## HTTPS란 무엇인가요? (SSL, 비대칭키 암호화)
> HTTP에 보안을 강화한 프로토콜이다.
> HTTP통신에서는 평문 통신을 하기 때문에 외부에서 도청이 가능한데, 평문을 서버에서만 알아볼 수 있도록 암호화한 것이다. 

<br>

### SSL(Secure Soket Layer)


### 암호화 방식
대칭키  
: 암호화와 복호화 하는 방식이 같다.

**비대칭키 암호화(공개키, 개인키)**  
: 암호화와 복호화 하는 방식이 다르다.  
  공개키는 누구나 볼 수 있는 키이고, 개인키는 서버가 가지고 있는 키이다. 공개키로 암호화를 하게 되면 개인키로만 풀 수 있기 때문에 중간에 탈취당해도 해독 할 수 없게 된다.
  
<br>

## URL과 URI의 차이점을 알고있나요?
> URI가 더 큰 범위로 URL은 자원의 위치를 가리키고, URI는 자원의 고유한 식별자이다.

### URL (Uniform Resource Locator)
- URI에 포함되는 개념이며, 해당 사이트의 특정 자원의 위치를 나타내는 주소
- Protocol, Domain name, Port, Path to the file까지 포함

### URI (Uniform Resource Identifier)
- 해당 사이트의 특정 자원의 위치를 나타내는 고유한 식별 주소
- Protocol, Domain name, Port, Path to the file, Parametes까지 포함

### URL과 URI의 차이
```
http://example.com/index
```
- index라는 경로를 나타내고 있다.
- 자원의 실제 위치이므로 URL이면서 URI이다.

```
http://example.com/user/107
```
- 위의 예시는 107의 ID값을 가지고 있는 자원을 식별하고 있다.
- URL(`http://example.com/user`)을 포함한 URI이다. (URL X)

```
http://example.com/user?id=107
```
- 뒤의 쿼리스트링 식별자(?id=107)를 포함하여 URI라고 볼 수 있다.
