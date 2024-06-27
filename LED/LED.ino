#include <cvzone.h>
SerialData serialData(1, 1); // serialData 객체 초기화

int valsRec[1]; // 받은 데이터를 저장할 배열, 1개의 요소가 있음

void setup() {
  serialData.begin(); // 올바른 함수 호출
  pinMode(13, OUTPUT);
}

void loop() {
  serialData.Get(valsRec); // 올바른 객체와 함수 이름
  digitalWrite(13, valsRec[0]); // 유효한 인덱스 [0]만 접근
}