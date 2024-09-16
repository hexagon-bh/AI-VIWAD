# 🚦AI-VIWAD
*Artificial Inteligence - Visual Impaired Walking Assistent Device*<br>
> 2023년 CodeFair - 시각장애인을 위한 보행 보조 장치

<img src="\README asses\md - 작품 사진.png" title="AI-VIWAD"></img><br/>
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
<img src="/README asses/md - 신발 내 장착.png"></img>
    - 신발 맞춤 제작 후 보드(ARDUINO) 탑재 가능하도록 후가공
    - 회로 제작 및 컬러센서 연결
    - 컬러센서를 통해 노란색을 인식하면 점자블록으로 인식
    - 인식 시 진동 모듈을 통해 진동을 통한 알림

2. 신호등 인식 및 빨간불 파란불 인식<br>
<img src="/README asses/md - 욜로 로고.png"></img>
    - Yolo v5를 사용하여 인공지능 제작
    - 빨간불일 때의 신호등과 파란 불일때의 신호등을 구분해서 학습
    - 신호등을 인식하면 tts를 통해 신호등의 상태를 음성으로 알림

3. 웹 개발<br>
    <table style="border: none;">
    <tr>
    <td><img src="/README asses/md - 웹 홈화면.png" alt="웹 홈화면" width="300"/></td>
    <td><img src="/README asses/md - 웹 캠화면.png" alt="웹 캠화면" width="300"/></td>
    </tr>
    </table>

    - python의 Flask를 사용한 웹 개발
    - ESP 캠을 사용하여 ip통신을 사용해 캠화면 무선 미러링
    - UI를 단순화하여 시각장애인분들이 사용 편리성과 접근성을 높임
    - tts를 통한 voice over기능 개발 시도(fail)

**[통신 방법]**
> arduino(신발)와 웹 서버에서의 통신을 위해 socket 통신을 사용하였습니다.  