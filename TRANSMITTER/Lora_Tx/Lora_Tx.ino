const int sensor_pin = A1;	/* Soil moisture sensor O/P pin */
const int relais_pompe = 5;
const int DHT11PIN = 4;
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
#include <SPI.h>
#include <dht11.h>
#include <RH_RF95.h>
dht11 DHT11;
RH_RF95 rf95;

void setup() {
  lcd.init();
  lcd.clear();         
  lcd.backlight();   
  pinMode(relais_pompe, OUTPUT);
  if (!rf95.init())
    Serial.println("init failed");
  rf95.setFrequency(868.0);
}

void loop() {
  float moisture_percentage;
  int sensor_analog;
  int chk = DHT11.read(DHT11PIN);
  sensor_analog = analogRead(sensor_pin);
  moisture_percentage = ( 100 - ( (sensor_analog/1023.00) * 100 ) );
  int final_moisture = (int)moisture_percentage;


// Sending Humidity, Temperature and Soil moisture to the LoRa-Rx from LoRa-Tx at 868MHz
  Serial.println("Sending to rf95_server");

  String dataString = (String)DHT11.humidity + "," + (String)DHT11.temperature + "," + (String)final_moisture + " ";
  uint8_t data[9];
  dataString.toCharArray(data, dataString.length());

  rf95.send(data, sizeof(data));

  rf95.waitPacketSent();
  // Now wait for a reply
  uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];
  uint8_t len = sizeof(buf);

  if (rf95.waitAvailableTimeout(3000))
  {
    // Should be a reply message for us now
    if (rf95.recv(buf, &len))
    {
      Serial.print("got reply: ");
      Serial.println((char*)buf);
    }
    else
    {
      Serial.println("recv failed");
    }
  }
  else
  {
    Serial.println("No reply, is rf95_server running?");
  }

  if(final_moisture <=50){
    digitalWrite(relais_pompe, LOW);
    lcd.clear();
    lcd.setCursor(0,0);   
    lcd.print("H:");
    lcd.print(DHT11.humidity);
    lcd.setCursor(6,0);   
    lcd.print("T:");
    lcd.print(DHT11.temperature);
    lcd.setCursor(12,0);   
    lcd.print("M:");
    lcd.print(final_moisture);
    lcd.setCursor(2,1);
    lcd.print("Motor : ON");
  }
  else{
    lcd.clear();
    digitalWrite(relais_pompe, HIGH);
    lcd.clear();
    lcd.setCursor(0,0);   
    lcd.print("H:");
    lcd.print(DHT11.humidity);
    lcd.setCursor(6,0);   
    lcd.print("T:");
    lcd.print(DHT11.temperature);
    lcd.setCursor(12,0);   
    lcd.print("M:");
    lcd.print(final_moisture);
    lcd.setCursor(2,1);
    lcd.print("Motor : OFF");
  }
  delay(5000);
}