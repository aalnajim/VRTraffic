from os import listdir
from os.path import isfile, join


def convertTime(time):
    # this method convert the time to ms from the beginning of the day
    splittedTime = time.split(":")
    if(len(splittedTime)>2):
        timeInMs = float(splittedTime[0])*60*60*1000 + float(splittedTime[1])*60*1000 + float(splittedTime[2])*1000
    else:
        timeInMs = float(splittedTime[0])*60*60*1000 + float(splittedTime[1])*60*1000 
    return timeInMs


def processSessionLog(sessionLogFilePath,startTime,endTime):
    # Experiment Info Parameters
    Vsync2Photons = 0 # time from vsync to photon in seconds
    refreshRate = 0 # the targeted refresh rate
    renderTarget = {'horizontal' : 0,'vertical':0}
    startTimeInMs = convertTime(startTime)
    endTimeInMs = convertTime(endTime)
    oldExpermintInfo = ""
    firstTime = 0


    # Statistics Parameters 
    times = []
    totalVideoPkts = []
    videoPktsPerSecond = []
    videoMbytesTotal = []
    videoMbitsPerSec = []
    totalLatencyMs = []
    networkLatencyMs = []
    encodeLatencyMs = []
    decodeLatencyMs = []
    fecPercentage = [] # forward error correction 
    fecErrorsTotal = [] 
    fecErrorsPerSec = []
    clientFPS = []
    serverFPS = []
    batteryPercentageHMD = []




    # GraphStatistics Parameters (all times in ms)
    gTimes = []
    totalPipelineLatencyS = []  
    gameTimeS = []
    serverCompositorS = []
    encoderS = []
    networkS = []
    decoderS = []
    decoderQueueS = []
    clientCompositorS = []
    vsyncQueueS = []
    gClientFPS = []
    gServerFPS = []



    with open(sessionLogFilePath,'r') as f:
        lines = f.readlines()
        counter = 0
        isFirstTime = True
        print("session_log.txt file processing \nExpermint Info:")
        for line in lines:
            words = line.split(":")
            currentTimeInMs = convertTime("{}:{}:{}".format(words[0].strip(),words[1].strip(),words[2].split(" ")[0].strip()))
            if(currentTimeInMs>=startTimeInMs and currentTimeInMs <= endTimeInMs):
                if(isFirstTime):
                    isFirstTime = False
                    firstTime = currentTimeInMs
                if "Render Target" in line:
                    value = words[3].split(" ")
                    renderTarget['horizontal'] = value[1].strip()
                    renderTarget['vertical'] = value[2].strip()
                    counter = counter + 1
                    if(counter == 3):
                        counter = 0
                        ExpermintInfo= "Vsync2Photons={}ms, RefreshRate={}Hz, Resolution=({}x{})".format(float(Vsync2Photons) * 1000,refreshRate,renderTarget["horizontal"],renderTarget["vertical"])
                        if ExpermintInfo != oldExpermintInfo:
                            print(ExpermintInfo)
                            oldExpermintInfo = ExpermintInfo
                elif "from Vsync to Photons" in line:
                    value = words[3].split(" ")
                    Vsync2Photons = value[1].strip()
                    counter = counter + 1
                    if(counter == 3):
                        counter = 0
                        ExpermintInfo= "Vsync2Photons={}ms, RefreshRate={}Hz, Resolution=({}x{})".format(float(Vsync2Photons) * 1000,refreshRate,renderTarget["horizontal"],renderTarget["vertical"])
                        if ExpermintInfo != oldExpermintInfo:
                            print(ExpermintInfo)
                            oldExpermintInfo = ExpermintInfo
                elif "Refresh Rate" in line:
                    value = words[3].split(" ")
                    refreshRate = value[1].strip()
                    counter = counter + 1
                    if(counter == 3):
                        counter = 0
                        ExpermintInfo= "Vsync2Photons={}ms, RefreshRate={}Hz, Resolution=({}x{})".format(float(Vsync2Photons) * 1000,refreshRate,renderTarget["horizontal"],renderTarget["vertical"])
                        if ExpermintInfo != oldExpermintInfo:
                            print(ExpermintInfo)
                            oldExpermintInfo = ExpermintInfo
                elif "GraphStatistics" in line:
                    splittedLine = line.split(" ")
                    splittedLine = splittedLine[2].split(":")
                    gTimes.append(currentTimeInMs)
                    totalPipelineLatencyS.append(float(splittedLine[3].split(",")[0].strip())*1000)
                    gameTimeS.append(float(splittedLine[4].split(",")[0].strip())*1000)
                    serverCompositorS.append(float(splittedLine[5].split(",")[0].strip())*1000)
                    encoderS.append(float(splittedLine[6].split(",")[0].strip())*1000)
                    networkS.append(float(splittedLine[7].split(",")[0].strip())*1000)
                    decoderS.append(float(splittedLine[8].split(",")[0].strip())*1000)
                    decoderQueueS.append(float(splittedLine[9].split(",")[0].strip())*1000)
                    clientCompositorS.append(float(splittedLine[10].split(",")[0].strip())*1000)
                    vsyncQueueS.append(float(splittedLine[11].split(",")[0].strip())*1000)
                    gClientFPS.append(float(splittedLine[12].split(",")[0].strip()))
                    gServerFPS.append(float(splittedLine[13].split(",")[0].split("}")[0].strip()))
                elif "Statistics" in line:
                    splittedLine = line.split(" ")
                    splittedLine = splittedLine[2].split(":")
                    times.append(currentTimeInMs)
                    totalVideoPkts.append(float(splittedLine[3].split(",")[0].strip()))
                    videoPktsPerSecond.append(float(splittedLine[4].split(",")[0].strip()))
                    videoMbytesTotal.append(float(splittedLine[5].split(",")[0].strip()))
                    videoMbitsPerSec.append(float(splittedLine[6].split(",")[0].strip()))
                    totalLatencyMs.append(float(splittedLine[7].split(",")[0].strip()))
                    networkLatencyMs.append(float(splittedLine[8].split(",")[0].strip()))
                    encodeLatencyMs.append(float(splittedLine[9].split(",")[0].strip()))
                    decodeLatencyMs.append(float(splittedLine[10].split(",")[0].strip()))
                    fecPercentage.append(float(splittedLine[11].split(",")[0].strip()))
                    fecErrorsTotal.append(float(splittedLine[12].split(",")[0].strip()))
                    fecErrorsPerSec.append(float(splittedLine[13].split(",")[0].strip()))
                    clientFPS.append(float(splittedLine[14].split(",")[0].strip()))
                    serverFPS.append(float(splittedLine[15].split(",")[0].strip()))
                    batteryPercentageHMD.append(float(splittedLine[16].split(",")[0].split("}")[0].strip()))
    print("---------------------")


