# AgritechGuard - An Automated and Secure Farming Solution

AgritechGuard is a smart farming solution designed to automate farm monitoring, irrigation, and enhance security using advanced technologies. This project aims to reduce the time farmers spend in the field by providing remote monitoring capabilities and automating irrigation processes.

## Features

- Automatic irrigation based on soil moisture levels.
- Remote monitoring of temperature, humidity, and soil moisture.
- Long-range wireless data transmission using LoRaWAN technology.
- Security system using YOLO v8 for object detection.
- Integration with ThingSpeak IOT database for data storage and retrieval.

## Components Used

- 2 Arduino Uno
- 2 Raspberry Pi3
- DHT11 and soil moisture sensors
- 2 LCD display with i2c module
- Relay module with water pump control
- LoRaWAN modules (Tx and Rx) for long-range data transmission
- YOLO v8 model for object detection
- Buzzer for security alerts
- ThingSpeak Database

## Softwares Used
  
- PyCharm IDE
- Arduino IDE
- Raspberry Pi Imager
- Putty
- VNC Viewer
  
### Prerequisites

- Arduino IDE for Embedded C programming.
- Python environment with required libraries for YOLO v8.
- Raspberry Pi setup with required dependencies.

## Project Documentation

- [PDF Documentation](https://github.com/CVBhanuPrakash/AgritechGuard/blob/main/images/BTP_3rd_Review.pdf)

## Project Images

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
  <div style="flex: 1; max-width: 48%; padding: 1%;">
    <h3>Transmitter Side:</h3>
    <img src="https://github.com/CVBhanuPrakash/AgritechGuard/blob/main/images/TransmitterEnd.jpg" style="max-width: 100%; height: auto;" alt="Transmitter Image">
  </div>
  <div style="flex: 1; max-width: 48%; padding: 1%;">
    <h3>Receiver Side:</h3>
    <img src="https://github.com/CVBhanuPrakash/AgritechGuard/blob/main/images/ReceiverEnd.jpg" style="max-width: 100%; height: auto;" alt="Receiver Image">
  </div>
</div>

## Project Video

- [Watch Project Video](https://drive.google.com/file/d/1Aa2_3-nHwf__IRAXLLYE0wAritepQV8B/view?usp=sharing)

This project represents the culmination of extensive research and development, combining IoT technology, sustainable energy solutions, and computer vision to optimize agricultural practices and enhance security in farming environments.

