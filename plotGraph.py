import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

def plotLogsResults(results):
    root_folder = "plots"

    for resultItem in results:
        gameName,sessionLogResult,OVRMetricsResult,logcatResults,steamVRLogResults = resultItem
        try:
            os.mkdir("{}/{}".format(root_folder,gameName))
        except:
            pass
        plotLatency(root_folder,gameName,sessionLogResult,OVRMetricsResult,logcatResults,steamVRLogResults)
        plotFPS(root_folder,gameName,sessionLogResult,OVRMetricsResult,logcatResults)
        plotpktsstats(root_folder,gameName,sessionLogResult)
        plotBatteryPercentage(root_folder,gameName,sessionLogResult,OVRMetricsResult)
        plotTemperature(root_folder,gameName,OVRMetricsResult,logcatResults)
        plotFramesStats(root_folder,gameName,OVRMetricsResult,logcatResults,steamVRLogResults)
        plotUtilization(root_folder,gameName,OVRMetricsResult,logcatResults)
        plotMaxRotationalSpeed(root_folder,gameName,OVRMetricsResult)
        plotFoveationLevel(root_folder,gameName,OVRMetricsResult,logcatResults)
        plotNumberOfTears(root_folder,gameName,logcatResults)
        plotPowerLevel(root_folder,gameName,logcatResults)
        plotLayersCount(root_folder,gameName,logcatResults)
        plotRunningTime(root_folder,gameName,steamVRLogResults)



def plotServerTracesResults(serverTracesResults):
    print("hello")



