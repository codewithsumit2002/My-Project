void setup(){
    Serial.begin(96000);
    pinMode(13,OUTPUT);
}
VOID LOOP(){
    digitalWrite(13,1);
    delay(1000);
    digitalWrite(13,0);
    delay(1000);
}
