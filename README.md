#  AgritechGuard 

## An Integrated Automated Farming and Security System
AgritechGuard is a smart farming solution designed to automate farm monitoring, irrigation, and enhance security using advanced technologies. This project aims to reduce the time farmers spend in the field by providing remote monitoring capabilities and automating irrigation processes.

## Features

- Automatic irrigation based on soil moisture levels.
- Remote monitoring of temperature, humidity, soil moisture and water pump condition.
- Long-range wireless data transmission using LoRaWAN technology.
- Security system using YOLO v8 for trespasser detection.
- Integration with ThingSpeak IOT database for data storage and retrieval.

## Components Used

- 2 Arduino Uno
- 2 Raspberry Pi 3
- DHT11 and soil moisture sensors
- 2 LCD display with i2c modules
- Relay module
- Water pump
- LoRaWAN modules (Tx and Rx) for long-range data transmission
- YOLO v8 model and COCO dataset for trespaser detection
- Buzzer for security alerts

## Softwares Used
  
- PyCharm IDE
- Arduino IDE
- Raspberry Pi Imager
- Putty
- VNC Viewer
- YOLO v8 with COCO dataset
- ThingSpeak Database

### Prerequisites

- Arduino IDE for Embedded C programming.
- Python environment with required libraries for YOLO v8.
- Raspberry Pi setup with required dependencies.


## Block Diagrams

![image](https://github.com/CVBhanuPrakash/AgritechGuard/assets/94560350/023f4f4e-7833-4365-adbf-17a231f8aed9)

![image](https://github.com/CVBhanuPrakash/AgritechGuard/assets/94560350/3d901fad-81a4-4dff-8331-cb72c5ec9823)

## Work Done

### IN 6th semester:

- Implemented automatic irrigation system with remote monitoring.
- 
- Crafted LoRaWAN technology to transmit data over long ranges.
- 
- Solar energy harvesting is employed to ensure sustainable power supply.

### IN 7th semester:

- Trespasser detection using computer vision and promptly send to ThingSpeak.
- 
- Implemented with Raspberry Pi 3.


# Results

### System at Transmitter End

![image](https://github.com/CVBhanuPrakash/AgritechGuard/assets/94560350/ca0c2965-4be8-4731-8dab-599251f9fe60)

### System at Receiver End

![image](https://github.com/CVBhanuPrakash/AgritechGuard/assets/94560350/a790154a-727b-4109-9744-ebc863d960c5)

### When no anomaly detected

![image](https://github.com/CVBhanuPrakash/AgritechGuard/assets/94560350/444f0e87-48e2-4c57-adef-9b791a56af26)

### When anomaly detected in consecutive frames

![image](https://github.com/CVBhanuPrakash/AgritechGuard/assets/94560350/50cce8be-550b-4f5c-b24b-9717b6ce02ae)

### Data being sent to ThingSpeak database and updating in Real-Time:

![image](https://github.com/CVBhanuPrakash/AgritechGuard/assets/94560350/b2bc9451-208e-4f78-bda9-68173b77b4f5)

## Challenges Faced

- Establishing a Wi Fi connection with Raspberry Pi 3. 

- The hardware connections proved to be challenging especially with i2C module.

- LoRaWAN won’t work as specified.

- Ensuring accurate differentiate person, animals, and potential intruders, with a focus on minimizing false alarms.

## Conclusion

- Irrigation is initiated based on soil moisture levels, with the Arduino autonomously controlling the pump's operation. 

- The farmer can conveniently monitor the farm remotely from their home. 

- The system employs solar energy harvesting techniques for power efficiency. 

- Additionally, it incorporates computer vision for detecting trespassers and issuing alert messages when unauthorized individuals are detected.


## Project Documentation

- [Project Documentation](https://github.com/CVBhanuPrakash/AgritechGuard/blob/main/images/BTP_3rd_Review.pdf)


## Project Video

- [Watch Project Video](https://drive.google.com/file/d/1Aa2_3-nHwf__IRAXLLYE0wAritepQV8B/view?usp=sharing)

This project represents the culmination of extensive research and development, combining IoT technology, sustainable energy solutions, and computer vision to optimize agricultural practices and enhance security in farming environments.

