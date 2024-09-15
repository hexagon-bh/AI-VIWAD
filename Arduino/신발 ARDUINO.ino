#include <SoftwareSerial.h>

String str = "";    //군집화 문자열 생성

#define BT_RXD 3
#define BT_TXD 4    //블루투스 핀 번호
#define S0 7
#define S1 8
#define S2 5
#define S3 6
#define SO 2    //컬러센서 핀 번호
#define size_list 1   //문자열 생성

double miss = 0.00001;                      //오차 범위 변수
double x[size_list] = {37.6592216491699};   //위도 센터좌표 리스트
double y[size_list] = {127.0794830322265};  //경토 센터좌표 리스트

int RF = 0;
int BF = 0;
int GF = 0;   //컬러센서 rgb 입력값
int ds = 100; //delay 시간값

int r = 33;
int g = 37;
int b = 42;   //보도블럭 rgb 색상값

SoftwareSerial bluetooth(BT_RXD, BT_TXD);   //블루투스 핀 설정

void setup() {
  Serial.begin(9600);     //시리얼 통신 9600 보드레이트 설정
  bluetooth.begin(9600);  //블루투스 통신 9600 보드레이트 설정
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(SO, INPUT);     //컬러센서 핀 출력, 입력 설정
  digitalWrite(S0, HIGH);
  digitalWrite(S1, LOW);  //컬러센서 작동
}

void loop() {
  int Bt;   //블루투스 통신용 변수 선언
  Serial.println(Bt);
  digitalWrite(S2,LOW);
  digitalWrite(S3,LOW);
  RF = pulseIn(SO,LOW);
  Serial.print("R = ");
  Serial.print(RF);       //컬러센서로 입력받은 빨간색 입력값 시리얼 모니터에 출력
  //delay(ds);
  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);
  GF = pulseIn(SO,LOW);
  Serial.print("G = ");
  Serial.print(GF);       //컬러센서로 입력받은 초록색 입력값 시리얼 모니터에 출력
  //delay(ds);
  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);
  BF = pulseIn(SO,LOW);
  Serial.print("B = ");
  Serial.println(BF);     //컬러센서로 입력받은 파란색 입력값 시리얼 모니터에 출력
  //delay(ds);
  if (r-7<=RF and r+7>=RF and g-7<=GF and g+7>=GF and b-7<=BF and b+7>=BF) {  //컬러센서로 입력받은 rgb값이 보도블럭의 색상값 오차에서 벗어나지 않을 때
    Bt = 10;    //블루투스 통신용 변수값 설정
    bluetooth.write(Bt);    //블루투스 신호 송신
    Serial.println(Bt);
    Serial.println("success");  //성공 문자 출력
    analogWrite(11,255);        //진동모터 작동
    delay(1000);                //1초 대기
    analogWrite(11,0);          //진동모터 작동 중지
    if (bluetooth.available()) {    //블루투스 데이터를 수신했을 때
      //Serial.println(bluetooth.read());
      str = bluetooth.readString();   //블루투스 수신 데이터를 문자 변수에 입력
      int first = str.indexOf(",");
      int strlength = str.length();
      String str1 = str.substring(0, first);
      String str2 = str.substring(first+1, strlength);  //문자열 및 문자열 숫자 갯수

      double flt1 = str1.toDouble();    //첫번째 문자열 비교
      double flt2 = str2.toDouble();    //두번째 문자열 비교
      Serial.println(flt1, 13);
      Serial.println(flt2, 13);         //시리얼 모니터에 문자열 출력

      for (int i = 0; i < size_list; i++) {   //센터좌표 리스트에 있는 좌표들과 비교
        if (flt1 >= x[i] - miss and flt1 <= x[i] + miss and flt2 >= y[i] - miss and flt2 <= y[i] + miss) {  //센터 좌표와의 오차 범위가 적을 때
          for (int i = 0; i < 5; i++) {   //5번 반복
            analogWrite(11,255);
            delay(250);
            analogWrite(11,0);
            delay(250);         //진동모터 위잉위잉
          }
        }
      }
    }
    
    
  }
}
