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

### Work for 6th Semester

![image](https://github.com/CVBhanuPrakash/AgritechGuard/blob/main/images/BD1.png)

### Work for 7th Semester

![image](https://github.com/CVBhanuPrakash/AgritechGuard/blob/main/images/BD2.png)

## Work Done

### IN 6th semester:

- Implemented automatic irrigation system with remote monitoring.
- Crafted LoRaWAN technology to transmit data over long ranges.
- Solar energy harvesting is employed to ensure sustainable power supply.

### IN 7th semester:

- Trespasser detection using computer vision and promptly send to ThingSpeak.
- Implemented with Raspberry Pi 3.

# Results

### System at Transmitter End

![image](https://github.com/CVBhanuPrakash/AgritechGuard/blob/main/images/Transmitter.jpg)

### System at Receiver End

![image](https://github.com/CVBhanuPrakash/AgritechGuard/blob/main/images/Receiver.jpg)

### When no anomaly detected

![image](https://github.com/CVBhanuPrakash/AgritechGuard/blob/main/images/No%20detection.jpg)

### When anomaly detected in consecutive frames

![image](https://github.com/CVBhanuPrakash/AgritechGuard/blob/main/images/Detected.jpg)

### Data being sent to ThingSpeak database and updating in Real-Time:

![image](https://github.com/CVBhanuPrakash/AgritechGuard/blob/main/images/ThingSpeak.png)

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

- [Project Final Report](https://drive.google.com/file/d/11_hseOgI_ycsSX9i6phKm5sgHNZydseM/view?usp=drive_link)

- [Project Final Slides](https://docs.google.com/presentation/d/1OepfI09y9D6plRo6uJYT0zQ8zTfaccmB/edit?usp=drive_link&ouid=100096952433351082672&rtpof=true&sd=true)


## Project Video

- [Watch Project Video](https://drive.google.com/file/d/1Aa2_3-nHwf__IRAXLLYE0wAritepQV8B/view?usp=sharing)

This project represents the culmination of extensive research and development, combining IoT technology, sustainable energy solutions, and computer vision to optimize agricultural practices and enhance security in farming environments.

