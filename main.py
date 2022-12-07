import sys
from os import listdir
from os.path import isfile, join
import plotGraph


def convertTime(time):
    # this method convert the time to ms from the beginning of the day
    splittedTime = time.split(":")
    if(len(splittedTime)>2):
        timeInMs = float(splittedTime[0])*60*60*1000 + float(splittedTime[1])*60*1000 + float(splittedTime[2])*1000
    else:
        timeInMs = float(splittedTime[0])*60*60*1000 + float(splittedTime[1])*60*1000 
    return timeInMs


def processSessionLog(sessionLogFilePath,startTimeInMs,endTimeInMs):
    # Experiment Info Parameters
    Vsync2Photons = 0 # time from vsync to photon in seconds
    refreshRate = 0 # the targeted refresh rate
    renderTarget = {'horizontal' : 0,'vertical':0}
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
    return((times,totalVideoPkts,videoPktsPerSecond,videoMbytesTotal,videoMbitsPerSec,totalLatencyMs,networkLatencyMs,encodeLatencyMs,
                decodeLatencyMs,fecPercentage,fecErrorsTotal,fecErrorsPerSec,clientFPS,serverFPS,batteryPercentageHMD),
           (gTimes,totalPipelineLatencyS,gameTimeS,serverCompositorS,encoderS,networkS,decoderS,decoderQueueS,clientCompositorS,
                vsyncQueueS,gClientFPS,gServerFPS)) # two tuples


def processOVRMetricsFolder(OVRMetricsFolderPath,startTimeInMs,endTimeInMs):
    #OVRMetricsResults = [] # a list of tuples of lists, each sublist containt the metrices of a file in the form of tuples
    Time_Stamp                                  = [] # a list of time stamps
    battery_level_percentage                    = [] # a list of battery level percentages
    battery_temperature_celcius                 = [] # a list of battery temperatures in celcius
    sensor_temperature_celcius                  = [] # a list of sensor temperatures celcius
    power_level_state                           = [] # a list of power level states
    average_frame_rate                          = [] # a list of average frame rates
    display_refresh_rate                        = [] # a list of display refresh rates
    average_prediction_milliseconds             = [] # a list of averages of prediction time in milliseconds
    early_frame_count                           = [] # a list of early frame counts
    stale_frame_count                           = [] # a list of stale frame counts
    maximum_rotational_speed_degrees_per_second = [] # a list of maximums of rotational speed degrees per second
    foveation_level                             = [] # a list of foveation levels
    eye_buffer_width                            = [] # a list of eye buffer widths (resolution)
    eye_buffer_height                           = [] # a list of eye buffer heights (resolution)
    app_gpu_time_microseconds                   = [] # a list of app gpu times microseconds
    timewarp_gpu_time_microseconds              = [] # a list of timewarp gpu times microseconds
    guardian_gpu_time_microseconds              = [] # a list of guardian gpu times microseconds
    cpu_utilization_percentage                  = [] # a list of cpu utilization percentages
    gpu_utilization_percentage                  = [] # a list of gpu utilization percentages
    stale_frames_consecutive                    = [] # a list of stale frames consecutives
    screen_power_consumption                    = [] # a list of screen power consumptions
    vrshell_average_frame_rate                  = [] # a list of vrshell average frame rates
    vrshell_gpu_time_microseconds               = [] # a list of vrshell gpu times in microseconds
    vrshell_and_guardian_gpu_time_microseconds  = [] # a list of vrshell and guardian gpu times in microseconds
    render_scale                                = [] # a list of render scale (where 100 mean original)

    print("OVRMetrics files:")
    for fileName in listdir(OVRMetricsFolderPath):
        fileTime = fileName.split("_")[1].split(".")[0]
        fileHour = fileTime[:2]
        fileMinute = fileTime[2:4]
        fileSecond = fileTime[4:]
        fileTimeInMs = convertTime("{}:{}:{}".format(fileHour,fileMinute,fileSecond))
        if(fileTimeInMs>=startTimeInMs and fileTimeInMs<=endTimeInMs):
            print("{} file processing".format(fileName))
            currentFilePath = "{}/{}".format(OVRMetricsFolderPath,fileName)
            with open(currentFilePath,'r') as f:
                lines = f.readlines()
                isHeader = True
                for line in lines:
                    if(isHeader):
                        isHeader = False 
                        continue
                    
                    splittedLine = line.split(",") 
                    Time_Stamp.append(splittedLine[0])
                    battery_level_percentage.append(splittedLine[3])
                    battery_temperature_celcius.append(splittedLine[4])
                    sensor_temperature_celcius.append(splittedLine[6])
                    power_level_state.append(splittedLine[8])
                    average_frame_rate.append(splittedLine[18])
                    display_refresh_rate.append(splittedLine[19])
                    average_prediction_milliseconds.append(splittedLine[20])
                    early_frame_count.append(splittedLine[22])
                    stale_frame_count.append(splittedLine[23])
                    maximum_rotational_speed_degrees_per_second.append(splittedLine[24])
                    foveation_level.append(splittedLine[25])
                    eye_buffer_width.append(splittedLine[26])
                    eye_buffer_height.append(splittedLine[27])
                    app_gpu_time_microseconds.append(splittedLine[28])
                    timewarp_gpu_time_microseconds.append(splittedLine[29])
                    guardian_gpu_time_microseconds.append(splittedLine[30])
                    cpu_utilization_percentage.append(splittedLine[31])
                    gpu_utilization_percentage.append(splittedLine[40])
                    stale_frames_consecutive.append(splittedLine[49])
                    screen_power_consumption.append(splittedLine[65])
                    vrshell_average_frame_rate.append(splittedLine[84])
                    vrshell_gpu_time_microseconds.append(splittedLine[85])
                    vrshell_and_guardian_gpu_time_microseconds.append(splittedLine[86])
                    render_scale.append(splittedLine[87].strip())
    
    
    print("---------------------") 
    return(Time_Stamp,battery_level_percentage,battery_temperature_celcius,sensor_temperature_celcius,power_level_state,
                average_frame_rate,display_refresh_rate,average_prediction_milliseconds,early_frame_count,stale_frame_count,
                maximum_rotational_speed_degrees_per_second,foveation_level,eye_buffer_width,eye_buffer_height,
                app_gpu_time_microseconds,timewarp_gpu_time_microseconds,guardian_gpu_time_microseconds,cpu_utilization_percentage,
                gpu_utilization_percentage,stale_frames_consecutive,screen_power_consumption,vrshell_average_frame_rate,
                vrshell_gpu_time_microseconds,vrshell_and_guardian_gpu_time_microseconds,render_scale)



# def processOVRMetricsFolder(OVRMetricsFolderPath,startTime,endTime):
#     startTimeInMs = convertTime(startTime)
#     endTimeInMs = convertTime(endTime)
#     OVRMetricsResults = [] # a list of lists of tuples, each sublist containt the metrices of a file in the form of tuples
#     for fileName in listdir(OVRMetricsFolderPath):
#         fileTime = fileName.split("_")[1].split(".")[0]
#         fileHour = fileTime[:2]
#         fileMinute = fileTime[2:4]
#         fileSecond = fileTime[4:]
#         fileTimeInMs = convertTime("{}:{}:{}".format(fileHour,fileMinute,fileSecond))
#         if(fileTimeInMs>=startTimeInMs and fileTimeInMs<=endTimeInMs):
#             print("OVRMetrics files: \n{} file processing".format(fileName))
#             currentFilePath = "{}/{}".format(OVRMetricsFolderPath,fileName)
#             with open(currentFilePath,'r') as f:
#                 lines = f.readlines()
#                 currentFileMetrices = [] # a list of tuples, each tuple represent the metrices of the current file at a specific time stamp
#                 isHeader = True
#                 for line in lines:
#                     if(isHeader):
#                         isHeader = False 
#                         continue
                    
#                     splittedLine = line.split(",") 
#                     Time_Stamp = splittedLine[0]
#                     battery_level_percentage = splittedLine[3]
#                     battery_temperature_celcius = splittedLine[4]
#                     sensor_temperature_celcius = splittedLine[6]
#                     power_level_state = splittedLine[8]
#                     average_frame_rate = splittedLine[18]
#                     display_refresh_rate = splittedLine[19]
#                     average_prediction_milliseconds = splittedLine[20]
#                     early_frame_count = splittedLine[22]
#                     stale_frame_count = splittedLine[23]
#                     maximum_rotational_speed_degrees_per_second = splittedLine[24]
#                     foveation_level = splittedLine[25]
#                     eye_buffer_width = splittedLine[26]
#                     eye_buffer_height = splittedLine[27]
#                     app_gpu_time_microseconds = splittedLine[28]
#                     timewarp_gpu_time_microseconds = splittedLine[29]
#                     guardian_gpu_time_microseconds = splittedLine[30]
#                     cpu_utilization_percentage = splittedLine[31]
#                     gpu_utilization_percentage = splittedLine[40]
#                     stale_frames_consecutive = splittedLine[49]
#                     screen_power_consumption = splittedLine[65]
#                     vrshell_average_frame_rate = splittedLine[84]
#                     vrshell_gpu_time_microseconds = splittedLine[85]
#                     vrshell_and_guardian_gpu_time_microseconds = splittedLine[86]
#                     render_scale = splittedLine[87].strip()
                    
#                     currentTimeStampTuple = (Time_Stamp,battery_level_percentage,battery_temperature_celcius,sensor_temperature_celcius,power_level_state,
#                                                 average_frame_rate,display_refresh_rate,average_prediction_milliseconds,early_frame_count,stale_frame_count,
#                                                 maximum_rotational_speed_degrees_per_second,foveation_level,eye_buffer_width,eye_buffer_height,
#                                                 app_gpu_time_microseconds,timewarp_gpu_time_microseconds,guardian_gpu_time_microseconds,cpu_utilization_percentage,
#                                                 gpu_utilization_percentage,stale_frames_consecutive,screen_power_consumption,vrshell_average_frame_rate,
#                                                 vrshell_gpu_time_microseconds,vrshell_and_guardian_gpu_time_microseconds,render_scale)
#                     currentFileMetrices.append(currentTimeStampTuple)
            


#             OVRMetricsResults.append(currentFileMetrices)
    
#     print("---------------------") 


def processLogcat(logcatFilePath,startTimeInMs,endTimeInMs):
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
    CPUandGPUTime = [] # displays the total time in (ms) it took to render a frame (CPUandGPUTime - App GPU time "appTime" = approximate clock time for the rendering thread)
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
    return (time,targetedFPS,achievedFPS,predictionTime,tear,earlyFrames,staleFrames,fov,CPUClockLevel,GPUClockLevel,PLS,batteryTemperature, 
                sensorTemperature,TWTime,appTime,guardianTime,CPUandGPUTime,LCnt,GPUUtilization,CPUUtilizationAverage,CPUUtilizationWorst)


