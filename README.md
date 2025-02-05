# Packet Sniffer

The network packet analysis and IDS project is a Python application developed using Scapy. The project consists of stages such as protocol analysis, anomaly detection, attack detection rules, automatic response mechanisms, and database integration. You can access the Turkish version [here](https://github.com/emir-ertunc/packet-sniffer/blob/main/README_TR.md).

## About the Project

This project is a Network Packet Analyzer and Intrusion Detection System (IDS) application developed using the Python programming language and the Scapy library to enhance network security. This system analyzes packets passing through the network, detects abnormal behaviors, and logs potential attacks, notifying administrators.

## Table of Contents

- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [Project Features](#project-features)
- [Development Process](#development-process)
- [Contributing](#contributing)
- [Contact](#contact)

## Installation Instructions

To run this project, follow these steps:

1. **Install Python**  
   The project is developed in Python 3.12.6 If you don't have Python installed on your computer, you can download and install it from the [official website](https://www.python.org/downloads/).

  **Using requirements.txt**
You can skip steps 2 and 3 if you install the required libraries via the requirements.txt file.
   ```
   pip install -r requirements.txt 
   ```

2. **Install Scapy Library**  
   The project requires the Scapy library to capture and analyze network packets. To install Scapy, type the following command in your terminal or command prompt:
   ```
   pip install scapy
   ```

3. **Install Pandas Library**  
   To visualize your log records more effectively, you need the Pandas and openpyxl libraries. To install them, type the following command in your terminal or command prompt:
   ```
   pip install pandas
   ```

4. **Clone the Project**
   You can use the following command to clone the project from GitHub:
   ```  
   git clone https://github.com/kullaniciadi/proje_adi.git
   ```
 
 ## Usage

To run the project, type the following command in your terminal or command prompt:
   ```
   python ids_main.py
   ```

When the application is running, the details of the captured packets will be displayed in the terminal and will also be logged into a file.

## Project Features

- **Packet Analysis:** The content of the packets passing through the network is analyzed.
- **Anomaly Detection:** Abnormal high traffic from a specific IP address or unexpected port traffic is detected.
- **Attack Detection Rules:** Specific types of attacks are detected using custom rules. **(planned for future)**
- **Automatic Response Mechanism:** Automatic actions are performed in the event of detected attacks. **(planned for future)**
- **Database Integration:** Captured packets and events are logged into a database. **(planned for future)**
- **Advanced Visualization:** Real-time traffic and detected attacks are visualized. **(planned for future)**
- **Performance Testing:** Performance Testing: The system's performance is tested under high traffic. **(planned for future)**
- **User Interface:** Adding a simplified interface for users who want to use the program without using a command system. **(planned for future)**

## Development Process

The project is developed in phases. The following phases are planned for the completion of the project:

1. ~Packet Analysis and Anomaly Detection~
2. Attack Detection Rules
3. Automatic Response Mechanism
4. Database Integration
5. Advanced Visualization
6. Performance and Scalability
7. Security Testing

## Contributing

If you want to contribute to this project, you can follow these steps:

1. Fork the project from GitHub.
2. Make your changes and commit them.
3. Open a pull request.

I welcome all kinds of contributions and suggestions!

## Contact

If you have any questions or suggestions regarding the project, please feel free to contact me using the information below:

- **Email:** [emir_ertunc@outlook.com](mailto:emir_ertunc@outlook.com)