def processOVRMetricsFolder(OVRMetricsFolderPath,startTime,endTime):
    startTimeInMs = convertTime(startTime)
    endTimeInMs = convertTime(endTime)
    OVRMetricsResults = [] # a list of lists of tuples, each sublist containt the metrices of a file in the form of tuples
    for fileName in listdir(OVRMetricsFolderPath):
        fileTime = fileName.split("_")[1].split(".")[0]
        fileHour = fileTime[:2]
        fileMinute = fileTime[2:4]
        fileSecond = fileTime[4:]
        fileTimeInMs = convertTime("{}:{}:{}".format(fileHour,fileMinute,fileSecond))
        if(fileTimeInMs>=startTimeInMs and fileTimeInMs<=endTimeInMs):
            print("OVRMetrics files: \n{} file processing".format(fileName))
            currentFilePath = "{}/{}".format(OVRMetricsFolderPath,fileName)
            with open(currentFilePath,'r') as f:
                lines = f.readlines()
                currentFileMetrices = [] # a list of tuples, each tuple represent the metrices of the current file at a specific time stamp
                isHeader = True
                for line in lines:
                    if(isHeader):
                        isHeader = False 
                        continue
                    
                    splittedLine = line.split(",") 
                    Time_Stamp = splittedLine[0]
                    battery_level_percentage = splittedLine[3]
                    battery_temperature_celcius = splittedLine[4]
                    sensor_temperature_celcius = splittedLine[6]
                    power_level_state = splittedLine[8]
                    average_frame_rate = splittedLine[18]
                    display_refresh_rate = splittedLine[19]
                    average_prediction_milliseconds = splittedLine[20]
                    early_frame_count = splittedLine[22]
                    stale_frame_count = splittedLine[23]
                    maximum_rotational_speed_degrees_per_second = splittedLine[24]
                    foveation_level = splittedLine[25]
                    eye_buffer_width = splittedLine[26]
                    eye_buffer_height = splittedLine[27]
                    app_gpu_time_microseconds = splittedLine[28]
                    timewarp_gpu_time_microseconds = splittedLine[29]
                    guardian_gpu_time_microseconds = splittedLine[30]
                    cpu_utilization_percentage = splittedLine[31]
                    gpu_utilization_percentage = splittedLine[40]
                    stale_frames_consecutive = splittedLine[49]
                    screen_power_consumption = splittedLine[65]
                    vrshell_average_frame_rate = splittedLine[84]
                    vrshell_gpu_time_microseconds = splittedLine[85]
                    vrshell_and_guardian_gpu_time_microseconds = splittedLine[86]
                    render_scale = splittedLine[87].strip()
                    
                    currentTimeStampTuple = (Time_Stamp,battery_level_percentage,battery_temperature_celcius,sensor_temperature_celcius,power_level_state,
                                                average_frame_rate,display_refresh_rate,average_prediction_milliseconds,early_frame_count,stale_frame_count,
                                                maximum_rotational_speed_degrees_per_second,foveation_level,eye_buffer_width,eye_buffer_height,
                                                app_gpu_time_microseconds,timewarp_gpu_time_microseconds,guardian_gpu_time_microseconds,cpu_utilization_percentage,
                                                gpu_utilization_percentage,stale_frames_consecutive,screen_power_consumption,vrshell_average_frame_rate,
                                                vrshell_gpu_time_microseconds,vrshell_and_guardian_gpu_time_microseconds,render_scale)
                    currentFileMetrices.append(currentTimeStampTuple)
            


            OVRMetricsResults.append(currentFileMetrices)
    
    print("---------------------") 