def processVRMonitorLogFile(filePath,startTimeInMs,endTimeInMs):
    appPerformanceStatsTimeStamp        = [] # the time stamp for these performance stats
    appID                               = [] # the application id
    NumFramePresents                    = [] # shows how many frames are presented in the application
    NumDroppedFrames                    = [] # shows how many frames are dropped in the application
    NumReprojected                      = [] # shows how many frames are reprojected in the application by timewarp
    NumFramePresentsOnStartup           = [] # shows how many frames are presented during the startup of the application
    NumDroppedFramesOnStartup           = [] # shows how many frames are dropped during the startup of the application
    NumReprojectedFramesOnStartup       = [] # shows how many frames are reprojected during the startup of the application by timewarp
    NumLoading                          = [] # shows how many loadings occur while using the application
    NumFramePresentsLoading             = [] # shows how many frames are presented during the loadings
    NumDroppedFramesLoading             = [] # shows how many frames are dropped during the loadings
    NumReprojectedFramesLoading         = [] # shows how many frames are reprojected during the loadings by timewarp
    NumTimedOut                         = [] # shows how many TimedOuts occur while using the application
    NumFramePresentsTimedOut            = [] # shows how many frames are presented during the TimesOuts
    NumDroppedFramesTimedOut            = [] # shows how many frames are dropped during the TimesOuts
    NumReprojectedFramesTimedOut        = [] # shows how many frames are reprojected during the TimedOuts by timewarp
    AvgSubmitsPerFrame                  = [] # shows how many times a frame is trasmitted in average (to measure the retransmission)
    AvgCompositorCPUTimeMS              = [] # shows the average CPU time in (ms) the compositor takes to finish a frame (overlay)
    AvgCompositorGPUTimeMS              = [] # shows the average GPU time in (ms) the compositor takes to finish a frame (overlay)
    AvgTargetFPS                        = [] # average Frame Per Second (FPS)
    AvgApplicationCPUTimeMS             = [] # shows the average CPU time in (ms) the application takes to finish a frame (overlay)
    AvgApplicationGPUTimeMS             = [] # shows the average GPU time in (ms) the application takes to finish a frame (overlay)
    AppSeconds                          = [] # shows the duration of the app in seconds (how long the app is run)
    AppHeadsetActiveSeconds             = [] # shows the duration of the app in seconds (how long the app is run) while the HMD is active
    # additional stats
    NumSingleDroppedFramesOverEntireRun = [] # shows how many single frames are dropped in the entire run
    Num2DroppedFramesOverEntireRun      = [] # shows how many two frames are dropped in the entire run
    Num3DroppedFramesOverEntireRun      = [] # shows how many three frames are dropped in the entire run
    Num4MoreDroppedFramesOverEntireRun  = [] # shows how many four or more frames are dropped in the entire run
    totalNumOfFramesEntireRun           = [] # shows how many total frames are received in the entire run
    totalNumOfExpectedFrameEntireRun    = [] # shows how many total frames are expected to be received in the entire run

    isStatistics = False
    overallFramesStatsFlag = False
    statisticsText = ""

    print("{} file processing".format(filePath))
    with open(filePath,'r') as f:
        lines = f.readlines()
        for line in lines:
            if ("App Performance Stats:" in line):
                time = convertTime(line.split(" ")[4])
                if(time < startTimeInMs or time > endTimeInMs):
                    continue
                isStatistics = True
                statisticsText = statisticsText + str(time)
            elif (isStatistics):
                if("AppHeadsetActiveSeconds" not in line):
                    splittedLine = line.split(" - ")
                    statisticsText = statisticsText + ","+ splittedLine[1].strip()
                else:
                    isStatistics = False
                    overallFramesStatsFlag = True
                    splittedLine = line.split(" - ")
                    statisticsText = statisticsText + ","+ splittedLine[1].strip()
            elif(overallFramesStatsFlag):
                if("Drops over entire run" in line):
                    overallFramesStatsFlag = False
                    splittedLine = line.split("-")
                    statisticsText = statisticsText + ",{},{},{},{},{},{}\n".format(splittedLine[2].strip().split(" ")[0],
                                        splittedLine[3].strip().split(" ")[0],splittedLine[4].strip().split(" ")[0],
                                        splittedLine[5].strip().split(" ")[0],splittedLine[6].strip().split(" ")[1],
                                        splittedLine[6].strip().split(" ")[3]) 


    splittedStatisticsText = statisticsText.split("\n")
    for tuple in splittedStatisticsText:
        if(len(tuple)>1):
            values = tuple.split(",")
            appPerformanceStatsTimeStamp.append(values[0])
            appID.append(values[1].split(":")[1].strip())
            NumFramePresents.append(values[2].split(":")[1].strip())
            NumDroppedFrames.append(values[3].split(":")[1].strip())
            NumReprojected.append(values[4].split(":")[1].strip())
            NumFramePresentsOnStartup.append(values[5].split(":")[1].strip())
            NumDroppedFramesOnStartup.append(values[6].split(":")[1].strip())
            NumReprojectedFramesOnStartup.append(values[7].split(":")[1].strip())
            NumLoading.append(values[8].split(":")[1].strip())
            NumFramePresentsLoading.append(values[9].split(":")[1].strip())
            NumDroppedFramesLoading.append(values[10].split(":")[1].strip())
            NumReprojectedFramesLoading.append(values[11].split(":")[1].strip())
            NumTimedOut.append(values[12].split(":")[1].strip())
            NumFramePresentsTimedOut.append(values[13].split(":")[1].strip())
            NumDroppedFramesTimedOut.append(values[14].split(":")[1].strip())
            NumReprojectedFramesTimedOut.append(values[15].split(":")[1].strip())
            AvgSubmitsPerFrame.append(values[16].split(":")[1].strip())
            AvgCompositorCPUTimeMS.append(values[17].split(":")[1].strip())
            AvgCompositorGPUTimeMS.append(values[18].split(":")[1].strip())
            AvgTargetFPS.append(values[19].split(":")[1].strip())
            AvgApplicationCPUTimeMS.append(values[20].split(":")[1].strip())
            AvgApplicationGPUTimeMS.append(values[21].split(":")[1].strip())
            AppSeconds.append(values[22].split(":")[1].strip())
            AppHeadsetActiveSeconds.append(values[23].split(":")[1].strip())
            # additional stats
            NumSingleDroppedFramesOverEntireRun.append(values[24].strip())
            Num2DroppedFramesOverEntireRun.append(values[25].strip())
            Num3DroppedFramesOverEntireRun.append(values[26].strip())
            Num4MoreDroppedFramesOverEntireRun.append(values[27].strip())
            totalNumOfFramesEntireRun.append(values[28].strip())
            totalNumOfExpectedFrameEntireRun.append(values[29].strip())
    
    
    return (appPerformanceStatsTimeStamp,appID,NumFramePresents
            ,NumDroppedFrames,NumReprojected,NumFramePresentsOnStartup,NumDroppedFramesOnStartup
            ,NumReprojectedFramesOnStartup,NumLoading,NumFramePresentsLoading,NumDroppedFramesLoading
            ,NumReprojectedFramesLoading,NumTimedOut,NumFramePresentsTimedOut,NumDroppedFramesTimedOut
            ,NumReprojectedFramesTimedOut,AvgSubmitsPerFrame,AvgCompositorCPUTimeMS,AvgCompositorGPUTimeMS
            ,AvgTargetFPS,AvgApplicationCPUTimeMS,AvgApplicationGPUTimeMS,AppSeconds,AppHeadsetActiveSeconds
            ,NumSingleDroppedFramesOverEntireRun,Num2DroppedFramesOverEntireRun,Num3DroppedFramesOverEntireRun
            ,Num4MoreDroppedFramesOverEntireRun,totalNumOfFramesEntireRun,totalNumOfExpectedFrameEntireRun)


# def processVRMonitorLogFile(filePath,appPerformanceStats,startTimeInMs,endTimeInMs):
#     appPerformanceStatsTimeStamp        = "" # the time stamp for these performance stats
#     appID                               = "" # the application id
#     NumFramePresents                    = "" # shows how many frames are presented in the application
#     NumDroppedFrames                    = "" # shows how many frames are dropped in the application
#     NumReprojected                      = "" # shows how many frames are reprojected in the application by timewarp
#     NumFramePresentsOnStartup           = "" # shows how many frames are presented during the startup of the application
#     NumDroppedFramesOnStartup           = "" # shows how many frames are dropped during the startup of the application
#     NumReprojectedFramesOnStartup       = "" # shows how many frames are reprojected during the startup of the application by timewarp
#     NumLoading                          = "" # shows how many loadings occur while using the application
#     NumFramePresentsLoading             = "" # shows how many frames are presented during the loadings
#     NumDroppedFramesLoading             = "" # shows how many frames are dropped during the loadings
#     NumReprojectedFramesLoading         = "" # shows how many frames are reprojected during the loadings by timewarp
#     NumTimedOut                         = "" # shows how many TimedOuts occur while using the application
#     NumFramePresentsTimedOut            = "" # shows how many frames are presented during the TimesOuts
#     NumDroppedFramesTimedOut            = "" # shows how many frames are dropped during the TimesOuts
#     NumReprojectedFramesTimedOut        = "" # shows how many frames are reprojected during the TimedOuts by timewarp
#     AvgSubmitsPerFrame                  = "" # shows how many times a frame is trasmitted in average (to measure the retransmission)
#     AvgCompositorCPUTimeMS              = "" # shows the average CPU time in (ms) the compositor takes to finish a frame (overlay)
#     AvgCompositorGPUTimeMS              = "" # shows the average GPU time in (ms) the compositor takes to finish a frame (overlay)
#     AvgTargetFPS                        = "" # average Frame Per Second (FPS)
#     AvgApplicationCPUTimeMS             = "" # shows the average CPU time in (ms) the application takes to finish a frame (overlay)
#     AvgApplicationGPUTimeMS             = "" # shows the average GPU time in (ms) the application takes to finish a frame (overlay)
#     AppSeconds                          = "" # shows the duration of the app in seconds (how long the app is run)
#     AppHeadsetActiveSeconds             = "" # shows the duration of the app in seconds (how long the app is run) while the HMD is active
#     # additional stats
#     NumSingleDroppedFramesOverEntireRun = "" # shows how many single frames are dropped in the entire run
#     Num2DroppedFramesOverEntireRun      = "" # shows how many two frames are dropped in the entire run
#     Num3DroppedFramesOverEntireRun      = "" # shows how many three frames are dropped in the entire run
#     Num4MoreDroppedFramesOverEntireRun  = "" # shows how many four or more frames are dropped in the entire run
#     totalNumOfFramesEntireRun           = "" # shows how many total frames are received in the entire run
#     totalNumOfExpectedFrameEntireRun    = "" # shows how many total frames are expected to be received in the entire run

#     isStatistics = False
#     overallFramesStatsFlag = False
#     statisticsText = ""

#     print("{} file processing".format(filePath.split("/")[1]))
#     with open(filePath,'r') as f:
#         lines = f.readlines()
#         for line in lines:
#             if ("App Performance Stats:" in line):
#                 time = convertTime(line.split(" ")[4])
#                 if(time < startTimeInMs or time > endTimeInMs):
#                     continue
#                 isStatistics = True
#                 statisticsText = statisticsText + str(time)
#             elif (isStatistics):
#                 if("AppHeadsetActiveSeconds" not in line):
#                     splittedLine = line.split(" - ")
#                     statisticsText = statisticsText + ","+ splittedLine[1].strip()
#                 else:
#                     isStatistics = False
#                     overallFramesStatsFlag = True
#                     splittedLine = line.split(" - ")
#                     statisticsText = statisticsText + ","+ splittedLine[1].strip()
#             elif(overallFramesStatsFlag):
#                 if("Drops over entire run" in line):
#                     overallFramesStatsFlag = False
#                     splittedLine = line.split("-")
#                     statisticsText = statisticsText + ",{},{},{},{},{},{}\n".format(splittedLine[2].strip().split(" ")[0],
#                                         splittedLine[3].strip().split(" ")[0],splittedLine[4].strip().split(" ")[0],
#                                         splittedLine[5].strip().split(" ")[0],splittedLine[6].strip().split(" ")[1],
#                                         splittedLine[6].strip().split(" ")[3]) 


#     splittedStatisticsText = statisticsText.split("\n")
#     for tuple in splittedStatisticsText:
#         if(len(tuple)>1):
#             values = tuple.split(",")
#             appPerformanceStatsTimeStamp        = values[0]
#             appID                               = values[1].split(":")[1].strip()
#             NumFramePresents                    = values[2].split(":")[1].strip()
#             NumDroppedFrames                    = values[3].split(":")[1].strip()
#             NumReprojected                      = values[4].split(":")[1].strip()
#             NumFramePresentsOnStartup           = values[5].split(":")[1].strip()
#             NumDroppedFramesOnStartup           = values[6].split(":")[1].strip()
#             NumReprojectedFramesOnStartup       = values[7].split(":")[1].strip()
#             NumLoading                          = values[8].split(":")[1].strip()
#             NumFramePresentsLoading             = values[9].split(":")[1].strip()
#             NumDroppedFramesLoading             = values[10].split(":")[1].strip()
#             NumReprojectedFramesLoading         = values[11].split(":")[1].strip()
#             NumTimedOut                         = values[12].split(":")[1].strip()
#             NumFramePresentsTimedOut            = values[13].split(":")[1].strip()
#             NumDroppedFramesTimedOut            = values[14].split(":")[1].strip()
#             NumReprojectedFramesTimedOut        = values[15].split(":")[1].strip()
#             AvgSubmitsPerFrame                  = values[16].split(":")[1].strip()
#             AvgCompositorCPUTimeMS              = values[17].split(":")[1].strip()
#             AvgCompositorGPUTimeMS              = values[18].split(":")[1].strip()
#             AvgTargetFPS                        = values[19].split(":")[1].strip()
#             AvgApplicationCPUTimeMS             = values[20].split(":")[1].strip()
#             AvgApplicationGPUTimeMS             = values[21].split(":")[1].strip()
#             AppSeconds                          = values[22].split(":")[1].strip()
#             AppHeadsetActiveSeconds             = values[23].split(":")[1].strip()
#             # additional stats
#             NumSingleDroppedFramesOverEntireRun = values[24].strip()
#             Num2DroppedFramesOverEntireRun      = values[25].strip()
#             Num3DroppedFramesOverEntireRun      = values[26].strip()
#             Num4MoreDroppedFramesOverEntireRun  = values[27].strip()
#             totalNumOfFramesEntireRun           = values[28].strip()
#             totalNumOfExpectedFrameEntireRun    = values[29].strip()
        
