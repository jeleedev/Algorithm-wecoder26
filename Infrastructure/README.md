- [Docker Image 와 Container 란?](#%EF%B8%8F-Docker-Image와-Container란?)
- [Docker-compose를 사용하는 이유는?](#%EF%B8%8F-Docker-compose를-사용하는-이유는?)

<br>

## 💡 Docker Image와 Container란?
> 서비스 운영에 필요한 서버 프로그램, 소스코드 및 라이브러리, 컴파일된 실행 파일을 묶은 형태를 Docker Image라 한다. Docker Container는 이미지를 실행(run)한 상태로 응용프로그램 자체를 캡슐화하여 독립적인 공간에서 동작시키는 기술이다.

### 추가적인 내용 기술
- Docker Image는 수백MB~수GB 이상의 용량을 가지지만, VM 위에 설치하는 것에 비하면 적은 용량이다.
- 하나의 이미지는 여러 컨테이너를 생성할 수 있고, 컨테이너가 삭제되더라도 이미지는 존재한다.
- Dockerfile로 이미지를 생성할 수 있고, 이 이미지를 실행시키면 Docker Container가 되는 것이다. 

<br>

## 💡️ Docker-compose를 사용하는 이유는?
> Docker Compose를 사용하는 이유는 docker run 명령어에 여러 옵션을 일일이 입력하는 번거로움을 해결시켜준다. 또한 Docker가 이미지를 build하고, 컨테이너화시키는 일련의 과정을 Docker Compose 파일을 통해 명시적으로 기록함으로써 여러 이미지를 컨테이너화하는데 편리하다. 또한 컨테이너 간 연결을 위해 가상 네트워크를 설정할 수 있는데, Docker Compose 기능을 사용하면 여러 독립적인 컨테이너 간 연결을 손쉽게 제어할 수 있다.

### 추가적인 내용 기술
- Docker Compose를 사용하면, Dockr Container를 실행하기 위한 명령어, 옵션들을 일일이 입력할 필요가 없다.
- Docker Compose를 사용하면 컨테이너끼리 연결이 편리하다.
- 특정 컨테이너끼리만 가상 네트워크를 연결시킴으로써 보안의 취약적을 해결할 수 있다.
- 결과적으로 Container가 여러개일 수록 이에 따른 옵션이 복잡하고 반복작업이 발생하는데, 이런 Conatiner간 연결을 효율적으로 관리하고 이 과정을 명시적인 파일로 관리할 수 있게 해주는 것이 Docker Compose 이다. 
