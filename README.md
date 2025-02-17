# 🚦 **AI-VIWAD**
*Artificial Intelligence - Visual Impaired Walking Assistant Device*  
> 2023년 CodeFair - 시각장애인을 위한 보행 보조 장치

![AI-VIWAD](/README%20asses/profile_image.png)  
[🎬 작동영상](https://youtu.be/XwjiE8r5t54)  
[👨‍💻 Team]: Makers🛠️  
[🛠️ Maker]: 조윤혁(Leader & Electronic), 송승현(Electronic & Software), 양예성(Software) / Assistant: 김강현(Web dev)  
[📅 Production period]: 2023.4 ~ 2023.10  
[📝 Engineering Files]: None  
[📄 Work Description]: [🔗작품 설명서](https://docs.google.com/document/d/1tyV2fjZkA8JoP6vy9Sr6bMmbAfNee75N/edit?usp=sharing&ouid=107164361597916380257&rtpof=true&sd=true)

---

## 🌟 **작품 소개 및 Software**

### 🦾 **AI-VIWAD - Artificial Intelligence Visual Impaired Walking Assistant Device**  
> **🚶‍♀️ 시각장애인을 위한 횡단보도를 안전하게 보행할 수 있도록 도와주는 AI를 활용한 웹 서비스**  

#### **💡 제작 동기**  
앞을 보지 못해 사고 위험이 있었던 경험과 ‘허우령’ 시각장애인 아나운서 인터뷰를 통해 시각장애인 보행의 위험 심각성을 느끼고, 이를 개선할 수 있는 장치와 웹 서비스를 개발하기로 결심했습니다. 🔧

---

## 🔧 **AI-VIWAD Software 및 Hardware 설명**

> **🚦 횡단보도의 점자블록과 신호등의 빨간불과 파란불을 인식하고, 이를 웹과 신발을 통해 알림을 줍니다.**

### **1. 🟡 점자블록 인식하기**  
> 아두이노와 컬러센서를 활용하여 점자블록을 인식하는 기술 💡

- **👟 전용 신발 제작 및 점자블록 인식**  
  - 신발 맞춤 제작 후 보드(ARDUINO) 탑재 가능하도록 후가공  
  - 회로 제작 및 컬러센서 연결  
  - 컬러센서를 통해 **노란색**을 인식하면 점자블록으로 인식 🟡  
  - 인식 시 **진동 모듈**을 통해 **진동 알림** 🕹️

  ![신발 내 장착](\README asses\md - 신발 내 장착.png)

---

### **2. 🚦 신호등 인식 및 빨간불/파란불 알림**  
> **YOLO v5**를 사용하여 신호등을 인식하고, 상태에 따라 음성으로 알림을 제공합니다. 📢

- **🔴 빨간불과 🟢 파란불 인식**  
  - YOLO v5로 신호등 상태 학습 📊  
  - 신호등을 인식하고 **TTS**(Text-to-Speech)를 통해 신호등의 상태(빨간불, 파란불)를 음성으로 알림 🎙️

  ![신호등 이미지](\README asses\md - 욜로 로고.jpg)

---

### **3. 🌐 웹 개발**  
> **Flask**와 **ESP 카메라**를 사용하여 실시간 웹 인터페이스 제공 💻

- **🖥️ 웹 개발 및 UI 개선**  
  - **Flask**를 사용한 웹 서버 개발 🖧  
  - **ESP 카메라**를 사용해 IP 통신을 통해 캠 화면을 무선으로 미러링 📸  
  - **UI**를 단순화하여 시각장애인들이 더 쉽게 사용하도록 디자인 개선 🎨  
  - **TTS**(음성 안내 기능) 구현 시도 (아직 개선 필요) 🔄

  ![웹 홈 화면](\README asses\md - 웹 홈화면.png)  
  ![웹 캠 화면](\README asses\md - 웹 캠화면.png)

---

### **4. 🔌 통신 방법**  
> **Arduino**(신발)와 **웹 서버** 간의 통신을 위해 **소켓 통신**을 사용 🌐

---

## **✨ 기타 특징**  
- **👨‍🦯 사용자 편의성**: UI와 음성 안내를 통해 시각장애인들이 보다 안전하고 효율적으로 보행할 수 있도록 설계됨.  
- **💥 진동 알림**: 점자블록을 인식했을 때 발에 진동을 전달하여 인식 여부를 알림.

---

🚶‍♂️ **AI-VIWAD**는 **시각장애인의 보행 안전**을 위해 AI, 하드웨어, 소프트웨어가 결합된 혁신적인 보조 장치입니다. 🦾