#             appPerformanceStatElement = (appPerformanceStatsTimeStamp,appID,NumFramePresents
#             ,NumDroppedFrames,NumReprojected,NumFramePresentsOnStartup,NumDroppedFramesOnStartup
#             ,NumReprojectedFramesOnStartup,NumLoading,NumFramePresentsLoading,NumDroppedFramesLoading
#             ,NumReprojectedFramesLoading,NumTimedOut,NumFramePresentsTimedOut,NumDroppedFramesTimedOut
#             ,NumReprojectedFramesTimedOut,AvgSubmitsPerFrame,AvgCompositorCPUTimeMS,AvgCompositorGPUTimeMS
#             ,AvgTargetFPS,AvgApplicationCPUTimeMS,AvgApplicationGPUTimeMS,AppSeconds,AppHeadsetActiveSeconds
#             ,NumSingleDroppedFramesOverEntireRun,Num2DroppedFramesOverEntireRun,Num3DroppedFramesOverEntireRun
#             ,Num4MoreDroppedFramesOverEntireRun,totalNumOfFramesEntireRun,totalNumOfExpectedFrameEntireRun)
#             appPerformanceStats.append(appPerformanceStatElement)


def processVRCompositorLogFile(filePath,appNames,startTimeInMs,endTimeInMs):
    appPerformanceStatsTimeStamp        = [] # the time stamp for these performance stats
    appName                             = [] # the application name
    appProcessID                        = [] # the application process id
    NumFramePresents                    = [] # shows how many frames are presented in the application
    NumDroppedFrames                    = [] # shows how many frames are dropped in the application
    NumReprojected                      = [] # shows how many frames are reprojected in the application by timewarp
    NumFramePresentsOnStartup           = [] # shows how many frames are presented during the startup of the application
    NumDroppedFramesOnStartup           = [] # shows how many frames are dropped during the startup of the application
    NumReprojectedFramesOnStartup       = [] # shows how many frames are reprojected during the startup of the application by timewarp
    NumLoading                          = [] # shows how many loadings occur while using the application
    NumFramePresentsLoading             = [] # shows how many frames are presented during the loadings
    NumDroppedFramesLoading             = [] # shows how many frames are dropped during the loadings
    NumReprojectedFramesLoading         = [] # shows how many frames are reprojected during the loadings by timewarp
    NumTimedOut                         = [] # shows how many TimedOuts occur while using the application
    NumFramePresentsTimedOut            = [] # shows how many frames are presented during the TimesOuts
    NumDroppedFramesTimedOut            = [] # shows how many frames are dropped during the TimesOuts
    NumReprojectedFramesTimedOut        = [] # shows how many frames are reprojected during the TimedOuts by timewarp
    AvgCompositorCPUTimeMS              = [] # shows the average CPU time in (ms) the compositor takes to finish a frame (overlay)
    AvgCompositorGPUTimeMS              = [] # shows the average GPU time in (ms) the compositor takes to finish a frame (overlay)
    AvgTargetFPS                        = [] # average Frame Per Second (FPS)
    AvgApplicationCPUTimeMS             = [] # shows the average CPU time in (ms) the application takes to finish a frame (overlay)
    AvgApplicationGPUTimeMS             = [] # shows the average GPU time in (ms) the application takes to finish a frame (overlay)
    # additional stats
    totalDroppedFramesOverEntireRun     = [] # shows how many frames are dropped in the entire run

    overallFramesStatsFlag = False
    isStatistics = False
    processIDs = []
    targetedAppsProcessIDs = {}
    processID = ""
    currentAppName = ""

    print("{} file processing".format(filePath))
    with open(filePath,'r') as f:
        lines = f.readlines()
        for line in lines:
            if("Lost pipe connection" in line):
                splittedLine = line.split(" ")
                currentAppName = splittedLine[10]
                for i in range (11,len(splittedLine)-1):
                    currentAppName = currentAppName + " " + splittedLine[i]
                if(currentAppName in appNames):
                    processID = splittedLine[len(splittedLine)-1].replace("(","").replace(")","").strip()
                    if processID not in processIDs:
                        processIDs.append(processID)
                        targetedAppsProcessIDs[processID] = currentAppName
            elif("Cumulative stats for pid:" in line):
                splittedLine = line.split(" ")
                processID = splittedLine[10].strip()
                time = convertTime(splittedLine[4]) #the stats time in (ms) from the beginning of the day
                if (time < startTimeInMs or time > endTimeInMs or processID not in targetedAppsProcessIDs):
                    continue
                else:
                    appPerformanceStatsTimeStamp.append(time)
                    appName.append(targetedAppsProcessIDs[processID])
                    appProcessID.append(processID)
                    isStatistics = True
            elif(isStatistics):
                if("#######" not in line):
                    values = line.split()
                    if(len(values)<1):
                        continue
                    if("Total" in line):
                        NumFramePresents.append(values[7].strip())
                        NumDroppedFrames.append(values[9].strip())
                        NumReprojected.append(values[11].strip())
                    elif("Startup" in line):
                        NumFramePresentsOnStartup.append(values[7].strip())
                        NumDroppedFramesOnStartup.append(values[9].strip())
                        NumReprojectedFramesOnStartup.append(values[11].strip())
                    elif("Loading" in line):
                        NumLoading.append(values[7].strip())
                        NumFramePresentsLoading.append(values[9].strip())
                        NumDroppedFramesLoading.append(values[11].strip())
                        NumReprojectedFramesLoading.append(values[13].strip())
                    elif("Timed out" in line):
                        NumTimedOut.append(values[8].strip())
                        NumFramePresentsTimedOut.append(values[10].strip())
                        NumDroppedFramesTimedOut.append(values[12].strip())
                        NumReprojectedFramesTimedOut.append(values[14].strip())
                    elif("Compositor Time" in line):
                        AvgCompositorCPUTimeMS.append(values[8].strip().replace("ms",""))
                        AvgCompositorGPUTimeMS.append(values[11].strip().replace("ms",""))
                    else:
                        AvgTargetFPS.append(values[10].strip())
                        AvgApplicationCPUTimeMS.append(values[13].strip().replace("ms",""))
                        AvgApplicationGPUTimeMS.append(values[16].strip().replace("ms",""))
                else:
                    isStatistics = False
                    overallFramesStatsFlag = True
            elif(overallFramesStatsFlag):
                values = line.split()
                overallFramesStatsFlag = False
                totalDroppedFramesOverEntireRun.append(values[9].strip())

    return (appPerformanceStatsTimeStamp,appName,appProcessID,NumFramePresents
            ,NumDroppedFrames,NumReprojected,NumFramePresentsOnStartup,NumDroppedFramesOnStartup
            ,NumReprojectedFramesOnStartup,NumLoading,NumFramePresentsLoading,NumDroppedFramesLoading
            ,NumReprojectedFramesLoading,NumTimedOut,NumFramePresentsTimedOut,NumDroppedFramesTimedOut
            ,NumReprojectedFramesTimedOut,AvgCompositorCPUTimeMS,AvgCompositorGPUTimeMS,AvgTargetFPS
            ,AvgApplicationCPUTimeMS,AvgApplicationGPUTimeMS,totalDroppedFramesOverEntireRun)


# def processVRCompositorLogFile(filePath,appNames,appPerformanceStats,startTimeInMs,endTimeInMs):
#     appPerformanceStatsTimeStamp        = "" # the time stamp for these performance stats
#     appName                             = "" # the application name
#     appProcessID                        = "" # the application process id
#     NumFramePresents                    = "" # shows how many frames are presented in the application
#     NumDroppedFrames                    = "" # shows how many frames are dropped in the application
#     NumReprojected                      = "" # shows how many frames are reprojected in the application by timewarp
#     NumFramePresentsOnStartup           = "" # shows how many frames are presented during the startup of the application
#     NumDroppedFramesOnStartup           = "" # shows how many frames are dropped during the startup of the application
#     NumReprojectedFramesOnStartup       = "" # shows how many frames are reprojected during the startup of the application by timewarp
#     NumLoading                          = "" # shows how many loadings occur while using the application
#     NumFramePresentsLoading             = "" # shows how many frames are presented during the loadings
#     NumDroppedFramesLoading             = "" # shows how many frames are dropped during the loadings
#     NumReprojectedFramesLoading         = "" # shows how many frames are reprojected during the loadings by timewarp
#     NumTimedOut                         = "" # shows how many TimedOuts occur while using the application
#     NumFramePresentsTimedOut            = "" # shows how many frames are presented during the TimesOuts
#     NumDroppedFramesTimedOut            = "" # shows how many frames are dropped during the TimesOuts
#     NumReprojectedFramesTimedOut        = "" # shows how many frames are reprojected during the TimedOuts by timewarp
#     AvgCompositorCPUTimeMS              = "" # shows the average CPU time in (ms) the compositor takes to finish a frame (overlay)
#     AvgCompositorGPUTimeMS              = "" # shows the average GPU time in (ms) the compositor takes to finish a frame (overlay)
#     AvgTargetFPS                        = "" # average Frame Per Second (FPS)
#     AvgApplicationCPUTimeMS             = "" # shows the average CPU time in (ms) the application takes to finish a frame (overlay)
#     AvgApplicationGPUTimeMS             = "" # shows the average GPU time in (ms) the application takes to finish a frame (overlay)
#     # additional stats
#     totalDroppedFramesOverEntireRun     = "" # shows how many frames are dropped in the entire run

#     overallFramesStatsFlag = False
#     isStatistics = False
#     processIDs = []
#     targetedAppsProcessIDs = {}
#     processID = ""
#     currentAppName = ""

#     print("{} file processing".format(filePath.split("/")[1]))
#     with open(filePath,'r') as f:
#         lines = f.readlines()
#         for line in lines:
#             if("Lost pipe connection" in line):
#                 splittedLine = line.split(" ")
#                 currentAppName = splittedLine[10]
#                 for i in range (11,len(splittedLine)-1):
#                     currentAppName = currentAppName + " " + splittedLine[i]
#                 if(currentAppName in appNames):
#                     processID = splittedLine[len(splittedLine)-1].replace("(","").replace(")","").strip()
#                     if processID not in processIDs:
#                         processIDs.append(processID)
#                         targetedAppsProcessIDs[processID] = currentAppName
#             elif("Cumulative stats for pid:" in line):
#                 splittedLine = line.split(" ")
#                 processID = splittedLine[10].strip()
#                 time = convertTime(splittedLine[4]) #the stats time in (ms) from the beginning of the day
#                 if (time < startTimeInMs or time > endTimeInMs or processID not in targetedAppsProcessIDs):
#                     continue
#                 else:
#                     appPerformanceStatsTimeStamp = time
#                     appName = targetedAppsProcessIDs[processID]
#                     appProcessID = processID
#                     isStatistics = True
#             elif(isStatistics):
#                 if("#######" not in line):
#                     values = line.split()
#                     if(len(values)<1):
#                         continue
#                     if("Total" in line):
#                         NumFramePresents                    = values[7].strip()
#                         NumDroppedFrames                    = values[9].strip()
#                         NumReprojected                      = values[11].strip()
#                     elif("Startup" in line):
#                         NumFramePresentsOnStartup           = values[7].strip()
#                         NumDroppedFramesOnStartup           = values[9].strip()
#                         NumReprojectedFramesOnStartup       = values[11].strip()
#                     elif("Loading" in line):
#                         NumLoading                          = values[7].strip()
#                         NumFramePresentsLoading             = values[9].strip()
#                         NumDroppedFramesLoading             = values[11].strip()
#                         NumReprojectedFramesLoading         = values[13].strip()
#                     elif("Timed out" in line):
#                         NumTimedOut                         = values[8].strip()
#                         NumFramePresentsTimedOut            = values[10].strip()
#                         NumDroppedFramesTimedOut            = values[12].strip()
#                         NumReprojectedFramesTimedOut        = values[14].strip()
#                     elif("Compositor Time" in line):
#                         AvgCompositorCPUTimeMS              = values[8].strip().replace("ms","")
#                         AvgCompositorGPUTimeMS              = values[11].strip().replace("ms","")
#                     else:
#                         AvgTargetFPS                        = values[10].strip()
#                         AvgApplicationCPUTimeMS             = values[13].strip().replace("ms","")
#                         AvgApplicationGPUTimeMS             = values[16].strip().replace("ms","")
#                 else:
#                     isStatistics = False
#                     overallFramesStatsFlag = True
#             elif(overallFramesStatsFlag):
#                 values = line.split()
#                 overallFramesStatsFlag = False
#                 totalDroppedFramesOverEntireRun = values[9].strip()

