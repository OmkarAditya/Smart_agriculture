#include <DHT.h>

#define MQPIN A5
#define DHTPIN 7    // Pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT sensor type
#define SOILPIN A0

int count=0;
float arr[4];
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // put your setup code here, to run once:
  pinMode(MQPIN,INPUT);
  pinMode(DHTPIN,INPUT);
  pinMode(SOILPIN,INPUT);
  dht.begin(); 
  Serial.begin(9600);
  

}

void loop() {

  // SOIL SENSOR
  float moisture_percentage;
  int sensor_analog = analogRead(SOILPIN);
  moisture_percentage = ( 100 - ( (sensor_analog/1023.00) * 100 ) );
  arr[0]=moisture_percentage;

  //DHT SENSOR
  float temperature = dht.readTemperature();
  arr[1]=temperature;
  float humidity = dht.readHumidity();
  arr[2]=humidity;

  //MQ PIN
  float gas = analogRead(MQPIN);
  arr[3]=gas;
  if(count==0){
      count++;
      
     for(int i=0;i<4;i++){
      Serial.println(arr[i]);
      
    } 
  }
  else if(count==20){
    count=0;
  }
  else{
   count++;
  }
 delay(1000);
  


}
