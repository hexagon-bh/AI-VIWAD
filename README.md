# 🚦AI-VIWAD
*Artificial Inteligence - Visual Impaired Walking Assistent Device*<br>
> 2023년 CodeFair - 시각장애인을 위한 보행 보조 장치

<img src="\md - 작품 사진.png" title="AI-VIWAD"></img><br/>
[작동영상]: https://youtu.be/XwjiE8r5t54<br>
[Team]: Makers🛠️<br>
[Maker]: 조윤혁(Leader & Electronic), 송승현(Electronic & Software), 양예성(Software) / Assistant: 김강현(Web dev)<br>
[Production period]: 2023.4 ~ 2023.10<br>
[Engeenioring Files]: None
[work description]: [🔗작품 설명서](https://docs.google.com/document/d/1tyV2fjZkA8JoP6vy9Sr6bMmbAfNee75N/edit?usp=sharing&ouid=107164361597916380257&rtpof=true&sd=true)

## 작품 소개 및 Software

<strong><span style="font-size:big">🦾AI-VIWAD - Artificial Inteligence - Visual Impaired Walking Assistent Device</span><strong>

> 시각장애인을 위한 횡단보도를 안전하게 보행할 수 있도록 도와주는 AI를 활용한 웹 서비스

**[제작 동기]**<br>
앞을 보지못해 사고 위험이 있었던 경험과 ‘허우령’ 시각장애인 아나운서 인터뷰를 통해 시각장애인 보행의 위험 심각성을 느껴 시각장애인의 보행을 돕는 장치 및 웹 서비스를 개발<br>

## AI-VIWAD Software 및 Hardware 설명
>횡단보도의 점자블록과 신호등의 빨간불과 파란불을 인식하고 그에 맞게 웹과 신발을 통해 알림을 준다.

**[점자블록 인식하기]**<br>
>아두이노를 사용해 컬러센서를 통한 점자블록 인식

1. 전용 신발을 제작 및 점자블록 인식<br>
<img src="/md - 신발 내 장착.png"></img>
    - 신발 맞춤 제작 후 보드(ARDUINO) 탑재 가능하도록 후가공
    - 회로 제작 및 컬러센서 연결
    - 컬러센서를 통해 노란색을 인식하면 점자블록으로 인식
    - 인식 시 진동 모듈을 통해 진동을 통한 알림

2. 신호등 인식(Yolo v5) 및 웹 개발<br>
    <table style="border: none;">
    <tr>
    <td><img src="/md - 웹 홈화면.png" alt="웹 홈화면" width="300"/></td>
    <td><img src="/md - 웹 캠화면.png" alt="웹 캠화면" width="300"/></td>
    </tr>
    </table>

    - Flask를 사용한 웹 개발
    - ESP 캠을 사용하여 ip통신을 사용해 캠화면 무선 미러링


**[서보모터 동시 제어]**<br>
>각 손가락의 관절을 미세하게 조정하기 위해 인터넷에 널리 알려진 실로 제어하는 방법이 아닌 서보모터를 사용하여 각 관절을 제어하였습니다.

1. 손가락 관절(모터) 위치
    (그림)
    [전자]: 총 12개의 모터를 제어하기 위하여 저희 서보모터 다채널 드라이버(PCA9685)를 사용하
        여 제어하였습니다.

2. Thread를 사용한 모터 동시 제어
    Thread를 사용하는 이유는....GPIO를 통해 모터를 제어할 때 보통은 한번에 하나의 모터만 제어할 	수 있다.(이는 컴퓨터가 하나의 프로세스에서 하나의 작업만 수행 할 수 있기 때문이다.) 해서 동시에 	12개의 모터를 제어하기 위하여 사용한다.<br>
    [Thread 개념]: https://www.yalco.kr/14_process_thread/

    - python의 threading 라이브러리를 사용하여 드라이버의 각 채널마다 연결 되어 있는 모터를 제	어 함.
    - 각 채널을 편리하게 제어하기 위해 Class(2.1)를 사용하여 다양한 제어 메서드를 제작 후 각 인스	턴스	 (즉, 채널 제어 메서드)의 모터 제어 메서드를 thread에 넣어줌. 

**[인공지능 PC 와 로봇 손(Raspberry Pi) 통신]**<br>
Socket 통신이란?..
> 🔖네트워크상에서 가동되는 두 개의 프로그램 간 양방향 통신의 하나의 엔드포인트

소켓은 TCP/IP 기반 네트워크 통신에서 데이터 송수신의 마지막 접점을 이야기한다. 즉, 소켓은 서버와 클라이언트 간 데이터를 주고받는 양방향 연결 지향성 통신.
소켓을 사용하기 위해서는 클라이언트와 서버 소켓으로 각각 구분되고, 통신을 하기 위해 IP주소와 포트번호를 이용한다.
- Python의 Pysocket 라이브러리 사용하였다.
- Bluetooth 모듈을 사용항 블루투스 통신을 시도하였지만 보낼 수 있는 데이터 비트 수 제한과 속도 제한으로 인하여 Socket 통신을 사용하였다.


## DiSRHiT 조작 메뉴얼

**[라즈베리파이 접속 command - ssh]**
> ssh rkdgus0810@[ip address(inet)] -p 22

*접속하면 현재 띄워져 있는 창은 라즈베리파이 cmd임.

**[directory 이동]**
> cd Desktop
> cd AI-Hand

**[가상환경 활성화]**
> source bin/activate

*입력 라인 맨 앞에 “(AI-Hand)" 뜨면 성공!!

**[socket통신 주소 확인]**
1. ip 주소 조회
> ifconfig

2. vscode 에서 main.py 파일 열고 Host 변수 값(ip주소)과 1번을 통해 조회한 ip주소가 같은지 확인

**[라즈베리파이 코드 실행]**
1. 초록 레버 on
2. 코드 실행
> python main. py

*초기값 log 뜨고 server 켜질 때까지 기다리기
(서버가 시작되면 ip주소랑 port번호 등이 뜸)

**[로컬 컴퓨터(AI) 코드 실행]**
<br>vscode 터미널에서 다음 명령어 실행
*vscode 터미널 열기ctrl + ~(단, shift x)
> python main.py

*통신이 시작됬다고 뜨면 성공!(초록색 글자로 뜸)

**[참고 및 주의 사항!!]**<br>
*혹시 만약에 작동 실패하면 [소켓 통심 주소 확인] 다시 한 번해보기!!
*메뉴얼 순서 중요!!
*대소문자 중요!!