#                 appPerformanceStatElement = (appPerformanceStatsTimeStamp,appName,appProcessID,NumFramePresents
#                     ,NumDroppedFrames,NumReprojected,NumFramePresentsOnStartup,NumDroppedFramesOnStartup
#                     ,NumReprojectedFramesOnStartup,NumLoading,NumFramePresentsLoading,NumDroppedFramesLoading
#                     ,NumReprojectedFramesLoading,NumTimedOut,NumFramePresentsTimedOut,NumDroppedFramesTimedOut
#                     ,NumReprojectedFramesTimedOut,AvgCompositorCPUTimeMS,AvgCompositorGPUTimeMS,AvgTargetFPS
#                     ,AvgApplicationCPUTimeMS,AvgApplicationGPUTimeMS,totalDroppedFramesOverEntireRun)
#                 appPerformanceStats.append(appPerformanceStatElement)


def processSteamVRLogFolder(steamVRLogFolder,appNames,startTimeInMs,endTimeInMs):
    appPerformanceStatsMonitorFile    = ()
    appPerformanceStatsCompositorFile = ()
    
    
    
    steamVRLogsFiles = listdir(steamVRLogFolder)

    print("steamVR logs files:")

    # processing VRmonitor Files
    if("vrmonitor.previous.txt" in steamVRLogsFiles or "vrmonitor.txt" in steamVRLogsFiles):  
        # app performance stats (vrmonitor.previous.txt and vrmonitor.txt):
        appPerformanceStatsTimeStamp        = [] # the time stamp for these performance stats
        appID                               = [] # the application id
        NumFramePresents                    = [] # shows how many frames are presented in the application
        NumDroppedFrames                    = [] # shows how many frames are dropped in the application
        NumReprojected                      = [] # shows how many frames are reprojected in the application by timewarp
        NumFramePresentsOnStartup           = [] # shows how many frames are presented during the startup of the application
        NumDroppedFramesOnStartup           = [] # shows how many frames are dropped during the startup of the application
        NumReprojectedFramesOnStartup       = [] # shows how many frames are reprojected during the startup of the application by timewarp
        NumLoading                          = [] # shows how many loadings occur while using the application
        NumFramePresentsLoading             = [] # shows how many frames are presented during the loadings
        NumDroppedFramesLoading             = [] # shows how many frames are dropped during the loadings
        NumReprojectedFramesLoading         = [] # shows how many frames are reprojected during the loadings by timewarp
        NumTimedOut                         = [] # shows how many TimedOuts occur while using the application
        NumFramePresentsTimedOut            = [] # shows how many frames are presented during the TimesOuts
        NumDroppedFramesTimedOut            = [] # shows how many frames are dropped during the TimesOuts
        NumReprojectedFramesTimedOut        = [] # shows how many frames are reprojected during the TimedOuts by timewarp
        AvgSubmitsPerFrame                  = [] # shows how many times a frame is trasmitted in average (to measure the retransmission)
        AvgCompositorCPUTimeMS              = [] # shows the average CPU time in (ms) the compositor takes to finish a frame (overlay)
        AvgCompositorGPUTimeMS              = [] # shows the average GPU time in (ms) the compositor takes to finish a frame (overlay)
        AvgTargetFPS                        = [] # average Frame Per Second (FPS)
        AvgApplicationCPUTimeMS             = [] # shows the average CPU time in (ms) the application takes to finish a frame (overlay)
        AvgApplicationGPUTimeMS             = [] # shows the average GPU time in (ms) the application takes to finish a frame (overlay)
        AppSeconds                          = [] # shows the duration of the app in seconds (how long the app is run)
        AppHeadsetActiveSeconds             = [] # shows the duration of the app in seconds (how long the app is run) while the HMD is active
        # additional stats
        NumSingleDroppedFramesOverEntireRun = [] # shows how many single frames are dropped in the entire run
        Num2DroppedFramesOverEntireRun      = [] # shows how many two frames are dropped in the entire run
        Num3DroppedFramesOverEntireRun      = [] # shows how many three frames are dropped in the entire run
        Num4MoreDroppedFramesOverEntireRun  = [] # shows how many four or more frames are dropped in the entire run
        totalNumOfFramesEntireRun           = [] # shows how many total frames are received in the entire run
        totalNumOfExpectedFrameEntireRun    = [] # shows how many total frames are expected to be received in the entire run    
        if("vrmonitor.previous.txt" in steamVRLogsFiles):
            filePath = "{}/{}".format(steamVRLogFolder,"vrmonitor.previous.txt")
            appPerformanceStatsTimeStamp,appID,NumFramePresents,NumDroppedFrames,NumReprojected,NumFramePresentsOnStartup\
                ,NumDroppedFramesOnStartup,NumReprojectedFramesOnStartup,NumLoading,NumFramePresentsLoading,NumDroppedFramesLoading \
                ,NumReprojectedFramesLoading,NumTimedOut,NumFramePresentsTimedOut,NumDroppedFramesTimedOut \
                ,NumReprojectedFramesTimedOut,AvgSubmitsPerFrame,AvgCompositorCPUTimeMS,AvgCompositorGPUTimeMS \
                ,AvgTargetFPS,AvgApplicationCPUTimeMS,AvgApplicationGPUTimeMS,AppSeconds,AppHeadsetActiveSeconds \
                ,NumSingleDroppedFramesOverEntireRun,Num2DroppedFramesOverEntireRun,Num3DroppedFramesOverEntireRun \
                ,Num4MoreDroppedFramesOverEntireRun,totalNumOfFramesEntireRun,totalNumOfExpectedFrameEntireRun = \
                processVRMonitorLogFile(filePath,startTimeInMs,endTimeInMs)
        if("vrmonitor.txt" in steamVRLogsFiles):
            filePath = "{}/{}".format(steamVRLogFolder,"vrmonitor.txt")
            appPerformanceStatsTimeStamp2,appID2,NumFramePresents2,NumDroppedFrames2,NumReprojected2,NumFramePresentsOnStartup2\
                ,NumDroppedFramesOnStartup2,NumReprojectedFramesOnStartup2,NumLoading2,NumFramePresentsLoading2,NumDroppedFramesLoading2 \
                ,NumReprojectedFramesLoading2,NumTimedOut2,NumFramePresentsTimedOut2,NumDroppedFramesTimedOut2 \
                ,NumReprojectedFramesTimedOut2,AvgSubmitsPerFrame2,AvgCompositorCPUTimeMS2,AvgCompositorGPUTimeMS2 \
                ,AvgTargetFPS2,AvgApplicationCPUTimeMS2,AvgApplicationGPUTimeMS2,AppSeconds2,AppHeadsetActiveSeconds2 \
                ,NumSingleDroppedFramesOverEntireRun2,Num2DroppedFramesOverEntireRun2,Num3DroppedFramesOverEntireRun2 \
                ,Num4MoreDroppedFramesOverEntireRun2,totalNumOfFramesEntireRun2,totalNumOfExpectedFrameEntireRun2 = \
                processVRMonitorLogFile(filePath,startTimeInMs,endTimeInMs)
            appPerformanceStatsTimeStamp        = appPerformanceStatsTimeStamp + appPerformanceStatsTimeStamp2
            appID                               = appID + appID2
            NumFramePresents                    = NumFramePresents + NumFramePresents2
            NumDroppedFrames                    = NumDroppedFrames + NumDroppedFrames2
            NumReprojected                      = NumReprojected + NumReprojected2
            NumFramePresentsOnStartup           = NumFramePresentsOnStartup + NumFramePresentsOnStartup2
            NumDroppedFramesOnStartup           = NumDroppedFramesOnStartup + NumDroppedFramesOnStartup2
            NumReprojectedFramesOnStartup       = NumReprojectedFramesOnStartup + NumReprojectedFramesOnStartup2
            NumLoading                          = NumLoading + NumLoading2
            NumFramePresentsLoading             = NumFramePresentsLoading + NumFramePresentsLoading2
            NumDroppedFramesLoading             = NumDroppedFramesLoading + NumDroppedFramesLoading2
            NumReprojectedFramesLoading         = NumReprojectedFramesLoading + NumReprojectedFramesLoading2
            NumTimedOut                         = NumTimedOut + NumTimedOut2
            NumFramePresentsTimedOut            = NumFramePresentsTimedOut + NumFramePresentsTimedOut2
            NumDroppedFramesTimedOut            = NumDroppedFramesTimedOut + NumDroppedFramesTimedOut2
            NumReprojectedFramesTimedOut        = NumReprojectedFramesTimedOut + NumReprojectedFramesTimedOut2
            AvgSubmitsPerFrame                  = AvgSubmitsPerFrame + AvgSubmitsPerFrame2
            AvgCompositorCPUTimeMS              = AvgCompositorCPUTimeMS + AvgCompositorCPUTimeMS2
            AvgCompositorGPUTimeMS              = AvgCompositorGPUTimeMS + AvgCompositorGPUTimeMS2
            AvgTargetFPS                        = AvgTargetFPS + AvgTargetFPS2
            AvgApplicationCPUTimeMS             = AvgApplicationCPUTimeMS + AvgApplicationCPUTimeMS2
            AvgApplicationGPUTimeMS             = AvgApplicationGPUTimeMS + AvgApplicationGPUTimeMS2
            AppSeconds                          = AppSeconds + AppSeconds2
            AppHeadsetActiveSeconds             = AppHeadsetActiveSeconds + AppHeadsetActiveSeconds2
            NumSingleDroppedFramesOverEntireRun = NumSingleDroppedFramesOverEntireRun + NumSingleDroppedFramesOverEntireRun2
            Num2DroppedFramesOverEntireRun      = Num2DroppedFramesOverEntireRun + Num2DroppedFramesOverEntireRun2
            Num3DroppedFramesOverEntireRun      = Num3DroppedFramesOverEntireRun + Num3DroppedFramesOverEntireRun2
            Num4MoreDroppedFramesOverEntireRun  = Num4MoreDroppedFramesOverEntireRun + Num4MoreDroppedFramesOverEntireRun2
            totalNumOfFramesEntireRun           = totalNumOfFramesEntireRun + totalNumOfFramesEntireRun2
            totalNumOfExpectedFrameEntireRun    = totalNumOfExpectedFrameEntireRun + totalNumOfExpectedFrameEntireRun2

        # the tuple of all the performance stats from the monitor file
        appPerformanceStatsMonitorFile = (appPerformanceStatsTimeStamp,appID,NumFramePresents
            ,NumDroppedFrames,NumReprojected,NumFramePresentsOnStartup,NumDroppedFramesOnStartup
            ,NumReprojectedFramesOnStartup,NumLoading,NumFramePresentsLoading,NumDroppedFramesLoading
            ,NumReprojectedFramesLoading,NumTimedOut,NumFramePresentsTimedOut,NumDroppedFramesTimedOut
            ,NumReprojectedFramesTimedOut,AvgSubmitsPerFrame,AvgCompositorCPUTimeMS,AvgCompositorGPUTimeMS
            ,AvgTargetFPS,AvgApplicationCPUTimeMS,AvgApplicationGPUTimeMS,AppSeconds,AppHeadsetActiveSeconds
            ,NumSingleDroppedFramesOverEntireRun,Num2DroppedFramesOverEntireRun,Num3DroppedFramesOverEntireRun
            ,Num4MoreDroppedFramesOverEntireRun,totalNumOfFramesEntireRun,totalNumOfExpectedFrameEntireRun)
        

    # processing vrcompositor Files
    if("vrcompositor.previous.txt" in steamVRLogsFiles or "vrcompositor.txt" in steamVRLogsFiles):  
        # app performance stats (vrcompositor.previous.txt and vrcompositor.txt):
        appPerformanceStatsTimeStamp        = [] # the time stamp for these performance stats
        appName                             = [] # the application name
        appProcessID                        = [] # the application process id
        NumFramePresents                    = [] # shows how many frames are presented in the application
        NumDroppedFrames                    = [] # shows how many frames are dropped in the application
        NumReprojected                      = [] # shows how many frames are reprojected in the application by timewarp
        NumFramePresentsOnStartup           = [] # shows how many frames are presented during the startup of the application
        NumDroppedFramesOnStartup           = [] # shows how many frames are dropped during the startup of the application
        NumReprojectedFramesOnStartup       = [] # shows how many frames are reprojected during the startup of the application by timewarp
        NumLoading                          = [] # shows how many loadings occur while using the application
        NumFramePresentsLoading             = [] # shows how many frames are presented during the loadings
        NumDroppedFramesLoading             = [] # shows how many frames are dropped during the loadings
        NumReprojectedFramesLoading         = [] # shows how many frames are reprojected during the loadings by timewarp
        NumTimedOut                         = [] # shows how many TimedOuts occur while using the application
        NumFramePresentsTimedOut            = [] # shows how many frames are presented during the TimesOuts
        NumDroppedFramesTimedOut            = [] # shows how many frames are dropped during the TimesOuts
        NumReprojectedFramesTimedOut        = [] # shows how many frames are reprojected during the TimedOuts by timewarp
        AvgCompositorCPUTimeMS              = [] # shows the average CPU time in (ms) the compositor takes to finish a frame (overlay)
        AvgCompositorGPUTimeMS              = [] # shows the average GPU time in (ms) the compositor takes to finish a frame (overlay)
        AvgTargetFPS                        = [] # average Frame Per Second (FPS)
        AvgApplicationCPUTimeMS             = [] # shows the average CPU time in (ms) the application takes to finish a frame (overlay)
        AvgApplicationGPUTimeMS             = [] # shows the average GPU time in (ms) the application takes to finish a frame (overlay)
        # additional stats
        totalDroppedFramesOverEntireRun     = [] # shows how many frames are dropped in the entire run
        if("vrcompositor.previous.txt" in steamVRLogsFiles):
            filePath = "{}/{}".format(steamVRLogFolder,"vrcompositor.previous.txt")
            appPerformanceStatsTimeStamp,appName,appProcessID,NumFramePresents \
            ,NumDroppedFrames,NumReprojected,NumFramePresentsOnStartup,NumDroppedFramesOnStartup\
            ,NumReprojectedFramesOnStartup,NumLoading,NumFramePresentsLoading,NumDroppedFramesLoading\
            ,NumReprojectedFramesLoading,NumTimedOut,NumFramePresentsTimedOut,NumDroppedFramesTimedOut\
            ,NumReprojectedFramesTimedOut,AvgCompositorCPUTimeMS,AvgCompositorGPUTimeMS,AvgTargetFPS\
            ,AvgApplicationCPUTimeMS,AvgApplicationGPUTimeMS,totalDroppedFramesOverEntireRun = \
                processVRCompositorLogFile(filePath,appNames,startTimeInMs,endTimeInMs)
        if("vrcompositor.txt" in steamVRLogsFiles):
            filePath = "{}/{}".format(steamVRLogFolder,"vrcompositor.txt")
            appPerformanceStatsTimeStamp2,appName2,appProcessID2,NumFramePresents2 \
            ,NumDroppedFrames2,NumReprojected2,NumFramePresentsOnStartup2,NumDroppedFramesOnStartup2\
            ,NumReprojectedFramesOnStartup2,NumLoading2,NumFramePresentsLoading2,NumDroppedFramesLoading2\
            ,NumReprojectedFramesLoading2,NumTimedOut2,NumFramePresentsTimedOut2,NumDroppedFramesTimedOut2\
            ,NumReprojectedFramesTimedOut2,AvgCompositorCPUTimeMS2,AvgCompositorGPUTimeMS2,AvgTargetFPS2\
            ,AvgApplicationCPUTimeMS2,AvgApplicationGPUTimeMS2,totalDroppedFramesOverEntireRun2 = \
                processVRCompositorLogFile(filePath,appNames,startTimeInMs,endTimeInMs)
            appPerformanceStatsTimeStamp        = appPerformanceStatsTimeStamp + appPerformanceStatsTimeStamp2
            appName                             = appName + appName2
            appProcessID                        = appProcessID + appProcessID2
            NumFramePresents                    = NumFramePresents + NumFramePresents2
            NumDroppedFrames                    = NumDroppedFrames + NumDroppedFrames2
            NumReprojected                      = NumReprojected + NumReprojected2
            NumFramePresentsOnStartup           = NumFramePresentsOnStartup + NumFramePresentsOnStartup2
            NumDroppedFramesOnStartup           = NumDroppedFramesOnStartup + NumDroppedFramesOnStartup2
            NumReprojectedFramesOnStartup       = NumReprojectedFramesOnStartup + NumReprojectedFramesOnStartup2
            NumLoading                          = NumLoading + NumLoading2
            NumFramePresentsLoading             = NumFramePresentsLoading + NumFramePresentsLoading2
            NumDroppedFramesLoading             = NumDroppedFramesLoading + NumDroppedFramesLoading2
            NumReprojectedFramesLoading         = NumReprojectedFramesLoading + NumReprojectedFramesLoading2
            NumTimedOut                         = NumTimedOut + NumTimedOut2
            NumFramePresentsTimedOut            = NumFramePresentsTimedOut + NumFramePresentsTimedOut2
            NumDroppedFramesTimedOut            = NumDroppedFramesTimedOut + NumDroppedFramesTimedOut2
            NumReprojectedFramesTimedOut        = NumReprojectedFramesTimedOut + NumReprojectedFramesTimedOut2
            AvgCompositorCPUTimeMS              = AvgCompositorCPUTimeMS + AvgCompositorCPUTimeMS2
            AvgCompositorGPUTimeMS              = AvgCompositorGPUTimeMS + AvgCompositorGPUTimeMS2
            AvgTargetFPS                        = AvgTargetFPS + AvgTargetFPS2
            AvgApplicationCPUTimeMS             = AvgApplicationCPUTimeMS + AvgApplicationCPUTimeMS2
            AvgApplicationGPUTimeMS             = AvgApplicationGPUTimeMS + AvgApplicationGPUTimeMS2
            totalDroppedFramesOverEntireRun     = totalDroppedFramesOverEntireRun + totalDroppedFramesOverEntireRun2

        # the tuple of all the performance stats from the compositor file
        appPerformanceStatsCompositorFile = (appPerformanceStatsTimeStamp,appName,appProcessID,NumFramePresents
            ,NumDroppedFrames,NumReprojected,NumFramePresentsOnStartup,NumDroppedFramesOnStartup
            ,NumReprojectedFramesOnStartup,NumLoading,NumFramePresentsLoading,NumDroppedFramesLoading
            ,NumReprojectedFramesLoading,NumTimedOut,NumFramePresentsTimedOut,NumDroppedFramesTimedOut
            ,NumReprojectedFramesTimedOut,AvgCompositorCPUTimeMS,AvgCompositorGPUTimeMS,AvgTargetFPS
            ,AvgApplicationCPUTimeMS,AvgApplicationGPUTimeMS,totalDroppedFramesOverEntireRun)
    
    print("---------------------") 
    return(appPerformanceStatsMonitorFile,appPerformanceStatsCompositorFile)


