# AgritechGuard - B.Tech Thesis Project

Welcome to AgritechGuard, an innovative agricultural monitoring system developed as part of a B.Tech thesis project. This comprehensive solution seamlessly integrates automated and manual irrigation capabilities, harnessing the power of LoRa WAN technology for wireless data transmission, even in remote regions without internet access. AgritechGuard prioritizes sustainability by incorporating solar energy harvesting, ensuring continuous operation during power outages. Moreover, it enhances farm security through the integration of the YOLO v8 model for trespasser detection. It integrates real-time camera data transmission to the Thingspeak IoT platform, providing a robust solution for data storage and retrieval. This integration allows for instantaneous data updates and facilitates the use of the database for generating alerts in response to potential security threats or other critical events.

## Key Features

- **Automated and Manual Irrigation**: AgritechGuard offers both automated and manual irrigation capabilities, allowing precise control over watering for agricultural fields.

- **LoRa WAN Technology**: It utilizes LoRa WAN technology for data transmission, making it suitable for remote locations with limited internet connectivity [Even if no internet connection].

- **Solar Energy Harvesting**: The system ensures continuous operation by harvesting solar energy, guaranteeing a sustainable power supply, even during power outages.

- **Enhanced Security**: AgritechGuard incorporates the YOLO v8 model for trespasser detection. It sends immediate notifications to users upon the detection of unauthorized trespassers, enhancing security on the farm.
  
- **Database:** AgritechGuard integrates with ThingSpeak, a cloud-based platform for IoT applications. Upon detecting a trespasser using the YOLO v8 model, the system immediately logs relevant data, such as images or videos, to the ThingSpeak realtime database.

- **Alerts:** Alerts can be sent through various channels, such as email, SMS, or push notifications to ensure that farmers are promptly informed about potential security threats.

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

