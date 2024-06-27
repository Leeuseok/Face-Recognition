#include <cvzone.h>
#include <Servo.h> 
SerialData serialData(1,1); //(numOfValsRec,digitsPerValRec)

Servo myservo;  // 서보 변수 선언
int servoPin = 9;

int valsRec[1];
void setup() {
  myservo.attach(servoPin); //서보로 9핀 사용하겠다고 설정 
  serialData.begin(); 

}

void loop() {
   serialData.Get(valsRec);
if(valsRec[0]==1){
    myservo.write(90);}
  
  else {
  myservo.write(0); }
}