def processLogsFolder(logsFolder,startTime,endTime):
    sessionLogFileName = 'session_log.txt'
    OVRMetricsFolderName = 'OVRMetrics'
    logcatFileName = 'logcat.txt'
    steamVRLogFName = "logs"
    appNames = ["Beat Saber","steamtours"]
    gamesFolders = listdir(logsFolder)
    startTimeInMs = convertTime(startTime)
    endTimeInMs = convertTime(endTime)

    LogsFolderResults = []
    sessionLogResult  = ()
    OVRMetricsResult  = ()
    logcatResults     = ()
    steamVRLogResults = ()


    if(len(gamesFolders)==0):
        print("WARNING: the logs files could not be found")
        return []


    print("logs files:")
    print("#####################################")


    for gameFolder in gamesFolders:
        if("." in gameFolder): # to skip hidden files and folders
            continue
        sessionLogResult  = ()
        OVRMetricsResult  = ()
        logcatResults     = ()
        steamVRLogResults = ()
        gameName = gameFolder
        gameFolderPath = "{}/{}".format(logsFolder,gameName)

        # process the session_log file
        if(sessionLogFileName in listdir(gameFolderPath)):     
            sessionLogFilePath = "{}/{}".format(gameFolderPath,sessionLogFileName)
            sessionLogResult = processSessionLog(sessionLogFilePath,startTimeInMs,endTimeInMs)
        else:
            print("make sure that '{}' file is inside the game folder {} in the path {}".format(sessionLogFileName,gameName,gameFolderPath))
        
        # process the OVRMetrics folder 
        if(OVRMetricsFolderName in listdir(gameFolderPath)):     
            OVRMetricsFolderPath = "{}/{}".format(gameFolderPath,OVRMetricsFolderName)
            OVRMetricsResult = processOVRMetricsFolder(OVRMetricsFolderPath,startTimeInMs,endTimeInMs)
        else:
            print("make sure that '{}' folder is inside the game folder {} in the path {}".format(OVRMetricsFolderName,gameName,gameFolderPath))

        # process the logcat file  
        if(logcatFileName in listdir(gameFolderPath)):     
            logcatFilePath = "{}/{}".format(gameFolderPath,logcatFileName)
            logcatResults = processLogcat(logcatFilePath,startTimeInMs,endTimeInMs)
        else:
            print("make sure that '{}' file is inside the game folder {} in the path {}".format(logcatFileName,gameName,gameFolderPath))

        # process the steamVRLog folder  
        if(steamVRLogFName in listdir(gameFolderPath)):     
            steamVRLogFolder = "{}/{}".format(gameFolderPath,steamVRLogFName)
            steamVRLogResults = processSteamVRLogFolder(steamVRLogFolder,appNames,startTimeInMs,endTimeInMs)
        else:
            print("make sure that '{}' folder is inside the game folder {} in the path {}".format(steamVRLogFName,gameName,gameFolderPath))
        
        LogsFolderResults.append((gameName,sessionLogResult,OVRMetricsResult,logcatResults,steamVRLogResults))

    
    print("#####################################")
    return LogsFolderResults