def processLogcat(logcatFilePath,startTime,endTime):
    startTimeInMs = convertTime(startTime)
    endTimeInMs = convertTime(endTime)
    time = []
    targetedFPS = []
    achievedFPS = []
    predictionTime = [] # this is the absolute time in (ms) between when an app queries the pose before rendering and the time the frame is displayed on the HMD screen
    tear = []  # the number of screen tears
    earlyFrames = [] # number of frames delivered before they were needed
    staleFrames = [] # the number of times a frame wasn’t delivered on time, and the previous frame was used instead
    fov = [] # indicates the level of Fixed Foveated Rendering (FFR) intensity
    CPUClockLevel, GPUClockLevel = ([] for i in range(2)) # specifies the CPU and GPU clock levels set by the app out of 4 (4 is very high and is a bottleneck)
    PLS = [] # indicates the current power level of the device: NORMAL (0), SAVE (1), and DANGER (2)
    batteryTemperature, sensorTemperature= ([] for i in range(2)) # indicate the battery and sensor temperature in celsius.
    TWTime = [] # displays the ATW GPU time in (ms), which is the amount of time ATW takes to render (correlates to the number of layers used 'LCnt' and their complexity)
    appTime = [] # displays the app GPU time in (ms), which is the amount of time the application spends rendering a single frame. If this time is longer than a single frame’s length (13.88ms for 72 frames per second), the app is GPU bound. Otherwise, the app is probably CPU bound
    guardianTime = [] # displays the Guardian GPU time in (ms), which is the amount of GPU time used by the Guardian boundary
    CPUandGPUTime = [] # displays the total time in (ms) it took to render a frame (CPUandGPUTime - App GPU time "appTime" = approximate clock time for the render thread)
    LCnt = [] # specifies the number of layers that ATW is rendering per frame, including system layers (affect TWTime and guardianTime)
    GPUUtilization = [] # displays the GPU utilization percentage
    CPUUtilizationAverage =[] # displays the average utilization percentage of all CPU cores
    CPUUtilizationWorst = [] # displays the utilization percentage of the worst-performing core

    with open(logcatFilePath,'r') as f:
        lines = f.readlines()
        print("{} file processing".format(logcatFilePath))
        for line in lines:
            if ("beginning" in line):
                continue
            words = line.split(" ")
            currentTimeInMs = convertTime(words[1])
            if(currentTimeInMs>=startTimeInMs and currentTimeInMs <= endTimeInMs and 'Prd=' in line):        
                matrices = words[len(words)-1]
                splittedMatrices = matrices.split(",")
                time.append(currentTimeInMs)
                targetedFPS.append(splittedMatrices[0].split("=")[1].split("/")[1])
                achievedFPS.append(splittedMatrices[0].split("=")[1].split("/")[0])
                predictionTime.append(splittedMatrices[1].split("=")[1].replace("ms",""))
                tear.append(splittedMatrices[2].split("=")[1])
                earlyFrames.append(splittedMatrices[3].split("=")[1])
                staleFrames.append(splittedMatrices[4].split("=")[1])
                fov.append(splittedMatrices[7].split("=")[1].replace("D",""))
                CPUClockLevel.append(splittedMatrices[8].split("=")[1].split("/")[0])
                GPUClockLevel.append(splittedMatrices[8].split("=")[1].split("/")[1])
                PLS.append(splittedMatrices[15].split("=")[1])
                batteryTemperature.append(splittedMatrices[16].split("=")[1].split("/")[0].replace("C",""))
                sensorTemperature.append(splittedMatrices[16].split("=")[1].split("/")[1].replace("C",""))
                TWTime.append(splittedMatrices[17].split("=")[1].replace("ms",""))
                appTime.append(splittedMatrices[18].split("=")[1].replace("ms",""))
                guardianTime.append(splittedMatrices[19].split("=")[1].replace("ms",""))
                CPUandGPUTime.append(splittedMatrices[20].split("=")[1].replace("ms",""))
                LCnt.append(splittedMatrices[21].split("=")[1].split("(")[0])
                GPUUtilization.append(str(round(float(splittedMatrices[23].split("=")[1])*100,2)))
                CPUUtilizationAverage.append(str(round(float(splittedMatrices[24].split("=")[1].split("(")[0])*100,2)))
                CPUUtilizationWorst.append(str(round(float(splittedMatrices[24].split("=")[1].split("(")[1].split(")")[0].replace("W",""))*100,2)))


def main():
    
    startTime = "22:00"
    endTime = "22:05"
    sessionLogFilePath = 'session_log.txt'
    OVRMetricsFolderPath = 'OVRMetrics'
    logcatFilePath = 'logcat3.txt'
    processSessionLog(sessionLogFilePath,startTime,endTime)
    processOVRMetricsFolder(OVRMetricsFolderPath,startTime,endTime)
    processLogcat(logcatFilePath,startTime,endTime)


if __name__ == "__main__":
   main()