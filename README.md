# timeKeep

Background

This project uses Raspberry pi 4 together with RFID RC522 tag reader to register employee time records. The idea is that when the employee meet up at work, the employee will swipe his card over the reader and his time of arrival will be registered. When the employee leaves the workspace he will swipe the card over the reader to allow registration of when he leaves. 

This project further develops a jupyter notebook GUI that can be accessed using remote.it that allows creating of a new employee in the system. The GUI part is meant for managers to:

Write employee name into the card
Add employee meeting or leaving time should the employee forget to swipe the card
To accomodate payroll of the employee, the manager can select a given employee and extract together with selection of a time boundaries. The program then extracts the meeting and leaving time followed by calculation of how many hours the employee has worked. A report is then generated and sent to an email of choice by the manager.

Setup

1)
First an Raspbian image containing the remote it application is written to a sd card following this tutorial https://support.remote.it/hc/en-us/articles/360045375151-Raspberry-Pi-Quick-Start-remote-itPi-SD-Card-image-

For connection over wifi the SSID and password of wifi is written into wpa_supplicant.conf 

2)
sudo apt-get upgrade && sudo apt-get -y install is executed to update the raspberry pi.

3) Following this guide Jupiter notebook is installed and a verified that one can connect to the notebook over the internet using remote.it
https://towardsdatascience.com/raspberry-pi-tutorial-on-hosting-a-jupyter-notebook-that-you-can-access-anywhere-32191f882b1f

4) RFID receiver software is installed on the raspberry pi following this guide https://pimylifeup.com/raspberry-pi-rfid-rc522/
