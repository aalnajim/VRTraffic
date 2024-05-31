# VRTraffic
#### a *Python* project to analyze the VR traffic characteristics of *Quest 2*. We gather the metrics using multiple tools including (*OVRMetrics*,*logcat*,*ALVR_session log file*, *wireshark*, ...). Then, we did post processing to analyze these matrices and get some insights out of it. All the project files will be available on (xxx).  

---

* ***Note***: this repo is missing the output files of the above tools due to the file size limitation of github. All the project files will be available on (xxx). The structure of the project should be as follow:

    > * VRTraffic
    >   * main.py
    >   * plotGraph.py
    >   * README.md
    >   * requirements.txt
    >   * plots (This is an output folder of of folders contain results plots)
    >   * venv  (This folder for virtual environment if used)
    >   * traces
    >       * gameName(s)
    >           * HMD_traces
    >               * WLAN_BOTH_DataFramesType1.csv
    >               * WLAN_BOTH_DataFramesType2.csv
    >               * WLAN_BOTH_DataFramesType3.csv
    >               * WLAN_BOTH_ManagementFrames.csv
    >               * WLAN_BOTH_RetransmittedDataFramesType1.csv
    >               * WLAN_BOTH_RetransmittedDataFramesType2.csv
    >               * WLAN_BOTH_RetransmittedDataFramesType3.csv
    >           * server_traces
    >               * server.csv
    >   * log_files  
    >       * gameName(s)
    >           * logcat.txt
    >           * session_log.txt
    >           * logs
    >               * vrcompositor.previous.txt
    >               * vrcompositor.txt
    >               * vrmonitor.previous.txt
    >               * vrmonitor.txt
    >           * OVRMetrics
    >               * file(s).csv
                   
---

* ***General Info***:
    1. The **HMD** is linked to the **AP** using *802.11ax* (*WiFi 6*), and the **server** is linked to the **AP** using *Ethernet* cable. The **AP** is linked to the *internet* using *1 Gbps* *FIOS*.
    2. The cummunication between the **HMD** and the **server** is done by using *ALVR* and *AirLink* protocols.
    3. In the **server** side, we use *steamVR* as a platform for the apps to stream the apps content using the protocols mentioned above.
    4. The **server** has an *RTX 2070 super GPU*, 8 cores (16 threads) *i7 CPU*, and a 32 *GBs* of *RAM*.
    5. The ***len*** shown in the *uplink* and *downlink* **server**.csv file represents the payload size in *bytes* (the application layer). For the headers size, we notice that for *UDP* packets the size of the headers is 42 *bytes*, and for *TCP* packets the size of the headers is 54 *bytes*. So, the size in the link will be payload size + 42 for *UDP* and payload + 54 for *TCP*.
    6. The ***data length*** shown in the *uplink* and *downlink* of *WLAN* traces represents the payload size in *bytes*, and the ***length*** field represents the size of the packet in the medium (payload + headers), and it is usually = the ***data length*** field + 104 *bytes* in the uplink (packets from the **HMD** to the **server**) and = ***the data length*** field + 99 *bytes* in the *downlink* (packets from the **server** to the **HMD**).

---

* ***Network Information***:
    1. The HMD information:
        * MAC address: 

            > Facebook_63:35:01 (80:f3:ef:63:35:01)

        * IP address : 
            
            > 192.168.1.179:5555

    2. The server information:
        * MAC address: 

            > Dell_31:58:70 (74:78:27:31:58:70)

        * IP address: 

            > 192.168.1.14 (IPV4)  
            > 2600:4040:7e0c:7800:66e0:ebab:76d0:ce5b (IPV6)  
            > 2600:4040:7e0c:7800:793c:58c6:f8e8:a20e (temp IPV6)

    3. The gateway (AP) information:
        * MAC address: 

            > Arcadyan_26:74:c0 (3c:bd:c5:26:74:c0) for main MAC address  
            > Arcadyan_26:74:c3 (3c:bd:c5:26:74:c3) for 802.11a  (OFDM)  
            > Arcadyan_26:74:c1 (3c:bd:c5:26:74:c1) for 802.11ax (HE)

        * IP address : 

            > 192.168.1.1  (IPV4)  
            > fe80::3ebd:c5ff:fe26:74c1%19  (IPV6)  