def processServerTraces(tracesFolder,startTimeInMs,endTimeInMs,HMD_IP,server_IP):
    gamesFolders = listdir(tracesFolder)
    serverTracesResults = []

    print("server traces files:")
    for gameFolder in gamesFolders:
        if("." in gameFolder): # to skip hidden files and folders
            continue
        gameName = gameFolder
        gameFolderPath = "{}/{}".format(tracesFolder,gameName)
        if("server_traces" in listdir(gameFolderPath)):     
            serverTracesFolderPath = "{}/{}".format(gameFolderPath,"server_traces")
            if("server.csv" in listdir(serverTracesFolderPath)):
                filePath = "{}/{}".format(serverTracesFolderPath,"server.csv")

                server_UP_BOTH_NBs           = [] # A list of the frames' numbers of the server's uplink for both (TCP and UDP) frames
                server_UP_BOTH_Times         = [] # A list of the frames' times of the server's uplink for both (TCP and UDP) frames
                server_UP_BOTH_Data_Sizes    = [] # A list of the frames' data sizes (the application layer payloads) in bytes of the server's uplink for both (TCP and UDP) frames
                server_UP_BOTH_Frames_Sizes  = [] # A list of the frames' sizes in the link (payloads + headers sizes) in bytes of the server's uplink for both (TCP and UDP) frames
                server_UP_TCP_NBs            = [] # A list of the frames' numbers of the server's uplink for TCP frames
                server_UP_TCP_Times          = [] # A list of the frames' times of the server's uplink for TCP frames
                server_UP_TCP_Data_Sizes     = [] # A list of the frames' data sizes (the application layer payloads) in bytes of the server's uplink for TCP frames
                server_UP_TCP_Frames_Sizes   = [] # A list of the frames' sizes in the link (payloads + headers sizes) in bytes of the server's uplink for TCP frames
                server_UP_UDP_NBs            = [] # A list of the frames' numbers of the server's uplink for UDP frames
                server_UP_UDP_Times          = [] # A list of the frames' times of the server's uplink for UDP frames
                server_UP_UDP_Data_Sizes     = [] # A list of the frames' data sizes (the application layer payloads) in bytes of the server's uplink for UDP frames
                server_UP_UDP_Frames_Sizes   = [] # A list of the frames' sizes in the link (payloads + headers sizes) in bytes of the server's uplink for UDP frames
                server_DWN_BOTH_NBs          = [] # A list of the frames' numbers of the server's downlink for both (TCP and UDP) frames
                server_DWN_BOTH_Times        = [] # A list of the frames' times of the server's downlink for both (TCP and UDP) frames
                server_DWN_BOTH_Data_Sizes   = [] # A list of the frames' data sizes (the application layer payloads) in bytes of the server's downlink for both (TCP and UDP) frames
                server_DWN_BOTH_Frames_Sizes = [] # A list of the frames' sizes in the link (payloads + headers sizes) in bytes of the server's downlink for both (TCP and UDP) frames
                server_DWN_TCP_NBs           = [] # A list of the frames' numbers of the server's downlink for TCP frames
                server_DWN_TCP_Times         = [] # A list of the frames' times of the server's downlink for TCP frames
                server_DWN_TCP_Data_Sizes    = [] # A list of the frames' data sizes (the application layer payloads) in bytes of the server's downlink for TCP frames
                server_DWN_TCP_Frames_Sizes  = [] # A list of the frames' sizes in the link (payloads + headers sizes) in bytes of the server's downlink for TCP frames
                server_DWN_UDP_NBs           = [] # A list of the frames' numbers of the server's downlink for UDP frames
                server_DWN_UDP_Times         = [] # A list of the frames' times of the server's downlink for UDP frames
                server_DWN_UDP_Data_Sizes    = [] # A list of the frames' data sizes (the application layer payloads) in bytes of the server's downlink for UDP frames
                server_DWN_UDP_Frames_Sizes  = [] # A list of the frames' sizes in the link (payloads + headers sizes) in bytes of the server's downlink for UDP frames

                print("{} file processing".format(filePath))

                isHeader = True
                with open(filePath,'rb') as f:
                    for line in f:
                        if(isHeader):
                            isHeader = False
                            continue

                        splittedLine = line.decode('cp1252').replace('"','').strip().split(",")
                        timeInMs = convertTime(splittedLine[1].split(" ")[1])
                        if(timeInMs > endTimeInMs):
                            break
                        if(timeInMs < startTimeInMs):
                            continue

                        if(splittedLine[2] == server_IP):     # server uplink (Ethernet)
                            if(splittedLine[3] == HMD_IP):
                                if(splittedLine[4] == "TCP"):
                                    infoPart = splittedLine[len(splittedLine)-1].strip()
                                    tempDataSizeField = infoPart.split()
                                    dataSizeField = [x for x in tempDataSizeField if "Len" in x]
                                    dataSize = dataSizeField[0].strip().split("=")[1].strip()
                                    server_UP_BOTH_NBs.append(splittedLine[0])
                                    server_UP_TCP_NBs.append(splittedLine[0])
                                    server_UP_BOTH_Times.append(timeInMs)
                                    server_UP_TCP_Times.append(timeInMs)
                                    server_UP_BOTH_Data_Sizes.append(dataSize)
                                    server_UP_TCP_Data_Sizes.append(dataSize)
                                    server_UP_BOTH_Frames_Sizes.append(splittedLine[5].strip())
                                    server_UP_TCP_Frames_Sizes.append(splittedLine[5].strip())
                                    
                                elif(splittedLine[4] == "UDP"):
                                    infoPart = splittedLine[len(splittedLine)-1].strip()
                                    tempDataSizeField = infoPart.split()
                                    dataSizeField = [x for x in tempDataSizeField if "Len" in x]
                                    dataSize = dataSizeField[0].strip().split("=")[1].strip()
                                    server_UP_BOTH_NBs.append(splittedLine[0])
                                    server_UP_UDP_NBs.append(splittedLine[0])
                                    server_UP_BOTH_Times.append(timeInMs)
                                    server_UP_UDP_Times.append(timeInMs)
                                    server_UP_BOTH_Data_Sizes.append(dataSize)
                                    server_UP_UDP_Data_Sizes.append(dataSize)
                                    server_UP_BOTH_Frames_Sizes.append(splittedLine[5].strip())
                                    server_UP_UDP_Frames_Sizes.append(splittedLine[5].strip())
                    
                        elif(splittedLine[2] == HMD_IP):     # server uplink (Ethernet)
                            if(splittedLine[3] == server_IP):
                                if(splittedLine[4] == "TCP"):
                                    infoPart = splittedLine[len(splittedLine)-1].strip()
                                    tempDataSizeField = infoPart.split()
                                    dataSizeField = [x for x in tempDataSizeField if "Len" in x]
                                    dataSize = dataSizeField[0].strip().split("=")[1].strip()
                                    server_DWN_BOTH_NBs.append(splittedLine[0])
                                    server_DWN_TCP_NBs.append(splittedLine[0])
                                    server_DWN_BOTH_Times.append(timeInMs)
                                    server_DWN_TCP_Times.append(timeInMs)
                                    server_DWN_BOTH_Data_Sizes.append(dataSize)
                                    server_DWN_TCP_Data_Sizes.append(dataSize)
                                    server_DWN_BOTH_Frames_Sizes.append(splittedLine[5].strip())
                                    server_DWN_TCP_Frames_Sizes.append(splittedLine[5].strip())
                                    
                                elif(splittedLine[4] == "UDP"):
                                    infoPart = splittedLine[len(splittedLine)-1].strip()
                                    tempDataSizeField = infoPart.split()
                                    dataSizeField = [x for x in tempDataSizeField if "Len" in x]
                                    dataSize = dataSizeField[0].strip().split("=")[1].strip()
                                    server_DWN_BOTH_NBs.append(splittedLine[0])
                                    server_DWN_UDP_NBs.append(splittedLine[0])
                                    server_DWN_BOTH_Times.append(timeInMs)
                                    server_DWN_UDP_Times.append(timeInMs)
                                    server_DWN_BOTH_Data_Sizes.append(dataSize)
                                    server_DWN_UDP_Data_Sizes.append(dataSize)
                                    server_DWN_BOTH_Frames_Sizes.append(splittedLine[5].strip())
                                    server_DWN_UDP_Frames_Sizes.append(splittedLine[5].strip())
                results = (server_UP_BOTH_NBs,server_UP_BOTH_Times,server_UP_BOTH_Data_Sizes,server_UP_BOTH_Frames_Sizes,server_UP_TCP_NBs,server_UP_TCP_Times,
                    server_UP_TCP_Data_Sizes,server_UP_TCP_Frames_Sizes,server_UP_UDP_NBs,server_UP_UDP_Times,server_UP_UDP_Data_Sizes,server_UP_UDP_Frames_Sizes,
                    server_DWN_BOTH_NBs,server_DWN_BOTH_Times,server_DWN_BOTH_Data_Sizes,server_DWN_BOTH_Frames_Sizes,server_DWN_TCP_NBs,server_DWN_TCP_Times,
                    server_DWN_TCP_Data_Sizes,server_DWN_TCP_Frames_Sizes,server_DWN_UDP_NBs,server_DWN_UDP_Times,server_DWN_UDP_Data_Sizes,server_DWN_UDP_Frames_Sizes)
                serverTracesResults.append((gameName,results))
            else:
                print("make sure that the trace file 'server.csv' is in the 'server_traces' folder in the path and its name is 'server.csv'".format(serverTracesFolderPath))
        else:
            print("make sure that 'server_traces' folder is inside the game folder {} in the path {}".format(gameName,gameFolderPath))
            
    

    print("---------------------") 

    return serverTracesResults


def processHMDManagementFramesTraces(filePath,startTimeInMs,endTimeInMs,HMD_MAC,AP_MAC2):
    
    HMD_UP_MANAGEMENT_FRAMES_NBs           = [] # A list of the management frames' numbers of the HMD's uplink
    HMD_UP_MANAGEMENT_FRAMES_Times         = [] # A list of the management frames' times of the HMD's uplink 
    HMD_UP_MANAGEMENT_FRAMES_DataRates     = [] # A list of the management frames' data rates in Mbps of the HMD's uplink
    HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes  = [] # A list of the frames' sizes in the link in bytes of the HMD's uplink (no data in management frames)
    HMD_DWN_MANAGEMENT_FRAMES_NBs          = [] # A list of the management frames' numbers of the HMD's downlink
    HMD_DWN_MANAGEMENT_FRAMES_Times        = [] # A list of the management frames' times of the HMD's downlink 
    HMD_DWN_MANAGEMENT_FRAMES_DataRates    = [] # A list of the management frames' data rates in Mbps of the HMD's downlink
    HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes = [] # A list of the frames' sizes in the link in bytes of the HMD's downlink (no data in management frames)
    
    isHeader = True
    with open(filePath,'rb') as f:
        for line in f:
            if(isHeader):
                isHeader = False
                continue

            splittedLine = line.decode('cp1252').replace('"','').strip().split(",")
            timeInMs = convertTime(splittedLine[1])#.split(" ")[1])
            if(timeInMs > endTimeInMs):
                break
            if(timeInMs < startTimeInMs):
                continue

            if(splittedLine[4] == HMD_MAC):     # HMD uplink (WLAN - management frames)
                if(splittedLine[5] == AP_MAC2):
                    HMD_UP_MANAGEMENT_FRAMES_NBs.append(splittedLine[0])
                    HMD_UP_MANAGEMENT_FRAMES_Times.append(timeInMs)
                    HMD_UP_MANAGEMENT_FRAMES_DataRates.append(splittedLine[10])
                    HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes.append(splittedLine[9])
        
            elif(splittedLine[4] == AP_MAC2):     # HMD downlink (WLAN - management frames)
                if(splittedLine[5] == "Broadcast"):
                    HMD_DWN_MANAGEMENT_FRAMES_NBs.append(splittedLine[0])
                    HMD_DWN_MANAGEMENT_FRAMES_Times.append(timeInMs)
                    HMD_DWN_MANAGEMENT_FRAMES_DataRates.append(splittedLine[10])
                    HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes.append(splittedLine[9])
                        
    results = (HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates,
                    HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes,HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times,
                    HMD_DWN_MANAGEMENT_FRAMES_DataRates,HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes)
    return results


def processHMDDataFramesTraces(filePath,startTimeInMs,endTimeInMs,HMD_MAC,MAC2,dataType):
    # This method used for all types of data frames (1,2, and 3)
    # dataType represents what data type is the file for (see the readme file)
    # TYPE1 does not have payload (data) in the frame, and it is only an uplink 
    # MAC2 is (AP_MAC2 for TYPE1) and (AP_MAC1 for TYPE2) and (server_MAC for TYPE3)

    HMD_UP_DATA_FRAMES_NBs           = [] # A list of the Data frames' numbers of the HMD's uplink
    HMD_UP_DATA_FRAMES_Times         = [] # A list of the Data frames' times of the HMD's uplink 
    HMD_UP_DATA_FRAMES_DataRates     = [] # A list of the Data frames' data rates in Mbps of the HMD's uplink
    HMD_UP_DATA_FRAMES_Data_Sizes    = [] # A list of the Data frames' payload (data) sizes in bytes of the HMD's uplink
    HMD_UP_DATA_FRAMES_Frames_Sizes  = [] # A list of the Data frames' (payload + headers) sizes in the link in bytes of the HMD's uplink
    HMD_UP_DATA_FRAMES_Frames_SeqNB  = [] # A list of the Data frames' 802.11 sequence numbers of the HMD's uplink
    HMD_DWN_DATA_FRAMES_NBs          = [] # A list of the data frames' numbers of the HMD's downlink
    HMD_DWN_DATA_FRAMES_Times        = [] # A list of the data frames' times of the HMD's downlink 
    HMD_DWN_DATA_FRAMES_DataRates    = [] # A list of the data frames' data rates in Mbps of the HMD's downlink
    HMD_DWN_DATA_FRAMES_Data_Sizes   = [] # A list of the Data frames' payload (data) sizes in bytes of the HMD's downlink
    HMD_DWN_DATA_FRAMES_Frames_Sizes = [] # A list of the Data frames' (payload + headers) sizes in the link in bytes of the HMD's downlink
    HMD_DWN_DATA_FRAMES_Frames_SeqNB = [] # A list of the Data frames' 802.11 sequence numbers of the HMD's downlink
    
    isHeader = True
    with open(filePath,'rb') as f:
        for line in f:
            if(isHeader):
                isHeader = False
                continue

            splittedLine = line.decode('cp1252').replace('"','').strip().split(",")
            timeInMs = convertTime(splittedLine[1])#.split(" ")[1])
            if(timeInMs > endTimeInMs):
                break
            if(timeInMs < startTimeInMs):
                continue

            if(splittedLine[4] == HMD_MAC):     # HMD uplink (WLAN - data frames)
                if(splittedLine[5] == MAC2):
                    HMD_UP_DATA_FRAMES_NBs.append(splittedLine[0]) 
                    HMD_UP_DATA_FRAMES_Times.append(timeInMs)
                    HMD_UP_DATA_FRAMES_Data_Sizes.append(splittedLine[8]) 
                    if("802.11a (OFDM)" == splittedLine[12]): 
                        HMD_UP_DATA_FRAMES_DataRates.append(splittedLine[10]) 
                        HMD_UP_DATA_FRAMES_Frames_Sizes.append(splittedLine[9]) 
                        HMD_UP_DATA_FRAMES_Frames_SeqNB.append(splittedLine[19]) 
                    elif("802.11ax (HE)" == splittedLine[12]):
                        HMD_UP_DATA_FRAMES_DataRates.append(splittedLine[11]) 
                        HMD_UP_DATA_FRAMES_Frames_Sizes.append(splittedLine[10]) 
                        HMD_UP_DATA_FRAMES_Frames_SeqNB.append(splittedLine[19])
                    else:
                        HMD_UP_DATA_FRAMES_DataRates.append(splittedLine[10]) 
                        HMD_UP_DATA_FRAMES_Frames_Sizes.append(splittedLine[9]) 
                        HMD_UP_DATA_FRAMES_Frames_SeqNB.append(splittedLine[18]) 

        
            elif(splittedLine[4] == MAC2):     # HMD downlink (WLAN - data frames)
                if(splittedLine[5] == HMD_MAC or splittedLine[5] == "Broadcast"):
                    HMD_DWN_DATA_FRAMES_NBs.append(splittedLine[0]) 
                    HMD_DWN_DATA_FRAMES_Times.append(timeInMs)
                    HMD_DWN_DATA_FRAMES_Data_Sizes.append(splittedLine[8]) 
                    if("802.11a (OFDM)" == splittedLine[12]): 
                        HMD_DWN_DATA_FRAMES_DataRates.append(splittedLine[10]) 
                        HMD_DWN_DATA_FRAMES_Frames_Sizes.append(splittedLine[9]) 
                        HMD_DWN_DATA_FRAMES_Frames_SeqNB.append(splittedLine[19]) 
                    elif("802.11ax (HE)" == splittedLine[12]):
                        HMD_DWN_DATA_FRAMES_DataRates.append(splittedLine[11]) 
                        HMD_DWN_DATA_FRAMES_Frames_Sizes.append(splittedLine[10]) 
                        HMD_DWN_DATA_FRAMES_Frames_SeqNB.append(splittedLine[19])
                    else:
                        HMD_DWN_DATA_FRAMES_DataRates.append(splittedLine[10]) 
                        HMD_DWN_DATA_FRAMES_Frames_Sizes.append(splittedLine[9]) 
                        HMD_DWN_DATA_FRAMES_Frames_SeqNB.append(splittedLine[18]) 
                        
    if(dataType == 1):
        results = (HMD_UP_DATA_FRAMES_NBs, HMD_UP_DATA_FRAMES_Times, HMD_UP_DATA_FRAMES_DataRates,
                    HMD_UP_DATA_FRAMES_Frames_Sizes,HMD_UP_DATA_FRAMES_Frames_SeqNB)
    elif (dataType == 2 or dataType == 3):
        results = (HMD_UP_DATA_FRAMES_NBs, HMD_UP_DATA_FRAMES_Times, HMD_UP_DATA_FRAMES_DataRates,
                    HMD_UP_DATA_FRAMES_Data_Sizes,HMD_UP_DATA_FRAMES_Frames_Sizes,HMD_UP_DATA_FRAMES_Frames_SeqNB,
                    HMD_DWN_DATA_FRAMES_NBs,HMD_DWN_DATA_FRAMES_Times, HMD_DWN_DATA_FRAMES_DataRates, HMD_DWN_DATA_FRAMES_Data_Sizes,
                    HMD_DWN_DATA_FRAMES_Frames_Sizes,HMD_DWN_DATA_FRAMES_Frames_SeqNB)
    else:
        sys.exit('ERROR: the data type of the data trace file has to be 1, 2, or 3. Check the readme file for more information')
    return results