def plotLatency(root_folder,gameName,sessionLogResult,OVRMetricsResult,logcatResults,steamVRLogResults):
    result_folder_name = "latency"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    try:
        os.mkdir(prefix)
    except:
        pass

    stats,gStats = sessionLogResult
    gTimes,totalPipelineLatencyS,gameTimeS,serverCompositorS,encoderS,networkS,decoderS,decoderQueueS,clientCompositorS,\
            vsyncQueueS,gClientFPS,gServerFPS = gStats

    Time_Stamp,battery_level_percentage,battery_temperature_celcius,sensor_temperature_celcius,power_level_state,\
        average_frame_rate,display_refresh_rate,average_prediction_milliseconds,early_frame_count,stale_frame_count,\
        maximum_rotational_speed_degrees_per_second,foveation_level,eye_buffer_width,eye_buffer_height,\
        app_gpu_time_microseconds,timewarp_gpu_time_microseconds,guardian_gpu_time_microseconds,cpu_utilization_percentage,\
        gpu_utilization_percentage,stale_frames_consecutive,screen_power_consumption,vrshell_average_frame_rate,\
        vrshell_gpu_time_microseconds,vrshell_and_guardian_gpu_time_microseconds,render_scale = OVRMetricsResult
    
    
    #################### Line Graph ####################
    # line graph for latency components from gStats
    x = [float(i)/1000 for i in gTimes[5000:5050]]

    y1 = [float(i) for i in totalPipelineLatencyS[5000:5050]]
    y1Label = 'totalPipelineLatencyS'
    
    y2 = [float(i) for i in gameTimeS[5000:5050]]
    y2Label = 'gameTimeS'

    y3 = [float(i) for i in serverCompositorS[5000:5050]]
    y3Label = 'serverCompositorS'
    
    y4 = [float(i) for i in encoderS[5000:5050]]
    y4Label = 'encoderS'

    y5 = [float(i) for i in networkS[5000:5050]]
    y5Label = 'networkS'
    
    y6 = [float(i) for i in decoderS[5000:5050]]
    y6Label = 'decoderS'

    y7 = [float(i) for i in decoderQueueS[5000:5050]]
    y7Label = 'decoderQueueS'
    
    y8 = [float(i) for i in clientCompositorS[5000:5050]]
    y8Label = 'clientCompositorS'

    y9 = [float(i) for i in vsyncQueueS[5000:5050]]
    y9Label = 'vsyncQueueS'

    plt.plot(x,y1,label=y1Label,c='red',marker = '.',linestyle='-.')
    plt.plot(x,y2,label=y2Label,c='blue',marker = 'x',)
    plt.plot(x,y3,label=y3Label,c='black',marker = '*',linestyle='-.')
    plt.plot(x,y4,label=y4Label,c='purple',marker = 'v')
    plt.plot(x,y5,label=y5Label,c='green',marker = 'x',linestyle='-.')
    plt.plot(x,y6,label=y6Label,marker = '.')
    plt.plot(x,y7,label=y7Label,c='orange',marker = '.',linestyle='-.')
    plt.plot(x,y8,label=y8Label,c='cyan',marker = 'x',)
    plt.plot(x,y9,label=y9Label,c='pink',marker = '*',linestyle='-.')

    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('times in (sec)', fontsize=12)
    plt.ylabel('latency in (ms)', fontsize=12)
    plt.title("{}".format(gameName))
    #plt.yticks([0,20,40,60])
    plt.savefig('{}/results1.png'.format(prefix))
    plt.show()
    ####################################################



    #################### CDF  Graph ####################
    # CDF Graph for latency components from gStats
    tempTotalPipelineLatency = []
    tempGameTime = []
    tempServerCompositor = []
    tempEncoder = []
    tempNetwork = []
    tempDecoder = []
    tempDecoderQueue = []
    tempClientCompositor = []
    tempVsyncQueueS = []
    tempClientFPS = []
    tempServerFPS = []
    count = 0
    for x in totalPipelineLatencyS:
        if x < 125:
            tempTotalPipelineLatency.append(x)
            tempGameTime.append(gameTimeS[count])
            tempServerCompositor.append(serverCompositorS[count])
            tempEncoder.append(encoderS[count])
            tempNetwork.append(networkS[count])
            tempDecoder.append(decoderS[count])
            tempDecoderQueue.append(decoderQueueS[count])
            tempClientCompositor.append(clientCompositorS[count])
            tempVsyncQueueS.append(vsyncQueueS[count])
            tempClientFPS.append(gClientFPS[count])
            tempServerFPS.append(gServerFPS[count])
        count = count + 1    

    data1 = [float(i) for i in tempTotalPipelineLatency]
    data2 = [float(i) for i in tempGameTime]
    data3 = [float(i) for i in tempServerCompositor]
    data4 = [float(i) for i in tempEncoder]
    data5 = [float(i) for i in tempNetwork]
    data6 = [float(i) for i in tempDecoder]
    data7 = [float(i) for i in tempDecoderQueue]
    data8 = [float(i) for i in tempClientCompositor]
    data9 = [float(i) for i in tempVsyncQueueS]
    x1 = np.sort(data1)
    x2 = np.sort(data2)
    x3 = np.sort(data3)
    x4 = np.sort(data4)
    x5 = np.sort(data5)
    x6 = np.sort(data6)
    x7 = np.sort(data7)
    x8 = np.sort(data8)
    x9 = np.sort(data9)
    y1 = np.arange(len(x1))/float(len(x1))
    y2 = np.arange(len(x2))/float(len(x2))
    y3 = np.arange(len(x3))/float(len(x3))
    y4 = np.arange(len(x4))/float(len(x4))
    y5 = np.arange(len(x5))/float(len(x5))
    y6 = np.arange(len(x6))/float(len(x6))
    y7 = np.arange(len(x7))/float(len(x7))
    y8 = np.arange(len(x8))/float(len(x8))
    y9 = np.arange(len(x9))/float(len(x9))
    plt.plot(x1, y1,label=y1Label,c='red',linestyle='-.')
    plt.plot(x2, y2,label=y2Label,c='blue',linestyle='-')
    plt.plot(x3, y3,label=y3Label,c='black',linestyle=':')
    plt.plot(x4, y4,label=y4Label,c='purple',linestyle='--')
    plt.plot(x5, y5,label=y5Label,c='green',linestyle='-.')
    plt.plot(x6, y6,label=y6Label,linestyle='-')
    plt.plot(x7, y7,label=y7Label,c='orange',linestyle=':')
    plt.plot(x8, y8,label=y8Label,c='cyan',linestyle='--')
    plt.plot(x9, y9,label=y9Label,c='pink',linestyle='-.')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('latency in (ms)', fontsize=12)
    plt.ylabel('CDF', fontsize=12)
    plt.title("{}".format(gameName))
    plt.yticks([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
    plt.xticks([0,10,20,30,40,50,60,70,80,90,100,110,120])
    plt.savefig('{}/results2.png'.format(prefix))
    plt.show()
    ####################################################



    ############ Latency Components Line Graph ##############
    # from the OVRmatrics file
    newTimeStamp = relativeTime(Time_Stamp)
    x = [float(i)/1000 for i in newTimeStamp]
    y1 = [float(i) for i in average_prediction_milliseconds]
    y1Label = 'average prediction (ms)'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.')
    y2 = [float(i)/1000 for i in app_gpu_time_microseconds]
    y2Label = 'app gpu time (ms)'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='-')
    y3 = [float(i)/1000 for i in timewarp_gpu_time_microseconds]
    y3Label = 'timewarp gpu time (ms)'
    plt.plot(x,y3,label=y3Label,c='purple',linestyle=':')
    y4 = [float(i)/1000 for i in guardian_gpu_time_microseconds]
    y4Label = 'guardian gpu time (ms)'
    plt.plot(x,y4,label=y4Label,c='green',linestyle='-.')
    y5 = [float(i)/1000 for i in vrshell_gpu_time_microseconds]
    y5Label = 'vrshell gpu time (ms)'
    plt.plot(x,y5,label=y5Label,c='black',linestyle='-')
    y6 = [float(i)/1000 for i in vrshell_and_guardian_gpu_time_microseconds]
    y6Label = 'vrshell and guardian gpu time (ms)'
    plt.plot(x,y6,label=y6Label,c='orange',linestyle=':')
    
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('latency (ms)', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results3.png'.format(prefix))
    plt.show()
    ####################################################   



    #################### CDF  Graph ####################
    # CDF Graph for latency components from OVRMetrics    
    data1 = [float(i) for i in average_prediction_milliseconds]
    data2 = [float(i)/1000 for i in app_gpu_time_microseconds]
    data3 = [float(i)/1000 for i in timewarp_gpu_time_microseconds]
    data4 = [float(i)/1000 for i in guardian_gpu_time_microseconds]
    data5 = [float(i)/1000 for i in vrshell_gpu_time_microseconds]
    data6 = [float(i)/1000 for i in vrshell_and_guardian_gpu_time_microseconds]
    x1 = np.sort(data1)
    x2 = np.sort(data2)
    x3 = np.sort(data3)
    x4 = np.sort(data4)
    x5 = np.sort(data5)
    x6 = np.sort(data6)
    y1 = np.arange(len(x1))/float(len(x1))
    y2 = np.arange(len(x2))/float(len(x2))
    y3 = np.arange(len(x3))/float(len(x3))
    y4 = np.arange(len(x4))/float(len(x4))
    y5 = np.arange(len(x5))/float(len(x5))
    y6 = np.arange(len(x6))/float(len(x6))
    plt.plot(x1, y1,label=y1Label,c='red',linestyle='-.')
    plt.plot(x2, y2,label=y2Label,c='blue',linestyle='-')
    plt.plot(x3, y3,label=y3Label,c='black',linestyle=':')
    plt.plot(x4, y4,label=y4Label,c='purple',linestyle='--')
    plt.plot(x5, y5,label=y5Label,c='green',linestyle='-.')
    plt.plot(x6, y6,label=y6Label,linestyle='-')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('latency in (ms)', fontsize=12)
    plt.ylabel('CDF', fontsize=12)
    plt.title("{}".format(gameName))
    plt.yticks([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
    # plt.xticks([0,100,200,300,400,500,600,700,800,900,1000])
    plt.savefig('{}/results4.png'.format(prefix))
    plt.show()
    ####################################################


    ############ Latency Components Line Graph ##############
    # from the logcat file
    time,targetedFPS,achievedFPS,predictionTime,tear,earlyFrames,staleFrames,fov,CPUClockLevel\
        ,GPUClockLevel,PLS,batteryTemperature, sensorTemperature,TWTime,appTime,guardianTime\
        ,CPUandGPUTime,LCnt,GPUUtilization,CPUUtilizationAverage,CPUUtilizationWorst = logcatResults
    newTime = relativeTime(time)
    gpuTime = []
    cpuTime = []
    for i in range(len(time)):
        tempGPUTime = float(TWTime[i])+float(appTime[i])+float(guardianTime[i])
        gpuTime.append(tempGPUTime)
        cpuTime.append(float(CPUandGPUTime[i])-tempGPUTime)


    x = [float(i)/1000 for i in newTime]
    y1 = [float(i) for i in predictionTime]
    y1Label = 'prediction time (ms)'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.')
    y2 = [float(i) for i in TWTime]
    y2Label = 'timewarp gpu time (ms)'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='-')
    y3 = [float(i) for i in appTime]
    y3Label = 'app gpu time (ms)'
    plt.plot(x,y3,label=y3Label,c='purple',linestyle=':')
    y4 = [float(i) for i in guardianTime]
    y4Label = 'guardian gpu time (ms)'
    plt.plot(x,y4,label=y4Label,c='green',linestyle='-.')
    y5 = [float(i) for i in CPUandGPUTime]
    y5Label = 'cpu and gpu time (ms)'
    plt.plot(x,y5,label=y5Label,c='black',linestyle='-')
    y6 = [float(i) for i in gpuTime]
    y6Label = 'gpu time (ms)'
    plt.plot(x,y6,label=y6Label,c='orange',linestyle=':')
    y7 = [float(i) for i in cpuTime]
    y7Label = 'cpu time (ms)'
    plt.plot(x,y7,label=y7Label,c='cyan',linestyle=':')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('latency (ms)', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results5.png'.format(prefix))
    plt.show()
    ###################################################   


    #################### CDF  Graph ####################
    # CDF Graph for latency components from logcat
    data1 = [float(i) for i in predictionTime]
    data2 = [float(i) for i in TWTime]
    data3 = [float(i) for i in appTime]
    data4 = [float(i) for i in guardianTime]
    data5 = [float(i) for i in CPUandGPUTime]
    data6 = [float(i) for i in gpuTime]
    data7 = [float(i) for i in cpuTime]
    x1 = np.sort(data1)
    x2 = np.sort(data2)
    x3 = np.sort(data3)
    x4 = np.sort(data4)
    x5 = np.sort(data5)
    x6 = np.sort(data6)
    x7 = np.sort(data7)
    y1 = np.arange(len(x1))/float(len(x1))
    y2 = np.arange(len(x2))/float(len(x2))
    y3 = np.arange(len(x3))/float(len(x3))
    y4 = np.arange(len(x4))/float(len(x4))
    y5 = np.arange(len(x5))/float(len(x5))
    y6 = np.arange(len(x6))/float(len(x6))
    y7 = np.arange(len(x7))/float(len(x7))
    plt.plot(x1, y1,label=y1Label,c='red',linestyle='-.')
    plt.plot(x2, y2,label=y2Label,c='blue',linestyle='-')
    plt.plot(x3, y3,label=y3Label,c='black',linestyle=':')
    plt.plot(x4, y4,label=y4Label,c='purple',linestyle='--')
    plt.plot(x5, y5,label=y5Label,c='green',linestyle='-.')
    plt.plot(x6, y6,label=y6Label,c="cyan",linestyle='-')
    plt.plot(x7, y7,label=y7Label,linestyle='-')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('latency in (ms)', fontsize=12)
    plt.ylabel('CDF', fontsize=12)
    plt.title("{}".format(gameName))
    plt.yticks([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
    plt.savefig('{}/results6.png'.format(prefix))
    plt.show()
    ####################################################



    ############ Latency Components Line Graph ##############
    # from the appPerformanceStatsMonitorFile of steamVRLogResults
    appPerformanceStatsMonitorFile,appPerformanceStatsCompositorFile = steamVRLogResults
    appPerformanceStatsTimeStamp,appID,NumFramePresents,NumDroppedFrames,NumReprojected,\
        NumFramePresentsOnStartup,NumDroppedFramesOnStartup,NumReprojectedFramesOnStartup,\
        NumLoading,NumFramePresentsLoading,NumDroppedFramesLoading,NumReprojectedFramesLoading,\
        NumTimedOut,NumFramePresentsTimedOut,NumDroppedFramesTimedOut,NumReprojectedFramesTimedOut,\
        AvgSubmitsPerFrame,AvgCompositorCPUTimeMS,AvgCompositorGPUTimeMS,AvgTargetFPS,\
        AvgApplicationCPUTimeMS,AvgApplicationGPUTimeMS,AppSeconds,AppHeadsetActiveSeconds,\
        NumSingleDroppedFramesOverEntireRun,Num2DroppedFramesOverEntireRun,Num3DroppedFramesOverEntireRun,\
        Num4MoreDroppedFramesOverEntireRun,totalNumOfFramesEntireRun,totalNumOfExpectedFrameEntireRun = appPerformanceStatsMonitorFile
    appPerformanceStatsNewTimeStamp = relativeTime(appPerformanceStatsTimeStamp)
    x = [float(i)/1000 for i in appPerformanceStatsNewTimeStamp]
    y1 = [float(i) for i in AvgCompositorCPUTimeMS]
    y1Label = 'compositor cpu'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.',marker="x")
    y2 = [float(i) for i in AvgCompositorGPUTimeMS]
    y2Label = 'compositor gpu'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='-',marker="v")
    y3 = [float(i) for i in AvgApplicationCPUTimeMS]
    y3Label = 'app cpu'
    plt.plot(x,y3,label=y3Label,c='green',linestyle='--',marker="D")
    y4 = [float(i) for i in AvgApplicationGPUTimeMS]
    y4Label = 'app gpu'
    plt.plot(x,y4,label=y4Label,c='black',linestyle=':',marker=".")
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('avg latency (ms)', fontsize=12)
    plt.savefig('{}/results7.png'.format(prefix))
    plt.show()
    ####################################################



    #################### CDF  Graph ####################
    # from the appPerformanceStatsMonitorFile of steamVRLogResults    
    data1 = [float(i) for i in AvgCompositorCPUTimeMS]
    data2 = [float(i) for i in AvgCompositorGPUTimeMS]
    data3 = [float(i) for i in AvgApplicationCPUTimeMS]
    data4 = [float(i) for i in AvgApplicationGPUTimeMS]
    x1 = np.sort(data1)
    x2 = np.sort(data2)
    x3 = np.sort(data3)
    x4 = np.sort(data4)
    y1 = np.arange(len(x1))/float(len(x1))
    y2 = np.arange(len(x2))/float(len(x2))
    y3 = np.arange(len(x3))/float(len(x3))
    y4 = np.arange(len(x4))/float(len(x4))
    plt.plot(x1, y1,label=y1Label,c='red',linestyle='-.',marker="x")
    plt.plot(x2, y2,label=y2Label,c='blue',linestyle='-',marker="v")
    plt.plot(x3, y3,label=y3Label,c='black',linestyle=':',marker="D")
    plt.plot(x4, y4,label=y4Label,c='purple',linestyle='--',marker=".")
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('latency in (ms)', fontsize=12)
    plt.ylabel('CDF', fontsize=12)
    plt.title("{}".format(gameName))
    plt.yticks([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
    plt.savefig('{}/results8.png'.format(prefix))
    plt.show()
    ####################################################



    ############ Latency Components Line Graph ##############
    # from the appPerformanceStatsCompositorFile of steamVRLogResults
    appPerformanceStatsTimeStamp,appName,appProcessID,NumFramePresents,NumDroppedFrames,NumReprojected,\
        NumFramePresentsOnStartup,NumDroppedFramesOnStartup,NumReprojectedFramesOnStartup,NumLoading,NumFramePresentsLoading,\
        NumDroppedFramesLoading,NumReprojectedFramesLoading,NumTimedOut,NumFramePresentsTimedOut,NumDroppedFramesTimedOut,\
        NumReprojectedFramesTimedOut,AvgCompositorCPUTimeMS,AvgCompositorGPUTimeMS,AvgTargetFPS,AvgApplicationCPUTimeMS,\
        AvgApplicationGPUTimeMS,totalDroppedFramesOverEntireRun = appPerformanceStatsCompositorFile
    appPerformanceStatsNewTimeStamp = relativeTime(appPerformanceStatsTimeStamp)
    x = [float(i)/1000 for i in appPerformanceStatsNewTimeStamp]
    y1 = [float(i) for i in AvgCompositorCPUTimeMS]
    y1Label = 'compositor cpu'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.',marker="x")
    y2 = [float(i) for i in AvgCompositorGPUTimeMS]
    y2Label = 'compositor gpu'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='-',marker="v")
    y3 = [float(i) for i in AvgApplicationCPUTimeMS]
    y3Label = 'app cpu'
    plt.plot(x,y3,label=y3Label,c='green',linestyle='--',marker="D")
    y4 = [float(i) for i in AvgApplicationGPUTimeMS]
    y4Label = 'app gpu'
    plt.plot(x,y4,label=y4Label,c='black',linestyle=':',marker=".")
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('avg latency (ms)', fontsize=12)
    plt.savefig('{}/results9.png'.format(prefix))
    plt.show()
    ####################################################



    #################### CDF  Graph ####################
    # from the appPerformanceStatsCompositorFile of steamVRLogResults    
    data1 = [float(i) for i in AvgCompositorCPUTimeMS]
    data2 = [float(i) for i in AvgCompositorGPUTimeMS]
    data3 = [float(i) for i in AvgApplicationCPUTimeMS]
    data4 = [float(i) for i in AvgApplicationGPUTimeMS]
    x1 = np.sort(data1)
    x2 = np.sort(data2)
    x3 = np.sort(data3)
    x4 = np.sort(data4)
    y1 = np.arange(len(x1))/float(len(x1))
    y2 = np.arange(len(x2))/float(len(x2))
    y3 = np.arange(len(x3))/float(len(x3))
    y4 = np.arange(len(x4))/float(len(x4))
    plt.plot(x1, y1,label=y1Label,c='red',linestyle='-.',marker="x")
    plt.plot(x2, y2,label=y2Label,c='blue',linestyle='-',marker="v")
    plt.plot(x3, y3,label=y3Label,c='black',linestyle=':',marker="D")
    plt.plot(x4, y4,label=y4Label,c='purple',linestyle='--',marker=".")
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('latency in (ms)', fontsize=12)
    plt.ylabel('CDF', fontsize=12)
    plt.title("{}".format(gameName))
    plt.yticks([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
    plt.savefig('{}/results10.png'.format(prefix))
    plt.show()
    ####################################################



def plotFPS(root_folder,gameName,sessionLogResult,OVRMetricsResult,logcatResults):

    result_folder_name = "frame_rate"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    try:
        os.mkdir(prefix)
    except:
        pass

    stats,gStats = sessionLogResult
    gTimes,totalPipelineLatencyS,gameTimeS,serverCompositorS,encoderS,networkS,decoderS,decoderQueueS,clientCompositorS,\
                vsyncQueueS,gClientFPS,gServerFPS = gStats
    times, totalVideoPkts,videoPktsPerSecond,videoMbytesTotal,videoMbitsPerSec,totalLatencyMs,\
            networkLatencyMs,encodeLatencyMs,decodeLatencyMs,fecPercentage,fecErrorsTotal,fecErrorsPerSec,\
            clientFPS,serverFPS,batteryPercentageHMD = stats
    newGTimes = relativeTime(gTimes)
    newTimes  = relativeTime(times)



    ############# Client vs Server FPS Graph #############
    # from gStats of session_log
    x = [float(i)/1000 for i in newGTimes[5000:5050]]
    y1 = [float(i) for i in gClientFPS[5000:5050]]
    y1Label = 'ClientFPS'
    y2 = [float(i) for i in gServerFPS[5000:5050]]
    y2Label = 'ServerFPS'
    plt.plot(x,y1,label=y1Label,c='red',marker = '.',linestyle='-.')
    plt.plot(x,y2,label=y2Label,c='blue',marker = 'x',)
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('times in (sec)', fontsize=12)
    plt.ylabel('fps', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results1.png'.format(prefix))
    plt.show()
    ####################################################



    ############# Client vs Server FPS Graph #############
    # from stats of session_log
    x = [float(i)/1000 for i in newTimes]
    y1 = [i for i in clientFPS]
    y1Label = 'clientFPS'
    y2 = [i for i in serverFPS]
    y2Label = 'serverFPS'
    plt.plot(x,y1,label=y1Label,c='blue',)
    plt.plot(x,y2,label=y2Label,c='red',)
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('times in (sec)', fontsize=12)
    plt.ylabel('FPS', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results2.png'.format(prefix))
    plt.show()
    ####################################################



    #### fps (server) vs refresh rate(client) Graph ####
    # from OVRmatrics
    Time_Stamp,battery_level_percentage,battery_temperature_celcius,sensor_temperature_celcius,power_level_state,\
                average_frame_rate,display_refresh_rate,average_prediction_milliseconds,early_frame_count,stale_frame_count,\
                maximum_rotational_speed_degrees_per_second,foveation_level,eye_buffer_width,eye_buffer_height,\
                app_gpu_time_microseconds,timewarp_gpu_time_microseconds,guardian_gpu_time_microseconds,cpu_utilization_percentage,\
                gpu_utilization_percentage,stale_frames_consecutive,screen_power_consumption,vrshell_average_frame_rate,\
                vrshell_gpu_time_microseconds,vrshell_and_guardian_gpu_time_microseconds,render_scale = OVRMetricsResult
    newTimeStamp = relativeTime(Time_Stamp)
    x = [float(i)/1000 for i in newTimeStamp]
    y1 = [float(i) for i in average_frame_rate]
    y1Label = 'average frame rate'
    y2 = [float(i) for i in display_refresh_rate]
    y2Label = 'display refresh rate (target fps)'
    y3 = [float(i) for i in vrshell_average_frame_rate]
    y3Label = 'vrshell average frame rate'
    plt.plot(x,y1,label=y1Label,c='red')
    plt.plot(x,y2,label=y2Label,c='blue')
    plt.plot(x,y3,label=y3Label,c='green')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('times stamp in (sec)', fontsize=12)
    plt.ylabel('fps', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results3.png'.format(prefix))
    plt.show()
    ####################################################



    ######## targetedFPS vs. achievedFPS Graph #########
    # from logcat file
    time,targetedFPS,achievedFPS,predictionTime,tear,earlyFrames,staleFrames,fov,CPUClockLevel\
        ,GPUClockLevel,PLS,batteryTemperature, sensorTemperature,TWTime,appTime,guardianTime\
        ,CPUandGPUTime,LCnt,GPUUtilization,CPUUtilizationAverage,CPUUtilizationWorst = logcatResults
    newTime = relativeTime(time)
    x = [float(i)/1000 for i in newTime]
    y1 = [float(i) for i in targetedFPS]
    y1Label = 'targeted frame rate'
    y2 = [float(i) for i in achievedFPS]
    y2Label = 'achieved frame rate'
    plt.plot(x,y1,label=y1Label,c='red')
    plt.plot(x,y2,label=y2Label,c='blue')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('times stamp in (sec)', fontsize=12)
    plt.ylabel('fps', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results4.png'.format(prefix))
    plt.show()
    ####################################################



def plotpktsstats(root_folder,gameName,sessionLogResult):

    result_folder_name = "pkts_stats"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    try:
        os.mkdir(prefix)
    except:
        pass

    
    stats,gStats = sessionLogResult
    times, totalVideoPkts,videoPktsPerSecond,videoMbytesTotal,videoMbitsPerSec,totalLatencyMs,\
            networkLatencyMs,encodeLatencyMs,decodeLatencyMs,fecPercentage,fecErrorsTotal,fecErrorsPerSec,\
            clientFPS,serverFPS,batteryPercentageHMD = stats
    newTimes = relativeTime(times)


    ################# Total PKTS Graph #################
    x = [float(i)/1000 for i in newTimes]
    y = [float(i) for i in totalVideoPkts]
    yLabel = 'total video pkts'
    plt.plot(x,y,label=yLabel,c='red',)
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('times in (sec)', fontsize=12)
    plt.ylabel('total pkts', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results1.png'.format(prefix))
    plt.show()
    ####################################################



    ################ PKTS Per Sec Graph ################
    y = [float(i) for i in videoPktsPerSecond]
    yLabel = 'video pkts per sec'
    plt.plot(x,y,label=yLabel,c='blue',)
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('times in (sec)', fontsize=12)
    plt.ylabel('# of pkts', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results2.png'.format(prefix))
    plt.show()
    ####################################################



    ############## Video Total Size Graph ##############
    y = [float(i) for i in videoMbytesTotal]
    yLabel = 'video total size in (MB)'
    plt.plot(x,y,label=yLabel,c='green',)
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('times in (sec)', fontsize=12)
    plt.ylabel('size in (MB)', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results3.png'.format(prefix))
    plt.show()
    ####################################################



    ############### Video Bit Rate Graph ###############
    y = [float(i) for i in videoMbitsPerSec]
    yLabel = 'video bitrate in (Mbps)'
    plt.plot(x,y,label=yLabel,c='blue',)
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('times in (sec)', fontsize=12)
    plt.ylabel('bitrate (Mbps)', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results4.png'.format(prefix))
    plt.show()
    ####################################################



def plotBatteryPercentage(root_folder,gameName,sessionLogResult,OVRMetricsResult):
    
    result_folder_name = "battery_stats"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    try:
        os.mkdir(prefix)
    except:
        pass
    
    stats,gStats = sessionLogResult
    times, totalVideoPkts,videoPktsPerSecond,videoMbytesTotal,videoMbitsPerSec,totalLatencyMs,\
            networkLatencyMs,encodeLatencyMs,decodeLatencyMs,fecPercentage,fecErrorsTotal,fecErrorsPerSec,\
            clientFPS,serverFPS,batteryPercentageHMD = stats
    newTimes = relativeTime(times)

    
    ############# Battery Percentage Graph #############
    # from the session log file
    x = [float(i)/1000 for i in newTimes]
    y = [float(i) if i <= 100 else float(i)/100 for i in batteryPercentageHMD]
    yLabel = 'battery percentage'
    plt.plot(x,y,label=yLabel,c='blue',)
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('times in (sec)', fontsize=12)
    plt.ylabel('battery percentage', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results1.png'.format(prefix))
    plt.show()
    ####################################################



    ############# Battery Percentage Graph #############
    # from the OVRmatrics file
    Time_Stamp,battery_level_percentage,battery_temperature_celcius,sensor_temperature_celcius,power_level_state,\
            average_frame_rate,display_refresh_rate,average_prediction_milliseconds,early_frame_count,stale_frame_count,\
            maximum_rotational_speed_degrees_per_second,foveation_level,eye_buffer_width,eye_buffer_height,\
            app_gpu_time_microseconds,timewarp_gpu_time_microseconds,guardian_gpu_time_microseconds,cpu_utilization_percentage,\
            gpu_utilization_percentage,stale_frames_consecutive,screen_power_consumption,vrshell_average_frame_rate,\
            vrshell_gpu_time_microseconds,vrshell_and_guardian_gpu_time_microseconds,render_scale = OVRMetricsResult
    newTimeStamp = relativeTime(Time_Stamp)
    x = [float(i)/1000 for i in newTimeStamp]
    y = [float(i) for i in battery_level_percentage]
    yLabel = 'battery level percentage'
    plt.plot(x,y,label=yLabel,c='blue')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('times stamp in (sec)', fontsize=12)
    plt.ylabel('battery percentage', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results2.png'.format(prefix))
    plt.show()
    ####################################################



def plotTemperature(root_folder,gameName,OVRMetricsResult,logcatResults):
    
    result_folder_name = "temperature_stats"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    try:
        os.mkdir(prefix)
    except:
        pass

    ############ Temperature Celcius Graph #############
    # from the OVRmatrics file
    Time_Stamp,battery_level_percentage,battery_temperature_celcius,sensor_temperature_celcius,power_level_state,\
            average_frame_rate,display_refresh_rate,average_prediction_milliseconds,early_frame_count,stale_frame_count,\
            maximum_rotational_speed_degrees_per_second,foveation_level,eye_buffer_width,eye_buffer_height,\
            app_gpu_time_microseconds,timewarp_gpu_time_microseconds,guardian_gpu_time_microseconds,cpu_utilization_percentage,\
            gpu_utilization_percentage,stale_frames_consecutive,screen_power_consumption,vrshell_average_frame_rate,\
            vrshell_gpu_time_microseconds,vrshell_and_guardian_gpu_time_microseconds,render_scale = OVRMetricsResult
    newTimeStamp = relativeTime(Time_Stamp)
    x = [float(i)/1000 for i in newTimeStamp]
    y1 = [float(i) for i in battery_temperature_celcius]
    y1Label = 'battery'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.')
    y2 = [float(i) for i in sensor_temperature_celcius]
    y2Label = 'sensor'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='--')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('temperature in celsius', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results1.png'.format(prefix))
    plt.show()
    ####################################################



    ############ Temperature Celcius Graph #############
    # from the logcat file
    time,targetedFPS,achievedFPS,predictionTime,tear,earlyFrames,staleFrames,fov,CPUClockLevel\
        ,GPUClockLevel,PLS,batteryTemperature, sensorTemperature,TWTime,appTime,guardianTime\
        ,CPUandGPUTime,LCnt,GPUUtilization,CPUUtilizationAverage,CPUUtilizationWorst = logcatResults
    newTime = relativeTime(time)
    x = [float(i)/1000 for i in newTime]
    y1 = [float(i) for i in batteryTemperature]
    y1Label = 'battery'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.')
    y2 = [float(i) for i in sensorTemperature]
    y2Label = 'sensor'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='--')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('temperature in celsius', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results2.png'.format(prefix))
    plt.show()
    ####################################################



def plotFramesStats(root_folder,gameName,OVRMetricsResult,logcatResults,steamVRLogResults):

    result_folder_name = "frames_stats"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    try:
        os.mkdir(prefix)
    except:
        pass

    Time_Stamp,battery_level_percentage,battery_temperature_celcius,sensor_temperature_celcius,power_level_state,\
        average_frame_rate,display_refresh_rate,average_prediction_milliseconds,early_frame_count,stale_frame_count,\
        maximum_rotational_speed_degrees_per_second,foveation_level,eye_buffer_width,eye_buffer_height,\
        app_gpu_time_microseconds,timewarp_gpu_time_microseconds,guardian_gpu_time_microseconds,cpu_utilization_percentage,\
        gpu_utilization_percentage,stale_frames_consecutive,screen_power_consumption,vrshell_average_frame_rate,\
        vrshell_gpu_time_microseconds,vrshell_and_guardian_gpu_time_microseconds,render_scale = OVRMetricsResult
    newTimeStamp = relativeTime(Time_Stamp) 


    ################ Frames Stats Graph ################
    # from the OVRmatrics file
    Time_Stamp,battery_level_percentage,battery_temperature_celcius,sensor_temperature_celcius,power_level_state,\
            average_frame_rate,display_refresh_rate,average_prediction_milliseconds,early_frame_count,stale_frame_count,\
            maximum_rotational_speed_degrees_per_second,foveation_level,eye_buffer_width,eye_buffer_height,\
            app_gpu_time_microseconds,timewarp_gpu_time_microseconds,guardian_gpu_time_microseconds,cpu_utilization_percentage,\
            gpu_utilization_percentage,stale_frames_consecutive,screen_power_consumption,vrshell_average_frame_rate,\
            vrshell_gpu_time_microseconds,vrshell_and_guardian_gpu_time_microseconds,render_scale = OVRMetricsResult
    newTimeStamp = relativeTime(Time_Stamp)
    x = [float(i)/1000 for i in newTimeStamp]
    y1 = [float(i) for i in early_frame_count]
    y1Label = 'early frames'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.')
    y2 = [float(i) for i in stale_frame_count]
    y2Label = 'stale frames'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='-')
    y3 = [float(i) for i in stale_frames_consecutive]
    y3Label = 'stale frames consecutive'
    plt.plot(x,y3,label=y3Label,c='black',linestyle=':')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('# of frames', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results1.png'.format(prefix))
    plt.show()
    ####################################################



    ################ Frames Stats Graph ################
    # from the logcat file
    time,targetedFPS,achievedFPS,predictionTime,tear,earlyFrames,staleFrames,fov,CPUClockLevel\
        ,GPUClockLevel,PLS,batteryTemperature, sensorTemperature,TWTime,appTime,guardianTime\
        ,CPUandGPUTime,LCnt,GPUUtilization,CPUUtilizationAverage,CPUUtilizationWorst = logcatResults
    newTime = relativeTime(time)
    x = [float(i)/1000 for i in newTime]
    y1 = [float(i) for i in earlyFrames]
    y1Label = 'early frames'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.')
    y2 = [float(i) for i in staleFrames]
    y2Label = 'stale frames'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='-')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('# of frames', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results2.png'.format(prefix))
    plt.show()
    ####################################################



    ##### Frames Stats During Normal Running Graph #####
    # from the appPerformanceStatsMonitorFile of steamVRLogResults
    appPerformanceStatsMonitorFile,appPerformanceStatsCompositorFile = steamVRLogResults
    appPerformanceStatsTimeStamp,appID,NumFramePresents,NumDroppedFrames,NumReprojected,\
        NumFramePresentsOnStartup,NumDroppedFramesOnStartup,NumReprojectedFramesOnStartup,\
        NumLoading,NumFramePresentsLoading,NumDroppedFramesLoading,NumReprojectedFramesLoading,\
        NumTimedOut,NumFramePresentsTimedOut,NumDroppedFramesTimedOut,NumReprojectedFramesTimedOut,\
        AvgSubmitsPerFrame,AvgCompositorCPUTimeMS,AvgCompositorGPUTimeMS,AvgTargetFPS,\
        AvgApplicationCPUTimeMS,AvgApplicationGPUTimeMS,AppSeconds,AppHeadsetActiveSeconds,\
        NumSingleDroppedFramesOverEntireRun,Num2DroppedFramesOverEntireRun,Num3DroppedFramesOverEntireRun,\
        Num4MoreDroppedFramesOverEntireRun,totalNumOfFramesEntireRun,totalNumOfExpectedFrameEntireRun = appPerformanceStatsMonitorFile
    appPerformanceStatsNewTimeStamp = relativeTime(appPerformanceStatsTimeStamp)
    x = [float(i)/1000 for i in appPerformanceStatsNewTimeStamp]
    y1 = [float(i) for i in NumFramePresents]
    y1Label = 'presented frames'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.',marker="x")
    y2 = [float(i) for i in NumDroppedFrames]
    y2Label = 'dropped frames'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='-',marker="v")
    y3 = [float(i) for i in NumReprojected]
    y3Label = 'reprojected frames'
    plt.plot(x,y3,label=y3Label,c='green',linestyle=':',marker=".")
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('# of frames', fontsize=12)
    plt.title("frames stats of {} during game running".format(gameName),fontsize=12)
    plt.savefig('{}/results3.png'.format(prefix))
    plt.show()
    ####################################################



    ##### Frames Stats During the App Startup Graph #####
    # from the appPerformanceStatsMonitorFile of steamVRLogResults
    x = [float(i)/1000 for i in appPerformanceStatsNewTimeStamp]
    y1 = [float(i) for i in NumFramePresentsOnStartup]
    y1Label = 'presented frames'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.',marker="x")
    y2 = [float(i) for i in NumDroppedFramesOnStartup]
    y2Label = 'dropped frames'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='-',marker="v")
    y3 = [float(i) for i in NumReprojectedFramesOnStartup]
    y3Label = 'reprojected frames'
    plt.plot(x,y3,label=y3Label,c='green',linestyle=':',marker=".")
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('# of frames', fontsize=12)
    plt.title("frames stats of {} during game startup".format(gameName),fontsize=12)
    plt.savefig('{}/results4.png'.format(prefix))
    plt.show()
    ####################################################



    ##### Frames Stats During the App Loading Graph #####
    # from the appPerformanceStatsMonitorFile of steamVRLogResults
    x = [float(i)/1000 for i in appPerformanceStatsNewTimeStamp]
    y0 = [float(i) for i in NumLoading]
    y0Label = '# of loadings'
    plt.plot(x,y0,label=y0Label,c='black',linestyle='--',marker="D")    
    y1 = [float(i) for i in NumFramePresentsLoading]
    y1Label = 'presented frames'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.',marker="x")
    y2 = [float(i) for i in NumDroppedFramesLoading]
    y2Label = 'dropped frames'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='-',marker="v")
    y3 = [float(i) for i in NumReprojectedFramesLoading]
    y3Label = 'reprojected frames'
    plt.plot(x,y3,label=y3Label,c='green',linestyle=':',marker=".")
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('# of frames', fontsize=12)
    plt.title("frames stats of {} during game loading".format(gameName),fontsize=12)
    plt.savefig('{}/results5.png'.format(prefix))
    plt.show()
    ####################################################



    ##### Frames Stats During the App timeouts Graph #####
    # from the appPerformanceStatsMonitorFile of steamVRLogResults
    x = [float(i)/1000 for i in appPerformanceStatsNewTimeStamp]
    y0 = [float(i) for i in NumTimedOut]
    y0Label = '# of timeouts'
    plt.plot(x,y0,label=y0Label,c='black',linestyle='--',marker="D")    
    y1 = [float(i) for i in NumFramePresentsTimedOut]
    y1Label = 'presented frames'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.',marker="x")
    y2 = [float(i) for i in NumDroppedFramesTimedOut]
    y2Label = 'dropped frames'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='-',marker="v")
    y3 = [float(i) for i in NumReprojectedFramesTimedOut]
    y3Label = 'reprojected frames'
    plt.plot(x,y3,label=y3Label,c='green',linestyle=':',marker=".")
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('# of frames', fontsize=12)
    plt.title("frames stats of {} during game timeouts".format(gameName),fontsize=12)
    plt.savefig('{}/results6.png'.format(prefix))
    plt.show()
    ####################################################



    ##### Frames Stats During the Entire Run Graph #####
    # Dropped frames
    # from the appPerformanceStatsMonitorFile of steamVRLogResults
    x = [float(i)/1000 for i in appPerformanceStatsNewTimeStamp]
    y0 = [float(i) for i in NumSingleDroppedFramesOverEntireRun]
    y0Label = 'single frames'
    plt.plot(x,y0,label=y0Label,c='black',linestyle='--',marker="D")    
    y1 = [float(i) for i in Num2DroppedFramesOverEntireRun]
    y1Label = '2 frames'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.',marker="x")
    y2 = [float(i) for i in Num3DroppedFramesOverEntireRun]
    y2Label = '3 frames'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='-',marker="v")
    y3 = [float(i) for i in Num4MoreDroppedFramesOverEntireRun]
    y3Label = '> 4 frames'
    plt.plot(x,y3,label=y3Label,c='green',linestyle=':',marker=".")
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('# of dropped frames', fontsize=12)
    plt.title("dropped frames stats of {}".format(gameName),fontsize=12)
    plt.savefig('{}/results7.png'.format(prefix))
    plt.show()
    ####################################################



    ##### Frames Stats During the Entire Run Graph #####
    # Delivered vs. Expected
    # from the appPerformanceStatsMonitorFile of steamVRLogResults
    x = [float(i)/1000 for i in appPerformanceStatsNewTimeStamp]
    y0 = [float(i) for i in totalNumOfFramesEntireRun]
    y0Label = 'Delivered'
    plt.plot(x,y0,label=y0Label,c='black',linestyle='--',marker="D")    
    y1 = [float(i) for i in totalNumOfExpectedFrameEntireRun]
    y1Label = 'Expected'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.',marker="x")
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('# of frames', fontsize=12)
    plt.title("Expected vs. Delivered # of frames of {}".format(gameName),fontsize=12)
    plt.savefig('{}/results8.png'.format(prefix))
    plt.show()
    ####################################################



    ##### Frames Stats During the Entire Run Graph #####
    # average submit of a frame (based on re-submission)
    # from the appPerformanceStatsMonitorFile of steamVRLogResults
    x = [float(i)/1000 for i in appPerformanceStatsNewTimeStamp]
    y0 = [float(i) for i in AvgSubmitsPerFrame]
    y0Label = 'frame re-submitting'
    plt.plot(x,y0,label=y0Label,c='black',linestyle='--',marker="D")    
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('avg # of frame submitting', fontsize=12)
    plt.title("frames re-submitting of {}".format(gameName),fontsize=12)
    plt.savefig('{}/results9.png'.format(prefix))
    plt.show()
    ####################################################



   ##### Frames Stats During Normal Running Graph #####
    # from the appPerformanceStatsCompositorFile of steamVRLogResults
    appPerformanceStatsTimeStamp,appName,appProcessID,NumFramePresents,NumDroppedFrames,NumReprojected,\
        NumFramePresentsOnStartup,NumDroppedFramesOnStartup,NumReprojectedFramesOnStartup,NumLoading,NumFramePresentsLoading,\
        NumDroppedFramesLoading,NumReprojectedFramesLoading,NumTimedOut,NumFramePresentsTimedOut,NumDroppedFramesTimedOut,\
        NumReprojectedFramesTimedOut,AvgCompositorCPUTimeMS,AvgCompositorGPUTimeMS,AvgTargetFPS,AvgApplicationCPUTimeMS,\
        AvgApplicationGPUTimeMS,totalDroppedFramesOverEntireRun = appPerformanceStatsCompositorFile
    appPerformanceStatsNewTimeStamp = relativeTime(appPerformanceStatsTimeStamp)

    x = [float(i)/1000 for i in appPerformanceStatsNewTimeStamp]
    y1 = [float(i) for i in NumFramePresents]
    y1Label = 'presented frames'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.',marker="x")
    y2 = [float(i) for i in NumDroppedFrames]
    y2Label = 'dropped frames'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='-',marker="v")
    y3 = [float(i) for i in NumReprojected]
    y3Label = 'reprojected frames'
    plt.plot(x,y3,label=y3Label,c='green',linestyle=':',marker=".")
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('# of frames', fontsize=12)
    plt.title("frames stats of {} during game running".format(gameName),fontsize=12)
    plt.savefig('{}/results10.png'.format(prefix))
    plt.show()
    ####################################################



    ##### Frames Stats During the App Startup Graph #####
    # from the appPerformanceStatsCompositorFile of steamVRLogResults
    x = [float(i)/1000 for i in appPerformanceStatsNewTimeStamp]
    y1 = [float(i) for i in NumFramePresentsOnStartup]
    y1Label = 'presented frames'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.',marker="x")
    y2 = [float(i) for i in NumDroppedFramesOnStartup]
    y2Label = 'dropped frames'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='-',marker="v")
    y3 = [float(i) for i in NumReprojectedFramesOnStartup]
    y3Label = 'reprojected frames'
    plt.plot(x,y3,label=y3Label,c='green',linestyle=':',marker=".")
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('# of frames', fontsize=12)
    plt.title("frames stats of {} during game startup".format(gameName),fontsize=12)
    plt.savefig('{}/results11.png'.format(prefix))
    plt.show()
    ####################################################



    ##### Frames Stats During the App Loading Graph #####
    # from the appPerformanceStatsCompositorFile of steamVRLogResults
    x = [float(i)/1000 for i in appPerformanceStatsNewTimeStamp]
    y0 = [float(i) for i in NumLoading]
    y0Label = '# of loadings'
    plt.plot(x,y0,label=y0Label,c='black',linestyle='--',marker="D")    
    y1 = [float(i) for i in NumFramePresentsLoading]
    y1Label = 'presented frames'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.',marker="x")
    y2 = [float(i) for i in NumDroppedFramesLoading]
    y2Label = 'dropped frames'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='-',marker="v")
    y3 = [float(i) for i in NumReprojectedFramesLoading]
    y3Label = 'reprojected frames'
    plt.plot(x,y3,label=y3Label,c='green',linestyle=':',marker=".")
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('# of frames', fontsize=12)
    plt.title("frames stats of {} during game loading".format(gameName),fontsize=12)
    plt.savefig('{}/results12.png'.format(prefix))
    plt.show()
    ####################################################



    ##### Frames Stats During the App timeouts Graph #####
    # from the appPerformanceStatsCompositorFile of steamVRLogResults
    x = [float(i)/1000 for i in appPerformanceStatsNewTimeStamp]
    y0 = [float(i) for i in NumTimedOut]
    y0Label = '# of timeouts'
    plt.plot(x,y0,label=y0Label,c='black',linestyle='--',marker="D")    
    y1 = [float(i) for i in NumFramePresentsTimedOut]
    y1Label = 'presented frames'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.',marker="x")
    y2 = [float(i) for i in NumDroppedFramesTimedOut]
    y2Label = 'dropped frames'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='-',marker="v")
    y3 = [float(i) for i in NumReprojectedFramesTimedOut]
    y3Label = 'reprojected frames'
    plt.plot(x,y3,label=y3Label,c='green',linestyle=':',marker=".")
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('# of frames', fontsize=12)
    plt.title("frames stats of {} during game timeouts".format(gameName),fontsize=12)
    plt.savefig('{}/results13.png'.format(prefix))
    plt.show()
    ####################################################



    ##### Frames Stats During the Entire Run Graph #####
    # Delivered vs. Expected
    # from the appPerformanceStatsCompositorFile of steamVRLogResults
    x = [float(i)/1000 for i in appPerformanceStatsNewTimeStamp]
    y0 = [float(i) for i in totalDroppedFramesOverEntireRun]
    y0Label = 'dropped'
    plt.plot(x,y0,label=y0Label,c='black',linestyle='--',marker="D")    
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('# of dropped frames', fontsize=12)
    plt.title("# of dropped frames of {} over the entire run".format(gameName),fontsize=12)
    plt.savefig('{}/results14.png'.format(prefix))
    plt.show()
    ####################################################



def plotUtilization(root_folder,gameName,OVRMetricsResult,logcatResults):

    result_folder_name = "GPU_CPU_utilization"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    try:
        os.mkdir(prefix)
    except:
        pass

    Time_Stamp,battery_level_percentage,battery_temperature_celcius,sensor_temperature_celcius,power_level_state,\
        average_frame_rate,display_refresh_rate,average_prediction_milliseconds,early_frame_count,stale_frame_count,\
        maximum_rotational_speed_degrees_per_second,foveation_level,eye_buffer_width,eye_buffer_height,\
        app_gpu_time_microseconds,timewarp_gpu_time_microseconds,guardian_gpu_time_microseconds,cpu_utilization_percentage,\
        gpu_utilization_percentage,stale_frames_consecutive,screen_power_consumption,vrshell_average_frame_rate,\
        vrshell_gpu_time_microseconds,vrshell_and_guardian_gpu_time_microseconds,render_scale = OVRMetricsResult
    newTimeStamp = relativeTime(Time_Stamp) 


    ############ CPU/GPU Utilization Graph #############
    # from the OVRmatrics file
    Time_Stamp,battery_level_percentage,battery_temperature_celcius,sensor_temperature_celcius,power_level_state,\
            average_frame_rate,display_refresh_rate,average_prediction_milliseconds,early_frame_count,stale_frame_count,\
            maximum_rotational_speed_degrees_per_second,foveation_level,eye_buffer_width,eye_buffer_height,\
            app_gpu_time_microseconds,timewarp_gpu_time_microseconds,guardian_gpu_time_microseconds,cpu_utilization_percentage,\
            gpu_utilization_percentage,stale_frames_consecutive,screen_power_consumption,vrshell_average_frame_rate,\
            vrshell_gpu_time_microseconds,vrshell_and_guardian_gpu_time_microseconds,render_scale = OVRMetricsResult
    newTimeStamp = relativeTime(Time_Stamp)
    x = [float(i)/1000 for i in newTimeStamp]
    y1 = [float(i) for i in cpu_utilization_percentage]
    y1Label = 'cpu utilization percentage'
    plt.plot(x,y1,label=y1Label,c='blue')
    y2 = [float(i) for i in gpu_utilization_percentage]
    y2Label = 'gpu utilization percentage'
    plt.plot(x,y2,label=y2Label,c='black',linestyle=':')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('utilization percentage', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results1.png'.format(prefix))
    plt.show()
    ####################################################



    ############ CPU/GPU Utilization Graph #############
    # from the logcat file
    time,targetedFPS,achievedFPS,predictionTime,tear,earlyFrames,staleFrames,fov,CPUClockLevel\
        ,GPUClockLevel,PLS,batteryTemperature, sensorTemperature,TWTime,appTime,guardianTime\
        ,CPUandGPUTime,LCnt,GPUUtilization,CPUUtilizationAverage,CPUUtilizationWorst = logcatResults
    newTime = relativeTime(time)
    x = [float(i)/1000 for i in newTime]
    y1 = [float(i) for i in CPUUtilizationAverage]
    y1Label = 'avg cpu utilization percentage'
    plt.plot(x,y1,label=y1Label,c='blue')
    y2 = [float(i) for i in CPUUtilizationWorst]
    y2Label = 'worst cpu utilization percentage'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='-.')
    y3 = [float(i) for i in GPUUtilization]
    y3Label = 'gpu utilization percentage'
    plt.plot(x,y3,label=y3Label,c='black',linestyle=':')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('utilization percentage', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results2.png'.format(prefix))
    plt.show()
    ####################################################



    ############ CPU/GPU Clock Level Graph #############
    # from the logcat file
    time,targetedFPS,achievedFPS,predictionTime,tear,earlyFrames,staleFrames,fov,CPUClockLevel\
        ,GPUClockLevel,PLS,batteryTemperature, sensorTemperature,TWTime,appTime,guardianTime\
        ,CPUandGPUTime,LCnt,GPUUtilization,CPUUtilizationAverage,CPUUtilizationWorst = logcatResults
    newTime = relativeTime(time)
    x = [float(i)/1000 for i in newTime]
    y1 = [float(i) for i in CPUClockLevel]
    y1Label = 'cpu'
    plt.plot(x,y1,label=y1Label,c='blue')
    y2 = [float(i) for i in GPUClockLevel]
    y2Label = 'gpu'
    plt.plot(x,y2,label=y2Label,c='black',linestyle=':')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('clock level [1-4]', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results3.png'.format(prefix))
    plt.show()
    ####################################################



def plotMaxRotationalSpeed(root_folder,gameName,OVRMetricsResult):
    result_folder_name = "rotational_speed"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    try:
        os.mkdir(prefix)
    except:
        pass

    Time_Stamp,battery_level_percentage,battery_temperature_celcius,sensor_temperature_celcius,power_level_state,\
        average_frame_rate,display_refresh_rate,average_prediction_milliseconds,early_frame_count,stale_frame_count,\
        maximum_rotational_speed_degrees_per_second,foveation_level,eye_buffer_width,eye_buffer_height,\
        app_gpu_time_microseconds,timewarp_gpu_time_microseconds,guardian_gpu_time_microseconds,cpu_utilization_percentage,\
        gpu_utilization_percentage,stale_frames_consecutive,screen_power_consumption,vrshell_average_frame_rate,\
        vrshell_gpu_time_microseconds,vrshell_and_guardian_gpu_time_microseconds,render_scale = OVRMetricsResult
    newTimeStamp = relativeTime(Time_Stamp) 

    
    ############## Rotational Speed Graph ##############
    # from the OVRmatrics file
    Time_Stamp,battery_level_percentage,battery_temperature_celcius,sensor_temperature_celcius,power_level_state,\
            average_frame_rate,display_refresh_rate,average_prediction_milliseconds,early_frame_count,stale_frame_count,\
            maximum_rotational_speed_degrees_per_second,foveation_level,eye_buffer_width,eye_buffer_height,\
            app_gpu_time_microseconds,timewarp_gpu_time_microseconds,guardian_gpu_time_microseconds,cpu_utilization_percentage,\
            gpu_utilization_percentage,stale_frames_consecutive,screen_power_consumption,vrshell_average_frame_rate,\
            vrshell_gpu_time_microseconds,vrshell_and_guardian_gpu_time_microseconds,render_scale = OVRMetricsResult
    newTimeStamp = relativeTime(Time_Stamp)
    x = [float(i)/1000 for i in newTimeStamp]
    y1 = [float(i) for i in maximum_rotational_speed_degrees_per_second]
    y1Label = 'cpu utilization percentage'
    plt.plot(x,y1,label=y1Label,c='blue')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('maximum rotational speed (degrees/sec)', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results1.png'.format(prefix))
    plt.show()
    ####################################################



def plotFoveationLevel(root_folder,gameName,OVRMetricsResult,logcatResults):
    result_folder_name = "foveational_level"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    try:
        os.mkdir(prefix)
    except:
        pass

    Time_Stamp,battery_level_percentage,battery_temperature_celcius,sensor_temperature_celcius,power_level_state,\
        average_frame_rate,display_refresh_rate,average_prediction_milliseconds,early_frame_count,stale_frame_count,\
        maximum_rotational_speed_degrees_per_second,foveation_level,eye_buffer_width,eye_buffer_height,\
        app_gpu_time_microseconds,timewarp_gpu_time_microseconds,guardian_gpu_time_microseconds,cpu_utilization_percentage,\
        gpu_utilization_percentage,stale_frames_consecutive,screen_power_consumption,vrshell_average_frame_rate,\
        vrshell_gpu_time_microseconds,vrshell_and_guardian_gpu_time_microseconds,render_scale = OVRMetricsResult
    newTimeStamp = relativeTime(Time_Stamp) 

    
    ############## Foveation Level Graph ###############
    # from the OVRmatrics file
    Time_Stamp,battery_level_percentage,battery_temperature_celcius,sensor_temperature_celcius,power_level_state,\
            average_frame_rate,display_refresh_rate,average_prediction_milliseconds,early_frame_count,stale_frame_count,\
            maximum_rotational_speed_degrees_per_second,foveation_level,eye_buffer_width,eye_buffer_height,\
            app_gpu_time_microseconds,timewarp_gpu_time_microseconds,guardian_gpu_time_microseconds,cpu_utilization_percentage,\
            gpu_utilization_percentage,stale_frames_consecutive,screen_power_consumption,vrshell_average_frame_rate,\
            vrshell_gpu_time_microseconds,vrshell_and_guardian_gpu_time_microseconds,render_scale = OVRMetricsResult
    newTimeStamp = relativeTime(Time_Stamp)
    x = [float(i)/1000 for i in newTimeStamp]
    y1 = [float(i) for i in foveation_level]
    y1Label = 'foveation level'
    plt.plot(x,y1,label=y1Label,c='blue')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('foveation level [0-4]', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results1.png'.format(prefix))
    plt.show()
    ####################################################



    ############## Foveation Level Graph ###############
    # from the logcat file
    time,targetedFPS,achievedFPS,predictionTime,tear,earlyFrames,staleFrames,fov,CPUClockLevel\
        ,GPUClockLevel,PLS,batteryTemperature, sensorTemperature,TWTime,appTime,guardianTime\
        ,CPUandGPUTime,LCnt,GPUUtilization,CPUUtilizationAverage,CPUUtilizationWorst = logcatResults
    newTime = relativeTime(time)
    x = [float(i)/1000 for i in newTime]
    y1 = [float(i) for i in fov]
    y1Label = 'foveation level'
    plt.plot(x,y1,label=y1Label,c='blue')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('foveation level [0-4]', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results2.png'.format(prefix))
    plt.show()
    ####################################################



def plotNumberOfTears(root_folder,gameName,logcatResults):
    
    result_folder_name = "tears"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    try:
        os.mkdir(prefix)
    except:
        pass

    ############# Tear counts Line Graph ###############
    # nb of tears from the logcat file
    time,targetedFPS,achievedFPS,predictionTime,tear,earlyFrames,staleFrames,fov,CPUClockLevel\
        ,GPUClockLevel,PLS,batteryTemperature, sensorTemperature,TWTime,appTime,guardianTime\
        ,CPUandGPUTime,LCnt,GPUUtilization,CPUUtilizationAverage,CPUUtilizationWorst = logcatResults
    newTime = relativeTime(time)
    x = [float(i)/1000 for i in newTime]
    y1 = [float(i) for i in tear]
    y1Label = 'tears'
    plt.plot(x,y1,label=y1Label,c='blue')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('# of tears', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results1.png'.format(prefix))
    plt.show()
    #################################################### 



def plotPowerLevel(root_folder,gameName,logcatResults):
    result_folder_name = "power_level"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    try:
        os.mkdir(prefix)
    except:
        pass

    ############# Power Level Line Graph ###############
    # PLS from the logcat file
    time,targetedFPS,achievedFPS,predictionTime,tear,earlyFrames,staleFrames,fov,CPUClockLevel\
        ,GPUClockLevel,PLS,batteryTemperature, sensorTemperature,TWTime,appTime,guardianTime\
        ,CPUandGPUTime,LCnt,GPUUtilization,CPUUtilizationAverage,CPUUtilizationWorst = logcatResults
    newTime = relativeTime(time)
    x = [float(i)/1000 for i in newTime]
    y1 = [float(i) for i in PLS]
    y1Label = 'power level'
    plt.plot(x,y1,label=y1Label,c='blue')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('power level [0=Normal,1=Save,2=Danger]', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results1.png'.format(prefix))
    plt.show()
    #################################################### 



def plotLayersCount(root_folder,gameName,logcatResults):
    result_folder_name = "layers_count"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    try:
        os.mkdir(prefix)
    except:
        pass

    ############# Layers Count Line Graph ###############
    # LCnt from the logcat file
    time,targetedFPS,achievedFPS,predictionTime,tear,earlyFrames,staleFrames,fov,CPUClockLevel\
        ,GPUClockLevel,PLS,batteryTemperature, sensorTemperature,TWTime,appTime,guardianTime\
        ,CPUandGPUTime,LCnt,GPUUtilization,CPUUtilizationAverage,CPUUtilizationWorst = logcatResults
    newTime = relativeTime(time)
    x = [float(i)/1000 for i in newTime]
    y1 = [float(i) for i in LCnt]
    y1Label = 'LCnt'
    plt.plot(x,y1,label=y1Label,c='blue')
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('# of layers', fontsize=12)
    plt.title("{}".format(gameName))
    plt.savefig('{}/results1.png'.format(prefix))
    plt.show()
    #################################################### 



def plotRunningTime(root_folder,gameName,steamVRLogResults):
    result_folder_name = "running_time"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    try:
        os.mkdir(prefix)
    except:
        pass
    


    ############### Running Time Graph #################
    # from the appPerformanceStatsMonitorFile of steamVRLogResults
    appPerformanceStatsMonitorFile,appPerformanceStatsCompositorFile = steamVRLogResults
    appPerformanceStatsTimeStamp,appID,NumFramePresents,NumDroppedFrames,NumReprojected,\
        NumFramePresentsOnStartup,NumDroppedFramesOnStartup,NumReprojectedFramesOnStartup,\
        NumLoading,NumFramePresentsLoading,NumDroppedFramesLoading,NumReprojectedFramesLoading,\
        NumTimedOut,NumFramePresentsTimedOut,NumDroppedFramesTimedOut,NumReprojectedFramesTimedOut,\
        AvgSubmitsPerFrame,AvgCompositorCPUTimeMS,AvgCompositorGPUTimeMS,AvgTargetFPS,\
        AvgApplicationCPUTimeMS,AvgApplicationGPUTimeMS,AppSeconds,AppHeadsetActiveSeconds,\
        NumSingleDroppedFramesOverEntireRun,Num2DroppedFramesOverEntireRun,Num3DroppedFramesOverEntireRun,\
        Num4MoreDroppedFramesOverEntireRun,totalNumOfFramesEntireRun,totalNumOfExpectedFrameEntireRun = appPerformanceStatsMonitorFile
    appPerformanceStatsNewTimeStamp = relativeTime(appPerformanceStatsTimeStamp)
    x = [float(i)/1000 for i in appPerformanceStatsNewTimeStamp]
    y1 = [float(i) for i in AppSeconds]
    y1Label = 'app time'
    plt.plot(x,y1,label=y1Label,c='blue',linestyle='-.',marker="x")
    y2 = [float(i) for i in AppHeadsetActiveSeconds]
    y2Label = 'app HMD active time'
    plt.plot(x,y2,label=y2Label,c='red',linestyle='-',marker="v")
    plt.legend(loc='best', fontsize=10)
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    plt.xlabel('timestamp in (sec)', fontsize=12)
    plt.ylabel('time in seconds', fontsize=12)
    plt.savefig('{}/results1.png'.format(prefix))
    plt.show()
    ####################################################



def relativeTime(arrayOfTimes=[]):
    if(len(arrayOfTimes)<1):
        return[]
    else:
        return [float(x)-float(arrayOfTimes[0]) for x in arrayOfTimes]



def convertgameName(gameName):
    words = []
    temp = gameName.split("_")
    for j in range(len(temp)):
        if j == len(temp)-1:
            tempX = temp[j].split("-")[0].capitalize()
        else:
            tempX = temp[j].capitalize()
        words.append(tempX)
    return ' '.join(words)



def getGameStats(gameName,appName):
    gameStatsIndices = []
    for i in range(len(appName)):
        if appName[i] == gameName:
            gameStatsIndices.append(i)
    return gameStatsIndices



def getElementsAtIndices(listOfElemets,listOfIndices):
    result = []
    for index in listOfIndices:
        result.append(listOfElemets[index])
    return result