---

* ***Wireshark Filters***:
    1.  WLAN:
        1. The first filter is to capture all the frames coming *from* or going *to* the **AP** (3c:bd:c5:26:74:c3) or the **HMD** (3c:bd:c5:26:74:c3). It is used *before* start capturing. 

            > ether host 80:f3:ef:63:35:01 or ether host 3c:bd:c5:26:74:c3

        2. The second filter is used to filter the captured frames to get *only* the **management frames**, such as bacons, actions, and prope requests and responses, that is coming *from* or going *to* the **AP** or the **HMD**.  
           
            > wlan.fc.type eq 0 and ((wlan.sa == 3c:bd:c5:26:74:c3) or (wlan.sa == 80:f3:ef:63:35:01 and wlan.da == 3c:bd:c5:26:74:c3))

        3. The third filter is used to filter the captured frames to get *only* the **data frames** (uplink and downlink) that is coming from the **HMD** to the **server** or **AP** or going to the **HMD** from the **server** or **AP**. Some of the frames (***TYPE I***) that are going *from* the **HMD** *to* the **AP** does *not* have data, yet it is considered as **data frames**. These frames use *802.11a* (*OFDM*) protocol. There are other frames (***TYPE II***) transmitted between the **AP** and the **HMD** that *have* data and these frames usually use *802.11ax* (*HE*) protocol, yet there are a few of them (*from* the **HMD** *to* the **AP**) use *802.11a* (*OFDM*). The third type of frames (***TYPE III***) are the frames transmitted *from* the **server** *to* the **HMD** or the opposite. These frames *have* data (video frames or user tracking information) and they use *802.11ax* (*HE*) protocol.
        
            > wlan.fc.type eq 2 and ((wlan.sa == 80:f3:ef:63:35:01 and (wlan.da == 74:78:27:31:58:70 or wlan.da == 3c:bd:c5:26:74:c3 or wlan.da == 3c:bd:c5:26:74:c1)) or (wlan.da == 80:f3:ef:63:35:01 and (wlan.sa == 74:78:27:31:58:70 or wlan.sa == 3c:bd:c5:26:74:c3 or wlan.sa == 3c:bd:c5:26:74:c1)))  

            To split these three different types of **data frames**, we can use the following filters to create four different files:
            * This filter is used to filter the captured frames to get only the **data frames** (*QoS data*) that is coming *from* or going *to* the **server** or the **HMD** (***TYPE III***). These frames include *QoS data*.

                > wlan.fc.type eq 2 and ((wlan.sa == 80:f3:ef:63:35:01 and wlan.da == 74:78:27:31:58:70) or (wlan.da == 80:f3:ef:63:35:01 and wlan.sa == 74:78:27:31:58:70))

            *  This filter is used to filter the captured frames to get *only* the **data frames** (*QoS data*) that is coming *from* or going *to* the **AP** or the **HMD** (***TYPE II***). These frames include *QoS data*. These frames are used to keep track of the status of the *STAs*. In this case, the **HMD** use these frame to report the buffer status.

                > wlan.fc.type eq 2 and ((wlan.sa == 80:f3:ef:63:35:01 and wlan.da == 3c:bd:c5:26:74:c1 ) or (wlan.da == 80:f3:ef:63:35:01 and wlan.sa == 3c:bd:c5:26:74:c1))

            *  This filter is used to filter the captured frames to get *only* the **data frames** that is going *to* the **AP** *from* the **HMD**. The frames that does *not* have data (***TYPE I***). These frames usually are used by the *STAs* for power management, such as telling the **AP** that tha *STA* is going to sleep and wake up.

                > wlan.fc.type eq 2 and ((wlan.sa == 80:f3:ef:63:35:01 and wlan.da == 3c:bd:c5:26:74:c3 ) or (wlan.da == 80:f3:ef:63:35:01 and wlan.sa == 3c:bd:c5:26:74:c3))

            * This is used to filter the captured frames to get *only* the **data frames** (*QoS data*) that is coming *from* the **server** or **AP** and going *to* the **HMD** or the opposite (***TYPE III*** and ***II***). These frames include *QoS data*.

                > wlan.fc.type eq 2 and ((wlan.sa == 80:f3:ef:63:35:01 and (wlan.da == 74:78:27:31:58:70 or wlan.da == 3c:bd:c5:26:74:c1)) or (wlan.da == 80:f3:ef:63:35:01 and (wlan.sa == 74:78:27:31:58:70 or wlan.sa == 3c:bd:c5:26:74:c1)))

        4. The fourth filter is used to filter the captured frames to get *only* the **re-transmitted data frames** (*uplink* and *downlink*) that is coming *from* The **HMD** *to* the **server** or **AP** or going *to* the **HMD** *from* the **server** or **AP**. Some of the frames use *802.11a* (*OFDM*) protocol and the others use *802.11ax* (*HE*) protocol. 
            
            > wlan.fc.retry == 1 and ((wlan.sa == 80:f3:ef:63:35:01 and (wlan.da == 74:78:27:31:58:70 or wlan.da == 3c:bd:c5:26:74:c3 or wlan.da == 3c:bd:c5:26:74:c1)) or (wlan.da == 80:f3:ef:63:35:01 and (wlan.sa == 74:78:27:31:58:70 or wlan.sa == 3c:bd:c5:26:74:c3 or wlan.sa == 3c:bd:c5:26:74:c1)))

            To split these **re-transmitted data frames** based on the categories mentioned in (c), we can use the following filters to create four different files:
            * This filter is used to filter the captured frames to get *only* the **re-transmitted data frames** (*QoS data*) that is coming *from* or going *to* the **server** or the **HMD** (***TYPE III***). These frames include *QoS data*

                > wlan.fc.retry == 1 and ((wlan.sa == 80:f3:ef:63:35:01 and wlan.da == 74:78:27:31:58:70) or (wlan.da == 80:f3:ef:63:35:01 and wlan.sa == 74:78:27:31:58:70))

            * This filter is used to filter the captured frames to get *only* the **re-transmitted data frames** (*QoS data*) that is coming *from* or going *to* the **AP** or the **HMD** (***TYPE II***). These frames include *QoS data*.

                > wlan.fc.retry == 1 and ((wlan.sa == 80:f3:ef:63:35:01 and wlan.da == 3c:bd:c5:26:74:c1 ) or (wlan.da == 80:f3:ef:63:35:01 and wlan.sa == 3c:bd:c5:26:74:c1))

            * This filter is used to filter the captured frames to get *only* the **re-transmitted data frames** that is coming *from* or going *to* the **AP** or the **HMD**. The frames that does *not* have *data* (***TYPE I***).

                > wlan.fc.retry == 1 and ((wlan.sa == 80:f3:ef:63:35:01 and wlan.da == 3c:bd:c5:26:74:c3 ) or (wlan.da == 80:f3:ef:63:35:01 and wlan.sa == 3c:bd:c5:26:74:c3))

            * This filter is used to filter the captured frames to get *only* the **re-transmitted data frames** (*QoS data*) that is coming *from* the **server** or **AP** and going *to* the **HMD** or the opposite (***TYPE III*** and **II**). These frames include *QoS data*.

                > wlan.fc.retry == 1 and ((wlan.sa == 80:f3:ef:63:35:01 and (wlan.da == 74:78:27:31:58:70 or wlan.da == 3c:bd:c5:26:74:c1)) or (wlan.da == 80:f3:ef:63:35:01 and (wlan.sa == 74:78:27:31:58:70 or wlan.sa == 3c:bd:c5:26:74:c1)))

                
---

* ***useful links***: 
    - [OVR Metrics Tool Stats Definition Guide](https://developer.oculus.com/documentation/unity/ts-ovrstats/) 
    - [VrApi Stats Definition Guide](https://developer.oculus.com/documentation/native/android/ts-logcat-stats/)