def processHMDTraces(tracesFolder,startTimeInMs,endTimeInMs,HMD_MAC,server_MAC,AP_MAC1,AP_MAC2):
    gamesFolders = listdir(tracesFolder)
    HMDTracesResults = []

    print("HMD traces files:")
    for gameFolder in gamesFolders:
        if("." in gameFolder): # to skip hidden files and folders
            continue
        gameName = gameFolder
        gameFolderPath = "{}/{}".format(tracesFolder,gameName)
        if("HMD_traces" in listdir(gameFolderPath)):    
            HMDTracesFolderPath = "{}/{}".format(gameFolderPath,"HMD_traces")

            ### MANAGEMENT FRAMES ###
            if("WLAN_BOTH_ManagementFrames.csv" in listdir(HMDTracesFolderPath)):
                filePath = "{}/{}".format(HMDTracesFolderPath,"WLAN_BOTH_ManagementFrames.csv")
                print("{} file processing".format(filePath))

                HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates,\
                    HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes,HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times,\
                    HMD_DWN_MANAGEMENT_FRAMES_DataRates,HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes = processHMDManagementFramesTraces(filePath,startTimeInMs,endTimeInMs,HMD_MAC,AP_MAC2)
            else:
                HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates,\
                    HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes,HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times,\
                    HMD_DWN_MANAGEMENT_FRAMES_DataRates,HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes = []
                print("make sure that the trace file 'WLAN_BOTH_ManagementFrames.csv' is in the 'HMD_traces' folder in the path {} and its name is 'WLAN_BOTH_ManagementFrames.csv'".format(HMDTracesFolderPath))
            

            ### DATA FRAMES TYPE I ###
            if("WLAN_BOTH_DataFramesType1.csv" in listdir(HMDTracesFolderPath)):
                filePath = "{}/{}".format(HMDTracesFolderPath,"WLAN_BOTH_DataFramesType1.csv")
                print("{} file processing".format(filePath))

                HMD_UP_DATA1_FRAMES_NBs, HMD_UP_DATA1_FRAMES_Times, HMD_UP_DATA1_FRAMES_DataRates,\
                    HMD_UP_DATA1_FRAMES_Frames_Sizes,HMD_UP_DATA1_FRAMES_Frames_SeqNB= processHMDDataFramesTraces(filePath,startTimeInMs,endTimeInMs,HMD_MAC,AP_MAC2,1)

            else:
                HMD_UP_DATA1_FRAMES_NBs, HMD_UP_DATA1_FRAMES_Times, HMD_UP_DATA1_FRAMES_DataRates,\
                    HMD_UP_DATA1_FRAMES_Frames_Sizes,HMD_UP_DATA1_FRAMES_Frames_SeqNB = []
                print("make sure that the trace file 'WLAN_BOTH_DataFramesType1.csv' is in the 'HMD_traces' folder in the path {} and its name is 'WLAN_BOTH_DataFramesType1.csv'".format(HMDTracesFolderPath))

            
            ### RETRANSMITTED DATA FRAMES TYPE I ###
            if("WLAN_BOTH_RetransmittedDataFramesType1.csv" in listdir(HMDTracesFolderPath)):
                filePath = "{}/{}".format(HMDTracesFolderPath,"WLAN_BOTH_RetransmittedDataFramesType1.csv")
                print("{} file processing".format(filePath))

                HMD_UP_RE_DATA1_FRAMES_NBs, HMD_UP_RE_DATA1_FRAMES_Times, HMD_UP_RE_DATA1_FRAMES_DataRates,\
                    HMD_UP_RE_DATA1_FRAMES_Frames_Sizes,HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB= processHMDDataFramesTraces(filePath,startTimeInMs,endTimeInMs,HMD_MAC,AP_MAC2,1)

            else:
                HMD_UP_RE_DATA1_FRAMES_NBs, HMD_UP_RE_DATA1_FRAMES_Times, HMD_UP_RE_DATA1_FRAMES_DataRates,\
                    HMD_UP_RE_DATA1_FRAMES_Frames_Sizes,HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB = []
                print("make sure that the trace file 'WLAN_BOTH_RetransmittedDataFramesType1.csv' is in the 'HMD_traces' folder in the path {} and its name is 'WLAN_BOTH_RetransmittedDataFramesType1.csv'".format(HMDTracesFolderPath))

            
            ### DATA FRAMES TYPE II ###
            if("WLAN_BOTH_DataFramesType2.csv" in listdir(HMDTracesFolderPath)):
                filePath = "{}/{}".format(HMDTracesFolderPath,"WLAN_BOTH_DataFramesType2.csv")
                print("{} file processing".format(filePath))

                HMD_UP_DATA2_FRAMES_NBs, HMD_UP_DATA2_FRAMES_Times, HMD_UP_DATA2_FRAMES_DataRates,\
                    HMD_UP_DATA2_FRAMES_Data_Sizes, HMD_UP_DATA2_FRAMES_Frames_Sizes, HMD_UP_DATA2_FRAMES_Frames_SeqNB, \
                    HMD_DWN_DATA2_FRAMES_NBs,HMD_DWN_DATA2_FRAMES_Times, HMD_DWN_DATA2_FRAMES_DataRates, HMD_DWN_DATA2_FRAMES_Data_Sizes,\
                    HMD_DWN_DATA2_FRAMES_Frames_Sizes,HMD_DWN_DATA2_FRAMES_Frames_SeqNB = \
                        processHMDDataFramesTraces(filePath,startTimeInMs,endTimeInMs,HMD_MAC,AP_MAC1,2)

            else:
                HMD_UP_DATA2_FRAMES_NBs, HMD_UP_DATA2_FRAMES_Times, HMD_UP_DATA2_FRAMES_DataRates,\
                    HMD_UP_DATA2_FRAMES_Data_Sizes, HMD_UP_DATA2_FRAMES_Frames_Sizes, HMD_UP_DATA2_FRAMES_Frames_SeqNB, \
                    HMD_DWN_DATA2_FRAMES_NBs,HMD_DWN_DATA2_FRAMES_Times, HMD_DWN_DATA2_FRAMES_DataRates, HMD_DWN_DATA2_FRAMES_Data_Sizes,\
                    HMD_DWN_DATA2_FRAMES_Frames_Sizes,HMD_DWN_DATA2_FRAMES_Frames_SeqNB = []
                print("make sure that the trace file 'WLAN_BOTH_DataFramesType2.csv' is in the 'HMD_traces' folder in the path {} and its name is 'WLAN_BOTH_DataFramesType2.csv'".format(HMDTracesFolderPath))
            

            ### RETRANSMITTED DATA FRAMES TYPE II ###
            if("WLAN_BOTH_RetransmittedDataFramesType2.csv" in listdir(HMDTracesFolderPath)):
                filePath = "{}/{}".format(HMDTracesFolderPath,"WLAN_BOTH_RetransmittedDataFramesType2.csv")
                print("{} file processing".format(filePath))

                HMD_UP_RE_DATA2_FRAMES_NBs, HMD_UP_RE_DATA2_FRAMES_Times, HMD_UP_RE_DATA2_FRAMES_DataRates,\
                    HMD_UP_RE_DATA2_FRAMES_Data_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB, \
                    HMD_DWN_RE_DATA2_FRAMES_NBs,HMD_DWN_RE_DATA2_FRAMES_Times, HMD_DWN_RE_DATA2_FRAMES_DataRates, HMD_DWN_RE_DATA2_FRAMES_Data_Sizes,\
                    HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes,HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB = \
                        processHMDDataFramesTraces(filePath,startTimeInMs,endTimeInMs,HMD_MAC,AP_MAC1,2)

            else:
                HMD_UP_RE_DATA2_FRAMES_NBs, HMD_UP_RE_DATA2_FRAMES_Times, HMD_UP_RE_DATA2_FRAMES_DataRates,\
                    HMD_UP_RE_DATA2_FRAMES_Data_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB, \
                    HMD_DWN_RE_DATA2_FRAMES_NBs,HMD_DWN_RE_DATA2_FRAMES_Times, HMD_DWN_RE_DATA2_FRAMES_DataRates, HMD_DWN_RE_DATA2_FRAMES_Data_Sizes,\
                    HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes,HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB = []
                print("make sure that the trace file 'WLAN_BOTH_RetransmittedDataFramesType2.csv' is in the 'HMD_traces' folder in the path {} and its name is 'WLAN_BOTH_RetransmittedDataFramesType2.csv'".format(HMDTracesFolderPath))


            ### DATA FRAMES TYPE III ###
            if("WLAN_BOTH_DataFramesType3.csv" in listdir(HMDTracesFolderPath)):
                filePath = "{}/{}".format(HMDTracesFolderPath,"WLAN_BOTH_DataFramesType3.csv")
                print("{} file processing".format(filePath))

                HMD_UP_DATA3_FRAMES_NBs, HMD_UP_DATA3_FRAMES_Times, HMD_UP_DATA3_FRAMES_DataRates,\
                    HMD_UP_DATA3_FRAMES_Data_Sizes, HMD_UP_DATA3_FRAMES_Frames_Sizes, HMD_UP_DATA3_FRAMES_Frames_SeqNB, \
                    HMD_DWN_DATA3_FRAMES_NBs,HMD_DWN_DATA3_FRAMES_Times, HMD_DWN_DATA3_FRAMES_DataRates, HMD_DWN_DATA3_FRAMES_Data_Sizes,\
                    HMD_DWN_DATA3_FRAMES_Frames_Sizes,HMD_DWN_DATA3_FRAMES_Frames_SeqNB = \
                        processHMDDataFramesTraces(filePath,startTimeInMs,endTimeInMs,HMD_MAC,server_MAC,3)

            else:
                HMD_UP_DATA3_FRAMES_NBs, HMD_UP_DATA3_FRAMES_Times, HMD_UP_DATA3_FRAMES_DataRates,\
                    HMD_UP_DATA3_FRAMES_Data_Sizes, HMD_UP_DATA3_FRAMES_Frames_Sizes, HMD_UP_DATA3_FRAMES_Frames_SeqNB, \
                    HMD_DWN_DATA3_FRAMES_NBs,HMD_DWN_DATA3_FRAMES_Times, HMD_DWN_DATA3_FRAMES_DataRates, HMD_DWN_DATA3_FRAMES_Data_Sizes,\
                    HMD_DWN_DATA3_FRAMES_Frames_Sizes,HMD_DWN_DATA3_FRAMES_Frames_SeqNB = []
                print("make sure that the trace file 'WLAN_BOTH_DataFramesType3.csv' is in the 'HMD_traces' folder in the path {} and its name is 'WLAN_BOTH_DataFramesType3.csv'".format(HMDTracesFolderPath))
            

            ### RETRANSMITTED DATA FRAMES TYPE III ###
            if("WLAN_BOTH_RetransmittedDataFramesType3.csv" in listdir(HMDTracesFolderPath)):
                filePath = "{}/{}".format(HMDTracesFolderPath,"WLAN_BOTH_RetransmittedDataFramesType3.csv")
                print("{} file processing".format(filePath))

                HMD_UP_RE_DATA3_FRAMES_NBs, HMD_UP_RE_DATA3_FRAMES_Times, HMD_UP_RE_DATA3_FRAMES_DataRates,\
                    HMD_UP_RE_DATA3_FRAMES_Data_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB, \
                    HMD_DWN_RE_DATA3_FRAMES_NBs,HMD_DWN_RE_DATA3_FRAMES_Times, HMD_DWN_RE_DATA3_FRAMES_DataRates, HMD_DWN_RE_DATA3_FRAMES_Data_Sizes,\
                    HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes,HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB = \
                        processHMDDataFramesTraces(filePath,startTimeInMs,endTimeInMs,HMD_MAC,server_MAC,3)

            else:
                HMD_UP_RE_DATA3_FRAMES_NBs, HMD_UP_RE_DATA3_FRAMES_Times, HMD_UP_RE_DATA3_FRAMES_DataRates,\
                    HMD_UP_RE_DATA3_FRAMES_Data_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB, \
                    HMD_DWN_RE_DATA3_FRAMES_NBs,HMD_DWN_RE_DATA3_FRAMES_Times, HMD_DWN_RE_DATA3_FRAMES_DataRates, HMD_DWN_RE_DATA3_FRAMES_Data_Sizes,\
                    HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes,HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB = []
                print("make sure that the trace file 'WLAN_BOTH_RetransmittedDataFramesType3.csv' is in the 'HMD_traces' folder in the path {} and its name is 'WLAN_BOTH_RetransmittedDataFramesType3.csv'".format(HMDTracesFolderPath))



        else:
            print("make sure that 'HMD_traces' folder is inside the game folder {} in the path {}".format(gameName,gameFolderPath))

        results = (HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates,
                    HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes, HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times,
                    HMD_DWN_MANAGEMENT_FRAMES_DataRates, HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes, HMD_UP_DATA1_FRAMES_NBs, 
                    HMD_UP_DATA1_FRAMES_Times, HMD_UP_DATA1_FRAMES_DataRates, HMD_UP_DATA1_FRAMES_Frames_Sizes,
                    HMD_UP_DATA1_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA1_FRAMES_NBs, HMD_UP_RE_DATA1_FRAMES_Times, 
                    HMD_UP_RE_DATA1_FRAMES_DataRates, HMD_UP_RE_DATA1_FRAMES_Frames_Sizes, HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB,
                    HMD_UP_DATA2_FRAMES_NBs, HMD_UP_DATA2_FRAMES_Times, HMD_UP_DATA2_FRAMES_DataRates, HMD_UP_DATA2_FRAMES_Data_Sizes,
                    HMD_UP_DATA2_FRAMES_Frames_Sizes, HMD_UP_DATA2_FRAMES_Frames_SeqNB, HMD_DWN_DATA2_FRAMES_NBs, HMD_DWN_DATA2_FRAMES_Times, 
                    HMD_DWN_DATA2_FRAMES_DataRates, HMD_DWN_DATA2_FRAMES_Data_Sizes, HMD_DWN_DATA2_FRAMES_Frames_Sizes, 
                    HMD_DWN_DATA2_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA2_FRAMES_NBs, HMD_UP_RE_DATA2_FRAMES_Times, HMD_UP_RE_DATA2_FRAMES_DataRates,
                    HMD_UP_RE_DATA2_FRAMES_Data_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB, 
                    HMD_DWN_RE_DATA2_FRAMES_NBs, HMD_DWN_RE_DATA2_FRAMES_Times, HMD_DWN_RE_DATA2_FRAMES_DataRates, HMD_DWN_RE_DATA2_FRAMES_Data_Sizes,
                    HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB, HMD_UP_DATA3_FRAMES_NBs, HMD_UP_DATA3_FRAMES_Times, 
                    HMD_UP_DATA3_FRAMES_DataRates, HMD_UP_DATA3_FRAMES_Data_Sizes, HMD_UP_DATA3_FRAMES_Frames_Sizes, HMD_UP_DATA3_FRAMES_Frames_SeqNB,
                    HMD_DWN_DATA3_FRAMES_NBs, HMD_DWN_DATA3_FRAMES_Times, HMD_DWN_DATA3_FRAMES_DataRates, HMD_DWN_DATA3_FRAMES_Data_Sizes,
                    HMD_DWN_DATA3_FRAMES_Frames_Sizes, HMD_DWN_DATA3_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA3_FRAMES_NBs, HMD_UP_RE_DATA3_FRAMES_Times, 
                    HMD_UP_RE_DATA3_FRAMES_DataRates, HMD_UP_RE_DATA3_FRAMES_Data_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_Sizes, 
                    HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB, HMD_DWN_RE_DATA3_FRAMES_NBs, HMD_DWN_RE_DATA3_FRAMES_Times, HMD_DWN_RE_DATA3_FRAMES_DataRates, 
                    HMD_DWN_RE_DATA3_FRAMES_Data_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB)
        HMDTracesResults.append((gameName,results))
    

     

    return HMDTracesResults

        
def processTracesFolder(tracesFolder,startTime,endTime,HMD_IP,server_IP,HMD_MAC,server_MAC,AP_MAC1,AP_MAC2):
    startTimeInMs = convertTime(startTime)
    endTimeInMs = convertTime(endTime)
    gamesFolders = listdir(tracesFolder)
    tracesResults = []



    if(len(gamesFolders)==0):
        print("WARNING: the traces file could not be found")
        return [[],[]]
    
    print("traces files:")
    print("#####################################")

    tracesResults.append(processServerTraces(tracesFolder,startTimeInMs,endTimeInMs,HMD_IP,server_IP))
    tracesResults.append(processHMDTraces(tracesFolder,startTimeInMs,endTimeInMs,HMD_MAC,server_MAC,AP_MAC1,AP_MAC2))

    print("#####################################")
    

    return tracesResults


def main():
    

    startTime = "00:00:00"
    endTime = "23:59:59"
    # startTime = "22:00"   §
    # endTime = "22:05"
    # startTime = "15:15"
    # endTime = "15:20"
    HMD_IP = "192.168.1.179"      # the HMD is linked wirelessly to the access point
    server_IP = "192.168.1.14"    # the server is linked by a wired link to the access point
    HMD_MAC = "Facebook_63:35:01" # the HMD is linked wirelessly to the access point
    server_MAC = "Dell_31:58:70"  # the server is linked by a wired link to the access point
    AP_MAC1 = "Arcadyan_26:74:c1" # for 802.11ax (HE)
    AP_MAC2 = "Arcadyan_26:74:c3" # for 802.11a  (OFDM)
    tracesFolder = "traces"
    logsFolder = "log_files"

    
    LogsFolderResults = processLogsFolder(logsFolder,startTime,endTime)
    #serverTracesResults, HMDTracesResults = processTracesFolder(tracesFolder,startTime,endTime,HMD_IP,server_IP,HMD_MAC,server_MAC,AP_MAC1,AP_MAC2)
    

    plotGraph.plotResults(LogsFolderResults)


    # for resultItem in HMDTracesResults:
    #     results = resultItem.__getitem__(1)
    #     HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates, \
    #         HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes, HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times, \
    #         HMD_DWN_MANAGEMENT_FRAMES_DataRates, HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes, HMD_UP_DATA1_FRAMES_NBs, \
    #         HMD_UP_DATA1_FRAMES_Times, HMD_UP_DATA1_FRAMES_DataRates, HMD_UP_DATA1_FRAMES_Frames_Sizes, \
    #         HMD_UP_DATA1_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA1_FRAMES_NBs, HMD_UP_RE_DATA1_FRAMES_Times, \
    #         HMD_UP_RE_DATA1_FRAMES_DataRates, HMD_UP_RE_DATA1_FRAMES_Frames_Sizes, HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB, \
    #         HMD_UP_DATA2_FRAMES_NBs, HMD_UP_DATA2_FRAMES_Times, HMD_UP_DATA2_FRAMES_DataRates, HMD_UP_DATA2_FRAMES_Data_Sizes, \
    #         HMD_UP_DATA2_FRAMES_Frames_Sizes, HMD_UP_DATA2_FRAMES_Frames_SeqNB, HMD_DWN_DATA2_FRAMES_NBs, HMD_DWN_DATA2_FRAMES_Times, \
    #         HMD_DWN_DATA2_FRAMES_DataRates, HMD_DWN_DATA2_FRAMES_Data_Sizes, HMD_DWN_DATA2_FRAMES_Frames_Sizes, \
    #         HMD_DWN_DATA2_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA2_FRAMES_NBs, HMD_UP_RE_DATA2_FRAMES_Times, HMD_UP_RE_DATA2_FRAMES_DataRates, \
    #         HMD_UP_RE_DATA2_FRAMES_Data_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB,  \
    #         HMD_DWN_RE_DATA2_FRAMES_NBs, HMD_DWN_RE_DATA2_FRAMES_Times, HMD_DWN_RE_DATA2_FRAMES_DataRates, HMD_DWN_RE_DATA2_FRAMES_Data_Sizes, \
    #         HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB, HMD_UP_DATA3_FRAMES_NBs, HMD_UP_DATA3_FRAMES_Times, \
    #         HMD_UP_DATA3_FRAMES_DataRates, HMD_UP_DATA3_FRAMES_Data_Sizes, HMD_UP_DATA3_FRAMES_Frames_Sizes, HMD_UP_DATA3_FRAMES_Frames_SeqNB, \
    #         HMD_DWN_DATA3_FRAMES_NBs, HMD_DWN_DATA3_FRAMES_Times, HMD_DWN_DATA3_FRAMES_DataRates, HMD_DWN_DATA3_FRAMES_Data_Sizes, \
    #         HMD_DWN_DATA3_FRAMES_Frames_Sizes, HMD_DWN_DATA3_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA3_FRAMES_NBs, HMD_UP_RE_DATA3_FRAMES_Times, \
    #         HMD_UP_RE_DATA3_FRAMES_DataRates, HMD_UP_RE_DATA3_FRAMES_Data_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_Sizes, \
    #         HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB, HMD_DWN_RE_DATA3_FRAMES_NBs, HMD_DWN_RE_DATA3_FRAMES_Times, HMD_DWN_RE_DATA3_FRAMES_DataRates, \
    #         HMD_DWN_RE_DATA3_FRAMES_Data_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB = results
    #     counter = 1
    #     for i in range(len(HMD_DWN_DATA3_FRAMES_NBs)):
    #         print("({}) {}-{}-{}-{}-{}-{}".format(counter,HMD_DWN_DATA3_FRAMES_NBs[i],HMD_DWN_DATA3_FRAMES_Times[i],HMD_DWN_DATA3_FRAMES_DataRates[i],HMD_DWN_DATA3_FRAMES_Data_Sizes[i],HMD_DWN_DATA3_FRAMES_Frames_Sizes[i],HMD_DWN_DATA3_FRAMES_Frames_SeqNB[i]))
    #         counter = counter + 1
    #     for i in range(len(HMD_UP_DATA3_FRAMES_NBs)):
    #         print("({}) {}-{}-{}-{}-{}-{}".format(counter,HMD_UP_DATA3_FRAMES_NBs[i],HMD_UP_DATA3_FRAMES_Times[i],HMD_UP_DATA3_FRAMES_DataRates[i],HMD_UP_DATA3_FRAMES_Data_Sizes[i],HMD_UP_DATA3_FRAMES_Frames_Sizes[i],HMD_UP_DATA3_FRAMES_Frames_SeqNB[i]))
    #         counter = counter + 1

if __name__ == "__main__":
   main()