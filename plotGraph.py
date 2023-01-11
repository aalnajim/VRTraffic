import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
import math


root_folder = "plots"
saved_graph_resolution = 300

def plotLogsResults(results):

    try:
        os.mkdir("{}".format(root_folder))
    except:
        pass

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
    
    try:
        os.mkdir("{}".format(root_folder))
    except:
        pass

    for resultItem in serverTracesResults:
        gameName,results = resultItem
        try:
            os.mkdir("{}/{}".format(root_folder,gameName))
        except:
            pass
        try:
            os.mkdir("{}/{}/{}".format(root_folder,gameName,"server"))
        except:
            pass
        plotServerNBofFrames(root_folder,gameName,results)
        plotServerFramesInstantaneousRates(root_folder,gameName,results)
        plotServerDataInstantaneousRates(root_folder,gameName,results)
        plotServerSizeofFrames(root_folder,gameName,results)
        plotServerSizeofData(root_folder,gameName,results)
        plotServerAVGSizeofFrames(root_folder,gameName,results)
        plotServerAVGSizeofData(root_folder,gameName,results)



def plotHMDTracesResults(HMDTracesResults):
    try:
        os.mkdir("{}".format(root_folder))
    except:
        pass

    for resultItem in HMDTracesResults:
        gameName,results = resultItem
        try:
            os.mkdir("{}/{}".format(root_folder,gameName))
        except:
            pass
        try:
            os.mkdir("{}/{}/{}".format(root_folder,gameName,"HMD"))
        except:
            pass

        # HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates,\
        # HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes, HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times,\
        # HMD_DWN_MANAGEMENT_FRAMES_DataRates, HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes, HMD_UP_DATA1_FRAMES_NBs, \
        # HMD_UP_DATA1_FRAMES_Times, HMD_UP_DATA1_FRAMES_DataRates, HMD_UP_DATA1_FRAMES_Frames_Sizes,\
        # HMD_UP_DATA1_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA1_FRAMES_NBs, HMD_UP_RE_DATA1_FRAMES_Times, \
        # HMD_UP_RE_DATA1_FRAMES_DataRates, HMD_UP_RE_DATA1_FRAMES_Frames_Sizes, HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB,\
        # HMD_UP_DATA2_FRAMES_NBs, HMD_UP_DATA2_FRAMES_Times, HMD_UP_DATA2_FRAMES_DataRates, HMD_UP_DATA2_FRAMES_Data_Sizes,\
        # HMD_UP_DATA2_FRAMES_Frames_Sizes, HMD_UP_DATA2_FRAMES_Frames_SeqNB, HMD_DWN_DATA2_FRAMES_NBs, HMD_DWN_DATA2_FRAMES_Times, \
        # HMD_DWN_DATA2_FRAMES_DataRates, HMD_DWN_DATA2_FRAMES_Data_Sizes, HMD_DWN_DATA2_FRAMES_Frames_Sizes, \
        # HMD_DWN_DATA2_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA2_FRAMES_NBs, HMD_UP_RE_DATA2_FRAMES_Times, HMD_UP_RE_DATA2_FRAMES_DataRates,\
        # HMD_UP_RE_DATA2_FRAMES_Data_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB, \
        # HMD_DWN_RE_DATA2_FRAMES_NBs, HMD_DWN_RE_DATA2_FRAMES_Times, HMD_DWN_RE_DATA2_FRAMES_DataRates, HMD_DWN_RE_DATA2_FRAMES_Data_Sizes,\
        # HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB, HMD_UP_DATA3_FRAMES_NBs, HMD_UP_DATA3_FRAMES_Times, \
        # HMD_UP_DATA3_FRAMES_DataRates, HMD_UP_DATA3_FRAMES_Data_Sizes, HMD_UP_DATA3_FRAMES_Frames_Sizes, HMD_UP_DATA3_FRAMES_Frames_SeqNB,\
        # HMD_DWN_DATA3_FRAMES_NBs, HMD_DWN_DATA3_FRAMES_Times, HMD_DWN_DATA3_FRAMES_DataRates, HMD_DWN_DATA3_FRAMES_Data_Sizes,\
        # HMD_DWN_DATA3_FRAMES_Frames_Sizes, HMD_DWN_DATA3_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA3_FRAMES_NBs, HMD_UP_RE_DATA3_FRAMES_Times, \
        # HMD_UP_RE_DATA3_FRAMES_DataRates, HMD_UP_RE_DATA3_FRAMES_Data_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_Sizes, \
        # HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB, HMD_DWN_RE_DATA3_FRAMES_NBs, HMD_DWN_RE_DATA3_FRAMES_Times, HMD_DWN_RE_DATA3_FRAMES_DataRates, \
        # HMD_DWN_RE_DATA3_FRAMES_Data_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB = results 

        # newResults = eliminateRetransmittedFrames(results)
        # uniqueDataCombinedLists,retransmittedDataCombinedLists = combinedResultsLists(newResults)
        # HMD_UP_NBs,HMD_UPـTimes,HMD_UP_DataRates,HMD_UP_Data_Sizes,HMD_UP_Frames_Sizes,HMD_UP_Frames_SeqNB,HMD_DWN_NBs,HMD_DWNـTimes,\
        #     HMD_DWN_DataRates,HMD_DWN_Data_Sizes,HMD_DWN_Frames_Sizes,HMD_DWN_Frames_SeqNB = uniqueDataCombinedLists
        # HMD_UP_RE_NBs,HMD_UP_RE_Times,HMD_UP_RE_DataRates,HMD_UP_RE_Data_Sizes,HMD_UP_RE_Frames_Sizes,HMD_UP_RE_Frames_SeqNB,HMD_DWN_RE_NBs,HMD_DWN_RE_Times,\
        #     HMD_DWN_RE_DataRates,HMD_DWN_RE_Data_Sizes,HMD_DWN_RE_Frames_Sizes,HMD_DWN_RE_Frames_SeqNB = retransmittedDataCombinedLists
        # #print(computeOverallSucessRateSize(HMD_UP_Data_Sizes,HMD_UP_RE_Data_Sizes))
        # listOfResultsNB    = computePeriodicSucessRateNB(HMD_UPـTimes,HMD_UP_RE_Times,duration=1)
        # listOfResultsSizes = computePeriodicSucessRateSize(HMD_UPـTimes,HMD_UP_Data_Sizes,HMD_UP_RE_Times,HMD_UP_RE_Data_Sizes,duration=1)
        # for index in range(len(listOfResultsNB)):
        #     print("{}  -  {}".format(listOfResultsNB[index],listOfResultsSizes[index]))


        
        # plotHMDNBofFrames(root_folder,gameName,results)
        # plotHMDFramesInstantaneousRates(root_folder,gameName,results)
        # plotHMDDataInstantaneousRates(root_folder,gameName,results)
        # plotHMDSizeofFrames(root_folder,gameName,results)
        # plotHMDSizeofData(root_folder,gameName,results)
        # plotHMDAVGSizeofFrames(root_folder,gameName,results)
        # plotHMDAVGSizeofData(root_folder,gameName,results)
        # plotHMDSucessRateNB(root_folder,gameName,results)
        plotHMDSucessRateFrameSize(root_folder,gameName,results)
        # plotHMDSucessRateDataSize(root_folder,gameName,results)


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
    plt.savefig('{}/results1.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results2.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results3.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results4.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results5.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results6.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results7.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results8.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results9.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results10.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results1.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results2.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results3.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results4.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results1.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results2.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results3.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results4.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results1.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results2.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results1.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results2.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results1.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results2.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results3.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results4.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results5.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results6.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results7.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results8.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results9.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results10.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results11.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results12.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results13.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results14.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results1.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results2.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results3.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results1.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results1.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results2.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results1.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results1.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results1.png'.format(prefix),dpi=saved_graph_resolution)
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
    plt.savefig('{}/results1.png'.format(prefix),dpi=saved_graph_resolution)
    plt.show()
    ####################################################



def plotServerNBofFrames(root_folder,gameName,results):
    result_folder_name = "server/NB_of_frames"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    
    try:
        os.mkdir(prefix)
    except:
        pass


    server_UP_BOTH_NBs,server_UP_BOTH_Times,server_UP_BOTH_Data_Sizes,server_UP_BOTH_Frames_Sizes,server_UP_TCP_NBs,\
        server_UP_TCP_Times,server_UP_TCP_Data_Sizes,server_UP_TCP_Frames_Sizes,server_UP_UDP_NBs,server_UP_UDP_Times,\
        server_UP_UDP_Data_Sizes,server_UP_UDP_Frames_Sizes,server_DWN_BOTH_NBs,server_DWN_BOTH_Times,server_DWN_BOTH_Data_Sizes,\
        server_DWN_BOTH_Frames_Sizes,server_DWN_TCP_NBs,server_DWN_TCP_Times,server_DWN_TCP_Data_Sizes,server_DWN_TCP_Frames_Sizes,\
        server_DWN_UDP_NBs,server_DWN_UDP_Times,server_DWN_UDP_Data_Sizes,server_DWN_UDP_Frames_Sizes = results     

    #################### Line Graph ####################
    # line graph for nb of frames for different time durations from server.csv trace
    durations = [1,10,15,30,60]  # in seconds
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(server_UP_BOTH_Times,server_UP_UDP_Times,server_UP_TCP_Times),
                            (server_DWN_BOTH_Times,server_DWN_UDP_Times,server_DWN_TCP_Times)]
    
    
    for duration in durations:
        for i in range(len(flowDirections)):
            newTimesBoth = relativeTime(flowDirectionsLists[i].__getitem__(0))
            newTimesPeriodsBoth = convertTimeToPeriods(newTimesBoth,duration)
            listOfNBOfFramesBoth = computeNBOfFrames(newTimesBoth,duration)
            newTimesUDP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1))
            newTimesPeriodsUDP = convertTimeToPeriods(newTimesUDP,duration)
            listOfNBOfFramesUDP = computeNBOfFrames(newTimesUDP,duration)
            newTimesTCP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(2))
            newTimesPeriodsTCP = convertTimeToPeriods(newTimesTCP,duration)
            listOfNBOfFramesTCP = computeNBOfFrames(newTimesTCP,duration)
            x1 = newTimesPeriodsBoth
            y1 = listOfNBOfFramesBoth
            y1Label = 'Both'
            x2 = newTimesPeriodsUDP
            y2 = listOfNBOfFramesUDP
            y2Label = 'UDP'
            x3 = newTimesPeriodsTCP
            y3 = listOfNBOfFramesTCP
            y3Label = 'TCP'      
            plt.plot(x1,y1,label=y1Label,c='red',marker = '.',linestyle='-')
            plt.plot(x2,y2,label=y2Label,c='blue',marker = '.',linestyle='-')
            plt.plot(x3,y3,label=y3Label,c='green',marker = '.',linestyle='-')
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('# of frames', fontsize=12)
            plt.title("{} # of frames of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_NBFrames.png'.format(prefix,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ####################################################



    #################### CDF  Graph ####################
    # CDF Graph for nb of frames for different time durations from server.csv trace
    for duration in durations:
        for i in range(len(flowDirections)):    
            newTimesBoth = relativeTime(flowDirectionsLists[i].__getitem__(0))
            newTimesPeriodsBoth = convertTimeToPeriods(newTimesBoth,duration)
            listOfNBOfFramesBoth = computeNBOfFrames(newTimesBoth,duration)
            newTimesUDP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1))
            newTimesPeriodsUDP = convertTimeToPeriods(newTimesUDP,duration)
            listOfNBOfFramesUDP = computeNBOfFrames(newTimesUDP,duration)
            newTimesTCP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(2))
            newTimesPeriodsTCP = convertTimeToPeriods(newTimesTCP,duration)
            listOfNBOfFramesTCP = computeNBOfFrames(newTimesTCP,duration)
            
            data1 = [float(i) for i in listOfNBOfFramesBoth]
            data2 = [float(i) for i in listOfNBOfFramesUDP]
            data3 = [float(i) for i in listOfNBOfFramesTCP]
            
            x1 = np.sort(data1)
            x2 = np.sort(data2)
            x3 = np.sort(data3)

            y1 = np.arange(len(x1))/float(len(x1))
            y2 = np.arange(len(x2))/float(len(x2))
            y3 = np.arange(len(x3))/float(len(x3))

            y1Label =  'Both'
            y2Label =  'UDP'
            y3Label =  'TCP'

            plt.plot(x1, y1,label=y1Label,c='red',linestyle='-.')
            plt.plot(x2, y2,label=y2Label,c='blue',linestyle=':')
            plt.plot(x3, y3,label=y3Label,c='green',linestyle='--')

            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('# of frames', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF {} # of frames of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=9)
            plt.savefig('{}/{}_duration_{}_NBFrames_CDF.png'.format(prefix,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ####################################################



def plotHMDNBofFrames(root_folder,gameName,results):
    result_folder_name = "HMD/NB_of_frames"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    
    try:
        os.mkdir(prefix)
    except:
        pass


    HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates,\
        HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes, HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times,\
        HMD_DWN_MANAGEMENT_FRAMES_DataRates, HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes, HMD_UP_DATA1_FRAMES_NBs, \
        HMD_UP_DATA1_FRAMES_Times, HMD_UP_DATA1_FRAMES_DataRates, HMD_UP_DATA1_FRAMES_Frames_Sizes,\
        HMD_UP_DATA1_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA1_FRAMES_NBs, HMD_UP_RE_DATA1_FRAMES_Times, \
        HMD_UP_RE_DATA1_FRAMES_DataRates, HMD_UP_RE_DATA1_FRAMES_Frames_Sizes, HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB,\
        HMD_UP_DATA2_FRAMES_NBs, HMD_UP_DATA2_FRAMES_Times, HMD_UP_DATA2_FRAMES_DataRates, HMD_UP_DATA2_FRAMES_Data_Sizes,\
        HMD_UP_DATA2_FRAMES_Frames_Sizes, HMD_UP_DATA2_FRAMES_Frames_SeqNB, HMD_DWN_DATA2_FRAMES_NBs, HMD_DWN_DATA2_FRAMES_Times, \
        HMD_DWN_DATA2_FRAMES_DataRates, HMD_DWN_DATA2_FRAMES_Data_Sizes, HMD_DWN_DATA2_FRAMES_Frames_Sizes, \
        HMD_DWN_DATA2_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA2_FRAMES_NBs, HMD_UP_RE_DATA2_FRAMES_Times, HMD_UP_RE_DATA2_FRAMES_DataRates,\
        HMD_UP_RE_DATA2_FRAMES_Data_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB, \
        HMD_DWN_RE_DATA2_FRAMES_NBs, HMD_DWN_RE_DATA2_FRAMES_Times, HMD_DWN_RE_DATA2_FRAMES_DataRates, HMD_DWN_RE_DATA2_FRAMES_Data_Sizes,\
        HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB, HMD_UP_DATA3_FRAMES_NBs, HMD_UP_DATA3_FRAMES_Times, \
        HMD_UP_DATA3_FRAMES_DataRates, HMD_UP_DATA3_FRAMES_Data_Sizes, HMD_UP_DATA3_FRAMES_Frames_Sizes, HMD_UP_DATA3_FRAMES_Frames_SeqNB,\
        HMD_DWN_DATA3_FRAMES_NBs, HMD_DWN_DATA3_FRAMES_Times, HMD_DWN_DATA3_FRAMES_DataRates, HMD_DWN_DATA3_FRAMES_Data_Sizes,\
        HMD_DWN_DATA3_FRAMES_Frames_Sizes, HMD_DWN_DATA3_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA3_FRAMES_NBs, HMD_UP_RE_DATA3_FRAMES_Times, \
        HMD_UP_RE_DATA3_FRAMES_DataRates, HMD_UP_RE_DATA3_FRAMES_Data_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_Sizes, \
        HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB, HMD_DWN_RE_DATA3_FRAMES_NBs, HMD_DWN_RE_DATA3_FRAMES_Times, HMD_DWN_RE_DATA3_FRAMES_DataRates, \
        HMD_DWN_RE_DATA3_FRAMES_Data_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB = results   

    durations = [1,10,15,30,60]  # in seconds
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(HMD_UP_MANAGEMENT_FRAMES_Times,HMD_UP_DATA1_FRAMES_Times,HMD_UP_RE_DATA1_FRAMES_Times,HMD_UP_DATA2_FRAMES_Times,HMD_UP_RE_DATA2_FRAMES_Times,HMD_UP_DATA3_FRAMES_Times,HMD_UP_RE_DATA3_FRAMES_Times),
                            (HMD_DWN_MANAGEMENT_FRAMES_Times,[],[],HMD_DWN_DATA2_FRAMES_Times,HMD_DWN_RE_DATA2_FRAMES_Times,HMD_DWN_DATA3_FRAMES_Times,HMD_DWN_RE_DATA3_FRAMES_Times)]
    colors = ["red","blue","green","black","purple","cyan","pink"]
    lineStyles = ['-.',':',"--","-",'-.',':',"--"]
    markers = [".",",","1","x","|","+","v"]
    labels = ["management","data type1","retransmitted data type1","data type2","retransmitted data type2","data type3","retransmitted data type3"]




    #################### Line Graph 1 ####################    
    # Line Graph for nb of frames for different time durations from HMD traces folder (each direction will be in a graph)
    for duration in durations:
        for i in range(len(flowDirections)):
            folderPath = "{}/{}".format(prefix,flowDirections[i])
            try:
                os.mkdir(folderPath)
            except:
                pass
            firstFrame = min(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1)[0] if i==0 else 100000000,flowDirectionsLists[i].__getitem__(2)[0] if i == 0 else 100000000,flowDirectionsLists[i].__getitem__(3)[0],
                            flowDirectionsLists[i].__getitem__(4)[0],flowDirectionsLists[i].__getitem__(5)[0],flowDirectionsLists[i].__getitem__(6)[0])
            for j in range(len(flowDirectionsLists[i])):
                if(i == 1 and j in [1,2]):
                    continue
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfNBOfFrames = computeNBOfFrames(newTimes,duration)
                x = newTimesPeriods
                y = listOfNBOfFrames
                yLabel = '{}'.format(labels[j]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[j]),marker = '.',linestyle='-')
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('# of frames', fontsize=12)
            plt.title("{} # of frames of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_NBFrames.png'.format(folderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################


    #################### Line Graph 2 ####################    
    # Line Graph for nb of frames for different time durations from HMD traces folder (each data type will be in a graph)
    for duration in durations:
        for j in range(len(labels)):
            firstFrame = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0]) if j not in [1,2] else flowDirectionsLists[0].__getitem__(j)[0]
            for i in range(len(flowDirections)):
                if(i == 1 and j in [1,2]):
                        continue
                folderPath = "{}/{}".format(prefix,labels[j])
                try:
                    os.mkdir(folderPath)
                except:
                    pass
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfNBOfFrames = computeNBOfFrames(newTimes,duration)
                x = newTimesPeriods
                y = listOfNBOfFrames
                yLabel = '{}'.format(flowDirections[i]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[i]),marker = '.',linestyle='-')
                
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('# of frames', fontsize=12)
            plt.title("# of {} frames of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_NBFrames.png'.format(folderPath,labels[j],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### Line Graph 3 ####################
    # Line Graph for nb of frames for all the frames from all data types for different time durations from HMD traces folder
    folderPath = "{}/{}".format(prefix,"all_data_types")
    try:
        os.mkdir(folderPath)
    except:
        pass
    try:
        listOfFolders = ["DMR","DR","DM","D","R"]
        for tempFolder in listOfFolders:
            os.mkdir("{}/{}".format(folderPath,tempFolder))
    except:
        pass
    for duration in durations: 
        # [D+M+R] all data frames + all management frames + all re-transmitted frames (lists suffix 1) 
        uniqueDataCombinedLists_1,retransmittedDataCombinedLists_1 = combinedResultsLists(results,1)
        HMD_UP_NBs_1,HMD_UP_Times_1,HMD_UP_DataRates_1,HMD_UP_Data_Sizes_1,HMD_UP_Frames_Sizes_1,HMD_UP_Frames_SeqNB_1,HMD_DWN_NBs_1,HMD_DWN_Times_1,HMD_DWN_DataRates_1,HMD_DWN_Data_Sizes_1,HMD_DWN_Frames_Sizes_1,HMD_DWN_Frames_SeqNB_1 = uniqueDataCombinedLists_1
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_1[0],HMD_UP_Times_1)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeNBOfFrames(newTimesX1,duration)
        x1 = newTimesPeriodsX1
        y1 = listOfRatesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_1[0],HMD_DWN_Times_1)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeNBOfFrames(newTimesX2,duration)
        x2 = newTimesPeriodsX2
        y2 = listOfRatesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('# of frames', fontsize=12)
        plt.title("# of DMR frames of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DMR/{}_NBFrames.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D+R] all data frames + all re-transmitted frames (lists suffix 2) 
        uniqueDataCombinedLists_2,retransmittedDataCombinedLists_2 = combinedResultsLists(results,0)
        HMD_UP_NBs_2,HMD_UP_Times_2,HMD_UP_DataRates_2,HMD_UP_Data_Sizes_2,HMD_UP_Frames_Sizes_2,HMD_UP_Frames_SeqNB_2,HMD_DWN_NBs_2,HMD_DWN_Times_2,HMD_DWN_DataRates_2,HMD_DWN_Data_Sizes_2,HMD_DWN_Frames_Sizes_2,HMD_DWN_Frames_SeqNB_2 = uniqueDataCombinedLists_2
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_2[0],HMD_UP_Times_2)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeNBOfFrames(newTimesX1,duration)
        x1 = newTimesPeriodsX1
        y1 = listOfRatesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_2[0],HMD_DWN_Times_2)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeNBOfFrames(newTimesX2,duration)
        x2 = newTimesPeriodsX2
        y2 = listOfRatesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('# of frames', fontsize=12)
        plt.title("# of DR frames of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DR/{}_NBFrames.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D+M] all data frames + all management frames (lists suffix 3) 
        uniqueDataCombinedLists_3,retransmittedDataCombinedLists_3 = combinedResultsListsNoReTransmittedFrames(results,1)
        HMD_UP_NBs_3,HMD_UP_Times_3,HMD_UP_DataRates_3,HMD_UP_Data_Sizes_3,HMD_UP_Frames_Sizes_3,HMD_UP_Frames_SeqNB_3,HMD_DWN_NBs_3,HMD_DWN_Times_3,HMD_DWN_DataRates_3,HMD_DWN_Data_Sizes_3,HMD_DWN_Frames_Sizes_3,HMD_DWN_Frames_SeqNB_3 = uniqueDataCombinedLists_3
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_3[0],HMD_UP_Times_3)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeNBOfFrames(newTimesX1,duration)
        x1 = newTimesPeriodsX1
        y1 = listOfRatesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_3[0],HMD_DWN_Times_3)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeNBOfFrames(newTimesX2,duration)
        x2 = newTimesPeriodsX2
        y2 = listOfRatesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('# of frames', fontsize=12)
        plt.title("# of DM frames instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DM/{}_NBFrames.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D] all data frames (lists suffix 4) 
        uniqueDataCombinedLists_4,retransmittedDataCombinedLists_4 = combinedResultsListsNoReTransmittedFrames(results,0)
        HMD_UP_NBs_3,HMD_UP_Times_4,HMD_UP_DataRates_4,HMD_UP_Data_Sizes_4,HMD_UP_Frames_Sizes_4,HMD_UP_Frames_SeqNB_4,HMD_DWN_NBs_4,HMD_DWN_Times_4,HMD_DWN_DataRates_4,HMD_DWN_Data_Sizes_4,HMD_DWN_Frames_Sizes_4,HMD_DWN_Frames_SeqNB_4 = uniqueDataCombinedLists_4
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_4[0],HMD_UP_Times_4)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeNBOfFrames(newTimesX1,duration)
        x1 = newTimesPeriodsX1
        y1 = listOfRatesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_4[0],HMD_DWN_Times_4)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeNBOfFrames(newTimesX2,duration)
        x2 = newTimesPeriodsX2
        y2 = listOfRatesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('# of frames', fontsize=12)
        plt.title("# of D frames instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/D/{}_NBFrames.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [R] all re-transmitted frames (lists suffix 5)
        HMD_UP_RE_NBs_5,HMD_UP_RE_Times_5,HMD_UP_RE_DataRates_5,HMD_UP_RE_Data_Sizes_5,HMD_UP_RE_Frames_Sizes_5,HMD_UP_RE_Frames_SeqNB_5,HMD_DWN_RE_NBs_5,HMD_DWN_RE_Times_5,HMD_DWN_RE_DataRates_5,HMD_DWN_RE_Data_Sizes_5,HMD_DWN_RE_Frames_Sizes_5,HMD_DWN_RE_Frames_SeqNB_5 = retransmittedDataCombinedLists_1
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_RE_Times_5[0],HMD_UP_RE_Times_5)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeNBOfFrames(newTimesX1,duration)
        x1 = newTimesPeriodsX1
        y1 = listOfRatesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_RE_Times_5[0],HMD_DWN_RE_Times_5)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeNBOfFrames(newTimesX2,duration)
        x2 = newTimesPeriodsX2
        y2 = listOfRatesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('# of frames', fontsize=12)
        plt.title("# of R frames instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/R/{}_NBFrames.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()
        ######################################################



    #################### CDF  Graph 1 ####################
    # CDF Graph for nb of frames for different time durations from HMD traces folder (each direction will be in a graph)
    for duration in durations:
        for i in range(len(flowDirections)):
            folderPath = "{}/{}".format(prefix,flowDirections[i])
            try:
                os.mkdir(folderPath)
            except:
                pass
            firstFrame = min(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1)[0] if i==0 else 100000000,flowDirectionsLists[i].__getitem__(2)[0] if i == 0 else 100000000,flowDirectionsLists[i].__getitem__(3)[0],
                            flowDirectionsLists[i].__getitem__(4)[0],flowDirectionsLists[i].__getitem__(5)[0],flowDirectionsLists[i].__getitem__(6)[0])
            for j in range(len(flowDirectionsLists[i])):
                if(i == 1 and j in [1,2]):
                    continue
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfNBOfFrames = computeNBOfFrames(newTimes,duration)
                data = [float(value) for value in listOfNBOfFrames]
                x = np.sort(data)
                y = np.arange(len(x))/float(len(x))
                yLabel = '{}'.format(labels[j]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[j]),linestyle='{}'.format(lineStyles[j]))               
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('# of frames', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF {} # of frames of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=9)
            plt.savefig('{}/{}_duration_{}_NBFrames_CDF.png'.format(folderPath,flowDirections[i],duration),dpi= saved_graph_resolution)
            plt.show()
    ######################################################



    #################### CDF  Graph 2 ####################
    # CDF Graph for nb of frames for different time durations from HMD traces folder (each type of frame will be in a graph)
    for duration in durations:
        for j in range(len(labels)):
            firstFrame = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0]) if j not in [1,2] else flowDirectionsLists[0].__getitem__(j)[0]
            for i in range(len(flowDirections)):
                if(i == 1 and j in [1,2]):
                        continue
                folderPath = "{}/{}".format(prefix,labels[j])
                try:
                    os.mkdir(folderPath)
                except:
                    pass
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfNBOfFrames = computeNBOfFrames(newTimes,duration)
                data = [float(value) for value in listOfNBOfFrames]
                x = np.sort(data)
                y = np.arange(len(x))/float(len(x))
                yLabel = '{}'.format(flowDirections[i]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[i]),linestyle='{}'.format(lineStyles[i]))               
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('# of frames', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF # of {} frames of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=9)
            plt.savefig('{}/{}_frames_duration_{}_NBFrames_CDF.png'.format(folderPath,labels[j],duration),dpi= saved_graph_resolution)
            plt.show()
    ######################################################



    #################### CDF  Graph 3 ####################
    # CDF Graph for nb og frames for all the frames from all data types for different time durations from HMD traces folder
    folderPath = "{}/{}".format(prefix,"all_data_types")
    try:
        os.mkdir(folderPath)
    except:
        pass
    try:
        listOfFolders = ["DMR","DR","DM","D","R"]
        for tempFolder in listOfFolders:
            os.mkdir("{}/{}".format(folderPath,tempFolder))
    except:
        pass
    for duration in durations: 
        # [D+M+R] all data frames + all management frames + all re-transmitted frames (lists suffix 1) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_1[0],HMD_UP_Times_1)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeNBOfFrames(newTimesX1,duration)
        data1 = [float(value) for value in listOfRatesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_1[0],HMD_DWN_Times_1)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeNBOfFrames(newTimesX2,duration)
        data2 = [float(value) for value in listOfRatesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('# of frames', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of NB of DMR frames of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DMR/{}_NBFrames_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D+R] all data frames + all re-transmitted frames (lists suffix 2) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_2[0],HMD_UP_Times_2)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeNBOfFrames(newTimesX1,duration)
        data1 = [float(value) for value in listOfRatesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_2[0],HMD_DWN_Times_2)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeNBOfFrames(newTimesX2,duration)
        data2 = [float(value) for value in listOfRatesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('# of frames', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of NB of DR frames of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DR/{}_NBFrames_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D+M] all data frames + all management frames (lists suffix 3) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_3[0],HMD_UP_Times_3)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeNBOfFrames(newTimesX1,duration)
        data1 = [float(value) for value in listOfRatesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_3[0],HMD_DWN_Times_3)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeNBOfFrames(newTimesX2,duration)
        data2 = [float(value) for value in listOfRatesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('# of frames', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of NB of DM frames of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DM/{}_NBFrames_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D] all data frames (lists suffix 4) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_4[0],HMD_UP_Times_4)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeNBOfFrames(newTimesX1,duration)
        data1 = [float(value) for value in listOfRatesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_4[0],HMD_DWN_Times_4)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeNBOfFrames(newTimesX2,duration)
        data2 = [float(value) for value in listOfRatesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('# of frames', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of NB of D frames of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/D/{}_NBFrames_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [R] all re-transmitted frames (lists suffix 5)
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_RE_Times_5[0],HMD_UP_RE_Times_5)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeNBOfFrames(newTimesX1,duration)
        data1 = [float(value) for value in listOfRatesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_RE_Times_5[0],HMD_DWN_RE_Times_5)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeNBOfFrames(newTimesX2,duration)
        data2 = [float(value) for value in listOfRatesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('# of frames', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of NB of R frames of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/R/{}_NBFrames_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()
        ######################################################



def plotServerFramesInstantaneousRates(root_folder,gameName,results):
    result_folder_name = "server/frames_instantaneous_rates"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    
    try:
        os.mkdir(prefix)
    except:
        pass


    server_UP_BOTH_NBs,server_UP_BOTH_Times,server_UP_BOTH_Data_Sizes,server_UP_BOTH_Frames_Sizes,server_UP_TCP_NBs,\
        server_UP_TCP_Times,server_UP_TCP_Data_Sizes,server_UP_TCP_Frames_Sizes,server_UP_UDP_NBs,server_UP_UDP_Times,\
        server_UP_UDP_Data_Sizes,server_UP_UDP_Frames_Sizes,server_DWN_BOTH_NBs,server_DWN_BOTH_Times,server_DWN_BOTH_Data_Sizes,\
        server_DWN_BOTH_Frames_Sizes,server_DWN_TCP_NBs,server_DWN_TCP_Times,server_DWN_TCP_Data_Sizes,server_DWN_TCP_Frames_Sizes,\
        server_DWN_UDP_NBs,server_DWN_UDP_Times,server_DWN_UDP_Data_Sizes,server_DWN_UDP_Frames_Sizes = results     

    #################### Line Graph ####################
    # line graph for instantaneous rates for different time durations from server.csv trace
    durations = [1,10,15,30,60]  # in seconds
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(server_UP_BOTH_Times,server_UP_UDP_Times,server_UP_TCP_Times),
                            (server_DWN_BOTH_Times,server_DWN_UDP_Times,server_DWN_TCP_Times)]
    listOfFrameSizes = [(server_UP_BOTH_Frames_Sizes,server_UP_UDP_Frames_Sizes,server_UP_TCP_Frames_Sizes),
                        (server_DWN_BOTH_Frames_Sizes,server_DWN_UDP_Frames_Sizes,server_DWN_TCP_Frames_Sizes)]
    
    
    for duration in durations:
        for i in range(len(flowDirections)):
            newTimesBoth = relativeTime(flowDirectionsLists[i].__getitem__(0))
            newTimesPeriodsBoth = convertTimeToPeriods(newTimesBoth,duration)
            listOfRatesOfFramesBoth = computeInstantaneousRates(newTimesBoth,listOfFrameSizes[i].__getitem__(0),duration)
            newTimesUDP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1))
            newTimesPeriodsUDP = convertTimeToPeriods(newTimesUDP,duration)
            listOfRatesOfFramesUDP = computeInstantaneousRates(newTimesUDP,listOfFrameSizes[i].__getitem__(1),duration)
            newTimesTCP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(2))
            newTimesPeriodsTCP = convertTimeToPeriods(newTimesTCP,duration)
            listOfRatesOfFramesTCP = computeInstantaneousRates(newTimesTCP,listOfFrameSizes[i].__getitem__(2),duration)
            x1 = newTimesPeriodsBoth
            y1 = listOfRatesOfFramesBoth
            y1Label = 'Both'
            x2 = newTimesPeriodsUDP
            y2 = listOfRatesOfFramesUDP
            y2Label = 'UDP'
            x3 = newTimesPeriodsTCP
            y3 = listOfRatesOfFramesTCP
            y3Label = 'TCP'      
            plt.plot(x1,y1,label=y1Label,c='red',marker = '.',linestyle='-')
            plt.plot(x2,y2,label=y2Label,c='blue',marker = '.',linestyle='-')
            plt.plot(x3,y3,label=y3Label,c='green',marker = '.',linestyle='-')
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('instantaneous rate (Mbps)', fontsize=12)
            plt.title("{} instantaneous rates of frames of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_instantaneous_rates.png'.format(prefix,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ####################################################



    #################### CDF  Graph ####################
    # CDF Graph for instantaneous rates for different time durations from server.csv trace
    for duration in durations:
        for i in range(len(flowDirections)):    
            newTimesBoth = relativeTime(flowDirectionsLists[i].__getitem__(0))
            newTimesPeriodsBoth = convertTimeToPeriods(newTimesBoth,duration)
            listOfRatesOfFramesBoth = computeInstantaneousRates(newTimesBoth,listOfFrameSizes[i].__getitem__(0),duration)
            newTimesUDP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1))
            newTimesPeriodsUDP = convertTimeToPeriods(newTimesUDP,duration)
            listOfRatesOfFramesUDP = computeInstantaneousRates(newTimesUDP,listOfFrameSizes[i].__getitem__(1),duration)
            newTimesTCP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(2))
            newTimesPeriodsTCP = convertTimeToPeriods(newTimesTCP,duration)
            listOfRatesOfFramesTCP = computeInstantaneousRates(newTimesTCP,listOfFrameSizes[i].__getitem__(2),duration)
            
            data1 = [float(i) for i in listOfRatesOfFramesBoth]
            data2 = [float(i) for i in listOfRatesOfFramesUDP]
            data3 = [float(i) for i in listOfRatesOfFramesTCP]
            
            x1 = np.sort(data1)
            x2 = np.sort(data2)
            x3 = np.sort(data3)

            y1 = np.arange(len(x1))/float(len(x1))
            y2 = np.arange(len(x2))/float(len(x2))
            y3 = np.arange(len(x3))/float(len(x3))

            y1Label =  'Both'
            y2Label =  'UDP'
            y3Label =  'TCP'

            plt.plot(x1, y1,label=y1Label,c='red',linestyle='-.')
            plt.plot(x2, y2,label=y2Label,c='blue',linestyle=':')
            plt.plot(x3, y3,label=y3Label,c='green',linestyle='--')

            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('instantaneous rates (Mbps)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF {} instantaneous rates of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=9)
            plt.savefig('{}/{}_duration_{}_instantaneous_rates_CDF.png'.format(prefix,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ####################################################



def plotHMDFramesInstantaneousRates(root_folder,gameName,results):
    result_folder_name = "HMD/frames_instantaneous_rates"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    
    try:
        os.mkdir(prefix)
    except:
        pass

    HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates,\
        HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes, HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times,\
        HMD_DWN_MANAGEMENT_FRAMES_DataRates, HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes, HMD_UP_DATA1_FRAMES_NBs, \
        HMD_UP_DATA1_FRAMES_Times, HMD_UP_DATA1_FRAMES_DataRates, HMD_UP_DATA1_FRAMES_Frames_Sizes,\
        HMD_UP_DATA1_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA1_FRAMES_NBs, HMD_UP_RE_DATA1_FRAMES_Times, \
        HMD_UP_RE_DATA1_FRAMES_DataRates, HMD_UP_RE_DATA1_FRAMES_Frames_Sizes, HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB,\
        HMD_UP_DATA2_FRAMES_NBs, HMD_UP_DATA2_FRAMES_Times, HMD_UP_DATA2_FRAMES_DataRates, HMD_UP_DATA2_FRAMES_Data_Sizes,\
        HMD_UP_DATA2_FRAMES_Frames_Sizes, HMD_UP_DATA2_FRAMES_Frames_SeqNB, HMD_DWN_DATA2_FRAMES_NBs, HMD_DWN_DATA2_FRAMES_Times, \
        HMD_DWN_DATA2_FRAMES_DataRates, HMD_DWN_DATA2_FRAMES_Data_Sizes, HMD_DWN_DATA2_FRAMES_Frames_Sizes, \
        HMD_DWN_DATA2_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA2_FRAMES_NBs, HMD_UP_RE_DATA2_FRAMES_Times, HMD_UP_RE_DATA2_FRAMES_DataRates,\
        HMD_UP_RE_DATA2_FRAMES_Data_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB, \
        HMD_DWN_RE_DATA2_FRAMES_NBs, HMD_DWN_RE_DATA2_FRAMES_Times, HMD_DWN_RE_DATA2_FRAMES_DataRates, HMD_DWN_RE_DATA2_FRAMES_Data_Sizes,\
        HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB, HMD_UP_DATA3_FRAMES_NBs, HMD_UP_DATA3_FRAMES_Times, \
        HMD_UP_DATA3_FRAMES_DataRates, HMD_UP_DATA3_FRAMES_Data_Sizes, HMD_UP_DATA3_FRAMES_Frames_Sizes, HMD_UP_DATA3_FRAMES_Frames_SeqNB,\
        HMD_DWN_DATA3_FRAMES_NBs, HMD_DWN_DATA3_FRAMES_Times, HMD_DWN_DATA3_FRAMES_DataRates, HMD_DWN_DATA3_FRAMES_Data_Sizes,\
        HMD_DWN_DATA3_FRAMES_Frames_Sizes, HMD_DWN_DATA3_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA3_FRAMES_NBs, HMD_UP_RE_DATA3_FRAMES_Times, \
        HMD_UP_RE_DATA3_FRAMES_DataRates, HMD_UP_RE_DATA3_FRAMES_Data_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_Sizes, \
        HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB, HMD_DWN_RE_DATA3_FRAMES_NBs, HMD_DWN_RE_DATA3_FRAMES_Times, HMD_DWN_RE_DATA3_FRAMES_DataRates, \
        HMD_DWN_RE_DATA3_FRAMES_Data_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB = results 
    

    durations = [1,10,15,30,60]  # in seconds
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(HMD_UP_MANAGEMENT_FRAMES_Times,HMD_UP_DATA1_FRAMES_Times,HMD_UP_RE_DATA1_FRAMES_Times,HMD_UP_DATA2_FRAMES_Times,HMD_UP_RE_DATA2_FRAMES_Times,HMD_UP_DATA3_FRAMES_Times,HMD_UP_RE_DATA3_FRAMES_Times),
                            (HMD_DWN_MANAGEMENT_FRAMES_Times,[],[],HMD_DWN_DATA2_FRAMES_Times,HMD_DWN_RE_DATA2_FRAMES_Times,HMD_DWN_DATA3_FRAMES_Times,HMD_DWN_RE_DATA3_FRAMES_Times)]
    listOfFrameSizes = [(HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes,HMD_UP_DATA1_FRAMES_Frames_Sizes,HMD_UP_RE_DATA1_FRAMES_Frames_Sizes,HMD_UP_DATA2_FRAMES_Frames_Sizes,HMD_UP_RE_DATA2_FRAMES_Frames_Sizes,HMD_UP_DATA3_FRAMES_Frames_Sizes,HMD_UP_RE_DATA3_FRAMES_Frames_Sizes),
                        (HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes,[],[],HMD_DWN_DATA2_FRAMES_Frames_Sizes,HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes,HMD_DWN_DATA3_FRAMES_Frames_Sizes,HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes)]
    colors = ["red","blue","green","black","purple","cyan","pink"]
    lineStyles = ['-.',':',"--","-",'-.',':',"--"]
    markers = [".",",","1","x","|","+","v"]
    labels = ["management","data type1","retransmitted data type1","data type2","retransmitted data type2","data type3","retransmitted data type3"]


    #################### Line Graph 1 ####################
    # Line Graph for instantaneous rates for different time durations from HMD traces folder (each direction will be in a graph)
    for duration in durations:
        for i in range(len(flowDirections)):
            folderPath = "{}/{}".format(prefix,flowDirections[i])
            try:
                os.mkdir(folderPath)
            except:
                pass
            firstFrame = min(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1)[0] if i==0 else 100000000,flowDirectionsLists[i].__getitem__(2)[0] if i == 0 else 100000000,flowDirectionsLists[i].__getitem__(3)[0],
                            flowDirectionsLists[i].__getitem__(4)[0],flowDirectionsLists[i].__getitem__(5)[0],flowDirectionsLists[i].__getitem__(6)[0])
            for j in range(len(flowDirectionsLists[i])):
                if(i == 1 and j in [1,2]):
                    continue
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfRatesOfFrames = computeInstantaneousRates(newTimes,listOfFrameSizes[i].__getitem__(j),duration)
                x = newTimesPeriods
                y = listOfRatesOfFrames
                yLabel = '{}'.format(labels[j]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[j]),marker = '.',linestyle='-')
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('instantaneous rate (Mbps)', fontsize=12)
            plt.title("{} instantaneous rates of frames of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_instantaneous_rates.png'.format(folderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### Line Graph 2 ####################
    # Line Graph for instantaneous rates for different time durations from HMD traces folder (each data type will be in a graph)
    for duration in durations:
        for j in range(len(labels)):
            firstFrame = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0]) if j not in [1,2] else flowDirectionsLists[0].__getitem__(j)[0]
            for i in range(len(flowDirections)):
                if(i == 1 and j in [1,2]):
                        continue
                folderPath = "{}/{}".format(prefix,labels[j])
                try:
                    os.mkdir(folderPath)
                except:
                    pass
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfRatesOfFrames = computeInstantaneousRates(newTimes,listOfFrameSizes[i].__getitem__(j),duration)
                x = newTimesPeriods
                y = listOfRatesOfFrames
                yLabel = '{}'.format(flowDirections[i]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[i]),marker = '.',linestyle='-')
                
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('instantaneous rate (Mbps)', fontsize=12)
            plt.title("{} instantaneous rates of frames of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_instantaneous_rates.png'.format(folderPath,labels[j],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################


    #################### Line Graph 3 ####################
    # Line Graph for instantaneous rates for all the frames from all data types for different time durations from HMD traces folder
    folderPath = "{}/{}".format(prefix,"all_data_types")
    try:
        os.mkdir(folderPath)
    except:
        pass
    try:
        listOfFolders = ["DMR","DR","DM","D","R"]
        for tempFolder in listOfFolders:
            os.mkdir("{}/{}".format(folderPath,tempFolder))
    except:
        pass
    for duration in durations: 
        # [D+M+R] all data frames + all management frames + all re-transmitted frames (lists suffix 1) 
        uniqueDataCombinedLists_1,retransmittedDataCombinedLists_1 = combinedResultsLists(results,1)
        HMD_UP_NBs_1,HMD_UP_Times_1,HMD_UP_DataRates_1,HMD_UP_Data_Sizes_1,HMD_UP_Frames_Sizes_1,HMD_UP_Frames_SeqNB_1,HMD_DWN_NBs_1,HMD_DWN_Times_1,HMD_DWN_DataRates_1,HMD_DWN_Data_Sizes_1,HMD_DWN_Frames_Sizes_1,HMD_DWN_Frames_SeqNB_1 = uniqueDataCombinedLists_1
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_1[0],HMD_UP_Times_1)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeInstantaneousRates(newTimesX1,HMD_UP_Frames_Sizes_1,duration)
        x1 = newTimesPeriodsX1
        y1 = listOfRatesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_1[0],HMD_DWN_Times_1)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeInstantaneousRates(newTimesX2,HMD_DWN_Frames_Sizes_1,duration)
        x2 = newTimesPeriodsX2
        y2 = listOfRatesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('instantaneous rate (Mbps)', fontsize=12)
        plt.title("DMR instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DMR/{}_instantaneous_rate.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D+R] all data frames + all re-transmitted frames (lists suffix 2) 
        uniqueDataCombinedLists_2,retransmittedDataCombinedLists_2 = combinedResultsLists(results,0)
        HMD_UP_NBs_2,HMD_UP_Times_2,HMD_UP_DataRates_2,HMD_UP_Data_Sizes_2,HMD_UP_Frames_Sizes_2,HMD_UP_Frames_SeqNB_2,HMD_DWN_NBs_2,HMD_DWN_Times_2,HMD_DWN_DataRates_2,HMD_DWN_Data_Sizes_2,HMD_DWN_Frames_Sizes_2,HMD_DWN_Frames_SeqNB_2 = uniqueDataCombinedLists_2
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_2[0],HMD_UP_Times_2)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeInstantaneousRates(newTimesX1,HMD_UP_Frames_Sizes_2,duration)
        x1 = newTimesPeriodsX1
        y1 = listOfRatesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_2[0],HMD_DWN_Times_2)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeInstantaneousRates(newTimesX2,HMD_DWN_Frames_Sizes_2,duration)
        x2 = newTimesPeriodsX2
        y2 = listOfRatesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('instantaneous rate (Mbps)', fontsize=12)
        plt.title("DR instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DR/{}_instantaneous_rate.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D+M] all data frames + all management frames (lists suffix 3) 
        uniqueDataCombinedLists_3,retransmittedDataCombinedLists_3 = combinedResultsListsNoReTransmittedFrames(results,1)
        HMD_UP_NBs_3,HMD_UP_Times_3,HMD_UP_DataRates_3,HMD_UP_Data_Sizes_3,HMD_UP_Frames_Sizes_3,HMD_UP_Frames_SeqNB_3,HMD_DWN_NBs_3,HMD_DWN_Times_3,HMD_DWN_DataRates_3,HMD_DWN_Data_Sizes_3,HMD_DWN_Frames_Sizes_3,HMD_DWN_Frames_SeqNB_3 = uniqueDataCombinedLists_3
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_3[0],HMD_UP_Times_3)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeInstantaneousRates(newTimesX1,HMD_UP_Frames_Sizes_3,duration)
        x1 = newTimesPeriodsX1
        y1 = listOfRatesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_3[0],HMD_DWN_Times_3)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeInstantaneousRates(newTimesX2,HMD_DWN_Frames_Sizes_3,duration)
        x2 = newTimesPeriodsX2
        y2 = listOfRatesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('instantaneous rate (Mbps)', fontsize=12)
        plt.title("DM instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DM/{}_instantaneous_rate.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D] all data frames (lists suffix 4) 
        uniqueDataCombinedLists_4,retransmittedDataCombinedLists_4 = combinedResultsListsNoReTransmittedFrames(results,0)
        HMD_UP_NBs_3,HMD_UP_Times_4,HMD_UP_DataRates_4,HMD_UP_Data_Sizes_4,HMD_UP_Frames_Sizes_4,HMD_UP_Frames_SeqNB_4,HMD_DWN_NBs_4,HMD_DWN_Times_4,HMD_DWN_DataRates_4,HMD_DWN_Data_Sizes_4,HMD_DWN_Frames_Sizes_4,HMD_DWN_Frames_SeqNB_4 = uniqueDataCombinedLists_4
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_4[0],HMD_UP_Times_4)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeInstantaneousRates(newTimesX1,HMD_UP_Frames_Sizes_4,duration)
        x1 = newTimesPeriodsX1
        y1 = listOfRatesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_4[0],HMD_DWN_Times_4)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeInstantaneousRates(newTimesX2,HMD_DWN_Frames_Sizes_4,duration)
        x2 = newTimesPeriodsX2
        y2 = listOfRatesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('instantaneous rate (Mbps)', fontsize=12)
        plt.title("D instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/D/{}_instantaneous_rate.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [R] all re-transmitted frames (lists suffix 5)
        HMD_UP_RE_NBs_5,HMD_UP_RE_Times_5,HMD_UP_RE_DataRates_5,HMD_UP_RE_Data_Sizes_5,HMD_UP_RE_Frames_Sizes_5,HMD_UP_RE_Frames_SeqNB_5,HMD_DWN_RE_NBs_5,HMD_DWN_RE_Times_5,HMD_DWN_RE_DataRates_5,HMD_DWN_RE_Data_Sizes_5,HMD_DWN_RE_Frames_Sizes_5,HMD_DWN_RE_Frames_SeqNB_5 = retransmittedDataCombinedLists_1
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_RE_Times_5[0],HMD_UP_RE_Times_5)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeInstantaneousRates(newTimesX1,HMD_UP_RE_Frames_Sizes_5,duration)
        x1 = newTimesPeriodsX1
        y1 = listOfRatesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_RE_Times_5[0],HMD_DWN_RE_Times_5)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeInstantaneousRates(newTimesX2,HMD_DWN_RE_Frames_Sizes_5,duration)
        x2 = newTimesPeriodsX2
        y2 = listOfRatesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('instantaneous rate (Mbps)', fontsize=12)
        plt.title("R instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/R/{}_instantaneous_rate.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()
        ######################################################



    #################### CDF  Graph 1 ####################
    # CDF Graph for instantaneous rates for different time durations from HMD traces folder (each direction will be in a graph)
    for duration in durations:
        for i in range(len(flowDirections)):
            folderPath = "{}/{}".format(prefix,flowDirections[i])
            try:
                os.mkdir(folderPath)
            except:
                pass
            firstFrame = min(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1)[0] if i==0 else 100000000,flowDirectionsLists[i].__getitem__(2)[0] if i == 0 else 100000000,flowDirectionsLists[i].__getitem__(3)[0],
                            flowDirectionsLists[i].__getitem__(4)[0],flowDirectionsLists[i].__getitem__(5)[0],flowDirectionsLists[i].__getitem__(6)[0])
            for j in range(len(flowDirectionsLists[i])):
                if(i == 1 and j in [1,2]):
                    continue
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfRatesOfFrames = computeInstantaneousRates(newTimes,listOfFrameSizes[i].__getitem__(j),duration)
                data = [float(value) for value in listOfRatesOfFrames]
                x = np.sort(data)
                y = np.arange(len(x))/float(len(x))
                yLabel = '{}'.format(labels[j]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[j]),linestyle='{}'.format(lineStyles[j]))
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('instantaneous rate (Mbps)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF {} instantaneous rates of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_instantaneous_rates_CDF.png'.format(folderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### CDF  Graph 2 ####################
    # CDF Graph for instantaneous rates for different time durations from HMD traces folder (each data type will be in a graph)
    for duration in durations:
        for j in range(len(labels)):
            firstFrame = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0]) if j not in [1,2] else flowDirectionsLists[0].__getitem__(j)[0]
            for i in range(len(flowDirections)):
                if(i == 1 and j in [1,2]):
                        continue
                folderPath = "{}/{}".format(prefix,labels[j])
                try:
                    os.mkdir(folderPath)
                except:
                    pass
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfRatesOfFrames = computeInstantaneousRates(newTimes,listOfFrameSizes[i].__getitem__(j),duration)
                data = [float(value) for value in listOfRatesOfFrames]
                x = np.sort(data)
                y = np.arange(len(x))/float(len(x))
                yLabel = '{}'.format(flowDirections[i]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[i]),linestyle='{}'.format(lineStyles[i]))
                
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('instantaneous rate (Mbps)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF of {} frames instantaneous rates of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_instantaneous_rates_CDF.png'.format(folderPath,labels[j],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################


    #################### CDF  Graph 3 ####################
    # CDF Graph for instantaneous rates for all the frames from all data types for different time durations from HMD traces folder
    folderPath = "{}/{}".format(prefix,"all_data_types")
    try:
        os.mkdir(folderPath)
    except:
        pass
    try:
        listOfFolders = ["DMR","DR","DM","D","R"]
        for tempFolder in listOfFolders:
            os.mkdir("{}/{}".format(folderPath,tempFolder))
    except:
        pass  
    for duration in durations: 
        # [D+M+R] all data frames + all management frames + all re-transmitted frames (lists suffix 1) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_1[0],HMD_UP_Times_1)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeInstantaneousRates(newTimesX1,HMD_UP_Frames_Sizes_1,duration)
        data1 = [float(value) for value in listOfRatesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_1[0],HMD_DWN_Times_1)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeInstantaneousRates(newTimesX2,HMD_DWN_Frames_Sizes_1,duration)
        data2 = [float(value) for value in listOfRatesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('instantaneous rate (Mbps)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of DMR frames instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DMR/{}_instantaneous_rate_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D+R] all data frames + all re-transmitted frames (lists suffix 2) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_2[0],HMD_UP_Times_2)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeInstantaneousRates(newTimesX1,HMD_UP_Frames_Sizes_2,duration)
        data1 = [float(value) for value in listOfRatesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_2[0],HMD_DWN_Times_2)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeInstantaneousRates(newTimesX2,HMD_DWN_Frames_Sizes_2,duration)
        data2 = [float(value) for value in listOfRatesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('instantaneous rate (Mbps)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of DR frames instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DR/{}_instantaneous_rate_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D+M] all data frames + all management frames (lists suffix 3) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_3[0],HMD_UP_Times_3)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeInstantaneousRates(newTimesX1,HMD_UP_Frames_Sizes_3,duration)
        data1 = [float(value) for value in listOfRatesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_3[0],HMD_DWN_Times_3)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeInstantaneousRates(newTimesX2,HMD_DWN_Frames_Sizes_3,duration)
        data2 = [float(value) for value in listOfRatesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('instantaneous rate (Mbps)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of DM frames instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DM/{}_instantaneous_rate_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D] all data frames (lists suffix 4) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_4[0],HMD_UP_Times_4)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeInstantaneousRates(newTimesX1,HMD_UP_Frames_Sizes_4,duration)
        data1 = [float(value) for value in listOfRatesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_4[0],HMD_DWN_Times_4)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeInstantaneousRates(newTimesX2,HMD_DWN_Frames_Sizes_4,duration)
        data2 = [float(value) for value in listOfRatesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('instantaneous rate (Mbps)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of D frames instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/D/{}_instantaneous_rate_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [R] all re-transmitted frames (lists suffix 5)
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_RE_Times_5[0],HMD_UP_RE_Times_5)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeInstantaneousRates(newTimesX1,HMD_UP_RE_Frames_Sizes_5,duration)
        data1 = [float(value) for value in listOfRatesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_RE_Times_5[0],HMD_DWN_RE_Times_5)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeInstantaneousRates(newTimesX2,HMD_DWN_RE_Frames_Sizes_5,duration)
        data2 = [float(value) for value in listOfRatesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('instantaneous rate (Mbps)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of R frames instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/R/{}_instantaneous_rate_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()
        ######################################################



def plotServerDataInstantaneousRates(root_folder,gameName,results):
    result_folder_name = "server/data_instantaneous_rates"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    
    try:
        os.mkdir(prefix)
    except:
        pass


    server_UP_BOTH_NBs,server_UP_BOTH_Times,server_UP_BOTH_Data_Sizes,server_UP_BOTH_Frames_Sizes,server_UP_TCP_NBs,\
        server_UP_TCP_Times,server_UP_TCP_Data_Sizes,server_UP_TCP_Frames_Sizes,server_UP_UDP_NBs,server_UP_UDP_Times,\
        server_UP_UDP_Data_Sizes,server_UP_UDP_Frames_Sizes,server_DWN_BOTH_NBs,server_DWN_BOTH_Times,server_DWN_BOTH_Data_Sizes,\
        server_DWN_BOTH_Frames_Sizes,server_DWN_TCP_NBs,server_DWN_TCP_Times,server_DWN_TCP_Data_Sizes,server_DWN_TCP_Frames_Sizes,\
        server_DWN_UDP_NBs,server_DWN_UDP_Times,server_DWN_UDP_Data_Sizes,server_DWN_UDP_Frames_Sizes = results     

    #################### Line Graph ####################
    # line graph for instantaneous rates for different time durations from server.csv trace
    durations = [1,10,15,30,60]  # in seconds
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(server_UP_BOTH_Times,server_UP_UDP_Times,server_UP_TCP_Times),
                            (server_DWN_BOTH_Times,server_DWN_UDP_Times,server_DWN_TCP_Times)]
    listOfDataSizes = [(server_UP_BOTH_Data_Sizes,server_UP_UDP_Data_Sizes,server_UP_TCP_Data_Sizes),
                        (server_DWN_BOTH_Data_Sizes,server_DWN_UDP_Data_Sizes,server_DWN_TCP_Data_Sizes)]
    
    
    for duration in durations:
        for i in range(len(flowDirections)):
            newTimesBoth = relativeTime(flowDirectionsLists[i].__getitem__(0))
            newTimesPeriodsBoth = convertTimeToPeriods(newTimesBoth,duration)
            listOfRatesOfDataBoth = computeInstantaneousRates(newTimesBoth,listOfDataSizes[i].__getitem__(0),duration)
            newTimesUDP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1))
            newTimesPeriodsUDP = convertTimeToPeriods(newTimesUDP,duration)
            listOfRatesOfDataUDP = computeInstantaneousRates(newTimesUDP,listOfDataSizes[i].__getitem__(1),duration)
            newTimesTCP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(2))
            newTimesPeriodsTCP = convertTimeToPeriods(newTimesTCP,duration)
            listOfRatesOfDataTCP = computeInstantaneousRates(newTimesTCP,listOfDataSizes[i].__getitem__(2),duration)
            x1 = newTimesPeriodsBoth
            y1 = listOfRatesOfDataBoth
            y1Label = 'Both'
            x2 = newTimesPeriodsUDP
            y2 = listOfRatesOfDataUDP
            y2Label = 'UDP'
            x3 = newTimesPeriodsTCP
            y3 = listOfRatesOfDataTCP
            y3Label = 'TCP'      
            plt.plot(x1,y1,label=y1Label,c='red',marker = '.',linestyle='-')
            plt.plot(x2,y2,label=y2Label,c='blue',marker = '.',linestyle='-')
            plt.plot(x3,y3,label=y3Label,c='green',marker = '.',linestyle='-')
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('instantaneous rate (Mbps)', fontsize=12)
            plt.title("{} instantaneous rates of data of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_instantaneous_rates.png'.format(prefix,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ####################################################



    #################### CDF  Graph ####################
    # CDF Graph for instantaneous rates for different time durations from server.csv trace
    for duration in durations:
        for i in range(len(flowDirections)):    
            newTimesBoth = relativeTime(flowDirectionsLists[i].__getitem__(0))
            newTimesPeriodsBoth = convertTimeToPeriods(newTimesBoth,duration)
            listOfRatesOfDataBoth = computeInstantaneousRates(newTimesBoth,listOfDataSizes[i].__getitem__(0),duration)
            newTimesUDP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1))
            newTimesPeriodsUDP = convertTimeToPeriods(newTimesUDP,duration)
            listOfRatesOfDataUDP = computeInstantaneousRates(newTimesUDP,listOfDataSizes[i].__getitem__(1),duration)
            newTimesTCP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(2))
            newTimesPeriodsTCP = convertTimeToPeriods(newTimesTCP,duration)
            listOfRatesOfDataTCP = computeInstantaneousRates(newTimesTCP,listOfDataSizes[i].__getitem__(2),duration)
            
            data1 = [float(i) for i in listOfRatesOfDataBoth]
            data2 = [float(i) for i in listOfRatesOfDataUDP]
            data3 = [float(i) for i in listOfRatesOfDataTCP]
            
            x1 = np.sort(data1)
            x2 = np.sort(data2)
            x3 = np.sort(data3)

            y1 = np.arange(len(x1))/float(len(x1))
            y2 = np.arange(len(x2))/float(len(x2))
            y3 = np.arange(len(x3))/float(len(x3))

            y1Label =  'Both'
            y2Label =  'UDP'
            y3Label =  'TCP'

            plt.plot(x1, y1,label=y1Label,c='red',linestyle='-.')
            plt.plot(x2, y2,label=y2Label,c='blue',linestyle=':')
            plt.plot(x3, y3,label=y3Label,c='green',linestyle='--')

            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('instantaneous rates (Mbps)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF {} instantaneous rates (Mbps) of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=9)
            plt.savefig('{}/{}_duration_{}_instantaneous_rates_CDF.png'.format(prefix,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ####################################################



def plotHMDDataInstantaneousRates(root_folder,gameName,results):
    result_folder_name = "HMD/data_instantaneous_rates"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    
    try:
        os.mkdir(prefix)
    except:
        pass

    HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates,\
        HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes, HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times,\
        HMD_DWN_MANAGEMENT_FRAMES_DataRates, HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes, HMD_UP_DATA1_FRAMES_NBs, \
        HMD_UP_DATA1_FRAMES_Times, HMD_UP_DATA1_FRAMES_DataRates, HMD_UP_DATA1_FRAMES_Frames_Sizes,\
        HMD_UP_DATA1_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA1_FRAMES_NBs, HMD_UP_RE_DATA1_FRAMES_Times, \
        HMD_UP_RE_DATA1_FRAMES_DataRates, HMD_UP_RE_DATA1_FRAMES_Frames_Sizes, HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB,\
        HMD_UP_DATA2_FRAMES_NBs, HMD_UP_DATA2_FRAMES_Times, HMD_UP_DATA2_FRAMES_DataRates, HMD_UP_DATA2_FRAMES_Data_Sizes,\
        HMD_UP_DATA2_FRAMES_Frames_Sizes, HMD_UP_DATA2_FRAMES_Frames_SeqNB, HMD_DWN_DATA2_FRAMES_NBs, HMD_DWN_DATA2_FRAMES_Times, \
        HMD_DWN_DATA2_FRAMES_DataRates, HMD_DWN_DATA2_FRAMES_Data_Sizes, HMD_DWN_DATA2_FRAMES_Frames_Sizes, \
        HMD_DWN_DATA2_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA2_FRAMES_NBs, HMD_UP_RE_DATA2_FRAMES_Times, HMD_UP_RE_DATA2_FRAMES_DataRates,\
        HMD_UP_RE_DATA2_FRAMES_Data_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB, \
        HMD_DWN_RE_DATA2_FRAMES_NBs, HMD_DWN_RE_DATA2_FRAMES_Times, HMD_DWN_RE_DATA2_FRAMES_DataRates, HMD_DWN_RE_DATA2_FRAMES_Data_Sizes,\
        HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB, HMD_UP_DATA3_FRAMES_NBs, HMD_UP_DATA3_FRAMES_Times, \
        HMD_UP_DATA3_FRAMES_DataRates, HMD_UP_DATA3_FRAMES_Data_Sizes, HMD_UP_DATA3_FRAMES_Frames_Sizes, HMD_UP_DATA3_FRAMES_Frames_SeqNB,\
        HMD_DWN_DATA3_FRAMES_NBs, HMD_DWN_DATA3_FRAMES_Times, HMD_DWN_DATA3_FRAMES_DataRates, HMD_DWN_DATA3_FRAMES_Data_Sizes,\
        HMD_DWN_DATA3_FRAMES_Frames_Sizes, HMD_DWN_DATA3_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA3_FRAMES_NBs, HMD_UP_RE_DATA3_FRAMES_Times, \
        HMD_UP_RE_DATA3_FRAMES_DataRates, HMD_UP_RE_DATA3_FRAMES_Data_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_Sizes, \
        HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB, HMD_DWN_RE_DATA3_FRAMES_NBs, HMD_DWN_RE_DATA3_FRAMES_Times, HMD_DWN_RE_DATA3_FRAMES_DataRates, \
        HMD_DWN_RE_DATA3_FRAMES_Data_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB = results 
    

    durations = [1,10,15,30,60]  # in seconds
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(HMD_UP_DATA2_FRAMES_Times,HMD_UP_RE_DATA2_FRAMES_Times,HMD_UP_DATA3_FRAMES_Times,HMD_UP_RE_DATA3_FRAMES_Times),
                            (HMD_DWN_DATA2_FRAMES_Times,HMD_DWN_RE_DATA2_FRAMES_Times,HMD_DWN_DATA3_FRAMES_Times,HMD_DWN_RE_DATA3_FRAMES_Times)]
    listOfDataSizes = [(HMD_UP_DATA2_FRAMES_Data_Sizes,HMD_UP_RE_DATA2_FRAMES_Data_Sizes,HMD_UP_DATA3_FRAMES_Data_Sizes,HMD_UP_RE_DATA3_FRAMES_Data_Sizes),
                        (HMD_DWN_DATA2_FRAMES_Data_Sizes,HMD_DWN_RE_DATA2_FRAMES_Data_Sizes,HMD_DWN_DATA3_FRAMES_Data_Sizes,HMD_DWN_RE_DATA3_FRAMES_Data_Sizes)]
    colors = ["black","purple","cyan","pink"]
    lineStyles = ["-",'-.',':',"--"]
    markers = [".",",","1","x"]
    labels = ["data type2","retransmitted data type2","data type3","retransmitted data type3"]


    #################### Line Graph 1 ####################
    # Line Graph for instantaneous rates for different time durations from HMD traces folder (each direction will be in a graph)
    for duration in durations:
        for i in range(len(flowDirections)):
            folderPath = "{}/{}".format(prefix,flowDirections[i])
            try:
                os.mkdir(folderPath)
            except:
                pass
            firstFrame = min(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1)[0],flowDirectionsLists[i].__getitem__(2)[0],flowDirectionsLists[i].__getitem__(3)[0])
            for j in range(len(flowDirectionsLists[i])):
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfRatesOfFrames = computeInstantaneousRates(newTimes,listOfDataSizes[i].__getitem__(j),duration)
                x = newTimesPeriods
                y = listOfRatesOfFrames
                yLabel = '{}'.format(labels[j]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[j]),marker = '.',linestyle='-')
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('instantaneous rate (Mbps)', fontsize=12)
            plt.title("{} instantaneous rates of data of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_instantaneous_rates.png'.format(folderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### Line Graph 2 ####################
    # Line Graph for instantaneous rates for different time durations from HMD traces folder (each data type will be in a graph)
    for duration in durations:
        for j in range(len(labels)):
            firstFrame = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0])
            for i in range(len(flowDirections)):
                folderPath = "{}/{}".format(prefix,labels[j])
                try:
                    os.mkdir(folderPath)
                except:
                    pass
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfRatesOfFrames = computeInstantaneousRates(newTimes,listOfDataSizes[i].__getitem__(j),duration)
                x = newTimesPeriods
                y = listOfRatesOfFrames
                yLabel = '{}'.format(flowDirections[i]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[i]),marker = '.',linestyle='-')
                
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('instantaneous rate (Mbps)', fontsize=12)
            plt.title("{} instantaneous rates of data of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_instantaneous_rates.png'.format(folderPath,labels[j],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################


    #################### Line Graph 3 ####################
    # Line Graph for instantaneous rates for all the frames from all data types for different time durations from HMD traces folder
    folderPath = "{}/{}".format(prefix,"all_data_types")
    try:
        os.mkdir(folderPath)
    except:
        pass
    try:
        listOfFolders = ["DR","D","R"]
        for tempFolder in listOfFolders:
            os.mkdir("{}/{}".format(folderPath,tempFolder))
    except:
        pass
    for duration in durations: 
        # [D+R] all data frames + all re-transmitted frames (lists suffix 1) 
        uniqueDataCombinedLists_1,retransmittedDataCombinedLists_1 = combinedResultsLists(results,0)
        HMD_UP_NBs_1,HMD_UP_Times_1,HMD_UP_DataRates_1,HMD_UP_Data_Sizes_1,HMD_UP_Frames_Sizes_1,HMD_UP_Frames_SeqNB_1,HMD_DWN_NBs_1,HMD_DWN_Times_1,HMD_DWN_DataRates_1,HMD_DWN_Data_Sizes_1,HMD_DWN_Frames_Sizes_1,HMD_DWN_Frames_SeqNB_1 = uniqueDataCombinedLists_1
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_1[0],HMD_UP_Times_1)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeInstantaneousRates(newTimesX1,HMD_UP_Data_Sizes_1,duration)
        x1 = newTimesPeriodsX1
        y1 = listOfRatesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_1[0],HMD_DWN_Times_1)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeInstantaneousRates(newTimesX2,HMD_DWN_Data_Sizes_1,duration)
        x2 = newTimesPeriodsX2
        y2 = listOfRatesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('instantaneous rate (Mbps)', fontsize=12)
        plt.title("DR instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DR/{}_instantaneous_rate.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D] all data frames (lists suffix 2) 
        uniqueDataCombinedLists_2,retransmittedDataCombinedLists_2 = combinedResultsListsNoReTransmittedFrames(results,0)
        HMD_UP_NBs_2,HMD_UP_Times_2,HMD_UP_DataRates_2,HMD_UP_Data_Sizes_2,HMD_UP_Frames_Sizes_2,HMD_UP_Frames_SeqNB_2,HMD_DWN_NBs_2,HMD_DWN_Times_2,HMD_DWN_DataRates_2,HMD_DWN_Data_Sizes_2,HMD_DWN_Frames_Sizes_2,HMD_DWN_Frames_SeqNB_2 = uniqueDataCombinedLists_2
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_2[0],HMD_UP_Times_2)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeInstantaneousRates(newTimesX1,HMD_UP_Data_Sizes_2,duration)
        x1 = newTimesPeriodsX1
        y1 = listOfRatesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_2[0],HMD_DWN_Times_2)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeInstantaneousRates(newTimesX2,HMD_DWN_Data_Sizes_2,duration)
        x2 = newTimesPeriodsX2
        y2 = listOfRatesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('instantaneous rate (Mbps)', fontsize=12)
        plt.title("D instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/D/{}_instantaneous_rate.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [R] all re-transmitted frames (lists suffix 3)
        HMD_UP_RE_NBs_3,HMD_UP_RE_Times_3,HMD_UP_RE_DataRates_3,HMD_UP_RE_Data_Sizes_3,HMD_UP_RE_Frames_Sizes_3,HMD_UP_RE_Frames_SeqNB_3,HMD_DWN_RE_NBs_3,HMD_DWN_RE_Times_3,HMD_DWN_RE_DataRates_3,HMD_DWN_RE_Data_Sizes_3,HMD_DWN_RE_Frames_Sizes_3,HMD_DWN_RE_Frames_SeqNB_3 = retransmittedDataCombinedLists_1
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_RE_Times_3[0],HMD_UP_RE_Times_3)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeInstantaneousRates(newTimesX1,HMD_UP_RE_Data_Sizes_3,duration)
        x1 = newTimesPeriodsX1
        y1 = listOfRatesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_RE_Times_3[0],HMD_DWN_RE_Times_3)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeInstantaneousRates(newTimesX2,HMD_DWN_RE_Data_Sizes_3,duration)
        x2 = newTimesPeriodsX2
        y2 = listOfRatesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('instantaneous rate (Mbps)', fontsize=12)
        plt.title("R instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/R/{}_instantaneous_rate.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()
        ######################################################



    #################### CDF  Graph 1 ####################
    # CDF Graph for instantaneous rates for different time durations from HMD traces folder (each direction will be in a graph)
    for duration in durations:
        for i in range(len(flowDirections)):
            folderPath = "{}/{}".format(prefix,flowDirections[i])
            try:
                os.mkdir(folderPath)
            except:
                pass
            firstFrame = min(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1)[0],flowDirectionsLists[i].__getitem__(2)[0],flowDirectionsLists[i].__getitem__(3)[0])
            for j in range(len(flowDirectionsLists[i])):
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfRatesOfFrames = computeInstantaneousRates(newTimes,listOfDataSizes[i].__getitem__(j),duration)
                data = [float(value) for value in listOfRatesOfFrames]
                x = np.sort(data)
                y = np.arange(len(x))/float(len(x))
                yLabel = '{}'.format(labels[j]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[j]),linestyle='{}'.format(lineStyles[j]))
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('instantaneous rate (Mbps)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF {} instantaneous rates of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_instantaneous_rates_CDF.png'.format(folderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### CDF  Graph 2 ####################
    # CDF Graph for instantaneous rates for different time durations from HMD traces folder (each data type will be in a graph)
    for duration in durations:
        for j in range(len(labels)):
            firstFrame = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0])
            for i in range(len(flowDirections)):
                folderPath = "{}/{}".format(prefix,labels[j])
                try:
                    os.mkdir(folderPath)
                except:
                    pass
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfRatesOfFrames = computeInstantaneousRates(newTimes,listOfDataSizes[i].__getitem__(j),duration)
                data = [float(value) for value in listOfRatesOfFrames]
                x = np.sort(data)
                y = np.arange(len(x))/float(len(x))
                yLabel = '{}'.format(flowDirections[i]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[i]),linestyle='{}'.format(lineStyles[i]))
                
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('instantaneous rate (Mbps)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF of {} data instantaneous rates of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_instantaneous_rates_CDF.png'.format(folderPath,labels[j],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################


    #################### CDF  Graph 3 ####################
    # CDF Graph for instantaneous rates for all the frames from all data types for different time durations from HMD traces folder
    folderPath = "{}/{}".format(prefix,"all_data_types")
    try:
        os.mkdir(folderPath)
    except:
        pass
    try:
        listOfFolders = ["DR","D","R"]
        for tempFolder in listOfFolders:
            os.mkdir("{}/{}".format(folderPath,tempFolder))
    except:
        pass   
    for duration in durations: 
        # [D+R] all data frames + all re-transmitted frames (lists suffix 1) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_1[0],HMD_UP_Times_1)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeInstantaneousRates(newTimesX1,HMD_UP_Data_Sizes_1,duration)
        data1 = [float(value) for value in listOfRatesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_1[0],HMD_DWN_Times_1)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeInstantaneousRates(newTimesX2,HMD_DWN_Data_Sizes_1,duration)
        data2 = [float(value) for value in listOfRatesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('instantaneous rate (Mbps)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of DR data instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DR/{}_instantaneous_rate_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D] all data frames (lists suffix 2) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_2[0],HMD_UP_Times_2)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeInstantaneousRates(newTimesX1,HMD_UP_Data_Sizes_2,duration)
        data1 = [float(value) for value in listOfRatesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_2[0],HMD_DWN_Times_2)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeInstantaneousRates(newTimesX2,HMD_DWN_Data_Sizes_2,duration)
        data2 = [float(value) for value in listOfRatesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('instantaneous rate (Mbps)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of D data instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/D/{}_instantaneous_rate_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [R] all data frames + all management frames (lists suffix 3) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_RE_Times_3[0],HMD_UP_RE_Times_3)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfRatesOfFramesY1 = computeInstantaneousRates(newTimesX1,HMD_UP_RE_Data_Sizes_3,duration)
        data1 = [float(value) for value in listOfRatesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_RE_Times_3[0],HMD_DWN_RE_Times_3)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfRatesOfFramesY2 = computeInstantaneousRates(newTimesX2,HMD_DWN_RE_Data_Sizes_3,duration)
        data2 = [float(value) for value in listOfRatesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('instantaneous rate (Mbps)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of R data instantaneous rates of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/R/{}_instantaneous_rate_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()
        ######################################################



def plotServerSizeofFrames(root_folder,gameName,results):
    result_folder_name = "server/size_of_frames"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    
    try:
        os.mkdir(prefix)
    except:
        pass


    server_UP_BOTH_NBs,server_UP_BOTH_Times,server_UP_BOTH_Data_Sizes,server_UP_BOTH_Frames_Sizes,server_UP_TCP_NBs,\
        server_UP_TCP_Times,server_UP_TCP_Data_Sizes,server_UP_TCP_Frames_Sizes,server_UP_UDP_NBs,server_UP_UDP_Times,\
        server_UP_UDP_Data_Sizes,server_UP_UDP_Frames_Sizes,server_DWN_BOTH_NBs,server_DWN_BOTH_Times,server_DWN_BOTH_Data_Sizes,\
        server_DWN_BOTH_Frames_Sizes,server_DWN_TCP_NBs,server_DWN_TCP_Times,server_DWN_TCP_Data_Sizes,server_DWN_TCP_Frames_Sizes,\
        server_DWN_UDP_NBs,server_DWN_UDP_Times,server_DWN_UDP_Data_Sizes,server_DWN_UDP_Frames_Sizes = results     

    #################### Line Graph ####################
    # line graph for size of frames for all frames from server.csv trace
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(server_UP_BOTH_Times,server_UP_UDP_Times,server_UP_TCP_Times),
                            (server_DWN_BOTH_Times,server_DWN_UDP_Times,server_DWN_TCP_Times)]
    listOfFrameSizes = [(server_UP_BOTH_Frames_Sizes,server_UP_UDP_Frames_Sizes,server_UP_TCP_Frames_Sizes),
                        (server_DWN_BOTH_Frames_Sizes,server_DWN_UDP_Frames_Sizes,server_DWN_TCP_Frames_Sizes)]
    protocols = ["Both","UDP","TCP"]
    colors = ['red','blue','green']
    NBofFrames = 50
    plotStartTime = 50 # It starts at the specified second
    for i in range(len(flowDirections)):
        protocolIndex = 0
        for protocol in protocols:
            newTimes = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(protocolIndex)[0],flowDirectionsLists[i].__getitem__(protocolIndex))
            newTimesSec = [float(x)/1000 for x in newTimes]
            timesOfFrames = []
            sizeOfFrames = []
            counter = 0
            for j in range(len(newTimesSec)):
                if(newTimesSec[j]>=plotStartTime):
                    timesOfFrames.append(newTimesSec[j])
                    sizeOfFrames.append(float(listOfFrameSizes[i].__getitem__(protocolIndex)[j]))
                    counter = counter + 1
                    if counter>=NBofFrames:
                        break
            x = timesOfFrames
            y = sizeOfFrames
            yLabel = '{}'.format(protocol)   
            plt.plot(x,y,label=yLabel,c='{}'.format(colors[protocolIndex]),marker = '.',linestyle='-')
            protocolIndex = protocolIndex + 1
   
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('frame size (Bytes)', fontsize=12)
        plt.title("{} size of all frames of {} for {} frames starting from the second {}".format(flowDirections[i],gameName,NBofFrames,plotStartTime),fontsize="9")
        plt.savefig('{}/{}_sizes_of_all_frames.png'.format(prefix,flowDirections[i]),dpi=saved_graph_resolution)
        plt.show()
    ####################################################



    #################### Line Graph ####################
    # line graph for size of frames for all frames from server.csv trace (separate protocols)
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(server_UP_BOTH_Times,server_UP_UDP_Times,server_UP_TCP_Times),
                            (server_DWN_BOTH_Times,server_DWN_UDP_Times,server_DWN_TCP_Times)]
    listOfFrameSizes = [(server_UP_BOTH_Frames_Sizes,server_UP_UDP_Frames_Sizes,server_UP_TCP_Frames_Sizes),
                        (server_DWN_BOTH_Frames_Sizes,server_DWN_UDP_Frames_Sizes,server_DWN_TCP_Frames_Sizes)]
    protocols = ["Both","UDP","TCP"]
    colors = ['red','blue','green']
    NBofFrames = 50
    plotStartTime = 50 # It starts at the specified second
    for i in range(len(flowDirections)):
        protocolIndex = 0
        for protocol in protocols:
            newTimes = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(protocolIndex)[0],flowDirectionsLists[i].__getitem__(protocolIndex))
            newTimesSec = [float(x)/1000 for x in newTimes]
            timesOfFrames = []
            sizeOfFrames = []
            counter = 0
            for j in range(len(newTimesSec)):
                if(newTimesSec[j]>=plotStartTime):
                    timesOfFrames.append(newTimesSec[j])
                    sizeOfFrames.append(float(listOfFrameSizes[i].__getitem__(protocolIndex)[j]))
                    counter = counter + 1
                    if counter>=NBofFrames:
                        break

            x1 = timesOfFrames
            y1 = sizeOfFrames
            y1Label = '{}'.format(protocol)   
            plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[protocolIndex]),marker = '.',linestyle='-')
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('frame size (Bytes)', fontsize=12)
            plt.title("{} size of {} frames of {} for {} frames starting from the second {}".format(flowDirections[i],protocol,gameName,NBofFrames,plotStartTime),fontsize=9)
            plt.savefig('{}/{}_sizes_of_{}_frames.png'.format(prefix,flowDirections[i],protocol),dpi=saved_graph_resolution)
            plt.show()
            protocolIndex = protocolIndex + 1
   

    ####################################################



    #################### Line Graph ####################
    # line graph for size of frames for different time durations from server.csv trace
    durations = [1,10,15,30,60]  # in seconds
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(server_UP_BOTH_Times,server_UP_UDP_Times,server_UP_TCP_Times),
                            (server_DWN_BOTH_Times,server_DWN_UDP_Times,server_DWN_TCP_Times)]
    listOfFrameSizes = [([float(x)/(1024**2) for x in server_UP_BOTH_Frames_Sizes],[float(x)/(1024**2) for x in server_UP_UDP_Frames_Sizes]
                        ,[float(x)/(1024**2) for x in server_UP_TCP_Frames_Sizes]),([float(x)/(1024**2) for x in server_DWN_BOTH_Frames_Sizes]
                        ,[float(x)/(1024**2) for x in server_DWN_UDP_Frames_Sizes],[float(x)/(1024**2) for x in server_DWN_TCP_Frames_Sizes])]
    
    
    for duration in durations:
        for i in range(len(flowDirections)):
            newTimesBoth = relativeTime(flowDirectionsLists[i].__getitem__(0))
            newTimesPeriodsBoth = convertTimeToPeriods(newTimesBoth,duration)
            totalSizeOfFramesBoth = computeTotalSize(newTimesBoth,listOfFrameSizes[i].__getitem__(0),duration)
            newTimesUDP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1))
            newTimesPeriodsUDP = convertTimeToPeriods(newTimesUDP,duration)
            totalSizeOfFramesUDP = computeTotalSize(newTimesUDP,listOfFrameSizes[i].__getitem__(1),duration)
            newTimesTCP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(2))
            newTimesPeriodsTCP = convertTimeToPeriods(newTimesTCP,duration)
            totalSizeOfFramesTCP = computeTotalSize(newTimesTCP,listOfFrameSizes[i].__getitem__(2),duration)
            x1 = newTimesPeriodsBoth
            y1 = totalSizeOfFramesBoth
            y1Label = 'Both'
            x2 = newTimesPeriodsUDP
            y2 = totalSizeOfFramesUDP
            y2Label = 'UDP'
            x3 = newTimesPeriodsTCP
            y3 = totalSizeOfFramesTCP
            y3Label = 'TCP'      
            plt.plot(x1,y1,label=y1Label,c='red',marker = '.',linestyle='-')
            plt.plot(x2,y2,label=y2Label,c='blue',marker = '.',linestyle='-')
            plt.plot(x3,y3,label=y3Label,c='green',marker = '.',linestyle='-')
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('total frames size (MB)', fontsize=12)
            plt.title("{} total size of frames of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=9)
            plt.savefig('{}/{}_duration_{}_size_of_frames.png'.format(prefix,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ####################################################



    #################### CDF  Graph ####################
    # CDF Graph for size of frames for different time durations from server.csv trace
    for duration in durations:
        for i in range(len(flowDirections)):    
            newTimesBoth = relativeTime(flowDirectionsLists[i].__getitem__(0))
            newTimesPeriodsBoth = convertTimeToPeriods(newTimesBoth,duration)
            totalSizeOfFramesBoth = computeTotalSize(newTimesBoth,listOfFrameSizes[i].__getitem__(0),duration)
            newTimesUDP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1))
            newTimesPeriodsUDP = convertTimeToPeriods(newTimesUDP,duration)
            totalSizeOfFramesUDP = computeTotalSize(newTimesUDP,listOfFrameSizes[i].__getitem__(1),duration)
            newTimesTCP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(2))
            newTimesPeriodsTCP = convertTimeToPeriods(newTimesTCP,duration)
            totalSizeOfFramesTCP = computeTotalSize(newTimesTCP,listOfFrameSizes[i].__getitem__(2),duration)
            
            data1 = [float(i) for i in totalSizeOfFramesBoth]
            data2 = [float(i) for i in totalSizeOfFramesUDP]
            data3 = [float(i) for i in totalSizeOfFramesTCP]
            
            x1 = np.sort(data1)
            x2 = np.sort(data2)
            x3 = np.sort(data3)

            y1 = np.arange(len(x1))/float(len(x1))
            y2 = np.arange(len(x2))/float(len(x2))
            y3 = np.arange(len(x3))/float(len(x3))

            y1Label =  'Both'
            y2Label =  'UDP'
            y3Label =  'TCP'

            plt.plot(x1, y1,label=y1Label,c='red',linestyle='-.')
            plt.plot(x2, y2,label=y2Label,c='blue',linestyle=':')
            plt.plot(x3, y3,label=y3Label,c='green',linestyle='--')

            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('total frames size (MB)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF {} size of frames of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=9)
            plt.savefig('{}/{}_duration_{}_sizs_of_frames_CDF.png'.format(prefix,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ####################################################



def plotHMDSizeofFrames(root_folder,gameName,results):
    result_folder_name = "HMD/size_of_frames"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    
    try:
        os.mkdir(prefix)
    except:
        pass

    HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates,\
        HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes, HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times,\
        HMD_DWN_MANAGEMENT_FRAMES_DataRates, HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes, HMD_UP_DATA1_FRAMES_NBs, \
        HMD_UP_DATA1_FRAMES_Times, HMD_UP_DATA1_FRAMES_DataRates, HMD_UP_DATA1_FRAMES_Frames_Sizes,\
        HMD_UP_DATA1_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA1_FRAMES_NBs, HMD_UP_RE_DATA1_FRAMES_Times, \
        HMD_UP_RE_DATA1_FRAMES_DataRates, HMD_UP_RE_DATA1_FRAMES_Frames_Sizes, HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB,\
        HMD_UP_DATA2_FRAMES_NBs, HMD_UP_DATA2_FRAMES_Times, HMD_UP_DATA2_FRAMES_DataRates, HMD_UP_DATA2_FRAMES_Data_Sizes,\
        HMD_UP_DATA2_FRAMES_Frames_Sizes, HMD_UP_DATA2_FRAMES_Frames_SeqNB, HMD_DWN_DATA2_FRAMES_NBs, HMD_DWN_DATA2_FRAMES_Times, \
        HMD_DWN_DATA2_FRAMES_DataRates, HMD_DWN_DATA2_FRAMES_Data_Sizes, HMD_DWN_DATA2_FRAMES_Frames_Sizes, \
        HMD_DWN_DATA2_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA2_FRAMES_NBs, HMD_UP_RE_DATA2_FRAMES_Times, HMD_UP_RE_DATA2_FRAMES_DataRates,\
        HMD_UP_RE_DATA2_FRAMES_Data_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB, \
        HMD_DWN_RE_DATA2_FRAMES_NBs, HMD_DWN_RE_DATA2_FRAMES_Times, HMD_DWN_RE_DATA2_FRAMES_DataRates, HMD_DWN_RE_DATA2_FRAMES_Data_Sizes,\
        HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB, HMD_UP_DATA3_FRAMES_NBs, HMD_UP_DATA3_FRAMES_Times, \
        HMD_UP_DATA3_FRAMES_DataRates, HMD_UP_DATA3_FRAMES_Data_Sizes, HMD_UP_DATA3_FRAMES_Frames_Sizes, HMD_UP_DATA3_FRAMES_Frames_SeqNB,\
        HMD_DWN_DATA3_FRAMES_NBs, HMD_DWN_DATA3_FRAMES_Times, HMD_DWN_DATA3_FRAMES_DataRates, HMD_DWN_DATA3_FRAMES_Data_Sizes,\
        HMD_DWN_DATA3_FRAMES_Frames_Sizes, HMD_DWN_DATA3_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA3_FRAMES_NBs, HMD_UP_RE_DATA3_FRAMES_Times, \
        HMD_UP_RE_DATA3_FRAMES_DataRates, HMD_UP_RE_DATA3_FRAMES_Data_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_Sizes, \
        HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB, HMD_DWN_RE_DATA3_FRAMES_NBs, HMD_DWN_RE_DATA3_FRAMES_Times, HMD_DWN_RE_DATA3_FRAMES_DataRates, \
        HMD_DWN_RE_DATA3_FRAMES_Data_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB = results 
    

    durations = [1,10,15,30,60]  # in seconds
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(HMD_UP_MANAGEMENT_FRAMES_Times,HMD_UP_DATA1_FRAMES_Times,HMD_UP_RE_DATA1_FRAMES_Times,HMD_UP_DATA2_FRAMES_Times,HMD_UP_RE_DATA2_FRAMES_Times,HMD_UP_DATA3_FRAMES_Times,HMD_UP_RE_DATA3_FRAMES_Times),
                            (HMD_DWN_MANAGEMENT_FRAMES_Times,[],[],HMD_DWN_DATA2_FRAMES_Times,HMD_DWN_RE_DATA2_FRAMES_Times,HMD_DWN_DATA3_FRAMES_Times,HMD_DWN_RE_DATA3_FRAMES_Times)]
    listOfFrameSizes = [([float(x)/(1024**2) for x in HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes],[float(x)/(1024**2) for x in HMD_UP_DATA1_FRAMES_Frames_Sizes],[float(x)/(1024**2) for x in HMD_UP_RE_DATA1_FRAMES_Frames_Sizes],[float(x)/(1024**2) for x in HMD_UP_DATA2_FRAMES_Frames_Sizes],[float(x)/(1024**2) for x in HMD_UP_RE_DATA2_FRAMES_Frames_Sizes],[float(x)/(1024**2) for x in HMD_UP_DATA3_FRAMES_Frames_Sizes],[float(x)/(1024**2) for x in HMD_UP_RE_DATA3_FRAMES_Frames_Sizes]),
                        ([float(x)/(1024**2) for x in HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes],[],[],[float(x)/(1024**2) for x in HMD_DWN_DATA2_FRAMES_Frames_Sizes],[float(x)/(1024**2) for x in HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes],[float(x)/(1024**2) for x in HMD_DWN_DATA3_FRAMES_Frames_Sizes],[float(x)/(1024**2) for x in HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes])]
    colors = ["red","blue","green","black","purple","cyan","pink"]
    lineStyles = ['-.',':',"--","-",'-.',':',"--"]
    markers = [".",",","1","x","|","+","v"]
    labels = ["management","data type1","retransmitted data type1","data type2","retransmitted data type2","data type3","retransmitted data type3"]


    #################### Line Graph 1 ####################
    # Line Graph for total frame sizes for different time durations from HMD traces folder (each direction will be in a graph)
    for duration in durations:
        for i in range(len(flowDirections)):
            folderPath = "{}/{}".format(prefix,flowDirections[i])
            try:
                os.mkdir(folderPath)
            except:
                pass
            firstFrame = min(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1)[0] if i==0 else 100000000,flowDirectionsLists[i].__getitem__(2)[0] if i == 0 else 100000000,flowDirectionsLists[i].__getitem__(3)[0],
                            flowDirectionsLists[i].__getitem__(4)[0],flowDirectionsLists[i].__getitem__(5)[0],flowDirectionsLists[i].__getitem__(6)[0])
            for j in range(len(flowDirectionsLists[i])):
                if(i == 1 and j in [1,2]):
                    continue
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfTotalSizesOfFrames = computeTotalSize(newTimes,listOfFrameSizes[i].__getitem__(j),duration)
                x = newTimesPeriods
                y = listOfTotalSizesOfFrames
                yLabel = '{}'.format(labels[j]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[j]),marker = '.',linestyle='-')
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('total frames size (MB)', fontsize=12)
            plt.title("{} total size of frames of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_size_of_frames.png'.format(folderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### Line Graph 2 ####################
    # Line Graph for total frame sizes for different time durations from HMD traces folder (each data type will be in a graph)
    for duration in durations:
        for j in range(len(labels)):
            firstFrame = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0]) if j not in [1,2] else flowDirectionsLists[0].__getitem__(j)[0]
            for i in range(len(flowDirections)):
                if(i == 1 and j in [1,2]):
                        continue
                folderPath = "{}/{}".format(prefix,labels[j])
                try:
                    os.mkdir(folderPath)
                except:
                    pass
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfTotalSizesOfFrames = computeTotalSize(newTimes,listOfFrameSizes[i].__getitem__(j),duration)
                x = newTimesPeriods
                y = listOfTotalSizesOfFrames
                yLabel = '{}'.format(flowDirections[i]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[i]),marker = '.',linestyle='-')
                
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('total frames size (MB)', fontsize=12)
            plt.title("{} total size of frames of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_size_of_frames.png'.format(folderPath,labels[j],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################


    #################### Line Graph 3 ####################
    # Line Graph for total frame sizes for all the frames from all data types for different time durations from HMD traces folder
    folderPath = "{}/{}".format(prefix,"all_data_types")
    try:
        os.mkdir(folderPath)
    except:
        pass
    try:
        listOfFolders = ["DMR","DR","DM","D","R"]
        for tempFolder in listOfFolders:
            os.mkdir("{}/{}".format(folderPath,tempFolder))
    except:
        pass
        
    for duration in durations: 
        # [D+M+R] all data frames + all management frames + all re-transmitted frames (lists suffix 1) 
        uniqueDataCombinedLists_1,retransmittedDataCombinedLists_1 = combinedResultsLists(results,1)
        HMD_UP_NBs_1,HMD_UP_Times_1,HMD_UP_DataRates_1,HMD_UP_Data_Sizes_1,HMD_UP_Frames_Sizes_1,HMD_UP_Frames_SeqNB_1,HMD_DWN_NBs_1,HMD_DWN_Times_1,HMD_DWN_DataRates_1,HMD_DWN_Data_Sizes_1,HMD_DWN_Frames_Sizes_1,HMD_DWN_Frames_SeqNB_1 = uniqueDataCombinedLists_1
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_1[0],HMD_UP_Times_1)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeTotalSize(newTimesX1,[float(x)/(1024**2) for x in HMD_UP_Frames_Sizes_1],duration)
        x1 = newTimesPeriodsX1
        y1 = listOfTotalSizesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_1[0],HMD_DWN_Times_1)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeTotalSize(newTimesX2,[float(x)/(1024**2) for x in HMD_DWN_Frames_Sizes_1],duration)
        x2 = newTimesPeriodsX2
        y2 = listOfTotalSizesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('total frames size (MB)', fontsize=12)
        plt.title("DMR frames total size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DMR/{}_size_of_frames.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D+R] all data frames + all re-transmitted frames (lists suffix 2) 
        uniqueDataCombinedLists_2,retransmittedDataCombinedLists_2 = combinedResultsLists(results,0)
        HMD_UP_NBs_2,HMD_UP_Times_2,HMD_UP_DataRates_2,HMD_UP_Data_Sizes_2,HMD_UP_Frames_Sizes_2,HMD_UP_Frames_SeqNB_2,HMD_DWN_NBs_2,HMD_DWN_Times_2,HMD_DWN_DataRates_2,HMD_DWN_Data_Sizes_2,HMD_DWN_Frames_Sizes_2,HMD_DWN_Frames_SeqNB_2 = uniqueDataCombinedLists_2
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_2[0],HMD_UP_Times_2)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeTotalSize(newTimesX1,[float(x)/(1024**2) for x in HMD_UP_Frames_Sizes_2],duration)
        x1 = newTimesPeriodsX1
        y1 = listOfTotalSizesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_2[0],HMD_DWN_Times_2)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeTotalSize(newTimesX2,[float(x)/(1024**2) for x in HMD_DWN_Frames_Sizes_2],duration)
        x2 = newTimesPeriodsX2
        y2 = listOfTotalSizesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('total frames size (MB)', fontsize=12)
        plt.title("DR frames total size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DR/{}_size_of_frames.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D+M] all data frames + all management frames (lists suffix 3) 
        uniqueDataCombinedLists_3,retransmittedDataCombinedLists_3 = combinedResultsListsNoReTransmittedFrames(results,1)
        HMD_UP_NBs_3,HMD_UP_Times_3,HMD_UP_DataRates_3,HMD_UP_Data_Sizes_3,HMD_UP_Frames_Sizes_3,HMD_UP_Frames_SeqNB_3,HMD_DWN_NBs_3,HMD_DWN_Times_3,HMD_DWN_DataRates_3,HMD_DWN_Data_Sizes_3,HMD_DWN_Frames_Sizes_3,HMD_DWN_Frames_SeqNB_3 = uniqueDataCombinedLists_3
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_3[0],HMD_UP_Times_3)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeTotalSize(newTimesX1,[float(x)/(1024**2) for x in HMD_UP_Frames_Sizes_3],duration)
        x1 = newTimesPeriodsX1
        y1 = listOfTotalSizesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_3[0],HMD_DWN_Times_3)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeTotalSize(newTimesX2,[float(x)/(1024**2) for x in HMD_DWN_Frames_Sizes_3],duration)
        x2 = newTimesPeriodsX2
        y2 = listOfTotalSizesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('total frames size (MB)', fontsize=12)
        plt.title("DM frames total size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DM/{}_size_of_frames.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D] all data frames (lists suffix 4) 
        uniqueDataCombinedLists_4,retransmittedDataCombinedLists_4 = combinedResultsListsNoReTransmittedFrames(results,0)
        HMD_UP_NBs_3,HMD_UP_Times_4,HMD_UP_DataRates_4,HMD_UP_Data_Sizes_4,HMD_UP_Frames_Sizes_4,HMD_UP_Frames_SeqNB_4,HMD_DWN_NBs_4,HMD_DWN_Times_4,HMD_DWN_DataRates_4,HMD_DWN_Data_Sizes_4,HMD_DWN_Frames_Sizes_4,HMD_DWN_Frames_SeqNB_4 = uniqueDataCombinedLists_4
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_4[0],HMD_UP_Times_4)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeTotalSize(newTimesX1,[float(x)/(1024**2) for x in HMD_UP_Frames_Sizes_4],duration)
        x1 = newTimesPeriodsX1
        y1 = listOfTotalSizesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_4[0],HMD_DWN_Times_4)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeTotalSize(newTimesX2,[float(x)/(1024**2) for x in HMD_DWN_Frames_Sizes_4],duration)
        x2 = newTimesPeriodsX2
        y2 = listOfTotalSizesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('total frames size (MB)', fontsize=12)
        plt.title("D frames total size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/D/{}_size_of_frames.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [R] all re-transmitted frames (lists suffix 5)
        HMD_UP_RE_NBs_5,HMD_UP_RE_Times_5,HMD_UP_RE_DataRates_5,HMD_UP_RE_Data_Sizes_5,HMD_UP_RE_Frames_Sizes_5,HMD_UP_RE_Frames_SeqNB_5,HMD_DWN_RE_NBs_5,HMD_DWN_RE_Times_5,HMD_DWN_RE_DataRates_5,HMD_DWN_RE_Data_Sizes_5,HMD_DWN_RE_Frames_Sizes_5,HMD_DWN_RE_Frames_SeqNB_5 = retransmittedDataCombinedLists_1
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_RE_Times_5[0],HMD_UP_RE_Times_5)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeTotalSize(newTimesX1,[float(x)/(1024**2) for x in HMD_UP_RE_Frames_Sizes_5],duration)
        x1 = newTimesPeriodsX1
        y1 = listOfTotalSizesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_RE_Times_5[0],HMD_DWN_RE_Times_5)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeTotalSize(newTimesX2,[float(x)/(1024**2) for x in HMD_DWN_RE_Frames_Sizes_5],duration)
        x2 = newTimesPeriodsX2
        y2 = listOfTotalSizesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('total frames size (MB)', fontsize=12)
        plt.title("R frames total size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/R/{}_size_of_frames.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()
        ######################################################



    #################### CDF  Graph 1 ####################
    # CDF Graph for instantaneous rates for different time durations from HMD traces folder (each direction will be in a graph)
    for duration in durations:
        for i in range(len(flowDirections)):
            folderPath = "{}/{}".format(prefix,flowDirections[i])
            try:
                os.mkdir(folderPath)
            except:
                pass
            firstFrame = min(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1)[0] if i==0 else 100000000,flowDirectionsLists[i].__getitem__(2)[0] if i == 0 else 100000000,flowDirectionsLists[i].__getitem__(3)[0],
                            flowDirectionsLists[i].__getitem__(4)[0],flowDirectionsLists[i].__getitem__(5)[0],flowDirectionsLists[i].__getitem__(6)[0])
            for j in range(len(flowDirectionsLists[i])):
                if(i == 1 and j in [1,2]):
                    continue
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfTotalSizesOfFrames = computeTotalSize(newTimes,listOfFrameSizes[i].__getitem__(j),duration)
                data = [float(value) for value in listOfTotalSizesOfFrames]
                x = np.sort(data)
                y = np.arange(len(x))/float(len(x))
                yLabel = '{}'.format(labels[j]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[j]),linestyle='{}'.format(lineStyles[j]))
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('total frames size (MB)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF {} frames total size of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_size_of_frames_CDF.png'.format(folderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### CDF  Graph 2 ####################
    # CDF Graph for total frame sizes for different time durations from HMD traces folder (each data type will be in a graph)
    for duration in durations:
        for j in range(len(labels)):
            firstFrame = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0]) if j not in [1,2] else flowDirectionsLists[0].__getitem__(j)[0]
            for i in range(len(flowDirections)):
                if(i == 1 and j in [1,2]):
                        continue
                folderPath = "{}/{}".format(prefix,labels[j])
                try:
                    os.mkdir(folderPath)
                except:
                    pass
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfTotalSizesOfFrames = computeTotalSize(newTimes,listOfFrameSizes[i].__getitem__(j),duration)
                data = [float(value) for value in listOfTotalSizesOfFrames]
                x = np.sort(data)
                y = np.arange(len(x))/float(len(x))
                yLabel = '{}'.format(flowDirections[i]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[i]),linestyle='{}'.format(lineStyles[i]))
                
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('total frames size (MB)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF of {} frames total size of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_size_of_frames_CDF.png'.format(folderPath,labels[j],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################


    #################### CDF  Graph 3 ####################
    # CDF Graph for total frame sizes for all the frames from all data types for different time durations from HMD traces folder
    folderPath = "{}/{}".format(prefix,"all_data_types")
    try:
        os.mkdir(folderPath)
    except:
        pass
    try:
        listOfFolders = ["DMR","DR","DM","D","R"]
        for tempFolder in listOfFolders:
            os.mkdir("{}/{}".format(folderPath,tempFolder))
    except:
        pass
    for duration in durations: 
        # [D+M+R] all data frames + all management frames + all re-transmitted frames (lists suffix 1) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_1[0],HMD_UP_Times_1)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeTotalSize(newTimesX1,[float(x)/(1024**2) for x in HMD_UP_Frames_Sizes_1],duration)
        data1 = [float(value) for value in listOfTotalSizesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_1[0],HMD_DWN_Times_1)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeTotalSize(newTimesX2,[float(x)/(1024**2) for x in HMD_DWN_Frames_Sizes_1],duration)
        data2 = [float(value) for value in listOfTotalSizesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('total frames size (MB)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of DMR frames total size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DMR/{}_size_of_frames_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D+R] all data frames + all re-transmitted frames (lists suffix 2) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_2[0],HMD_UP_Times_2)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeTotalSize(newTimesX1,[float(x)/(1024**2) for x in HMD_UP_Frames_Sizes_2],duration)
        data1 = [float(value) for value in listOfTotalSizesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_2[0],HMD_DWN_Times_2)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeTotalSize(newTimesX2,[float(x)/(1024**2) for x in HMD_DWN_Frames_Sizes_2],duration)
        data2 = [float(value) for value in listOfTotalSizesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('total frames size (MB)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of DR frames total size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DR/{}_size_of_frames_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D+M] all data frames + all management frames (lists suffix 3) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_3[0],HMD_UP_Times_3)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeTotalSize(newTimesX1,[float(x)/(1024**2) for x in HMD_UP_Frames_Sizes_3],duration)
        data1 = [float(value) for value in listOfTotalSizesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_3[0],HMD_DWN_Times_3)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeTotalSize(newTimesX2,[float(x)/(1024**2) for x in HMD_DWN_Frames_Sizes_3],duration)
        data2 = [float(value) for value in listOfTotalSizesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('total frames size (MB)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of DM frames total size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DM/{}_size_of_frames_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D] all data frames (lists suffix 4) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_4[0],HMD_UP_Times_4)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeTotalSize(newTimesX1,[float(x)/(1024**2) for x in HMD_UP_Frames_Sizes_4],duration)
        data1 = [float(value) for value in listOfTotalSizesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_4[0],HMD_DWN_Times_4)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeTotalSize(newTimesX2,[float(x)/(1024**2) for x in HMD_DWN_Frames_Sizes_4],duration)
        data2 = [float(value) for value in listOfTotalSizesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('total frames size (MB)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of D frames total size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/D/{}_size_of_frames_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [R] all re-transmitted frames (lists suffix 5)
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_RE_Times_5[0],HMD_UP_RE_Times_5)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeTotalSize(newTimesX1,[float(x)/(1024**2) for x in HMD_UP_RE_Frames_Sizes_5],duration)
        data1 = [float(value) for value in listOfTotalSizesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_RE_Times_5[0],HMD_DWN_RE_Times_5)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeTotalSize(newTimesX2,[float(x)/(1024**2) for x in HMD_DWN_RE_Frames_Sizes_5],duration)
        data2 = [float(value) for value in listOfTotalSizesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('total frames size (MB)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of R frames total size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/R/{}_size_of_frames_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()
        ######################################################



def plotServerSizeofData(root_folder,gameName,results):
    result_folder_name = "server/size_of_data"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    
    try:
        os.mkdir(prefix)
    except:
        pass


    server_UP_BOTH_NBs,server_UP_BOTH_Times,server_UP_BOTH_Data_Sizes,server_UP_BOTH_Frames_Sizes,server_UP_TCP_NBs,\
        server_UP_TCP_Times,server_UP_TCP_Data_Sizes,server_UP_TCP_Frames_Sizes,server_UP_UDP_NBs,server_UP_UDP_Times,\
        server_UP_UDP_Data_Sizes,server_UP_UDP_Frames_Sizes,server_DWN_BOTH_NBs,server_DWN_BOTH_Times,server_DWN_BOTH_Data_Sizes,\
        server_DWN_BOTH_Frames_Sizes,server_DWN_TCP_NBs,server_DWN_TCP_Times,server_DWN_TCP_Data_Sizes,server_DWN_TCP_Frames_Sizes,\
        server_DWN_UDP_NBs,server_DWN_UDP_Times,server_DWN_UDP_Data_Sizes,server_DWN_UDP_Frames_Sizes = results     

    #################### Line Graph ####################
    # line graph for size of frames for all frames from server.csv trace
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(server_UP_BOTH_Times,server_UP_UDP_Times,server_UP_TCP_Times),
                            (server_DWN_BOTH_Times,server_DWN_UDP_Times,server_DWN_TCP_Times)]
    listOfFrameSizes = [(server_UP_BOTH_Data_Sizes,server_UP_UDP_Data_Sizes,server_UP_TCP_Data_Sizes),
                        (server_DWN_BOTH_Data_Sizes,server_DWN_UDP_Data_Sizes,server_DWN_TCP_Data_Sizes)]
    protocols = ["Both","UDP","TCP"]
    colors = ['red','blue','green']
    NBofFrames = 50
    plotStartTime = 50 # It starts at the specified second
    for i in range(len(flowDirections)):
        protocolIndex = 0
        for protocol in protocols:
            newTimes = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(protocolIndex)[0],flowDirectionsLists[i].__getitem__(protocolIndex))
            newTimesSec = [float(x)/1000 for x in newTimes]
            timesOfFrames = []
            sizeOfFrames = []
            counter = 0
            for j in range(len(newTimesSec)):
                if(newTimesSec[j]>=plotStartTime):
                    timesOfFrames.append(newTimesSec[j])
                    sizeOfFrames.append(float(listOfFrameSizes[i].__getitem__(protocolIndex)[j]))
                    counter = counter + 1
                    if counter>=NBofFrames:
                        break
            x = timesOfFrames
            y = sizeOfFrames
            yLabel = '{}'.format(protocol)   
            plt.plot(x,y,label=yLabel,c='{}'.format(colors[protocolIndex]),marker = '.',linestyle='-')
            protocolIndex = protocolIndex + 1
   
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('data size (Bytes)', fontsize=12)
        plt.title("{} size of data of {} for {} frames starting from the second {}".format(flowDirections[i],gameName,NBofFrames,plotStartTime),fontsize="9")
        plt.savefig('{}/{}_sizes_of_all_data.png'.format(prefix,flowDirections[i]),dpi=saved_graph_resolution)
        plt.show()
    ####################################################



    #################### Line Graph ####################
    # line graph for size of frames for all frames from server.csv trace (separate protocols)
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(server_UP_BOTH_Times,server_UP_UDP_Times,server_UP_TCP_Times),
                            (server_DWN_BOTH_Times,server_DWN_UDP_Times,server_DWN_TCP_Times)]
    listOfFrameSizes = [(server_UP_BOTH_Data_Sizes,server_UP_UDP_Data_Sizes,server_UP_TCP_Data_Sizes),
                        (server_DWN_BOTH_Data_Sizes,server_DWN_UDP_Data_Sizes,server_DWN_TCP_Data_Sizes)]
    protocols = ["Both","UDP","TCP"]
    colors = ['red','blue','green']
    NBofFrames = 50
    plotStartTime = 50 # It starts at the specified second
    for i in range(len(flowDirections)):
        protocolIndex = 0
        for protocol in protocols:
            newTimes = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(protocolIndex)[0],flowDirectionsLists[i].__getitem__(protocolIndex))
            newTimesSec = [float(x)/1000 for x in newTimes]
            timesOfFrames = []
            sizeOfFrames = []
            counter = 0
            for j in range(len(newTimesSec)):
                if(newTimesSec[j]>=plotStartTime):
                    timesOfFrames.append(newTimesSec[j])
                    sizeOfFrames.append(float(listOfFrameSizes[i].__getitem__(protocolIndex)[j]))
                    counter = counter + 1
                    if counter>=NBofFrames:
                        break

            x1 = timesOfFrames
            y1 = sizeOfFrames
            y1Label = '{}'.format(protocol)   
            plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[protocolIndex]),marker = '.',linestyle='-')
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('frame size (Bytes)', fontsize=12)
            plt.title("{} size of {} data of {} for {} frames starting from the second {}".format(flowDirections[i],protocol,gameName,NBofFrames,plotStartTime),fontsize=9)
            plt.savefig('{}/{}_sizes_of_{}_data.png'.format(prefix,flowDirections[i],protocol),dpi=saved_graph_resolution)
            plt.show()
            protocolIndex = protocolIndex + 1
   

    ####################################################



    #################### Line Graph ####################
    # line graph for size of frames for different time durations from server.csv trace
    durations = [1,10,15,30,60]  # in seconds
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(server_UP_BOTH_Times,server_UP_UDP_Times,server_UP_TCP_Times),
                            (server_DWN_BOTH_Times,server_DWN_UDP_Times,server_DWN_TCP_Times)]
    listOfFrameSizes = [([float(x)/(1024**2) for x in server_UP_BOTH_Data_Sizes],[float(x)/(1024**2) for x in server_UP_UDP_Data_Sizes]
                        ,[float(x)/(1024**2) for x in server_UP_TCP_Data_Sizes]),([float(x)/(1024**2) for x in server_DWN_BOTH_Data_Sizes]
                        ,[float(x)/(1024**2) for x in server_DWN_UDP_Data_Sizes],[float(x)/(1024**2) for x in server_DWN_TCP_Data_Sizes])]
    
    
    for duration in durations:
        for i in range(len(flowDirections)):
            newTimesBoth = relativeTime(flowDirectionsLists[i].__getitem__(0))
            newTimesPeriodsBoth = convertTimeToPeriods(newTimesBoth,duration)
            totalSizeOfFramesBoth = computeTotalSize(newTimesBoth,listOfFrameSizes[i].__getitem__(0),duration)
            newTimesUDP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1))
            newTimesPeriodsUDP = convertTimeToPeriods(newTimesUDP,duration)
            totalSizeOfFramesUDP = computeTotalSize(newTimesUDP,listOfFrameSizes[i].__getitem__(1),duration)
            newTimesTCP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(2))
            newTimesPeriodsTCP = convertTimeToPeriods(newTimesTCP,duration)
            totalSizeOfFramesTCP = computeTotalSize(newTimesTCP,listOfFrameSizes[i].__getitem__(2),duration)
            x1 = newTimesPeriodsBoth
            y1 = totalSizeOfFramesBoth
            y1Label = 'Both'
            x2 = newTimesPeriodsUDP
            y2 = totalSizeOfFramesUDP
            y2Label = 'UDP'
            x3 = newTimesPeriodsTCP
            y3 = totalSizeOfFramesTCP
            y3Label = 'TCP'      
            plt.plot(x1,y1,label=y1Label,c='red',marker = '.',linestyle='-')
            plt.plot(x2,y2,label=y2Label,c='blue',marker = '.',linestyle='-')
            plt.plot(x3,y3,label=y3Label,c='green',marker = '.',linestyle='-')
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('total data size (MB)', fontsize=12)
            plt.title("{} total size data of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=9)
            plt.savefig('{}/{}_duration_{}_size_of_data.png'.format(prefix,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ####################################################



    #################### CDF  Graph ####################
    # CDF Graph for size of frames for different time durations from server.csv trace
    for duration in durations:
        for i in range(len(flowDirections)):    
            newTimesBoth = relativeTime(flowDirectionsLists[i].__getitem__(0))
            newTimesPeriodsBoth = convertTimeToPeriods(newTimesBoth,duration)
            totalSizeOfFramesBoth = computeTotalSize(newTimesBoth,listOfFrameSizes[i].__getitem__(0),duration)
            newTimesUDP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1))
            newTimesPeriodsUDP = convertTimeToPeriods(newTimesUDP,duration)
            totalSizeOfFramesUDP = computeTotalSize(newTimesUDP,listOfFrameSizes[i].__getitem__(1),duration)
            newTimesTCP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(2))
            newTimesPeriodsTCP = convertTimeToPeriods(newTimesTCP,duration)
            totalSizeOfFramesTCP = computeTotalSize(newTimesTCP,listOfFrameSizes[i].__getitem__(2),duration)
            
            data1 = [float(i) for i in totalSizeOfFramesBoth]
            data2 = [float(i) for i in totalSizeOfFramesUDP]
            data3 = [float(i) for i in totalSizeOfFramesTCP]
            
            x1 = np.sort(data1)
            x2 = np.sort(data2)
            x3 = np.sort(data3)

            y1 = np.arange(len(x1))/float(len(x1))
            y2 = np.arange(len(x2))/float(len(x2))
            y3 = np.arange(len(x3))/float(len(x3))

            y1Label =  'Both'
            y2Label =  'UDP'
            y3Label =  'TCP'

            plt.plot(x1, y1,label=y1Label,c='red',linestyle='-.')
            plt.plot(x2, y2,label=y2Label,c='blue',linestyle=':')
            plt.plot(x3, y3,label=y3Label,c='green',linestyle='--')

            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('total data size (MB)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF {} size of data of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=9)
            plt.savefig('{}/{}_duration_{}_sizs_of_data_CDF.png'.format(prefix,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ####################################################



def plotHMDSizeofData(root_folder,gameName,results):
    result_folder_name = "HMD/size_of_data"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    
    try:
        os.mkdir(prefix)
    except:
        pass

    HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates,\
        HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes, HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times,\
        HMD_DWN_MANAGEMENT_FRAMES_DataRates, HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes, HMD_UP_DATA1_FRAMES_NBs, \
        HMD_UP_DATA1_FRAMES_Times, HMD_UP_DATA1_FRAMES_DataRates, HMD_UP_DATA1_FRAMES_Frames_Sizes,\
        HMD_UP_DATA1_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA1_FRAMES_NBs, HMD_UP_RE_DATA1_FRAMES_Times, \
        HMD_UP_RE_DATA1_FRAMES_DataRates, HMD_UP_RE_DATA1_FRAMES_Frames_Sizes, HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB,\
        HMD_UP_DATA2_FRAMES_NBs, HMD_UP_DATA2_FRAMES_Times, HMD_UP_DATA2_FRAMES_DataRates, HMD_UP_DATA2_FRAMES_Data_Sizes,\
        HMD_UP_DATA2_FRAMES_Frames_Sizes, HMD_UP_DATA2_FRAMES_Frames_SeqNB, HMD_DWN_DATA2_FRAMES_NBs, HMD_DWN_DATA2_FRAMES_Times, \
        HMD_DWN_DATA2_FRAMES_DataRates, HMD_DWN_DATA2_FRAMES_Data_Sizes, HMD_DWN_DATA2_FRAMES_Frames_Sizes, \
        HMD_DWN_DATA2_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA2_FRAMES_NBs, HMD_UP_RE_DATA2_FRAMES_Times, HMD_UP_RE_DATA2_FRAMES_DataRates,\
        HMD_UP_RE_DATA2_FRAMES_Data_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB, \
        HMD_DWN_RE_DATA2_FRAMES_NBs, HMD_DWN_RE_DATA2_FRAMES_Times, HMD_DWN_RE_DATA2_FRAMES_DataRates, HMD_DWN_RE_DATA2_FRAMES_Data_Sizes,\
        HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB, HMD_UP_DATA3_FRAMES_NBs, HMD_UP_DATA3_FRAMES_Times, \
        HMD_UP_DATA3_FRAMES_DataRates, HMD_UP_DATA3_FRAMES_Data_Sizes, HMD_UP_DATA3_FRAMES_Frames_Sizes, HMD_UP_DATA3_FRAMES_Frames_SeqNB,\
        HMD_DWN_DATA3_FRAMES_NBs, HMD_DWN_DATA3_FRAMES_Times, HMD_DWN_DATA3_FRAMES_DataRates, HMD_DWN_DATA3_FRAMES_Data_Sizes,\
        HMD_DWN_DATA3_FRAMES_Frames_Sizes, HMD_DWN_DATA3_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA3_FRAMES_NBs, HMD_UP_RE_DATA3_FRAMES_Times, \
        HMD_UP_RE_DATA3_FRAMES_DataRates, HMD_UP_RE_DATA3_FRAMES_Data_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_Sizes, \
        HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB, HMD_DWN_RE_DATA3_FRAMES_NBs, HMD_DWN_RE_DATA3_FRAMES_Times, HMD_DWN_RE_DATA3_FRAMES_DataRates, \
        HMD_DWN_RE_DATA3_FRAMES_Data_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB = results 
    

    durations = [1,10,15,30,60]  # in seconds
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(HMD_UP_DATA2_FRAMES_Times,HMD_UP_RE_DATA2_FRAMES_Times,HMD_UP_DATA3_FRAMES_Times,HMD_UP_RE_DATA3_FRAMES_Times),
                            (HMD_DWN_DATA2_FRAMES_Times,HMD_DWN_RE_DATA2_FRAMES_Times,HMD_DWN_DATA3_FRAMES_Times,HMD_DWN_RE_DATA3_FRAMES_Times)]
    listOfDataSizes = [([float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_UP_DATA2_FRAMES_Data_Sizes],[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_UP_RE_DATA2_FRAMES_Data_Sizes],[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_UP_DATA3_FRAMES_Data_Sizes],[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_UP_RE_DATA3_FRAMES_Data_Sizes]),
                        ([float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_DWN_DATA2_FRAMES_Data_Sizes],[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_DWN_RE_DATA2_FRAMES_Data_Sizes],[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_DWN_DATA3_FRAMES_Data_Sizes],[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_DWN_RE_DATA3_FRAMES_Data_Sizes])]
    colors = ["black","purple","cyan","pink"]
    lineStyles = ["-",'-.',':',"--"]
    markers = [".",",","1","x"]
    labels = ["data type2","retransmitted data type2","data type3","retransmitted data type3"]


    #################### Line Graph 1 ####################
    # Line Graph for total size of data for different time durations from HMD traces folder (each direction will be in a graph)
    for duration in durations:
        for i in range(len(flowDirections)):
            folderPath = "{}/{}".format(prefix,flowDirections[i])
            try:
                os.mkdir(folderPath)
            except:
                pass
            firstFrame = min(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1)[0],flowDirectionsLists[i].__getitem__(2)[0],flowDirectionsLists[i].__getitem__(3)[0])
            for j in range(len(flowDirectionsLists[i])):
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfTotalSizesOfData = computeTotalSize(newTimes,listOfDataSizes[i].__getitem__(j),duration)
                x = newTimesPeriods
                y = listOfTotalSizesOfData
                yLabel = '{}'.format(labels[j]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[j]),marker = '.',linestyle='-')
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('total data size (MB)', fontsize=12)
            plt.title("{} total size of data of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_size_of_data.png'.format(folderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### Line Graph 2 ####################
    # Line Graph for total size of data for different time durations from HMD traces folder (each data type will be in a graph)
    for duration in durations:
        for j in range(len(labels)):
            firstFrame = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0])
            for i in range(len(flowDirections)):
                folderPath = "{}/{}".format(prefix,labels[j])
                try:
                    os.mkdir(folderPath)
                except:
                    pass
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfTotalSizesOfData = computeTotalSize(newTimes,listOfDataSizes[i].__getitem__(j),duration)
                x = newTimesPeriods
                y = listOfTotalSizesOfData
                yLabel = '{}'.format(flowDirections[i]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[i]),marker = '.',linestyle='-')
                
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('total data size (MB)', fontsize=12)
            plt.title("{} total size of data of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_size_of_data.png'.format(folderPath,labels[j],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################


    #################### Line Graph 3 ####################
    # Line Graph for total size of data for all the frames from all data types for different time durations from HMD traces folder
    folderPath = "{}/{}".format(prefix,"all_data_types")
    try:
        os.mkdir(folderPath)
    except:
        pass
    try:
        listOfFolders = ["DR","D","R"]
        for tempFolder in listOfFolders:
            os.mkdir("{}/{}".format(folderPath,tempFolder))
    except:
        pass
    for duration in durations: 
        # [D+R] all data frames + all re-transmitted frames (lists suffix 1) 
        uniqueDataCombinedLists_1,retransmittedDataCombinedLists_1 = combinedResultsLists(results,0)
        HMD_UP_NBs_1,HMD_UP_Times_1,HMD_UP_DataRates_1,HMD_UP_Data_Sizes_1,HMD_UP_Frames_Sizes_1,HMD_UP_Frames_SeqNB_1,HMD_DWN_NBs_1,HMD_DWN_Times_1,HMD_DWN_DataRates_1,HMD_DWN_Data_Sizes_1,HMD_DWN_Frames_Sizes_1,HMD_DWN_Frames_SeqNB_1 = uniqueDataCombinedLists_1
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_1[0],HMD_UP_Times_1)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfDataY1 = computeTotalSize(newTimesX1,[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_UP_Data_Sizes_1],duration)
        x1 = newTimesPeriodsX1
        y1 = listOfTotalSizesOfDataY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_1[0],HMD_DWN_Times_1)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfDataY2 = computeTotalSize(newTimesX2,[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_DWN_Data_Sizes_1],duration)
        x2 = newTimesPeriodsX2
        y2 = listOfTotalSizesOfDataY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('total data size (MB)', fontsize=12)
        plt.title("DR total size of data of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DR/{}_size_of_data.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D] all data frames (lists suffix 2) 
        uniqueDataCombinedLists_2,retransmittedDataCombinedLists_2 = combinedResultsListsNoReTransmittedFrames(results,0)
        HMD_UP_NBs_2,HMD_UP_Times_2,HMD_UP_DataRates_2,HMD_UP_Data_Sizes_2,HMD_UP_Frames_Sizes_2,HMD_UP_Frames_SeqNB_2,HMD_DWN_NBs_2,HMD_DWN_Times_2,HMD_DWN_DataRates_2,HMD_DWN_Data_Sizes_2,HMD_DWN_Frames_Sizes_2,HMD_DWN_Frames_SeqNB_2 = uniqueDataCombinedLists_2
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_2[0],HMD_UP_Times_2)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfDataY1 = computeTotalSize(newTimesX1,[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_UP_Data_Sizes_2],duration)
        x1 = newTimesPeriodsX1
        y1 = listOfTotalSizesOfDataY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_2[0],HMD_DWN_Times_2)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfDataY2 = computeTotalSize(newTimesX2,[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_DWN_Data_Sizes_2],duration)
        x2 = newTimesPeriodsX2
        y2 = listOfTotalSizesOfDataY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('total data size (MB)', fontsize=12)
        plt.title("D total size of data of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/D/{}_size_of_data.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [R] all re-transmitted frames (lists suffix 3)
        HMD_UP_RE_NBs_3,HMD_UP_RE_Times_3,HMD_UP_RE_DataRates_3,HMD_UP_RE_Data_Sizes_3,HMD_UP_RE_Frames_Sizes_3,HMD_UP_RE_Frames_SeqNB_3,HMD_DWN_RE_NBs_3,HMD_DWN_RE_Times_3,HMD_DWN_RE_DataRates_3,HMD_DWN_RE_Data_Sizes_3,HMD_DWN_RE_Frames_Sizes_3,HMD_DWN_RE_Frames_SeqNB_3 = retransmittedDataCombinedLists_1
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_RE_Times_3[0],HMD_UP_RE_Times_3)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfDataY1 = computeTotalSize(newTimesX1,[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_UP_RE_Data_Sizes_3],duration)
        x1 = newTimesPeriodsX1
        y1 = listOfTotalSizesOfDataY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_RE_Times_3[0],HMD_DWN_RE_Times_3)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfDataY2 = computeTotalSize(newTimesX2,[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_DWN_RE_Data_Sizes_3],duration)
        x2 = newTimesPeriodsX2
        y2 = listOfTotalSizesOfDataY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('total data size (MB)', fontsize=12)
        plt.title("R total size of data of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/R/{}_size_of_data.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()
        ######################################################



    #################### CDF  Graph 1 ####################
    # CDF Graph for total size of data for different time durations from HMD traces folder (each direction will be in a graph)
    for duration in durations:
        for i in range(len(flowDirections)):
            folderPath = "{}/{}".format(prefix,flowDirections[i])
            try:
                os.mkdir(folderPath)
            except:
                pass
            firstFrame = min(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1)[0],flowDirectionsLists[i].__getitem__(2)[0],flowDirectionsLists[i].__getitem__(3)[0])
            for j in range(len(flowDirectionsLists[i])):
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfTotalSizesOfData = computeTotalSize(newTimes,listOfDataSizes[i].__getitem__(j),duration)
                data = [float(value) for value in listOfTotalSizesOfData]
                x = np.sort(data)
                y = np.arange(len(x))/float(len(x))
                yLabel = '{}'.format(labels[j]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[j]),linestyle='{}'.format(lineStyles[j]))
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('total data size (MB)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF {} total size of data of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_size_of_data_CDF.png'.format(folderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### CDF  Graph 2 ####################
    # CDF Graph for total size of data for different time durations from HMD traces folder (each data type will be in a graph)
    for duration in durations:
        for j in range(len(labels)):
            firstFrame = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0])
            for i in range(len(flowDirections)):
                folderPath = "{}/{}".format(prefix,labels[j])
                try:
                    os.mkdir(folderPath)
                except:
                    pass
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfTotalSizesOfData = computeTotalSize(newTimes,listOfDataSizes[i].__getitem__(j),duration)
                data = [float(value) for value in listOfTotalSizesOfData]
                x = np.sort(data)
                y = np.arange(len(x))/float(len(x))
                yLabel = '{}'.format(flowDirections[i]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[i]),linestyle='{}'.format(lineStyles[i]))
                
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('total data size (MB)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF of {} total size of data of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_size_of_data_CDF.png'.format(folderPath,labels[j],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################


    #################### CDF  Graph 3 ####################
    # CDF Graph for total size of data for all the frames from all data types for different time durations from HMD traces folder
    folderPath = "{}/{}".format(prefix,"all_data_types")
    try:
        os.mkdir(folderPath)
    except:
        pass
    try:
        listOfFolders = ["DR","D","R"]
        for tempFolder in listOfFolders:
            os.mkdir("{}/{}".format(folderPath,tempFolder))
    except:
        pass
    for duration in durations: 
        # [D+R] all data frames + all re-transmitted frames (lists suffix 1) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_1[0],HMD_UP_Times_1)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfDataY1 = computeTotalSize(newTimesX1,[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_UP_Data_Sizes_1],duration)
        data1 = [float(value) for value in listOfTotalSizesOfDataY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_1[0],HMD_DWN_Times_1)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfDataY2 = computeTotalSize(newTimesX2,[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_DWN_Data_Sizes_1],duration)
        data2 = [float(value) for value in listOfTotalSizesOfDataY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('total data size (MB)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of DR total size of data of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DR/{}_size_of_data_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D] all data frames (lists suffix 2) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_2[0],HMD_UP_Times_2)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfDataY1 = computeTotalSize(newTimesX1,[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_UP_Data_Sizes_2],duration)
        data1 = [float(value) for value in listOfTotalSizesOfDataY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_2[0],HMD_DWN_Times_2)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfDataY2 = computeTotalSize(newTimesX2,[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_DWN_Data_Sizes_2],duration)
        data2 = [float(value) for value in listOfTotalSizesOfDataY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('total data size (MB)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of D total size of data of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/D/{}_size_of_data_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [R] all data frames + all management frames (lists suffix 3) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_RE_Times_3[0],HMD_UP_RE_Times_3)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfDataY1 = computeTotalSize(newTimesX1,[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_UP_RE_Data_Sizes_3],duration)
        data1 = [float(value) for value in listOfTotalSizesOfDataY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_RE_Times_3[0],HMD_DWN_RE_Times_3)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfDataY2 = computeTotalSize(newTimesX2,[float(0) if x == '' else (float(x)/(1024**2)) for x in HMD_DWN_RE_Data_Sizes_3],duration)
        data2 = [float(value) for value in listOfTotalSizesOfDataY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('total data size (MB)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of R total size of data of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/R/{}_size_of_data_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()
        ######################################################



def plotServerAVGSizeofFrames(root_folder,gameName,results):
    result_folder_name = "server/avg_size_of_frames"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    
    try:
        os.mkdir(prefix)
    except:
        pass


    server_UP_BOTH_NBs,server_UP_BOTH_Times,server_UP_BOTH_Data_Sizes,server_UP_BOTH_Frames_Sizes,server_UP_TCP_NBs,\
        server_UP_TCP_Times,server_UP_TCP_Data_Sizes,server_UP_TCP_Frames_Sizes,server_UP_UDP_NBs,server_UP_UDP_Times,\
        server_UP_UDP_Data_Sizes,server_UP_UDP_Frames_Sizes,server_DWN_BOTH_NBs,server_DWN_BOTH_Times,server_DWN_BOTH_Data_Sizes,\
        server_DWN_BOTH_Frames_Sizes,server_DWN_TCP_NBs,server_DWN_TCP_Times,server_DWN_TCP_Data_Sizes,server_DWN_TCP_Frames_Sizes,\
        server_DWN_UDP_NBs,server_DWN_UDP_Times,server_DWN_UDP_Data_Sizes,server_DWN_UDP_Frames_Sizes = results     



    #################### Line Graph ####################
    # line graph for avg size of frames for different time durations from server.csv trace
    durations = [1,10,15,30,60]  # in seconds
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(server_UP_BOTH_Times,server_UP_UDP_Times,server_UP_TCP_Times),
                            (server_DWN_BOTH_Times,server_DWN_UDP_Times,server_DWN_TCP_Times)]
    listOfFrameSizes = [([float(x) for x in server_UP_BOTH_Frames_Sizes],[float(x) for x in server_UP_UDP_Frames_Sizes]
                        ,[float(x) for x in server_UP_TCP_Frames_Sizes]),([float(x) for x in server_DWN_BOTH_Frames_Sizes]
                        ,[float(x) for x in server_DWN_UDP_Frames_Sizes],[float(x) for x in server_DWN_TCP_Frames_Sizes])]
    
    
    for duration in durations:
        for i in range(len(flowDirections)):
            newTimesBoth = relativeTime(flowDirectionsLists[i].__getitem__(0))
            newTimesPeriodsBoth = convertTimeToPeriods(newTimesBoth,duration)
            avgSizeOfFramesBoth = computeAVGSize(newTimesBoth,listOfFrameSizes[i].__getitem__(0),duration)
            newTimesUDP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1))
            newTimesPeriodsUDP = convertTimeToPeriods(newTimesUDP,duration)
            avgSizeOfFramesUDP = computeAVGSize(newTimesUDP,listOfFrameSizes[i].__getitem__(1),duration)
            newTimesTCP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(2))
            newTimesPeriodsTCP = convertTimeToPeriods(newTimesTCP,duration)
            avgSizeOfFramesTCP = computeAVGSize(newTimesTCP,listOfFrameSizes[i].__getitem__(2),duration)
            x1 = newTimesPeriodsBoth
            y1 = avgSizeOfFramesBoth
            y1Label = 'Both'
            x2 = newTimesPeriodsUDP
            y2 = avgSizeOfFramesUDP
            y2Label = 'UDP'
            x3 = newTimesPeriodsTCP
            y3 = avgSizeOfFramesTCP
            y3Label = 'TCP'      
            plt.plot(x1,y1,label=y1Label,c='red',marker = '.',linestyle='-')
            plt.plot(x2,y2,label=y2Label,c='blue',marker = '.',linestyle='-')
            plt.plot(x3,y3,label=y3Label,c='green',marker = '.',linestyle='-')
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('avg frames size (bytes)', fontsize=12)
            plt.title("{} avg size of frames of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=9)
            plt.savefig('{}/{}_duration_{}_avg_size_of_frames.png'.format(prefix,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ####################################################



    #################### CDF  Graph ####################
    # CDF Graph for size of frames for different time durations from server.csv trace
    for duration in durations:
        for i in range(len(flowDirections)):    
            newTimesBoth = relativeTime(flowDirectionsLists[i].__getitem__(0))
            newTimesPeriodsBoth = convertTimeToPeriods(newTimesBoth,duration)
            avgSizeOfFramesBoth = computeAVGSize(newTimesBoth,listOfFrameSizes[i].__getitem__(0),duration)
            newTimesUDP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1))
            newTimesPeriodsUDP = convertTimeToPeriods(newTimesUDP,duration)
            avgSizeOfFramesUDP = computeAVGSize(newTimesUDP,listOfFrameSizes[i].__getitem__(1),duration)
            newTimesTCP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(2))
            newTimesPeriodsTCP = convertTimeToPeriods(newTimesTCP,duration)
            avgSizeOfFramesTCP = computeAVGSize(newTimesTCP,listOfFrameSizes[i].__getitem__(2),duration)
            
            data1 = [float(i) for i in avgSizeOfFramesBoth]
            data2 = [float(i) for i in avgSizeOfFramesUDP]
            data3 = [float(i) for i in avgSizeOfFramesTCP]
            
            x1 = np.sort(data1)
            x2 = np.sort(data2)
            x3 = np.sort(data3)

            y1 = np.arange(len(x1))/float(len(x1))
            y2 = np.arange(len(x2))/float(len(x2))
            y3 = np.arange(len(x3))/float(len(x3))

            y1Label =  'Both'
            y2Label =  'UDP'
            y3Label =  'TCP'

            plt.plot(x1, y1,label=y1Label,c='red',linestyle='-.')
            plt.plot(x2, y2,label=y2Label,c='blue',linestyle=':')
            plt.plot(x3, y3,label=y3Label,c='green',linestyle='--')

            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('avg frames size (bytes)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF {} avg size of frames of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=9)
            plt.savefig('{}/{}_duration_{}_avg_sizs_of_frames_CDF.png'.format(prefix,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ####################################################



def plotHMDAVGSizeofFrames(root_folder,gameName,results):
    result_folder_name = "HMD/avg_size_of_frames"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    
    try:
        os.mkdir(prefix)
    except:
        pass

    HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates,\
        HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes, HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times,\
        HMD_DWN_MANAGEMENT_FRAMES_DataRates, HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes, HMD_UP_DATA1_FRAMES_NBs, \
        HMD_UP_DATA1_FRAMES_Times, HMD_UP_DATA1_FRAMES_DataRates, HMD_UP_DATA1_FRAMES_Frames_Sizes,\
        HMD_UP_DATA1_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA1_FRAMES_NBs, HMD_UP_RE_DATA1_FRAMES_Times, \
        HMD_UP_RE_DATA1_FRAMES_DataRates, HMD_UP_RE_DATA1_FRAMES_Frames_Sizes, HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB,\
        HMD_UP_DATA2_FRAMES_NBs, HMD_UP_DATA2_FRAMES_Times, HMD_UP_DATA2_FRAMES_DataRates, HMD_UP_DATA2_FRAMES_Data_Sizes,\
        HMD_UP_DATA2_FRAMES_Frames_Sizes, HMD_UP_DATA2_FRAMES_Frames_SeqNB, HMD_DWN_DATA2_FRAMES_NBs, HMD_DWN_DATA2_FRAMES_Times, \
        HMD_DWN_DATA2_FRAMES_DataRates, HMD_DWN_DATA2_FRAMES_Data_Sizes, HMD_DWN_DATA2_FRAMES_Frames_Sizes, \
        HMD_DWN_DATA2_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA2_FRAMES_NBs, HMD_UP_RE_DATA2_FRAMES_Times, HMD_UP_RE_DATA2_FRAMES_DataRates,\
        HMD_UP_RE_DATA2_FRAMES_Data_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB, \
        HMD_DWN_RE_DATA2_FRAMES_NBs, HMD_DWN_RE_DATA2_FRAMES_Times, HMD_DWN_RE_DATA2_FRAMES_DataRates, HMD_DWN_RE_DATA2_FRAMES_Data_Sizes,\
        HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB, HMD_UP_DATA3_FRAMES_NBs, HMD_UP_DATA3_FRAMES_Times, \
        HMD_UP_DATA3_FRAMES_DataRates, HMD_UP_DATA3_FRAMES_Data_Sizes, HMD_UP_DATA3_FRAMES_Frames_Sizes, HMD_UP_DATA3_FRAMES_Frames_SeqNB,\
        HMD_DWN_DATA3_FRAMES_NBs, HMD_DWN_DATA3_FRAMES_Times, HMD_DWN_DATA3_FRAMES_DataRates, HMD_DWN_DATA3_FRAMES_Data_Sizes,\
        HMD_DWN_DATA3_FRAMES_Frames_Sizes, HMD_DWN_DATA3_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA3_FRAMES_NBs, HMD_UP_RE_DATA3_FRAMES_Times, \
        HMD_UP_RE_DATA3_FRAMES_DataRates, HMD_UP_RE_DATA3_FRAMES_Data_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_Sizes, \
        HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB, HMD_DWN_RE_DATA3_FRAMES_NBs, HMD_DWN_RE_DATA3_FRAMES_Times, HMD_DWN_RE_DATA3_FRAMES_DataRates, \
        HMD_DWN_RE_DATA3_FRAMES_Data_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB = results 
    

    durations = [1,10,15,30,60]  # in seconds
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(HMD_UP_MANAGEMENT_FRAMES_Times,HMD_UP_DATA1_FRAMES_Times,HMD_UP_RE_DATA1_FRAMES_Times,HMD_UP_DATA2_FRAMES_Times,HMD_UP_RE_DATA2_FRAMES_Times,HMD_UP_DATA3_FRAMES_Times,HMD_UP_RE_DATA3_FRAMES_Times),
                            (HMD_DWN_MANAGEMENT_FRAMES_Times,[],[],HMD_DWN_DATA2_FRAMES_Times,HMD_DWN_RE_DATA2_FRAMES_Times,HMD_DWN_DATA3_FRAMES_Times,HMD_DWN_RE_DATA3_FRAMES_Times)]
    listOfFrameSizes = [([float(x) for x in HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes],[float(x) for x in HMD_UP_DATA1_FRAMES_Frames_Sizes],[float(x) for x in HMD_UP_RE_DATA1_FRAMES_Frames_Sizes],[float(x) for x in HMD_UP_DATA2_FRAMES_Frames_Sizes],[float(x) for x in HMD_UP_RE_DATA2_FRAMES_Frames_Sizes],[float(x) for x in HMD_UP_DATA3_FRAMES_Frames_Sizes],[float(x) for x in HMD_UP_RE_DATA3_FRAMES_Frames_Sizes]),
                        ([float(x) for x in HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes],[],[],[float(x) for x in HMD_DWN_DATA2_FRAMES_Frames_Sizes],[float(x) for x in HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes],[float(x) for x in HMD_DWN_DATA3_FRAMES_Frames_Sizes],[float(x) for x in HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes])]
    colors = ["red","blue","green","black","purple","cyan","pink"]
    lineStyles = ['-.',':',"--","-",'-.',':',"--"]
    markers = [".",",","1","x","|","+","v"]
    labels = ["management","data type1","retransmitted data type1","data type2","retransmitted data type2","data type3","retransmitted data type3"]


    #################### Line Graph 1 ####################
    # Line Graph for average frame sizes for different time durations from HMD traces folder (each direction will be in a graph)
    for duration in durations:
        for i in range(len(flowDirections)):
            folderPath = "{}/{}".format(prefix,flowDirections[i])
            try:
                os.mkdir(folderPath)
            except:
                pass
            firstFrame = min(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1)[0] if i==0 else 100000000,flowDirectionsLists[i].__getitem__(2)[0] if i == 0 else 100000000,flowDirectionsLists[i].__getitem__(3)[0],
                            flowDirectionsLists[i].__getitem__(4)[0],flowDirectionsLists[i].__getitem__(5)[0],flowDirectionsLists[i].__getitem__(6)[0])
            for j in range(len(flowDirectionsLists[i])):
                if(i == 1 and j in [1,2]):
                    continue
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfTotalSizesOfFrames = computeAVGSize(newTimes,listOfFrameSizes[i].__getitem__(j),duration)
                x = newTimesPeriods
                y = listOfTotalSizesOfFrames
                yLabel = '{}'.format(labels[j]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[j]),marker = '.',linestyle='-')
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('average frames size (bytes)', fontsize=12)
            plt.title("{} average size of frames of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_size_of_frames.png'.format(folderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### Line Graph 2 ####################
    # Line Graph for average frame sizes for different time durations from HMD traces folder (each data type will be in a graph)
    for duration in durations:
        for j in range(len(labels)):
            firstFrame = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0]) if j not in [1,2] else flowDirectionsLists[0].__getitem__(j)[0]
            for i in range(len(flowDirections)):
                if(i == 1 and j in [1,2]):
                        continue
                folderPath = "{}/{}".format(prefix,labels[j])
                try:
                    os.mkdir(folderPath)
                except:
                    pass
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfTotalSizesOfFrames = computeAVGSize(newTimes,listOfFrameSizes[i].__getitem__(j),duration)
                x = newTimesPeriods
                y = listOfTotalSizesOfFrames
                yLabel = '{}'.format(flowDirections[i]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[i]),marker = '.',linestyle='-')
                
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('average frames size (bytes)', fontsize=12)
            plt.title("{} average size of frames of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_size_of_frames.png'.format(folderPath,labels[j],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################


    #################### Line Graph 3 ####################
    # Line Graph for average frame sizes for all the frames from all data types for different time durations from HMD traces folder
    folderPath = "{}/{}".format(prefix,"all_data_types")
    try:
        os.mkdir(folderPath)
    except:
        pass
    try:
        listOfFolders = ["DMR","DR","DM","D","R"]
        for tempFolder in listOfFolders:
            os.mkdir("{}/{}".format(folderPath,tempFolder))
    except:
        pass
        
    for duration in durations: 
        # [D+M+R] all data frames + all management frames + all re-transmitted frames (lists suffix 1) 
        uniqueDataCombinedLists_1,retransmittedDataCombinedLists_1 = combinedResultsLists(results,1)
        HMD_UP_NBs_1,HMD_UP_Times_1,HMD_UP_DataRates_1,HMD_UP_Data_Sizes_1,HMD_UP_Frames_Sizes_1,HMD_UP_Frames_SeqNB_1,HMD_DWN_NBs_1,HMD_DWN_Times_1,HMD_DWN_DataRates_1,HMD_DWN_Data_Sizes_1,HMD_DWN_Frames_Sizes_1,HMD_DWN_Frames_SeqNB_1 = uniqueDataCombinedLists_1
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_1[0],HMD_UP_Times_1)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeAVGSize(newTimesX1,[float(x) for x in HMD_UP_Frames_Sizes_1],duration)
        x1 = newTimesPeriodsX1
        y1 = listOfTotalSizesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_1[0],HMD_DWN_Times_1)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeAVGSize(newTimesX2,[float(x) for x in HMD_DWN_Frames_Sizes_1],duration)
        x2 = newTimesPeriodsX2
        y2 = listOfTotalSizesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('average frames size (bytes)', fontsize=12)
        plt.title("DMR frames average size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DMR/{}_size_of_frames.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D+R] all data frames + all re-transmitted frames (lists suffix 2) 
        uniqueDataCombinedLists_2,retransmittedDataCombinedLists_2 = combinedResultsLists(results,0)
        HMD_UP_NBs_2,HMD_UP_Times_2,HMD_UP_DataRates_2,HMD_UP_Data_Sizes_2,HMD_UP_Frames_Sizes_2,HMD_UP_Frames_SeqNB_2,HMD_DWN_NBs_2,HMD_DWN_Times_2,HMD_DWN_DataRates_2,HMD_DWN_Data_Sizes_2,HMD_DWN_Frames_Sizes_2,HMD_DWN_Frames_SeqNB_2 = uniqueDataCombinedLists_2
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_2[0],HMD_UP_Times_2)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeAVGSize(newTimesX1,[float(x) for x in HMD_UP_Frames_Sizes_2],duration)
        x1 = newTimesPeriodsX1
        y1 = listOfTotalSizesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_2[0],HMD_DWN_Times_2)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeAVGSize(newTimesX2,[float(x) for x in HMD_DWN_Frames_Sizes_2],duration)
        x2 = newTimesPeriodsX2
        y2 = listOfTotalSizesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('average frames size (bytes)', fontsize=12)
        plt.title("DR frames average size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DR/{}_size_of_frames.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D+M] all data frames + all management frames (lists suffix 3) 
        uniqueDataCombinedLists_3,retransmittedDataCombinedLists_3 = combinedResultsListsNoReTransmittedFrames(results,1)
        HMD_UP_NBs_3,HMD_UP_Times_3,HMD_UP_DataRates_3,HMD_UP_Data_Sizes_3,HMD_UP_Frames_Sizes_3,HMD_UP_Frames_SeqNB_3,HMD_DWN_NBs_3,HMD_DWN_Times_3,HMD_DWN_DataRates_3,HMD_DWN_Data_Sizes_3,HMD_DWN_Frames_Sizes_3,HMD_DWN_Frames_SeqNB_3 = uniqueDataCombinedLists_3
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_3[0],HMD_UP_Times_3)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeAVGSize(newTimesX1,[float(x) for x in HMD_UP_Frames_Sizes_3],duration)
        x1 = newTimesPeriodsX1
        y1 = listOfTotalSizesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_3[0],HMD_DWN_Times_3)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeAVGSize(newTimesX2,[float(x) for x in HMD_DWN_Frames_Sizes_3],duration)
        x2 = newTimesPeriodsX2
        y2 = listOfTotalSizesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('average frames size (bytes)', fontsize=12)
        plt.title("DM frames average size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DM/{}_size_of_frames.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D] all data frames (lists suffix 4) 
        uniqueDataCombinedLists_4,retransmittedDataCombinedLists_4 = combinedResultsListsNoReTransmittedFrames(results,0)
        HMD_UP_NBs_3,HMD_UP_Times_4,HMD_UP_DataRates_4,HMD_UP_Data_Sizes_4,HMD_UP_Frames_Sizes_4,HMD_UP_Frames_SeqNB_4,HMD_DWN_NBs_4,HMD_DWN_Times_4,HMD_DWN_DataRates_4,HMD_DWN_Data_Sizes_4,HMD_DWN_Frames_Sizes_4,HMD_DWN_Frames_SeqNB_4 = uniqueDataCombinedLists_4
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_4[0],HMD_UP_Times_4)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeAVGSize(newTimesX1,[float(x) for x in HMD_UP_Frames_Sizes_4],duration)
        x1 = newTimesPeriodsX1
        y1 = listOfTotalSizesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_4[0],HMD_DWN_Times_4)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeAVGSize(newTimesX2,[float(x) for x in HMD_DWN_Frames_Sizes_4],duration)
        x2 = newTimesPeriodsX2
        y2 = listOfTotalSizesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('average frames size (bytes)', fontsize=12)
        plt.title("D frames average size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/D/{}_size_of_frames.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [R] all re-transmitted frames (lists suffix 5)
        HMD_UP_RE_NBs_5,HMD_UP_RE_Times_5,HMD_UP_RE_DataRates_5,HMD_UP_RE_Data_Sizes_5,HMD_UP_RE_Frames_Sizes_5,HMD_UP_RE_Frames_SeqNB_5,HMD_DWN_RE_NBs_5,HMD_DWN_RE_Times_5,HMD_DWN_RE_DataRates_5,HMD_DWN_RE_Data_Sizes_5,HMD_DWN_RE_Frames_Sizes_5,HMD_DWN_RE_Frames_SeqNB_5 = retransmittedDataCombinedLists_1
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_RE_Times_5[0],HMD_UP_RE_Times_5)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeAVGSize(newTimesX1,[float(x) for x in HMD_UP_RE_Frames_Sizes_5],duration)
        x1 = newTimesPeriodsX1
        y1 = listOfTotalSizesOfFramesY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_RE_Times_5[0],HMD_DWN_RE_Times_5)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeAVGSize(newTimesX2,[float(x) for x in HMD_DWN_RE_Frames_Sizes_5],duration)
        x2 = newTimesPeriodsX2
        y2 = listOfTotalSizesOfFramesY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('average frames size (bytes)', fontsize=12)
        plt.title("R frames average size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/R/{}_size_of_frames.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()
        ######################################################



    #################### CDF  Graph 1 ####################
    # CDF Graph for average frames sizes for different time durations from HMD traces folder (each direction will be in a graph)
    for duration in durations:
        for i in range(len(flowDirections)):
            folderPath = "{}/{}".format(prefix,flowDirections[i])
            try:
                os.mkdir(folderPath)
            except:
                pass
            firstFrame = min(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1)[0] if i==0 else 100000000,flowDirectionsLists[i].__getitem__(2)[0] if i == 0 else 100000000,flowDirectionsLists[i].__getitem__(3)[0],
                            flowDirectionsLists[i].__getitem__(4)[0],flowDirectionsLists[i].__getitem__(5)[0],flowDirectionsLists[i].__getitem__(6)[0])
            for j in range(len(flowDirectionsLists[i])):
                if(i == 1 and j in [1,2]):
                    continue
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfTotalSizesOfFrames = computeAVGSize(newTimes,listOfFrameSizes[i].__getitem__(j),duration)
                data = [float(value) for value in listOfTotalSizesOfFrames]
                x = np.sort(data)
                y = np.arange(len(x))/float(len(x))
                yLabel = '{}'.format(labels[j]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[j]),linestyle='{}'.format(lineStyles[j]))
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('average frames size (bytes)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF {} frames average size of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_size_of_frames_CDF.png'.format(folderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### CDF  Graph 2 ####################
    # CDF Graph for average frame sizes for different time durations from HMD traces folder (each data type will be in a graph)
    for duration in durations:
        for j in range(len(labels)):
            firstFrame = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0]) if j not in [1,2] else flowDirectionsLists[0].__getitem__(j)[0]
            for i in range(len(flowDirections)):
                if(i == 1 and j in [1,2]):
                        continue
                folderPath = "{}/{}".format(prefix,labels[j])
                try:
                    os.mkdir(folderPath)
                except:
                    pass
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfTotalSizesOfFrames = computeAVGSize(newTimes,listOfFrameSizes[i].__getitem__(j),duration)
                data = [float(value) for value in listOfTotalSizesOfFrames]
                x = np.sort(data)
                y = np.arange(len(x))/float(len(x))
                yLabel = '{}'.format(flowDirections[i]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[i]),linestyle='{}'.format(lineStyles[i]))
                
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('average frames size (bytes)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF of {} frames average size of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_size_of_frames_CDF.png'.format(folderPath,labels[j],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################


    #################### CDF  Graph 3 ####################
    # CDF Graph for average frame sizes for all the frames from all data types for different time durations from HMD traces folder
    folderPath = "{}/{}".format(prefix,"all_data_types")
    try:
        os.mkdir(folderPath)
    except:
        pass
    try:
        listOfFolders = ["DMR","DR","DM","D","R"]
        for tempFolder in listOfFolders:
            os.mkdir("{}/{}".format(folderPath,tempFolder))
    except:
        pass
    for duration in durations: 
        # [D+M+R] all data frames + all management frames + all re-transmitted frames (lists suffix 1) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_1[0],HMD_UP_Times_1)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeAVGSize(newTimesX1,[float(x) for x in HMD_UP_Frames_Sizes_1],duration)
        data1 = [float(value) for value in listOfTotalSizesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_1[0],HMD_DWN_Times_1)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeAVGSize(newTimesX2,[float(x) for x in HMD_DWN_Frames_Sizes_1],duration)
        data2 = [float(value) for value in listOfTotalSizesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('average frames size (bytes)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of DMR frames average size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DMR/{}_size_of_frames_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D+R] all data frames + all re-transmitted frames (lists suffix 2) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_2[0],HMD_UP_Times_2)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeAVGSize(newTimesX1,[float(x) for x in HMD_UP_Frames_Sizes_2],duration)
        data1 = [float(value) for value in listOfTotalSizesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_2[0],HMD_DWN_Times_2)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeAVGSize(newTimesX2,[float(x) for x in HMD_DWN_Frames_Sizes_2],duration)
        data2 = [float(value) for value in listOfTotalSizesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('average frames size (bytes)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of DR frames average size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DR/{}_size_of_frames_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D+M] all data frames + all management frames (lists suffix 3) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_3[0],HMD_UP_Times_3)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeAVGSize(newTimesX1,[float(x) for x in HMD_UP_Frames_Sizes_3],duration)
        data1 = [float(value) for value in listOfTotalSizesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_3[0],HMD_DWN_Times_3)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeAVGSize(newTimesX2,[float(x) for x in HMD_DWN_Frames_Sizes_3],duration)
        data2 = [float(value) for value in listOfTotalSizesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('average frames size (bytes)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of DM frames average size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DM/{}_size_of_frames_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D] all data frames (lists suffix 4) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_4[0],HMD_UP_Times_4)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeAVGSize(newTimesX1,[float(x) for x in HMD_UP_Frames_Sizes_4],duration)
        data1 = [float(value) for value in listOfTotalSizesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_4[0],HMD_DWN_Times_4)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeAVGSize(newTimesX2,[float(x) for x in HMD_DWN_Frames_Sizes_4],duration)
        data2 = [float(value) for value in listOfTotalSizesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('average frames size (bytes)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of D frames average size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/D/{}_size_of_frames_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [R] all re-transmitted frames (lists suffix 5)
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_RE_Times_5[0],HMD_UP_RE_Times_5)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfFramesY1 = computeAVGSize(newTimesX1,[float(x) for x in HMD_UP_RE_Frames_Sizes_5],duration)
        data1 = [float(value) for value in listOfTotalSizesOfFramesY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_RE_Times_5[0],HMD_DWN_RE_Times_5)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfFramesY2 = computeAVGSize(newTimesX2,[float(x) for x in HMD_DWN_RE_Frames_Sizes_5],duration)
        data2 = [float(value) for value in listOfTotalSizesOfFramesY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('average frames size (bytes)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of R frames average size of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/R/{}_size_of_frames_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()
        ######################################################



def plotServerAVGSizeofData(root_folder,gameName,results):
    result_folder_name = "server/avg_size_of_data"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    
    try:
        os.mkdir(prefix)
    except:
        pass


    server_UP_BOTH_NBs,server_UP_BOTH_Times,server_UP_BOTH_Data_Sizes,server_UP_BOTH_Frames_Sizes,server_UP_TCP_NBs,\
        server_UP_TCP_Times,server_UP_TCP_Data_Sizes,server_UP_TCP_Frames_Sizes,server_UP_UDP_NBs,server_UP_UDP_Times,\
        server_UP_UDP_Data_Sizes,server_UP_UDP_Frames_Sizes,server_DWN_BOTH_NBs,server_DWN_BOTH_Times,server_DWN_BOTH_Data_Sizes,\
        server_DWN_BOTH_Frames_Sizes,server_DWN_TCP_NBs,server_DWN_TCP_Times,server_DWN_TCP_Data_Sizes,server_DWN_TCP_Frames_Sizes,\
        server_DWN_UDP_NBs,server_DWN_UDP_Times,server_DWN_UDP_Data_Sizes,server_DWN_UDP_Frames_Sizes = results     


    #################### Line Graph ####################
    # line graph for avg size of frames for different time durations from server.csv trace
    durations = [1,10,15,30,60]  # in seconds
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(server_UP_BOTH_Times,server_UP_UDP_Times,server_UP_TCP_Times),
                            (server_DWN_BOTH_Times,server_DWN_UDP_Times,server_DWN_TCP_Times)]
    listOfFrameSizes = [([float(x) for x in server_UP_BOTH_Data_Sizes],[float(x) for x in server_UP_UDP_Data_Sizes]
                        ,[float(x) for x in server_UP_TCP_Data_Sizes]),([float(x) for x in server_DWN_BOTH_Data_Sizes]
                        ,[float(x) for x in server_DWN_UDP_Data_Sizes],[float(x) for x in server_DWN_TCP_Data_Sizes])]
    
    
    for duration in durations:
        for i in range(len(flowDirections)):
            newTimesBoth = relativeTime(flowDirectionsLists[i].__getitem__(0))
            newTimesPeriodsBoth = convertTimeToPeriods(newTimesBoth,duration)
            avgSizeOfFramesBoth = computeAVGSize(newTimesBoth,listOfFrameSizes[i].__getitem__(0),duration)
            newTimesUDP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1))
            newTimesPeriodsUDP = convertTimeToPeriods(newTimesUDP,duration)
            avgSizeOfFramesUDP = computeAVGSize(newTimesUDP,listOfFrameSizes[i].__getitem__(1),duration)
            newTimesTCP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(2))
            newTimesPeriodsTCP = convertTimeToPeriods(newTimesTCP,duration)
            avgSizeOfFramesTCP = computeAVGSize(newTimesTCP,listOfFrameSizes[i].__getitem__(2),duration)
            x1 = newTimesPeriodsBoth
            y1 = avgSizeOfFramesBoth
            y1Label = 'Both'
            x2 = newTimesPeriodsUDP
            y2 = avgSizeOfFramesUDP
            y2Label = 'UDP'
            x3 = newTimesPeriodsTCP
            y3 = avgSizeOfFramesTCP
            y3Label = 'TCP'      
            plt.plot(x1,y1,label=y1Label,c='red',marker = '.',linestyle='-')
            plt.plot(x2,y2,label=y2Label,c='blue',marker = '.',linestyle='-')
            plt.plot(x3,y3,label=y3Label,c='green',marker = '.',linestyle='-')
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('avg data size (bytes)', fontsize=12)
            plt.title("{} avg size data of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=9)
            plt.savefig('{}/{}_duration_{}_avg_size_of_data.png'.format(prefix,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ####################################################



    #################### CDF  Graph ####################
    # CDF Graph for size of frames for different time durations from server.csv trace
    for duration in durations:
        for i in range(len(flowDirections)):    
            newTimesBoth = relativeTime(flowDirectionsLists[i].__getitem__(0))
            newTimesPeriodsBoth = convertTimeToPeriods(newTimesBoth,duration)
            avgSizeOfFramesBoth = computeAVGSize(newTimesBoth,listOfFrameSizes[i].__getitem__(0),duration)
            newTimesUDP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1))
            newTimesPeriodsUDP = convertTimeToPeriods(newTimesUDP,duration)
            avgSizeOfFramesUDP = computeAVGSize(newTimesUDP,listOfFrameSizes[i].__getitem__(1),duration)
            newTimesTCP = relativeTimeFromAPointOfTime(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(2))
            newTimesPeriodsTCP = convertTimeToPeriods(newTimesTCP,duration)
            avgSizeOfFramesTCP = computeAVGSize(newTimesTCP,listOfFrameSizes[i].__getitem__(2),duration)
            
            data1 = [float(i) for i in avgSizeOfFramesBoth]
            data2 = [float(i) for i in avgSizeOfFramesUDP]
            data3 = [float(i) for i in avgSizeOfFramesTCP]
            
            x1 = np.sort(data1)
            x2 = np.sort(data2)
            x3 = np.sort(data3)

            y1 = np.arange(len(x1))/float(len(x1))
            y2 = np.arange(len(x2))/float(len(x2))
            y3 = np.arange(len(x3))/float(len(x3))

            y1Label =  'Both'
            y2Label =  'UDP'
            y3Label =  'TCP'

            plt.plot(x1, y1,label=y1Label,c='red',linestyle='-.')
            plt.plot(x2, y2,label=y2Label,c='blue',linestyle=':')
            plt.plot(x3, y3,label=y3Label,c='green',linestyle='--')

            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('avg data size (bytes)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF {} avg size of data of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=9)
            plt.savefig('{}/{}_duration_{}_avg_sizs_of_data_CDF.png'.format(prefix,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ####################################################



def plotHMDAVGSizeofData(root_folder,gameName,results):
    result_folder_name = "HMD/average_size_of_data"
    prefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name)
    
    try:
        os.mkdir(prefix)
    except:
        pass

    HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates,\
        HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes, HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times,\
        HMD_DWN_MANAGEMENT_FRAMES_DataRates, HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes, HMD_UP_DATA1_FRAMES_NBs, \
        HMD_UP_DATA1_FRAMES_Times, HMD_UP_DATA1_FRAMES_DataRates, HMD_UP_DATA1_FRAMES_Frames_Sizes,\
        HMD_UP_DATA1_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA1_FRAMES_NBs, HMD_UP_RE_DATA1_FRAMES_Times, \
        HMD_UP_RE_DATA1_FRAMES_DataRates, HMD_UP_RE_DATA1_FRAMES_Frames_Sizes, HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB,\
        HMD_UP_DATA2_FRAMES_NBs, HMD_UP_DATA2_FRAMES_Times, HMD_UP_DATA2_FRAMES_DataRates, HMD_UP_DATA2_FRAMES_Data_Sizes,\
        HMD_UP_DATA2_FRAMES_Frames_Sizes, HMD_UP_DATA2_FRAMES_Frames_SeqNB, HMD_DWN_DATA2_FRAMES_NBs, HMD_DWN_DATA2_FRAMES_Times, \
        HMD_DWN_DATA2_FRAMES_DataRates, HMD_DWN_DATA2_FRAMES_Data_Sizes, HMD_DWN_DATA2_FRAMES_Frames_Sizes, \
        HMD_DWN_DATA2_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA2_FRAMES_NBs, HMD_UP_RE_DATA2_FRAMES_Times, HMD_UP_RE_DATA2_FRAMES_DataRates,\
        HMD_UP_RE_DATA2_FRAMES_Data_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB, \
        HMD_DWN_RE_DATA2_FRAMES_NBs, HMD_DWN_RE_DATA2_FRAMES_Times, HMD_DWN_RE_DATA2_FRAMES_DataRates, HMD_DWN_RE_DATA2_FRAMES_Data_Sizes,\
        HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB, HMD_UP_DATA3_FRAMES_NBs, HMD_UP_DATA3_FRAMES_Times, \
        HMD_UP_DATA3_FRAMES_DataRates, HMD_UP_DATA3_FRAMES_Data_Sizes, HMD_UP_DATA3_FRAMES_Frames_Sizes, HMD_UP_DATA3_FRAMES_Frames_SeqNB,\
        HMD_DWN_DATA3_FRAMES_NBs, HMD_DWN_DATA3_FRAMES_Times, HMD_DWN_DATA3_FRAMES_DataRates, HMD_DWN_DATA3_FRAMES_Data_Sizes,\
        HMD_DWN_DATA3_FRAMES_Frames_Sizes, HMD_DWN_DATA3_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA3_FRAMES_NBs, HMD_UP_RE_DATA3_FRAMES_Times, \
        HMD_UP_RE_DATA3_FRAMES_DataRates, HMD_UP_RE_DATA3_FRAMES_Data_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_Sizes, \
        HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB, HMD_DWN_RE_DATA3_FRAMES_NBs, HMD_DWN_RE_DATA3_FRAMES_Times, HMD_DWN_RE_DATA3_FRAMES_DataRates, \
        HMD_DWN_RE_DATA3_FRAMES_Data_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB = results 
    

    durations = [1,10,15,30,60]  # in seconds
    flowDirections = ["uplink","downlink"]
    flowDirectionsLists = [(HMD_UP_DATA2_FRAMES_Times,HMD_UP_RE_DATA2_FRAMES_Times,HMD_UP_DATA3_FRAMES_Times,HMD_UP_RE_DATA3_FRAMES_Times),
                            (HMD_DWN_DATA2_FRAMES_Times,HMD_DWN_RE_DATA2_FRAMES_Times,HMD_DWN_DATA3_FRAMES_Times,HMD_DWN_RE_DATA3_FRAMES_Times)]
    listOfDataSizes = [([float(0) if x == '' else float(x) for x in HMD_UP_DATA2_FRAMES_Data_Sizes],[float(0) if x == '' else float(x) for x in HMD_UP_RE_DATA2_FRAMES_Data_Sizes],[float(0) if x == '' else float(x) for x in HMD_UP_DATA3_FRAMES_Data_Sizes],[float(0) if x == '' else float(x) for x in HMD_UP_RE_DATA3_FRAMES_Data_Sizes]),
                        ([float(0) if x == '' else float(x) for x in HMD_DWN_DATA2_FRAMES_Data_Sizes],[float(0) if x == '' else float(x) for x in HMD_DWN_RE_DATA2_FRAMES_Data_Sizes],[float(0) if x == '' else float(x) for x in HMD_DWN_DATA3_FRAMES_Data_Sizes],[float(0) if x == '' else float(x) for x in HMD_DWN_RE_DATA3_FRAMES_Data_Sizes])]
    colors = ["black","purple","cyan","pink"]
    lineStyles = ["-",'-.',':',"--"]
    markers = [".",",","1","x"]
    labels = ["data type2","retransmitted data type2","data type3","retransmitted data type3"]


    #################### Line Graph 1 ####################
    # Line Graph for average size of data for different time durations from HMD traces folder (each direction will be in a graph)
    for duration in durations:
        for i in range(len(flowDirections)):
            folderPath = "{}/{}".format(prefix,flowDirections[i])
            try:
                os.mkdir(folderPath)
            except:
                pass
            firstFrame = min(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1)[0],flowDirectionsLists[i].__getitem__(2)[0],flowDirectionsLists[i].__getitem__(3)[0])
            for j in range(len(flowDirectionsLists[i])):
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfTotalSizesOfData = computeAVGSize(newTimes,listOfDataSizes[i].__getitem__(j),duration)
                x = newTimesPeriods
                y = listOfTotalSizesOfData
                yLabel = '{}'.format(labels[j]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[j]),marker = '.',linestyle='-')
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('average data size (bytes)', fontsize=12)
            plt.title("{} average size of data of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_size_of_data.png'.format(folderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### Line Graph 2 ####################
    # Line Graph for average size of data for different time durations from HMD traces folder (each data type will be in a graph)
    for duration in durations:
        for j in range(len(labels)):
            firstFrame = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0])
            for i in range(len(flowDirections)):
                folderPath = "{}/{}".format(prefix,labels[j])
                try:
                    os.mkdir(folderPath)
                except:
                    pass
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfTotalSizesOfData = computeAVGSize(newTimes,listOfDataSizes[i].__getitem__(j),duration)
                x = newTimesPeriods
                y = listOfTotalSizesOfData
                yLabel = '{}'.format(flowDirections[i]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[i]),marker = '.',linestyle='-')
                
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('time in (sec)', fontsize=12)
            plt.ylabel('average data size (bytes)', fontsize=12)
            plt.title("{} average size of data of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_size_of_data.png'.format(folderPath,labels[j],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################


    #################### Line Graph 3 ####################
    # Line Graph for average size of data for all the frames from all data types for different time durations from HMD traces folder
    folderPath = "{}/{}".format(prefix,"all_data_types")
    try:
        os.mkdir(folderPath)
    except:
        pass
    try:
        listOfFolders = ["DR","D","R"]
        for tempFolder in listOfFolders:
            os.mkdir("{}/{}".format(folderPath,tempFolder))
    except:
        pass
    for duration in durations: 
        # [D+R] all data frames + all re-transmitted frames (lists suffix 1) 
        uniqueDataCombinedLists_1,retransmittedDataCombinedLists_1 = combinedResultsLists(results,0)
        HMD_UP_NBs_1,HMD_UP_Times_1,HMD_UP_DataRates_1,HMD_UP_Data_Sizes_1,HMD_UP_Frames_Sizes_1,HMD_UP_Frames_SeqNB_1,HMD_DWN_NBs_1,HMD_DWN_Times_1,HMD_DWN_DataRates_1,HMD_DWN_Data_Sizes_1,HMD_DWN_Frames_Sizes_1,HMD_DWN_Frames_SeqNB_1 = uniqueDataCombinedLists_1
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_1[0],HMD_UP_Times_1)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfDataY1 = computeAVGSize(newTimesX1,[float(0) if x == '' else float(x) for x in HMD_UP_Data_Sizes_1],duration)
        x1 = newTimesPeriodsX1
        y1 = listOfTotalSizesOfDataY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_1[0],HMD_DWN_Times_1)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfDataY2 = computeAVGSize(newTimesX2,[float(0) if x == '' else float(x) for x in HMD_DWN_Data_Sizes_1],duration)
        x2 = newTimesPeriodsX2
        y2 = listOfTotalSizesOfDataY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('average data size (bytes)', fontsize=12)
        plt.title("DR average size of data of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DR/{}_size_of_data.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D] all data frames (lists suffix 2) 
        uniqueDataCombinedLists_2,retransmittedDataCombinedLists_2 = combinedResultsListsNoReTransmittedFrames(results,0)
        HMD_UP_NBs_2,HMD_UP_Times_2,HMD_UP_DataRates_2,HMD_UP_Data_Sizes_2,HMD_UP_Frames_Sizes_2,HMD_UP_Frames_SeqNB_2,HMD_DWN_NBs_2,HMD_DWN_Times_2,HMD_DWN_DataRates_2,HMD_DWN_Data_Sizes_2,HMD_DWN_Frames_Sizes_2,HMD_DWN_Frames_SeqNB_2 = uniqueDataCombinedLists_2
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_2[0],HMD_UP_Times_2)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfDataY1 = computeAVGSize(newTimesX1,[float(0) if x == '' else float(x) for x in HMD_UP_Data_Sizes_2],duration)
        x1 = newTimesPeriodsX1
        y1 = listOfTotalSizesOfDataY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_2[0],HMD_DWN_Times_2)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfDataY2 = computeAVGSize(newTimesX2,[float(0) if x == '' else float(x) for x in HMD_DWN_Data_Sizes_2],duration)
        x2 = newTimesPeriodsX2
        y2 = listOfTotalSizesOfDataY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('average data size (bytes)', fontsize=12)
        plt.title("D average size of data of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/D/{}_size_of_data.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [R] all re-transmitted frames (lists suffix 3)
        HMD_UP_RE_NBs_3,HMD_UP_RE_Times_3,HMD_UP_RE_DataRates_3,HMD_UP_RE_Data_Sizes_3,HMD_UP_RE_Frames_Sizes_3,HMD_UP_RE_Frames_SeqNB_3,HMD_DWN_RE_NBs_3,HMD_DWN_RE_Times_3,HMD_DWN_RE_DataRates_3,HMD_DWN_RE_Data_Sizes_3,HMD_DWN_RE_Frames_Sizes_3,HMD_DWN_RE_Frames_SeqNB_3 = retransmittedDataCombinedLists_1
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_RE_Times_3[0],HMD_UP_RE_Times_3)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfDataY1 = computeAVGSize(newTimesX1,[float(0) if x == '' else float(x) for x in HMD_UP_RE_Data_Sizes_3],duration)
        x1 = newTimesPeriodsX1
        y1 = listOfTotalSizesOfDataY1
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_RE_Times_3[0],HMD_DWN_RE_Times_3)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfDataY2 = computeAVGSize(newTimesX2,[float(0) if x == '' else float(x) for x in HMD_DWN_RE_Data_Sizes_3],duration)
        x2 = newTimesPeriodsX2
        y2 = listOfTotalSizesOfDataY2
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('time in (sec)', fontsize=12)
        plt.ylabel('average data size (bytes)', fontsize=12)
        plt.title("R average size of data of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/R/{}_size_of_data.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()
        ######################################################



    #################### CDF  Graph 1 ####################
    # CDF Graph for average size of data for different time durations from HMD traces folder (each direction will be in a graph)
    for duration in durations:
        for i in range(len(flowDirections)):
            folderPath = "{}/{}".format(prefix,flowDirections[i])
            try:
                os.mkdir(folderPath)
            except:
                pass
            firstFrame = min(flowDirectionsLists[i].__getitem__(0)[0],flowDirectionsLists[i].__getitem__(1)[0],flowDirectionsLists[i].__getitem__(2)[0],flowDirectionsLists[i].__getitem__(3)[0])
            for j in range(len(flowDirectionsLists[i])):
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfTotalSizesOfData = computeAVGSize(newTimes,listOfDataSizes[i].__getitem__(j),duration)
                data = [float(value) for value in listOfTotalSizesOfData]
                x = np.sort(data)
                y = np.arange(len(x))/float(len(x))
                yLabel = '{}'.format(labels[j]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[j]),linestyle='{}'.format(lineStyles[j]))
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('average data size (bytes)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF {} average size of data of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_size_of_data_CDF.png'.format(folderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### CDF  Graph 2 ####################
    # CDF Graph for total size of data for different time durations from HMD traces folder (each data type will be in a graph)
    for duration in durations:
        for j in range(len(labels)):
            firstFrame = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0])
            for i in range(len(flowDirections)):
                folderPath = "{}/{}".format(prefix,labels[j])
                try:
                    os.mkdir(folderPath)
                except:
                    pass
                newTimes = relativeTimeFromAPointOfTime(firstFrame,flowDirectionsLists[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfTotalSizesOfData = computeAVGSize(newTimes,listOfDataSizes[i].__getitem__(j),duration)
                data = [float(value) for value in listOfTotalSizesOfData]
                x = np.sort(data)
                y = np.arange(len(x))/float(len(x))
                yLabel = '{}'.format(flowDirections[i]) 
                plt.plot(x,y,label=yLabel,c='{}'.format(colors[i]),linestyle='{}'.format(lineStyles[i]))
                
            plt.legend(loc='best', fontsize=10)
            plt.grid(color='grey', linestyle='--', linewidth=0.5)
            plt.xlabel('average data size (bytes)', fontsize=12)
            plt.ylabel('CDF', fontsize=12)
            plt.title("CDF of {} average size of data of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            plt.savefig('{}/{}_duration_{}_size_of_data_CDF.png'.format(folderPath,labels[j],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################


    #################### CDF  Graph 3 ####################
    # CDF Graph for average size of data for all the frames from all data types for different time durations from HMD traces folder
    folderPath = "{}/{}".format(prefix,"all_data_types")
    try:
        os.mkdir(folderPath)
    except:
        pass
    try:
        listOfFolders = ["DR","D","R"]
        for tempFolder in listOfFolders:
            os.mkdir("{}/{}".format(folderPath,tempFolder))
    except:
        pass
    for duration in durations:         
        # [D+R] all data frames + all re-transmitted frames (lists suffix 1) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_1[0],HMD_UP_Times_1)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfDataY1 = computeAVGSize(newTimesX1,[float(0) if x == '' else float(x) for x in HMD_UP_Data_Sizes_1],duration)
        data1 = [float(value) for value in listOfTotalSizesOfDataY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_1[0],HMD_DWN_Times_1)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfDataY2 = computeAVGSize(newTimesX2,[float(0) if x == '' else float(x) for x in HMD_DWN_Data_Sizes_1],duration)
        data2 = [float(value) for value in listOfTotalSizesOfDataY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('average data size (bytes)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of DR average size of data of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/DR/{}_size_of_data_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [D] all data frames (lists suffix 2) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_Times_2[0],HMD_UP_Times_2)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfDataY1 = computeAVGSize(newTimesX1,[float(0) if x == '' else float(x) for x in HMD_UP_Data_Sizes_2],duration)
        data1 = [float(value) for value in listOfTotalSizesOfDataY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_Times_2[0],HMD_DWN_Times_2)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfDataY2 = computeAVGSize(newTimesX2,[float(0) if x == '' else float(x) for x in HMD_DWN_Data_Sizes_2],duration)
        data2 = [float(value) for value in listOfTotalSizesOfDataY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('average data size (bytes)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of D average size of data of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/D/{}_size_of_data_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()

        # [R] all data frames + all management frames (lists suffix 3) 
        newTimesX1 = relativeTimeFromAPointOfTime(HMD_UP_RE_Times_3[0],HMD_UP_RE_Times_3)
        newTimesPeriodsX1 = convertTimeToPeriods(newTimesX1,duration)
        listOfTotalSizesOfDataY1 = computeAVGSize(newTimesX1,[float(0) if x == '' else float(x) for x in HMD_UP_RE_Data_Sizes_3],duration)
        data1 = [float(value) for value in listOfTotalSizesOfDataY1]
        x1 = np.sort(data1)
        y1 = np.arange(len(x1))/float(len(x1))
        y1Label = "uplink"
        plt.plot(x1,y1,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        newTimesX2 = relativeTimeFromAPointOfTime(HMD_DWN_RE_Times_3[0],HMD_DWN_RE_Times_3)
        newTimesPeriodsX2 = convertTimeToPeriods(newTimesX2,duration)
        listOfTotalSizesOfDataY2 = computeAVGSize(newTimesX2,[float(0) if x == '' else float(x) for x in HMD_DWN_RE_Data_Sizes_3],duration)
        data2 = [float(value) for value in listOfTotalSizesOfDataY2]
        x2 = np.sort(data2)
        y2 = np.arange(len(x2))/float(len(x2))
        y2Label = "downlink"
        plt.plot(x2,y2,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        plt.legend(loc='best', fontsize=10)
        plt.grid(color='grey', linestyle='--', linewidth=0.5)
        plt.xlabel('average data size (bytes)', fontsize=12)
        plt.ylabel('CDF', fontsize=12)
        plt.title("CDF of R average size of data of {} for a duration of {} sec".format(gameName,duration),fontsize=10)
        plt.savefig('{}/R/{}_size_of_data_CDF.png'.format(folderPath,duration),dpi=saved_graph_resolution)
        plt.show()
        ######################################################



def plotHMDSucessRateNB(root_folder,gameName,results):
    result_folder_name_sucess = "HMD/sucess_rates"
    result_folder_name_retransmission = "HMD/retransmission_rates"
    tempSucessPrefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name_sucess)
    tempRetransmissionPrefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name_retransmission)
    sucessPrefix = "{}/{}".format(tempSucessPrefix,"based_on_NB_of_Frames")
    retransmissionPrefix = "{}/{}".format(tempRetransmissionPrefix,"based_on_NB_of_Frames")
    try:
        os.mkdir(tempSucessPrefix)
        os.mkdir(tempRetransmissionPrefix)
    except:
        pass
    try:
        os.mkdir(sucessPrefix)
        os.mkdir(retransmissionPrefix)
    except:
        pass

    print("\033[93m{}\033[00m" .format("overall rates based on # of frames: "))

    newResults = eliminateRetransmittedFrames(results)
    HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates,\
        HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes, HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times,\
        HMD_DWN_MANAGEMENT_FRAMES_DataRates, HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes, HMD_UP_DATA1_FRAMES_NBs, \
        HMD_UP_DATA1_FRAMES_Times, HMD_UP_DATA1_FRAMES_DataRates, HMD_UP_DATA1_FRAMES_Frames_Sizes,\
        HMD_UP_DATA1_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA1_FRAMES_NBs, HMD_UP_RE_DATA1_FRAMES_Times, \
        HMD_UP_RE_DATA1_FRAMES_DataRates, HMD_UP_RE_DATA1_FRAMES_Frames_Sizes, HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB,\
        HMD_UP_DATA2_FRAMES_NBs, HMD_UP_DATA2_FRAMES_Times, HMD_UP_DATA2_FRAMES_DataRates, HMD_UP_DATA2_FRAMES_Data_Sizes,\
        HMD_UP_DATA2_FRAMES_Frames_Sizes, HMD_UP_DATA2_FRAMES_Frames_SeqNB, HMD_DWN_DATA2_FRAMES_NBs, HMD_DWN_DATA2_FRAMES_Times, \
        HMD_DWN_DATA2_FRAMES_DataRates, HMD_DWN_DATA2_FRAMES_Data_Sizes, HMD_DWN_DATA2_FRAMES_Frames_Sizes, \
        HMD_DWN_DATA2_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA2_FRAMES_NBs, HMD_UP_RE_DATA2_FRAMES_Times, HMD_UP_RE_DATA2_FRAMES_DataRates,\
        HMD_UP_RE_DATA2_FRAMES_Data_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB, \
        HMD_DWN_RE_DATA2_FRAMES_NBs, HMD_DWN_RE_DATA2_FRAMES_Times, HMD_DWN_RE_DATA2_FRAMES_DataRates, HMD_DWN_RE_DATA2_FRAMES_Data_Sizes,\
        HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB, HMD_UP_DATA3_FRAMES_NBs, HMD_UP_DATA3_FRAMES_Times, \
        HMD_UP_DATA3_FRAMES_DataRates, HMD_UP_DATA3_FRAMES_Data_Sizes, HMD_UP_DATA3_FRAMES_Frames_Sizes, HMD_UP_DATA3_FRAMES_Frames_SeqNB,\
        HMD_DWN_DATA3_FRAMES_NBs, HMD_DWN_DATA3_FRAMES_Times, HMD_DWN_DATA3_FRAMES_DataRates, HMD_DWN_DATA3_FRAMES_Data_Sizes,\
        HMD_DWN_DATA3_FRAMES_Frames_Sizes, HMD_DWN_DATA3_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA3_FRAMES_NBs, HMD_UP_RE_DATA3_FRAMES_Times, \
        HMD_UP_RE_DATA3_FRAMES_DataRates, HMD_UP_RE_DATA3_FRAMES_Data_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_Sizes, \
        HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB, HMD_DWN_RE_DATA3_FRAMES_NBs, HMD_DWN_RE_DATA3_FRAMES_Times, HMD_DWN_RE_DATA3_FRAMES_DataRates, \
        HMD_DWN_RE_DATA3_FRAMES_Data_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB = newResults   
    
    uniqueDataCombinedLists,retransmittedDataCombinedLists = combinedResultsLists(results,0)
    HMD_UP_NBs,HMD_UP_Times,HMD_UP_DataRates,HMD_UP_Data_Sizes,HMD_UP_Frames_Sizes,HMD_UP_Frames_SeqNB,HMD_DWN_NBs,HMD_DWN_Times,HMD_DWN_DataRates,HMD_DWN_Data_Sizes,HMD_DWN_Frames_Sizes,HMD_DWN_Frames_SeqNB = uniqueDataCombinedLists
    HMD_UP_RE_NBs,HMD_UP_RE_Times,HMD_UP_RE_DataRates,HMD_UP_RE_Data_Sizes,HMD_UP_RE_Frames_Sizes,HMD_UP_RE_Frames_SeqNB,HMD_DWN_RE_NBs,HMD_DWN_RE_Times,HMD_DWN_RE_DataRates,HMD_DWN_RE_Data_Sizes,HMD_DWN_RE_Frames_Sizes,HMD_DWN_RE_Frames_SeqNB = retransmittedDataCombinedLists
    
    # both directions of each data type and retransmission data types
    tempHMD_DATA1_FRAMES_Times = HMD_UP_DATA1_FRAMES_Times
    tempHMD_DATA2_FRAMES_Times = HMD_UP_DATA2_FRAMES_Times + HMD_DWN_DATA2_FRAMES_Times
    tempHMD_DATA3_FRAMES_Times = HMD_UP_DATA3_FRAMES_Times + HMD_DWN_DATA3_FRAMES_Times
    tempHMD_DATA_FRAMES_Times  = HMD_UP_Times + HMD_DWN_Times
    tempHMD_DATA2_FRAMES_Times.sort()
    tempHMD_DATA3_FRAMES_Times.sort()
    tempHMD_DATA_FRAMES_Times.sort()

    tempHMD_RE_DATA1_FRAMES_Times = HMD_UP_RE_DATA1_FRAMES_Times
    tempHMD_RE_DATA2_FRAMES_Times = HMD_UP_RE_DATA2_FRAMES_Times + HMD_DWN_RE_DATA2_FRAMES_Times
    tempHMD_RE_DATA3_FRAMES_Times = HMD_UP_RE_DATA3_FRAMES_Times + HMD_DWN_RE_DATA3_FRAMES_Times
    tempHMD_RE_DATA_FRAMES_Times  = HMD_UP_RE_Times + HMD_DWN_RE_Times
    tempHMD_RE_DATA2_FRAMES_Times.sort()
    tempHMD_RE_DATA3_FRAMES_Times.sort()
    tempHMD_RE_DATA_FRAMES_Times.sort()

    # both directions for all data types and retransmission data types
    tempHMD_Data_Times    = tempHMD_DATA1_FRAMES_Times + tempHMD_DATA2_FRAMES_Times + tempHMD_DATA3_FRAMES_Times
    tempHMD_RE_Data_Times = tempHMD_RE_DATA1_FRAMES_Times + tempHMD_RE_DATA2_FRAMES_Times + tempHMD_RE_DATA3_FRAMES_Times
    tempHMD_Data_Times.sort()
    tempHMD_RE_Data_Times.sort()

    durations = [1,10,15,30,60]  # in seconds
    flowDirections = ["uplink","downlink","both_directions"]
    flowDirectionsLists = [(HMD_UP_DATA1_FRAMES_Times,HMD_UP_DATA2_FRAMES_Times,HMD_UP_DATA3_FRAMES_Times,HMD_UP_Times),
                            ([],HMD_DWN_DATA2_FRAMES_Times,HMD_DWN_DATA3_FRAMES_Times,HMD_DWN_Times),
                            (tempHMD_DATA1_FRAMES_Times,tempHMD_DATA2_FRAMES_Times,tempHMD_DATA3_FRAMES_Times,tempHMD_DATA_FRAMES_Times)]
    flowDirectionsLists_RE = [(HMD_UP_RE_DATA1_FRAMES_Times,HMD_UP_RE_DATA2_FRAMES_Times,HMD_UP_RE_DATA3_FRAMES_Times,HMD_UP_RE_Times),
                            ([],HMD_DWN_RE_DATA2_FRAMES_Times,HMD_DWN_RE_DATA3_FRAMES_Times,HMD_DWN_RE_Times),
                            (tempHMD_RE_DATA1_FRAMES_Times,tempHMD_RE_DATA2_FRAMES_Times,tempHMD_RE_DATA3_FRAMES_Times,tempHMD_RE_DATA_FRAMES_Times)]
    
    colors = ["red","blue","green","black","purple","cyan","pink"]
    lineStyles = ['-.',':',"--","-",'-.',':',"--"]
    markers = [".",",","1","x","|","+","v"]
    labels = ["data type1","data type2","data type3","all_data_types"]
    firstFrame = [0.0,0.0,0.0]

    #################### Line Graph 1 ####################    
    # Line Graph for sucess and retransmission rates based on the # of frames for different time durations from HMD traces folder (each direction will be in a graph)
    overallRatesFlag = True
    firstIteration = True
    for duration in durations:
        if(not firstIteration):
            overallRatesFlag = False
        firstIteration = False
        for i in range(len(flowDirections)):
            sucessFolderPath = "{}/{}".format(sucessPrefix,flowDirections[i])
            retransmissionFolderPath = "{}/{}".format(retransmissionPrefix,flowDirections[i])
            try:
                os.mkdir(sucessFolderPath)
                os.mkdir(retransmissionFolderPath)
            except:
                pass
            firstFrame[i] = min(flowDirectionsLists[i].__getitem__(0)[0] if i==0 else 100000000,flowDirectionsLists[i].__getitem__(1)[0],flowDirectionsLists[i].__getitem__(2)[0])
            fig1, ax1 = plt.subplots()
            fig2, ax2 = plt.subplots()
            for j in range(len(flowDirectionsLists[i])):
                if(i == 1 and j ==0):
                    continue
                # compute the overall sucess and retransmission rates
                if(overallRatesFlag):
                    overallSucessRate = computeOverallSucessRateNB(flowDirectionsLists[i].__getitem__(j),flowDirectionsLists_RE[i].__getitem__(j))
                    overallRetransmissionRate = 100 - overallSucessRate
                    sucessRateText = "[+] the overall sucess rate of {}-{} is {}".format(labels[j],flowDirections[i],overallSucessRate)
                    retransmissionRateText = "[+] the overall retrnamission rate of {}-{} is {}".format(labels[j],flowDirections[i],overallRetransmissionRate)
                    sucessFileTitle = "overall_sucess_rates.txt"
                    retransmissionFileTitle = "overall_retransmission_rates.txt"
                    sucessFilePath = "{}/{}".format(sucessFolderPath,sucessFileTitle)
                    retransmissionFilePath = "{}/{}".format(retransmissionFolderPath,retransmissionFileTitle)
                    # write the overall sucess rate to the 'overall_sucess_rates.txt' file
                    try:
                        if(not checkExistence(sucessFilePath,sucessRateText)):
                            f = open(sucessFilePath, "a")
                            f.write("\n{}".format(sucessRateText))
                            f.close()
                    except:
                        f = open(sucessFilePath, "a")
                        f.write("\n{}".format(sucessRateText))
                        f.close()

                    # write the overall retransmission rate to the 'overall_retransmission_rates.txt' file
                    try:
                        if(not checkExistence(retransmissionFilePath,retransmissionRateText)):
                            f = open(retransmissionFilePath, "a")
                            f.write("\n{}".format(retransmissionRateText))
                            f.close()
                    except:
                        f = open(retransmissionFilePath, "a")
                        f.write("\n{}".format(retransmissionRateText))
                        f.close()

                    # print the result in the console
                    print("\033[96m\t{}\033[00m" .format(sucessRateText))
                    print("\033[91m\t{}\033[00m" .format(retransmissionRateText))
                    print()

                # compute the periodic sucess and retransmission rates
                newTimes = relativeTimeFromAPointOfTime(firstFrame[i],flowDirectionsLists[i].__getitem__(j))
                newTimes_RE = relativeTimeFromAPointOfTime(firstFrame[i],flowDirectionsLists_RE[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfSucessRates = computePeriodicSucessRateNB(newTimes,newTimes_RE,duration)
                listOfRetransmissionRates = [100-x for x in listOfSucessRates]
                x = newTimesPeriods
                y_sucess = listOfSucessRates
                y_RE = listOfRetransmissionRates
                yLabel = '{}'.format(labels[j]) 
                ax1.plot(x,y_sucess,label=yLabel,c='{}'.format(colors[j]),marker = '.',linestyle='-')
                ax2.plot(x,y_RE,label=yLabel,c='{}'.format(colors[j]),marker = '.',linestyle='-')
            ax1.legend(loc='best', fontsize=10)
            ax2.legend(loc='best', fontsize=10)
            ax1.grid(color='grey', linestyle='--', linewidth=0.5)
            ax2.grid(color='grey', linestyle='--', linewidth=0.5)
            ax1.set_xlabel('time in (sec)', fontsize=12)
            ax2.set_xlabel('time in (sec)', fontsize=12)
            ax1.set_ylabel('sucess rate percentage', fontsize=12)
            ax2.set_ylabel('retransmission rate percentage', fontsize=12)
            ax1.set_title("{} sucess rate of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            ax2.set_title("{} retransmission rate of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            fig1.savefig('{}/{}_duration_{}_sucessRate.png'.format(sucessFolderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            fig2.savefig('{}/{}_duration_{}_retransmissionRate.png'.format(retransmissionFolderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################


    #################### Line Graph 2 ####################    
    # Line Graph for sucess and retransmission rates based on the # of frames for different time durations from HMD traces folder (each data type will be in a graph)
    overallRatesFlag = True
    firstIteration = True
    for duration in durations:
        if(not firstIteration):
            overallRatesFlag = False
        firstIteration = False
        for j in range(len(labels)):
            firstTime = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0]) if not j == 0 else flowDirectionsLists[0].__getitem__(j)[0]
            fig1, ax1 = plt.subplots()
            fig2, ax2 = plt.subplots()
            for i in range(len(flowDirections)):
                if(i == 1 and j ==0):
                        continue
                sucessFolderPath = "{}/{}".format(sucessPrefix,labels[j])
                retransmissionFolderPath = "{}/{}".format(retransmissionPrefix,labels[j])
                try:
                    os.mkdir(sucessFolderPath)
                    os.mkdir(retransmissionFolderPath)
                except:
                    pass
                # compute the overall sucess and retransmission rates
                if(overallRatesFlag):
                    overallSucessRate = computeOverallSucessRateNB(flowDirectionsLists[i].__getitem__(j),flowDirectionsLists_RE[i].__getitem__(j))
                    overallRetransmissionRate = 100 - overallSucessRate
                    sucessRateText = "[+] the overall sucess rate of {}-{} is {}".format(labels[j],flowDirections[i],overallSucessRate)
                    retransmissionRateText = "[+] the overall retrnamission rate of {}-{} is {}".format(labels[j],flowDirections[i],overallRetransmissionRate)
                    sucessFileTitle = "overall_sucess_rates.txt"
                    retransmissionFileTitle = "overall_retransmission_rates.txt"
                    sucessFilePath = "{}/{}".format(sucessFolderPath,sucessFileTitle)
                    retransmissionFilePath = "{}/{}".format(retransmissionFolderPath,retransmissionFileTitle)
                    # write the overall sucess rate to the 'overall_sucess_rates.txt' file
                    try:
                        if(not checkExistence(sucessFilePath,sucessRateText)):
                            f = open(sucessFilePath, "a")
                            f.write("\n{}".format(sucessRateText))
                            f.close()
                    except:
                        f = open(sucessFilePath, "a")
                        f.write("\n{}".format(sucessRateText))
                        f.close()

                    # write the overall retransmission rate to the 'overall_retransmission_rates.txt' file
                    try:
                        if(not checkExistence(retransmissionFilePath,retransmissionRateText)):
                            f = open(retransmissionFilePath, "a")
                            f.write("\n{}".format(retransmissionRateText))
                            f.close()
                    except:
                        f = open(retransmissionFilePath, "a")
                        f.write("\n{}".format(retransmissionRateText))
                        f.close()

                    # print the result in the console
                    print("\033[96m\t{}\033[00m" .format(sucessRateText))
                    print("\033[91m\t{}\033[00m" .format(retransmissionRateText))
                    print()

                # compute the periodic sucess and retransmission rates    
                newTimes = relativeTimeFromAPointOfTime(firstTime,flowDirectionsLists[i].__getitem__(j))
                newTimes_RE = relativeTimeFromAPointOfTime(firstTime,flowDirectionsLists_RE[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfSucessRates = computePeriodicSucessRateNB(newTimes,newTimes_RE,duration)
                listOfRetransmissionRates = [100-x for x in listOfSucessRates]
                x = newTimesPeriods
                y_sucess = listOfSucessRates
                y_RE = listOfRetransmissionRates
                yLabel = '{}'.format(flowDirections[i]) 
                ax1.plot(x,y_sucess,label=yLabel,c='{}'.format(colors[i]),marker = '.',linestyle='-')
                ax2.plot(x,y_RE,label=yLabel,c='{}'.format(colors[i]),marker = '.',linestyle='-')
                
            ax1.legend(loc='best', fontsize=10)
            ax2.legend(loc='best', fontsize=10)
            ax1.grid(color='grey', linestyle='--', linewidth=0.5)
            ax2.grid(color='grey', linestyle='--', linewidth=0.5)
            ax1.set_xlabel('time in (sec)', fontsize=12)
            ax2.set_xlabel('time in (sec)', fontsize=12)
            ax1.set_ylabel('sucess rate percentage', fontsize=12)
            ax2.set_ylabel('retransmission rate percentage', fontsize=12)
            ax1.set_title("{} sucess rate of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            ax2.set_title("{} retransmission rate of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            fig1.savefig('{}/{}_duration_{}_sucessRate.png'.format(sucessFolderPath,labels[j],duration),dpi=saved_graph_resolution)
            fig2.savefig('{}/{}_duration_{}_retransmissionRate.png'.format(retransmissionFolderPath,labels[j],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### Line Graph 3 ####################
    # Line Graph for sucess and retransmission rates based on the # of frames for different time durations from HMD traces folder (for all data types and both directions [uplink and downlink])
    
    sucessFolderPath = "{}/{}".format(sucessPrefix,"{}_{}".format(labels[3],flowDirections[2]))
    retransmissionFolderPath = "{}/{}".format(retransmissionPrefix,"{}_{}".format(labels[3],flowDirections[2]))
    try:
        os.mkdir(sucessFolderPath)
        os.mkdir(retransmissionFolderPath)
    except:
        pass
    overallSucessRate = computeOverallSucessRateNB(tempHMD_Data_Times,tempHMD_RE_Data_Times)
    overallRetransmissionRate = 100 - overallSucessRate
    sucessRateText = "[+] the overall sucess rate of {}-{} is {}".format(labels[3],flowDirections[2],overallSucessRate)
    retransmissionRateText = "[+] the overall retrnamission rate of {}-{} is {}".format(labels[3],flowDirections[2],overallRetransmissionRate)
    sucessFileTitle = "overall_sucess_rates.txt"
    retransmissionFileTitle = "overall_retransmission_rates.txt"
    sucessFilePath = "{}/{}".format(sucessFolderPath,sucessFileTitle)
    retransmissionFilePath = "{}/{}".format(retransmissionFolderPath,retransmissionFileTitle)
    # write the overall sucess rate to the 'overall_sucess_rates.txt' file
    try:
        if(not checkExistence(sucessFilePath,sucessRateText)):
            f = open(sucessFilePath, "a")
            f.write("\n{}".format(sucessRateText))
            f.close()
    except:
        f = open(sucessFilePath, "a")
        f.write("\n{}".format(sucessRateText))
        f.close()

    # write the overall retransmission rate to the 'overall_retransmission_rates.txt' file
    try:
        if(not checkExistence(retransmissionFilePath,retransmissionRateText)):
            f = open(retransmissionFilePath, "a")
            f.write("\n{}".format(retransmissionRateText))
            f.close()
    except:
        f = open(retransmissionFilePath, "a")
        f.write("\n{}".format(retransmissionRateText))
        f.close()

    # print the result in the console
    print("\033[96m\t{}\033[00m" .format(sucessRateText))
    print("\033[91m\t{}\033[00m" .format(retransmissionRateText))
    print()


    for duration in durations: 
        # [D] all data frames
        fig1, ax1 = plt.subplots()
        fig2, ax2 = plt.subplots() 
        fig3, ax3 = plt.subplots() 
        newTimes = relativeTimeFromAPointOfTime(tempHMD_Data_Times[0],tempHMD_Data_Times)
        newTimes_RE = relativeTimeFromAPointOfTime(tempHMD_Data_Times[0],tempHMD_RE_Data_Times)
        newTimesPeriods = convertTimeToPeriods(newTimes,duration)
        listOfSucessRates = computePeriodicSucessRateNB(newTimes,newTimes_RE,duration)
        listOfRetransmissionRates = [100-x for x in listOfSucessRates]
        x = newTimesPeriods
        y1 = listOfSucessRates
        y2 = listOfRetransmissionRates
        ylabel  = "all data types - both directions"
        y1Label = "sucess rate"
        y2Label = "retransmission rate"
        ax1.plot(x,y1,label=yLabel,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        ax2.plot(x,y2,label=yLabel,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        ax3.plot(x,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        ax3.plot(x,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        ax1.legend(loc='best', fontsize=10)
        ax2.legend(loc='best', fontsize=10)
        ax3.legend(loc='best', fontsize=10)
        ax1.grid(color='grey', linestyle='--', linewidth=0.5)
        ax2.grid(color='grey', linestyle='--', linewidth=0.5)
        ax3.grid(color='grey', linestyle='--', linewidth=0.5)
        ax1.set_xlabel('time in (sec)', fontsize=12)
        ax2.set_xlabel('time in (sec)', fontsize=12)
        ax3.set_xlabel('time in (sec)', fontsize=12)
        ax1.set_ylabel('sucess rate percentage', fontsize=12)
        ax2.set_ylabel('retransmission rate percentage', fontsize=12)
        ax3.set_ylabel('rate percentage', fontsize=12)
        ax1.set_title("{}-{} sucess rate of {} \nfor a duration of {} sec".format(labels[3],flowDirections[2],gameName,duration),fontsize=10)
        ax2.set_title("{}-{} retransmission rate of {} \nfor a duration of {} sec".format(labels[3],flowDirections[2],gameName,duration),fontsize=10)
        ax3.set_title("{}-{} sucess and retransmission rates of {} \nfor a duration of {} sec".format(labels[3],flowDirections[2],gameName,duration),fontsize=10)
        fig1.savefig('{}/{}_duration_{}_sucessRate.png'.format(sucessFolderPath,labels[3],duration),dpi=saved_graph_resolution)
        fig2.savefig('{}/{}_duration_{}_retransmissionRate.png'.format(retransmissionFolderPath,labels[3],duration),dpi=saved_graph_resolution)
        fig3.savefig('{}/{}_duration_{}_sucessANDretransmissionRate.png'.format(sucessFolderPath,labels[3],duration),dpi=saved_graph_resolution)
        fig3.savefig('{}/{}_duration_{}_sucessANDretransmissionRate.png'.format(retransmissionFolderPath,labels[3],duration),dpi=saved_graph_resolution)
        plt.show()

    #################### CDF  Graph 1 ####################
    # CDF Graph for sucess and retransmission rates based on the # of frames for different time durations from HMD traces folder (each direction will be in a graph)
    for duration in durations:
        for i in range(len(flowDirections)):
            sucessFolderPath = "{}/{}".format(sucessPrefix,flowDirections[i])
            retransmissionFolderPath = "{}/{}".format(retransmissionPrefix,flowDirections[i])
            try:
                os.mkdir(sucessFolderPath)
                os.mkdir(retransmissionFolderPath)
            except:
                pass
            firstFrame[i] = min(flowDirectionsLists[i].__getitem__(0)[0] if i==0 else 100000000,flowDirectionsLists[i].__getitem__(1)[0],flowDirectionsLists[i].__getitem__(2)[0])
            fig1, ax1 = plt.subplots()
            fig2, ax2 = plt.subplots()
            for j in range(len(flowDirectionsLists[i])):
                if(i == 1 and j ==0):
                    continue
                # compute the periodic sucess and retransmission rates
                newTimes = relativeTimeFromAPointOfTime(firstFrame[i],flowDirectionsLists[i].__getitem__(j))
                newTimes_RE = relativeTimeFromAPointOfTime(firstFrame[i],flowDirectionsLists_RE[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfSucessRates = computePeriodicSucessRateNB(newTimes,newTimes_RE,duration)
                listOfRetransmissionRates = [100-x for x in listOfSucessRates]
                data_sucess = [float(value) for value in listOfSucessRates]
                x_sucess = np.sort(data_sucess)
                y_sucess = np.arange(len(x_sucess))/float(len(x_sucess))
                data_retransmission = [float(value) for value in listOfRetransmissionRates]
                x_retransmission = np.sort(data_retransmission)
                y_retransmission = np.arange(len(x_retransmission))/float(len(x_retransmission))
                yLabel = '{}'.format(labels[j]) 
                ax1.plot(x_sucess,y_sucess,label=yLabel,c='{}'.format(colors[j]),linestyle='{}'.format(lineStyles[j]))
                ax2.plot(x_retransmission,y_retransmission,label=yLabel,c='{}'.format(colors[j]),linestyle='{}'.format(lineStyles[j]))
            ax1.legend(loc='best', fontsize=10)
            ax2.legend(loc='best', fontsize=10)
            ax1.grid(color='grey', linestyle='--', linewidth=0.5)
            ax2.grid(color='grey', linestyle='--', linewidth=0.5)
            ax1.set_xlabel('sucess rate percentage', fontsize=12)
            ax2.set_xlabel('retransmission rate percentage', fontsize=12)
            ax1.set_ylabel('CDF', fontsize=12)
            ax2.set_ylabel('CDF', fontsize=12)
            ax1.set_title("CDF of {} sucess rate of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            ax2.set_title("CDF of {} retransmission rate of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            fig1.savefig('{}/{}_duration_{}_sucessRate_CDF.png'.format(sucessFolderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            fig2.savefig('{}/{}_duration_{}_retransmissionRate_CDF.png'.format(retransmissionFolderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### CDF  Graph 2 ####################
    # CDF Graph for sucess and retransmission rates based on the # of frames for different time durations from HMD traces folder (each data type will be in a graph)
    for duration in durations:
        for j in range(len(labels)):
            firstTime = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0]) if not j == 0 else flowDirectionsLists[0].__getitem__(j)[0]
            fig1, ax1 = plt.subplots()
            fig2, ax2 = plt.subplots()
            for i in range(len(flowDirections)):
                if(i == 1 and j ==0):
                        continue
                sucessFolderPath = "{}/{}".format(sucessPrefix,labels[j])
                retransmissionFolderPath = "{}/{}".format(retransmissionPrefix,labels[j])
                try:
                    os.mkdir(sucessFolderPath)
                    os.mkdir(retransmissionFolderPath)
                except:
                    pass
                # compute the periodic sucess and retransmission rates    
                newTimes = relativeTimeFromAPointOfTime(firstTime,flowDirectionsLists[i].__getitem__(j))
                newTimes_RE = relativeTimeFromAPointOfTime(firstTime,flowDirectionsLists_RE[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfSucessRates = computePeriodicSucessRateNB(newTimes,newTimes_RE,duration)
                listOfRetransmissionRates = [100-x for x in listOfSucessRates]
                data_sucess = [float(value) for value in listOfSucessRates]
                x_sucess = np.sort(data_sucess)
                y_sucess = np.arange(len(x_sucess))/float(len(x_sucess))
                data_retransmission = [float(value) for value in listOfRetransmissionRates]
                x_retransmission = np.sort(data_retransmission)
                y_retransmission = np.arange(len(x_retransmission))/float(len(x_retransmission))
                yLabel = '{}'.format(flowDirections[i]) 
                ax1.plot(x_sucess,y_sucess,label=yLabel,c='{}'.format(colors[i]),linestyle='{}'.format(lineStyles[i]))
                ax2.plot(x_retransmission,y_retransmission,label=yLabel,c='{}'.format(colors[i]),linestyle='{}'.format(lineStyles[i]))
                
            ax1.legend(loc='best', fontsize=10)
            ax2.legend(loc='best', fontsize=10)
            ax1.grid(color='grey', linestyle='--', linewidth=0.5)
            ax2.grid(color='grey', linestyle='--', linewidth=0.5)
            ax1.set_xlabel('sucess rate percentage', fontsize=12)
            ax2.set_xlabel('retransmission rate percentage', fontsize=12)
            ax1.set_ylabel('CDF', fontsize=12)
            ax2.set_ylabel('CDF', fontsize=12)
            ax1.set_title("CDF of {} sucess rate of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            ax2.set_title("CDF of {} retransmission rate of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            fig1.savefig('{}/{}_duration_{}_sucessRate_CDF.png'.format(sucessFolderPath,labels[j],duration),dpi=saved_graph_resolution)
            fig2.savefig('{}/{}_duration_{}_retransmissionRateCDF.png'.format(retransmissionFolderPath,labels[j],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### CDF  Graph 3 ####################
    # CDF Graph for sucess and retransmission rates based on the # of frames for different time durations from HMD traces folder (for all data types and both directions [uplink and downlink])
    
    sucessFolderPath = "{}/{}".format(sucessPrefix,"{}_{}".format(labels[3],flowDirections[2]))
    retransmissionFolderPath = "{}/{}".format(retransmissionPrefix,"{}_{}".format(labels[3],flowDirections[2]))
    try:
        os.mkdir(sucessFolderPath)
        os.mkdir(retransmissionFolderPath)
    except:
        pass

    for duration in durations: 
        # [D] all data frames
        fig1, ax1 = plt.subplots()
        fig2, ax2 = plt.subplots() 
        fig3, ax3 = plt.subplots() 
        newTimes = relativeTimeFromAPointOfTime(tempHMD_Data_Times[0],tempHMD_Data_Times)
        newTimes_RE = relativeTimeFromAPointOfTime(tempHMD_Data_Times[0],tempHMD_RE_Data_Times)
        newTimesPeriods = convertTimeToPeriods(newTimes,duration)
        listOfSucessRates = computePeriodicSucessRateNB(newTimes,newTimes_RE,duration)
        listOfRetransmissionRates = [100-x for x in listOfSucessRates]
        data_sucess = [float(value) for value in listOfSucessRates]
        data_retransmission = [float(value) for value in listOfRetransmissionRates]
        x_sucess = np.sort(data_sucess)
        x_retransmission = np.sort(data_retransmission)
        y_sucess = np.arange(len(x_sucess))/float(len(x_sucess))
        y_retransmission = np.arange(len(x_retransmission))/float(len(x_retransmission))
        ylabel  = "all data types - both directions"
        y1Label = "sucess rate"
        y2Label = "retransmission rate"
        ax1.plot(x_sucess,y_sucess,label=yLabel,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        ax2.plot(x_retransmission,y_retransmission,label=yLabel,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        ax3.plot(x_sucess,y_sucess,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        ax3.plot(x_retransmission,y_retransmission,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        ax1.legend(loc='best', fontsize=10)
        ax2.legend(loc='best', fontsize=10)
        ax3.legend(loc='best', fontsize=10)
        ax1.grid(color='grey', linestyle='--', linewidth=0.5)
        ax2.grid(color='grey', linestyle='--', linewidth=0.5)
        ax3.grid(color='grey', linestyle='--', linewidth=0.5)
        ax1.set_xlabel('sucess rate percentage', fontsize=12)
        ax2.set_xlabel('retransmission rate percentage', fontsize=12)
        ax3.set_xlabel('rate percentage', fontsize=12)
        ax1.set_ylabel('CDF', fontsize=12)
        ax2.set_ylabel('CDF', fontsize=12)
        ax3.set_ylabel('CDF', fontsize=12)
        ax1.set_title("{}-{} CDF of sucess rate of {} \nfor a duration of {} sec".format(labels[3],flowDirections[2],gameName,duration),fontsize=10)
        ax2.set_title("{}-{} CDF of retransmission rate of {} \nfor a duration of {} sec".format(labels[3],flowDirections[2],gameName,duration),fontsize=10)
        ax3.set_title("{}-{} CDF of sucess and retransmission rates of {} \nfor a duration of {} sec".format(labels[3],flowDirections[2],gameName,duration),fontsize=10)
        fig1.savefig('{}/{}_duration_{}_sucessRate_CDF.png'.format(sucessFolderPath,labels[3],duration),dpi=saved_graph_resolution)
        fig2.savefig('{}/{}_duration_{}_retransmissionRate_CDF.png'.format(retransmissionFolderPath,labels[3],duration),dpi=saved_graph_resolution)
        fig3.savefig('{}/{}_duration_{}_sucessANDretransmissionRate_CDF.png'.format(sucessFolderPath,labels[3],duration),dpi=saved_graph_resolution)
        fig3.savefig('{}/{}_duration_{}_sucessANDretransmissionRate_CDF.png'.format(retransmissionFolderPath,labels[3],duration),dpi=saved_graph_resolution)
        plt.show()
    ######################################################



def plotHMDSucessRateFrameSize(root_folder,gameName,results):
    result_folder_name_sucess = "HMD/sucess_rates"
    result_folder_name_retransmission = "HMD/retransmission_rates"
    tempSucessPrefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name_sucess)
    tempRetransmissionPrefix = "{}/{}/{}".format(root_folder,gameName,result_folder_name_retransmission)
    sucessPrefix = "{}/{}".format(tempSucessPrefix,"based_on_size_of_Frames")
    retransmissionPrefix = "{}/{}".format(tempRetransmissionPrefix,"based_on_size_of_Frames")
    try:
        os.mkdir(tempSucessPrefix)
        os.mkdir(tempRetransmissionPrefix)
    except:
        pass
    try:
        os.mkdir(sucessPrefix)
        os.mkdir(retransmissionPrefix)
    except:
        pass

    print("\033[93m{}\033[00m" .format("overall rates based on size of frames: "))

    newResults = eliminateRetransmittedFrames(results)
    HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates,\
        HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes, HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times,\
        HMD_DWN_MANAGEMENT_FRAMES_DataRates, HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes, HMD_UP_DATA1_FRAMES_NBs, \
        HMD_UP_DATA1_FRAMES_Times, HMD_UP_DATA1_FRAMES_DataRates, HMD_UP_DATA1_FRAMES_Frames_Sizes,\
        HMD_UP_DATA1_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA1_FRAMES_NBs, HMD_UP_RE_DATA1_FRAMES_Times, \
        HMD_UP_RE_DATA1_FRAMES_DataRates, HMD_UP_RE_DATA1_FRAMES_Frames_Sizes, HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB,\
        HMD_UP_DATA2_FRAMES_NBs, HMD_UP_DATA2_FRAMES_Times, HMD_UP_DATA2_FRAMES_DataRates, HMD_UP_DATA2_FRAMES_Data_Sizes,\
        HMD_UP_DATA2_FRAMES_Frames_Sizes, HMD_UP_DATA2_FRAMES_Frames_SeqNB, HMD_DWN_DATA2_FRAMES_NBs, HMD_DWN_DATA2_FRAMES_Times, \
        HMD_DWN_DATA2_FRAMES_DataRates, HMD_DWN_DATA2_FRAMES_Data_Sizes, HMD_DWN_DATA2_FRAMES_Frames_Sizes, \
        HMD_DWN_DATA2_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA2_FRAMES_NBs, HMD_UP_RE_DATA2_FRAMES_Times, HMD_UP_RE_DATA2_FRAMES_DataRates,\
        HMD_UP_RE_DATA2_FRAMES_Data_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB, \
        HMD_DWN_RE_DATA2_FRAMES_NBs, HMD_DWN_RE_DATA2_FRAMES_Times, HMD_DWN_RE_DATA2_FRAMES_DataRates, HMD_DWN_RE_DATA2_FRAMES_Data_Sizes,\
        HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB, HMD_UP_DATA3_FRAMES_NBs, HMD_UP_DATA3_FRAMES_Times, \
        HMD_UP_DATA3_FRAMES_DataRates, HMD_UP_DATA3_FRAMES_Data_Sizes, HMD_UP_DATA3_FRAMES_Frames_Sizes, HMD_UP_DATA3_FRAMES_Frames_SeqNB,\
        HMD_DWN_DATA3_FRAMES_NBs, HMD_DWN_DATA3_FRAMES_Times, HMD_DWN_DATA3_FRAMES_DataRates, HMD_DWN_DATA3_FRAMES_Data_Sizes,\
        HMD_DWN_DATA3_FRAMES_Frames_Sizes, HMD_DWN_DATA3_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA3_FRAMES_NBs, HMD_UP_RE_DATA3_FRAMES_Times, \
        HMD_UP_RE_DATA3_FRAMES_DataRates, HMD_UP_RE_DATA3_FRAMES_Data_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_Sizes, \
        HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB, HMD_DWN_RE_DATA3_FRAMES_NBs, HMD_DWN_RE_DATA3_FRAMES_Times, HMD_DWN_RE_DATA3_FRAMES_DataRates, \
        HMD_DWN_RE_DATA3_FRAMES_Data_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB = newResults   
    
    uniqueDataCombinedLists,retransmittedDataCombinedLists = combinedResultsLists(results,0)
    HMD_UP_NBs,HMD_UP_Times,HMD_UP_DataRates,HMD_UP_Data_Sizes,HMD_UP_Frames_Sizes,HMD_UP_Frames_SeqNB,HMD_DWN_NBs,HMD_DWN_Times,HMD_DWN_DataRates,HMD_DWN_Data_Sizes,HMD_DWN_Frames_Sizes,HMD_DWN_Frames_SeqNB = uniqueDataCombinedLists
    HMD_UP_RE_NBs,HMD_UP_RE_Times,HMD_UP_RE_DataRates,HMD_UP_RE_Data_Sizes,HMD_UP_RE_Frames_Sizes,HMD_UP_RE_Frames_SeqNB,HMD_DWN_RE_NBs,HMD_DWN_RE_Times,HMD_DWN_RE_DataRates,HMD_DWN_RE_Data_Sizes,HMD_DWN_RE_Frames_Sizes,HMD_DWN_RE_Frames_SeqNB = retransmittedDataCombinedLists
    
    # times and sizes of frames for both directions of each data type and retransmission data types
    tempHMD_DATA1_FRAMES_Times = HMD_UP_DATA1_FRAMES_Times
    tempHMD_DATA2_FRAMES_Times = HMD_UP_DATA2_FRAMES_Times + HMD_DWN_DATA2_FRAMES_Times
    tempHMD_DATA3_FRAMES_Times = HMD_UP_DATA3_FRAMES_Times + HMD_DWN_DATA3_FRAMES_Times
    tempHMD_DATA_FRAMES_Times  = HMD_UP_Times + HMD_DWN_Times
    tempHMD_DATA1_FRAMES_Frames_Sizes = HMD_UP_DATA1_FRAMES_Frames_Sizes
    tempHMD_DATA2_FRAMES_Frames_Sizes = HMD_UP_DATA2_FRAMES_Frames_Sizes + HMD_DWN_DATA2_FRAMES_Frames_Sizes
    tempHMD_DATA3_FRAMES_Frames_Sizes = HMD_UP_DATA3_FRAMES_Frames_Sizes + HMD_DWN_DATA3_FRAMES_Frames_Sizes
    tempHMD_DATA_FRAMES_Frames_Sizes  = HMD_UP_Frames_Sizes + HMD_DWN_Frames_Sizes
    tempHMD_DATA2_FRAMES_Times, tempHMD_DATA2_FRAMES_Frames_Sizes = sort_two_lists(tempHMD_DATA2_FRAMES_Times, tempHMD_DATA2_FRAMES_Frames_Sizes)
    tempHMD_DATA3_FRAMES_Times, tempHMD_DATA3_FRAMES_Frames_Sizes = sort_two_lists(tempHMD_DATA3_FRAMES_Times, tempHMD_DATA3_FRAMES_Frames_Sizes)
    tempHMD_DATA_FRAMES_Times, tempHMD_DATA_FRAMES_Frames_Sizes   = sort_two_lists(tempHMD_DATA_FRAMES_Times, tempHMD_DATA_FRAMES_Frames_Sizes)

    tempHMD_RE_DATA1_FRAMES_Times = HMD_UP_RE_DATA1_FRAMES_Times
    tempHMD_RE_DATA2_FRAMES_Times = HMD_UP_RE_DATA2_FRAMES_Times + HMD_DWN_RE_DATA2_FRAMES_Times
    tempHMD_RE_DATA3_FRAMES_Times = HMD_UP_RE_DATA3_FRAMES_Times + HMD_DWN_RE_DATA3_FRAMES_Times
    tempHMD_RE_DATA_FRAMES_Times  = HMD_UP_RE_Times + HMD_DWN_RE_Times
    tempHMD_RE_DATA1_FRAMES_Frames_Sizes = HMD_UP_RE_DATA1_FRAMES_Frames_Sizes
    tempHMD_RE_DATA2_FRAMES_Frames_Sizes = HMD_UP_RE_DATA2_FRAMES_Frames_Sizes + HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes
    tempHMD_RE_DATA3_FRAMES_Frames_Sizes = HMD_UP_RE_DATA3_FRAMES_Frames_Sizes + HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes
    tempHMD_RE_DATA_FRAMES_Frames_Sizes  = HMD_UP_RE_Frames_Sizes + HMD_DWN_RE_Frames_Sizes
    tempHMD_RE_DATA2_FRAMES_Times, tempHMD_RE_DATA2_FRAMES_Frames_Sizes = sort_two_lists(tempHMD_RE_DATA2_FRAMES_Times, tempHMD_RE_DATA2_FRAMES_Frames_Sizes)
    tempHMD_RE_DATA3_FRAMES_Times, tempHMD_RE_DATA3_FRAMES_Frames_Sizes = sort_two_lists(tempHMD_RE_DATA3_FRAMES_Times, tempHMD_RE_DATA3_FRAMES_Frames_Sizes)
    tempHMD_RE_DATA_FRAMES_Times, tempHMD_RE_DATA_FRAMES_Frames_Sizes   = sort_two_lists(tempHMD_RE_DATA_FRAMES_Times, tempHMD_RE_DATA_FRAMES_Frames_Sizes)

    # times of sizes frames for both directions for all data types and retransmission data types
    tempHMD_Data_Times    = tempHMD_DATA1_FRAMES_Times + tempHMD_DATA2_FRAMES_Times + tempHMD_DATA3_FRAMES_Times
    tempHMD_RE_Data_Times = tempHMD_RE_DATA1_FRAMES_Times + tempHMD_RE_DATA2_FRAMES_Times + tempHMD_RE_DATA3_FRAMES_Times
    tempHMD_Data_Frames_Sizes    = tempHMD_DATA1_FRAMES_Frames_Sizes + tempHMD_DATA2_FRAMES_Frames_Sizes + tempHMD_DATA3_FRAMES_Frames_Sizes
    tempHMD_RE_Data_Frames_Sizes = tempHMD_RE_DATA1_FRAMES_Frames_Sizes + tempHMD_RE_DATA2_FRAMES_Frames_Sizes + tempHMD_RE_DATA3_FRAMES_Frames_Sizes
    tempHMD_Data_Times,tempHMD_Data_Frames_Sizes = sort_two_lists(tempHMD_Data_Times,tempHMD_Data_Frames_Sizes)
    tempHMD_RE_Data_Times,tempHMD_RE_Data_Frames_Sizes = sort_two_lists(tempHMD_RE_Data_Times,tempHMD_RE_Data_Frames_Sizes)

    durations = [1,10,15,30,60]  # in seconds
    flowDirections = ["uplink","downlink","both_directions"]
    flowDirectionsLists = [(HMD_UP_DATA1_FRAMES_Times,HMD_UP_DATA2_FRAMES_Times,HMD_UP_DATA3_FRAMES_Times,HMD_UP_Times),
                            ([],HMD_DWN_DATA2_FRAMES_Times,HMD_DWN_DATA3_FRAMES_Times,HMD_DWN_Times),
                            (tempHMD_DATA1_FRAMES_Times,tempHMD_DATA2_FRAMES_Times,tempHMD_DATA3_FRAMES_Times,tempHMD_DATA_FRAMES_Times)]
    flowDirectionsLists_RE = [(HMD_UP_RE_DATA1_FRAMES_Times,HMD_UP_RE_DATA2_FRAMES_Times,HMD_UP_RE_DATA3_FRAMES_Times,HMD_UP_RE_Times),
                            ([],HMD_DWN_RE_DATA2_FRAMES_Times,HMD_DWN_RE_DATA3_FRAMES_Times,HMD_DWN_RE_Times),
                            (tempHMD_RE_DATA1_FRAMES_Times,tempHMD_RE_DATA2_FRAMES_Times,tempHMD_RE_DATA3_FRAMES_Times,tempHMD_RE_DATA_FRAMES_Times)]
    listOfFrameSizes =   [(HMD_UP_DATA1_FRAMES_Frames_Sizes,HMD_UP_DATA2_FRAMES_Frames_Sizes,HMD_UP_DATA3_FRAMES_Frames_Sizes,HMD_UP_Frames_Sizes),
                            ([],HMD_DWN_DATA2_FRAMES_Frames_Sizes,HMD_DWN_DATA3_FRAMES_Frames_Sizes,HMD_DWN_Frames_Sizes),
                            (tempHMD_DATA1_FRAMES_Frames_Sizes,tempHMD_DATA2_FRAMES_Frames_Sizes,tempHMD_DATA3_FRAMES_Frames_Sizes,tempHMD_DATA_FRAMES_Frames_Sizes)]
    listOfFrameSizes_RE =[(HMD_UP_RE_DATA1_FRAMES_Frames_Sizes,HMD_UP_RE_DATA2_FRAMES_Frames_Sizes,HMD_UP_RE_DATA3_FRAMES_Frames_Sizes,HMD_UP_RE_Frames_Sizes),
                            ([],HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes,HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes,HMD_DWN_RE_Frames_Sizes),
                            (tempHMD_RE_DATA1_FRAMES_Frames_Sizes,tempHMD_RE_DATA2_FRAMES_Frames_Sizes,tempHMD_RE_DATA3_FRAMES_Frames_Sizes,tempHMD_RE_DATA_FRAMES_Frames_Sizes)]
    
    colors = ["red","blue","green","black","purple","cyan","pink"]
    lineStyles = ['-.',':',"--","-",'-.',':',"--"]
    markers = [".",",","1","x","|","+","v"]
    labels = ["data type1","data type2","data type3","all_data_types"]
    firstFrame = [0.0,0.0,0.0]

    #################### Line Graph 1 ####################    
    # Line Graph for sucess and retransmission rates based on the # of frames for different time durations from HMD traces folder (each direction will be in a graph)
    overallRatesFlag = True
    firstIteration = True
    for duration in durations:
        if(not firstIteration):
            overallRatesFlag = False
        firstIteration = False
        for i in range(len(flowDirections)):
            sucessFolderPath = "{}/{}".format(sucessPrefix,flowDirections[i])
            retransmissionFolderPath = "{}/{}".format(retransmissionPrefix,flowDirections[i])
            try:
                os.mkdir(sucessFolderPath)
                os.mkdir(retransmissionFolderPath)
            except:
                pass
            firstFrame[i] = min(flowDirectionsLists[i].__getitem__(0)[0] if i==0 else 100000000,flowDirectionsLists[i].__getitem__(1)[0],flowDirectionsLists[i].__getitem__(2)[0])
            fig1, ax1 = plt.subplots()
            fig2, ax2 = plt.subplots()
            for j in range(len(flowDirectionsLists[i])):
                if(i == 1 and j ==0):
                    continue
                # compute the overall sucess and retransmission rates based on frames sizes
                if(overallRatesFlag):
                    overallSucessRate = computeOverallSucessRateSize(listOfFrameSizes[i].__getitem__(j),listOfFrameSizes_RE[i].__getitem__(j))
                    overallRetransmissionRate = 100 - overallSucessRate
                    sucessRateText = "[+] the overall sucess rate of {}-{} is {}".format(labels[j],flowDirections[i],overallSucessRate)
                    retransmissionRateText = "[+] the overall retrnamission rate of {}-{} is {}".format(labels[j],flowDirections[i],overallRetransmissionRate)
                    sucessFileTitle = "overall_sucess_rates.txt"
                    retransmissionFileTitle = "overall_retransmission_rates.txt"
                    sucessFilePath = "{}/{}".format(sucessFolderPath,sucessFileTitle)
                    retransmissionFilePath = "{}/{}".format(retransmissionFolderPath,retransmissionFileTitle)
                    # write the overall sucess rate to the 'overall_sucess_rates.txt' file
                    try:
                        if(not checkExistence(sucessFilePath,sucessRateText)):
                            f = open(sucessFilePath, "a")
                            f.write("\n{}".format(sucessRateText))
                            f.close()
                    except:
                        f = open(sucessFilePath, "a")
                        f.write("\n{}".format(sucessRateText))
                        f.close()

                    # write the overall retransmission rate to the 'overall_retransmission_rates.txt' file
                    try:
                        if(not checkExistence(retransmissionFilePath,retransmissionRateText)):
                            f = open(retransmissionFilePath, "a")
                            f.write("\n{}".format(retransmissionRateText))
                            f.close()
                    except:
                        f = open(retransmissionFilePath, "a")
                        f.write("\n{}".format(retransmissionRateText))
                        f.close()

                    # print the result in the console
                    print("\033[96m\t{}\033[00m" .format(sucessRateText))
                    print("\033[91m\t{}\033[00m" .format(retransmissionRateText))
                    print()

                # compute the periodic sucess and retransmission rates
                newTimes = relativeTimeFromAPointOfTime(firstFrame[i],flowDirectionsLists[i].__getitem__(j))
                newTimes_RE = relativeTimeFromAPointOfTime(firstFrame[i],flowDirectionsLists_RE[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfSucessRates = computePeriodicSucessRateSize(newTimes,listOfFrameSizes[i].__getitem__(j),newTimes_RE,listOfFrameSizes_RE[i].__getitem__(j),duration)
                listOfRetransmissionRates = [100-x for x in listOfSucessRates]
                x = newTimesPeriods
                y_sucess = listOfSucessRates
                y_RE = listOfRetransmissionRates
                yLabel = '{}'.format(labels[j]) 
                ax1.plot(x,y_sucess,label=yLabel,c='{}'.format(colors[j]),marker = '.',linestyle='-')
                ax2.plot(x,y_RE,label=yLabel,c='{}'.format(colors[j]),marker = '.',linestyle='-')
            ax1.legend(loc='best', fontsize=10)
            ax2.legend(loc='best', fontsize=10)
            ax1.grid(color='grey', linestyle='--', linewidth=0.5)
            ax2.grid(color='grey', linestyle='--', linewidth=0.5)
            ax1.set_xlabel('time in (sec)', fontsize=12)
            ax2.set_xlabel('time in (sec)', fontsize=12)
            ax1.set_ylabel('sucess rate percentage', fontsize=12)
            ax2.set_ylabel('retransmission rate percentage', fontsize=12)
            ax1.set_title("{} sucess rate of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            ax2.set_title("{} retransmission rate of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            fig1.savefig('{}/{}_duration_{}_sucessRate.png'.format(sucessFolderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            fig2.savefig('{}/{}_duration_{}_retransmissionRate.png'.format(retransmissionFolderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################


    #################### Line Graph 2 ####################    
    # Line Graph for sucess and retransmission rates based on the # of frames for different time durations from HMD traces folder (each data type will be in a graph)
    overallRatesFlag = True
    firstIteration = True
    for duration in durations:
        if(not firstIteration):
            overallRatesFlag = False
        firstIteration = False
        for j in range(len(labels)):
            firstTime = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0]) if not j == 0 else flowDirectionsLists[0].__getitem__(j)[0]
            fig1, ax1 = plt.subplots()
            fig2, ax2 = plt.subplots()
            for i in range(len(flowDirections)):
                if(i == 1 and j ==0):
                        continue
                sucessFolderPath = "{}/{}".format(sucessPrefix,labels[j])
                retransmissionFolderPath = "{}/{}".format(retransmissionPrefix,labels[j])
                try:
                    os.mkdir(sucessFolderPath)
                    os.mkdir(retransmissionFolderPath)
                except:
                    pass
                # compute the overall sucess and retransmission rates
                if(overallRatesFlag):
                    overallSucessRate = computeOverallSucessRateSize(listOfFrameSizes[i].__getitem__(j),listOfFrameSizes_RE[i].__getitem__(j))
                    overallRetransmissionRate = 100 - overallSucessRate
                    sucessRateText = "[+] the overall sucess rate of {}-{} is {}".format(labels[j],flowDirections[i],overallSucessRate)
                    retransmissionRateText = "[+] the overall retrnamission rate of {}-{} is {}".format(labels[j],flowDirections[i],overallRetransmissionRate)
                    sucessFileTitle = "overall_sucess_rates.txt"
                    retransmissionFileTitle = "overall_retransmission_rates.txt"
                    sucessFilePath = "{}/{}".format(sucessFolderPath,sucessFileTitle)
                    retransmissionFilePath = "{}/{}".format(retransmissionFolderPath,retransmissionFileTitle)
                    # write the overall sucess rate to the 'overall_sucess_rates.txt' file
                    try:
                        if(not checkExistence(sucessFilePath,sucessRateText)):
                            f = open(sucessFilePath, "a")
                            f.write("\n{}".format(sucessRateText))
                            f.close()
                    except:
                        f = open(sucessFilePath, "a")
                        f.write("\n{}".format(sucessRateText))
                        f.close()

                    # write the overall retransmission rate to the 'overall_retransmission_rates.txt' file
                    try:
                        if(not checkExistence(retransmissionFilePath,retransmissionRateText)):
                            f = open(retransmissionFilePath, "a")
                            f.write("\n{}".format(retransmissionRateText))
                            f.close()
                    except:
                        f = open(retransmissionFilePath, "a")
                        f.write("\n{}".format(retransmissionRateText))
                        f.close()

                    # print the result in the console
                    print("\033[96m\t{}\033[00m" .format(sucessRateText))
                    print("\033[91m\t{}\033[00m" .format(retransmissionRateText))
                    print()

                # compute the periodic sucess and retransmission rates    
                newTimes = relativeTimeFromAPointOfTime(firstTime,flowDirectionsLists[i].__getitem__(j))
                newTimes_RE = relativeTimeFromAPointOfTime(firstTime,flowDirectionsLists_RE[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfSucessRates = computePeriodicSucessRateSize(newTimes,listOfFrameSizes[i].__getitem__(j),newTimes_RE,listOfFrameSizes_RE[i].__getitem__(j),duration)
                listOfRetransmissionRates = [100-x for x in listOfSucessRates]
                x = newTimesPeriods
                y_sucess = listOfSucessRates
                y_RE = listOfRetransmissionRates
                yLabel = '{}'.format(flowDirections[i]) 
                ax1.plot(x,y_sucess,label=yLabel,c='{}'.format(colors[i]),marker = '.',linestyle='-')
                ax2.plot(x,y_RE,label=yLabel,c='{}'.format(colors[i]),marker = '.',linestyle='-')                
            ax1.legend(loc='best', fontsize=10)
            ax2.legend(loc='best', fontsize=10)
            ax1.grid(color='grey', linestyle='--', linewidth=0.5)
            ax2.grid(color='grey', linestyle='--', linewidth=0.5)
            ax1.set_xlabel('time in (sec)', fontsize=12)
            ax2.set_xlabel('time in (sec)', fontsize=12)
            ax1.set_ylabel('sucess rate percentage', fontsize=12)
            ax2.set_ylabel('retransmission rate percentage', fontsize=12)
            ax1.set_title("{} sucess rate of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            ax2.set_title("{} retransmission rate of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            fig1.savefig('{}/{}_duration_{}_sucessRate.png'.format(sucessFolderPath,labels[j],duration),dpi=saved_graph_resolution)
            fig2.savefig('{}/{}_duration_{}_retransmissionRate.png'.format(retransmissionFolderPath,labels[j],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### Line Graph 3 ####################
    # Line Graph for sucess and retransmission rates based on the # of frames for different time durations from HMD traces folder (for all data types and both directions [uplink and downlink])
    
    sucessFolderPath = "{}/{}".format(sucessPrefix,"{}_{}".format(labels[3],flowDirections[2]))
    retransmissionFolderPath = "{}/{}".format(retransmissionPrefix,"{}_{}".format(labels[3],flowDirections[2]))
    try:
        os.mkdir(sucessFolderPath)
        os.mkdir(retransmissionFolderPath)
    except:
        pass
    overallSucessRate = computeOverallSucessRateNB(tempHMD_Data_Frames_Sizes,tempHMD_RE_Data_Frames_Sizes)
    overallRetransmissionRate = 100 - overallSucessRate
    sucessRateText = "[+] the overall sucess rate of {}-{} is {}".format(labels[3],flowDirections[2],overallSucessRate)
    retransmissionRateText = "[+] the overall retrnamission rate of {}-{} is {}".format(labels[3],flowDirections[2],overallRetransmissionRate)
    sucessFileTitle = "overall_sucess_rates.txt"
    retransmissionFileTitle = "overall_retransmission_rates.txt"
    sucessFilePath = "{}/{}".format(sucessFolderPath,sucessFileTitle)
    retransmissionFilePath = "{}/{}".format(retransmissionFolderPath,retransmissionFileTitle)
    # write the overall sucess rate to the 'overall_sucess_rates.txt' file
    try:
        if(not checkExistence(sucessFilePath,sucessRateText)):
            f = open(sucessFilePath, "a")
            f.write("\n{}".format(sucessRateText))
            f.close()
    except:
        f = open(sucessFilePath, "a")
        f.write("\n{}".format(sucessRateText))
        f.close()

    # write the overall retransmission rate to the 'overall_retransmission_rates.txt' file
    try:
        if(not checkExistence(retransmissionFilePath,retransmissionRateText)):
            f = open(retransmissionFilePath, "a")
            f.write("\n{}".format(retransmissionRateText))
            f.close()
    except:
        f = open(retransmissionFilePath, "a")
        f.write("\n{}".format(retransmissionRateText))
        f.close()

    # print the result in the console
    print("\033[96m\t{}\033[00m" .format(sucessRateText))
    print("\033[91m\t{}\033[00m" .format(retransmissionRateText))
    print()


    for duration in durations: 
        # [D] all data frames
        fig1, ax1 = plt.subplots()
        fig2, ax2 = plt.subplots() 
        fig3, ax3 = plt.subplots() 
        newTimes = relativeTimeFromAPointOfTime(tempHMD_Data_Times[0],tempHMD_Data_Times)
        newTimes_RE = relativeTimeFromAPointOfTime(tempHMD_Data_Times[0],tempHMD_RE_Data_Times)
        newTimesPeriods = convertTimeToPeriods(newTimes,duration)
        listOfSucessRates = computePeriodicSucessRateSize(newTimes,tempHMD_Data_Frames_Sizes,newTimes_RE,tempHMD_RE_Data_Frames_Sizes,duration)
        listOfRetransmissionRates = [100-x for x in listOfSucessRates]
        x = newTimesPeriods
        y1 = listOfSucessRates
        y2 = listOfRetransmissionRates
        ylabel  = "all data types - both directions"
        y1Label = "sucess rate"
        y2Label = "retransmission rate"
        ax1.plot(x,y1,label=yLabel,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        ax2.plot(x,y2,label=yLabel,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        ax3.plot(x,y1,label=y1Label,c='{}'.format(colors[0]),marker = '.',linestyle='-')
        ax3.plot(x,y2,label=y2Label,c='{}'.format(colors[1]),marker = '.',linestyle='-')
        ax1.legend(loc='best', fontsize=10)
        ax2.legend(loc='best', fontsize=10)
        ax3.legend(loc='best', fontsize=10)
        ax1.grid(color='grey', linestyle='--', linewidth=0.5)
        ax2.grid(color='grey', linestyle='--', linewidth=0.5)
        ax3.grid(color='grey', linestyle='--', linewidth=0.5)
        ax1.set_xlabel('time in (sec)', fontsize=12)
        ax2.set_xlabel('time in (sec)', fontsize=12)
        ax3.set_xlabel('time in (sec)', fontsize=12)
        ax1.set_ylabel('sucess rate percentage', fontsize=12)
        ax2.set_ylabel('retransmission rate percentage', fontsize=12)
        ax3.set_ylabel('rate percentage', fontsize=12)
        ax1.set_title("{}-{} sucess rate of {} \nfor a duration of {} sec".format(labels[3],flowDirections[2],gameName,duration),fontsize=10)
        ax2.set_title("{}-{} retransmission rate of {} \nfor a duration of {} sec".format(labels[3],flowDirections[2],gameName,duration),fontsize=10)
        ax3.set_title("{}-{} sucess and retransmission rates of {} \nfor a duration of {} sec".format(labels[3],flowDirections[2],gameName,duration),fontsize=10)
        fig1.savefig('{}/{}_duration_{}_sucessRate.png'.format(sucessFolderPath,labels[3],duration),dpi=saved_graph_resolution)
        fig2.savefig('{}/{}_duration_{}_retransmissionRate.png'.format(retransmissionFolderPath,labels[3],duration),dpi=saved_graph_resolution)
        fig3.savefig('{}/{}_duration_{}_sucessANDretransmissionRate.png'.format(sucessFolderPath,labels[3],duration),dpi=saved_graph_resolution)
        fig3.savefig('{}/{}_duration_{}_sucessANDretransmissionRate.png'.format(retransmissionFolderPath,labels[3],duration),dpi=saved_graph_resolution)
        plt.show()

    #################### CDF  Graph 1 ####################
    # CDF Graph for sucess and retransmission rates based on the # of frames for different time durations from HMD traces folder (each direction will be in a graph)
    for duration in durations:
        for i in range(len(flowDirections)):
            sucessFolderPath = "{}/{}".format(sucessPrefix,flowDirections[i])
            retransmissionFolderPath = "{}/{}".format(retransmissionPrefix,flowDirections[i])
            try:
                os.mkdir(sucessFolderPath)
                os.mkdir(retransmissionFolderPath)
            except:
                pass
            firstFrame[i] = min(flowDirectionsLists[i].__getitem__(0)[0] if i==0 else 100000000,flowDirectionsLists[i].__getitem__(1)[0],flowDirectionsLists[i].__getitem__(2)[0])
            fig1, ax1 = plt.subplots()
            fig2, ax2 = plt.subplots()
            for j in range(len(flowDirectionsLists[i])):
                if(i == 1 and j ==0):
                    continue
                # compute the periodic sucess and retransmission rates
                newTimes = relativeTimeFromAPointOfTime(firstFrame[i],flowDirectionsLists[i].__getitem__(j))
                newTimes_RE = relativeTimeFromAPointOfTime(firstFrame[i],flowDirectionsLists_RE[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfSucessRates = computePeriodicSucessRateSize(newTimes,listOfFrameSizes[i].__getitem__(j),newTimes_RE,listOfFrameSizes_RE[i].__getitem__(j),duration)
                listOfRetransmissionRates = [100-x for x in listOfSucessRates]
                data_sucess = [float(value) for value in listOfSucessRates]
                x_sucess = np.sort(data_sucess)
                y_sucess = np.arange(len(x_sucess))/float(len(x_sucess))
                data_retransmission = [float(value) for value in listOfRetransmissionRates]
                x_retransmission = np.sort(data_retransmission)
                y_retransmission = np.arange(len(x_retransmission))/float(len(x_retransmission))
                yLabel = '{}'.format(labels[j]) 
                ax1.plot(x_sucess,y_sucess,label=yLabel,c='{}'.format(colors[j]),linestyle='{}'.format(lineStyles[j]))
                ax2.plot(x_retransmission,y_retransmission,label=yLabel,c='{}'.format(colors[j]),linestyle='{}'.format(lineStyles[j]))
            ax1.legend(loc='best', fontsize=10)
            ax2.legend(loc='best', fontsize=10)
            ax1.grid(color='grey', linestyle='--', linewidth=0.5)
            ax2.grid(color='grey', linestyle='--', linewidth=0.5)
            ax1.set_xlabel('sucess rate percentage', fontsize=12)
            ax2.set_xlabel('retransmission rate percentage', fontsize=12)
            ax1.set_ylabel('CDF', fontsize=12)
            ax2.set_ylabel('CDF', fontsize=12)
            ax1.set_title("CDF of {} sucess rate of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            ax2.set_title("CDF of {} retransmission rate of {} for a duration of {} sec".format(flowDirections[i],gameName,duration),fontsize=10)
            fig1.savefig('{}/{}_duration_{}_sucessRate_CDF.png'.format(sucessFolderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            fig2.savefig('{}/{}_duration_{}_retransmissionRate_CDF.png'.format(retransmissionFolderPath,flowDirections[i],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### CDF  Graph 2 ####################
    # CDF Graph for sucess and retransmission rates based on the # of frames for different time durations from HMD traces folder (each data type will be in a graph)
    for duration in durations:
        for j in range(len(labels)):
            firstTime = min(flowDirectionsLists[0].__getitem__(j)[0],flowDirectionsLists[1].__getitem__(j)[0]) if not j == 0 else flowDirectionsLists[0].__getitem__(j)[0]
            fig1, ax1 = plt.subplots()
            fig2, ax2 = plt.subplots()
            for i in range(len(flowDirections)):
                if(i == 1 and j ==0):
                        continue
                sucessFolderPath = "{}/{}".format(sucessPrefix,labels[j])
                retransmissionFolderPath = "{}/{}".format(retransmissionPrefix,labels[j])
                try:
                    os.mkdir(sucessFolderPath)
                    os.mkdir(retransmissionFolderPath)
                except:
                    pass
                # compute the periodic sucess and retransmission rates    
                newTimes = relativeTimeFromAPointOfTime(firstTime,flowDirectionsLists[i].__getitem__(j))
                newTimes_RE = relativeTimeFromAPointOfTime(firstTime,flowDirectionsLists_RE[i].__getitem__(j))
                newTimesPeriods = convertTimeToPeriods(newTimes,duration)
                listOfSucessRates = computePeriodicSucessRateSize(newTimes,listOfFrameSizes[i].__getitem__(j),newTimes_RE,listOfFrameSizes_RE[i].__getitem__(j),duration)
                listOfRetransmissionRates = [100-x for x in listOfSucessRates]
                data_sucess = [float(value) for value in listOfSucessRates]
                x_sucess = np.sort(data_sucess)
                y_sucess = np.arange(len(x_sucess))/float(len(x_sucess))
                data_retransmission = [float(value) for value in listOfRetransmissionRates]
                x_retransmission = np.sort(data_retransmission)
                y_retransmission = np.arange(len(x_retransmission))/float(len(x_retransmission))
                yLabel = '{}'.format(flowDirections[i]) 
                ax1.plot(x_sucess,y_sucess,label=yLabel,c='{}'.format(colors[i]),linestyle='{}'.format(lineStyles[i]))
                ax2.plot(x_retransmission,y_retransmission,label=yLabel,c='{}'.format(colors[i]),linestyle='{}'.format(lineStyles[i]))
                
            ax1.legend(loc='best', fontsize=10)
            ax2.legend(loc='best', fontsize=10)
            ax1.grid(color='grey', linestyle='--', linewidth=0.5)
            ax2.grid(color='grey', linestyle='--', linewidth=0.5)
            ax1.set_xlabel('sucess rate percentage', fontsize=12)
            ax2.set_xlabel('retransmission rate percentage', fontsize=12)
            ax1.set_ylabel('CDF', fontsize=12)
            ax2.set_ylabel('CDF', fontsize=12)
            ax1.set_title("CDF of {} sucess rate of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            ax2.set_title("CDF of {} retransmission rate of {} for a duration of {} sec".format(labels[j],gameName,duration),fontsize=10)
            fig1.savefig('{}/{}_duration_{}_sucessRate_CDF.png'.format(sucessFolderPath,labels[j],duration),dpi=saved_graph_resolution)
            fig2.savefig('{}/{}_duration_{}_retransmissionRateCDF.png'.format(retransmissionFolderPath,labels[j],duration),dpi=saved_graph_resolution)
            plt.show()
    ######################################################



    #################### CDF  Graph 3 ####################
    # CDF Graph for sucess and retransmission rates based on the # of frames for different time durations from HMD traces folder (for all data types and both directions [uplink and downlink])
    
    sucessFolderPath = "{}/{}".format(sucessPrefix,"{}_{}".format(labels[3],flowDirections[2]))
    retransmissionFolderPath = "{}/{}".format(retransmissionPrefix,"{}_{}".format(labels[3],flowDirections[2]))
    try:
        os.mkdir(sucessFolderPath)
        os.mkdir(retransmissionFolderPath)
    except:
        pass

    for duration in durations: 
        # [D] all data frames
        fig1, ax1 = plt.subplots()
        fig2, ax2 = plt.subplots() 
        fig3, ax3 = plt.subplots() 
        newTimes = relativeTimeFromAPointOfTime(tempHMD_Data_Times[0],tempHMD_Data_Times)
        newTimes_RE = relativeTimeFromAPointOfTime(tempHMD_Data_Times[0],tempHMD_RE_Data_Times)
        newTimesPeriods = convertTimeToPeriods(newTimes,duration)
        listOfSucessRates = computePeriodicSucessRateSize(newTimes,tempHMD_Data_Frames_Sizes,newTimes_RE,tempHMD_RE_Data_Frames_Sizes,duration)
        listOfRetransmissionRates = [100-x for x in listOfSucessRates]
        data_sucess = [float(value) for value in listOfSucessRates]
        data_retransmission = [float(value) for value in listOfRetransmissionRates]
        x_sucess = np.sort(data_sucess)
        x_retransmission = np.sort(data_retransmission)
        y_sucess = np.arange(len(x_sucess))/float(len(x_sucess))
        y_retransmission = np.arange(len(x_retransmission))/float(len(x_retransmission))
        ylabel  = "all data types - both directions"
        y1Label = "sucess rate"
        y2Label = "retransmission rate"
        ax1.plot(x_sucess,y_sucess,label=yLabel,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        ax2.plot(x_retransmission,y_retransmission,label=yLabel,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        ax3.plot(x_sucess,y_sucess,label=y1Label,c='{}'.format(colors[0]),linestyle='{}'.format(lineStyles[0]))
        ax3.plot(x_retransmission,y_retransmission,label=y2Label,c='{}'.format(colors[1]),linestyle='{}'.format(lineStyles[1]))
        ax1.legend(loc='best', fontsize=10)
        ax2.legend(loc='best', fontsize=10)
        ax3.legend(loc='best', fontsize=10)
        ax1.grid(color='grey', linestyle='--', linewidth=0.5)
        ax2.grid(color='grey', linestyle='--', linewidth=0.5)
        ax3.grid(color='grey', linestyle='--', linewidth=0.5)
        ax1.set_xlabel('sucess rate percentage', fontsize=12)
        ax2.set_xlabel('retransmission rate percentage', fontsize=12)
        ax3.set_xlabel('rate percentage', fontsize=12)
        ax1.set_ylabel('CDF', fontsize=12)
        ax2.set_ylabel('CDF', fontsize=12)
        ax3.set_ylabel('CDF', fontsize=12)
        ax1.set_title("{}-{} CDF of sucess rate of {} \nfor a duration of {} sec".format(labels[3],flowDirections[2],gameName,duration),fontsize=10)
        ax2.set_title("{}-{} CDF of retransmission rate of {} \nfor a duration of {} sec".format(labels[3],flowDirections[2],gameName,duration),fontsize=10)
        ax3.set_title("{}-{} CDF of sucess and retransmission rates of {} \nfor a duration of {} sec".format(labels[3],flowDirections[2],gameName,duration),fontsize=10)
        fig1.savefig('{}/{}_duration_{}_sucessRate_CDF.png'.format(sucessFolderPath,labels[3],duration),dpi=saved_graph_resolution)
        fig2.savefig('{}/{}_duration_{}_retransmissionRate_CDF.png'.format(retransmissionFolderPath,labels[3],duration),dpi=saved_graph_resolution)
        fig3.savefig('{}/{}_duration_{}_sucessANDretransmissionRate_CDF.png'.format(sucessFolderPath,labels[3],duration),dpi=saved_graph_resolution)
        fig3.savefig('{}/{}_duration_{}_sucessANDretransmissionRate_CDF.png'.format(retransmissionFolderPath,labels[3],duration),dpi=saved_graph_resolution)
        plt.show()
    ######################################################



def relativeTime(arrayOfTimes=[]):
    if(len(arrayOfTimes)<1):
        return[]
    else:
        return [float(x)-float(arrayOfTimes[0]) for x in arrayOfTimes]



def relativeTimeFromAPointOfTime(firstTime,arrayOfTimes=[]):
    if(len(arrayOfTimes)<1):
        return[]
    else:
        return [float(x)-firstTime for x in arrayOfTimes]



def convertTimeToPeriods(listOfTimeStamps,duration=1):
    # This method is used to convert the list of times to a list of periods based on a duration
    # input: listOfTimeStamps in ms starting from 0
    #        duration of the resulted times
    # output: a list of periods based on the duration
    duration = 1 if duration == 0 else duration
    listOfTimesPeriods = []   
    beginningOfInterval = 0
    intervalTime = 0
    counter = 1
    #relativeListOfTimeStamps = listOfTimeStamps if listOfTimeStamps[0] == 0 else relativeTime(listOfTimeStamps)
    relativeListOfTimeStamps = listOfTimeStamps 
    newListOfTimeStamps = [float(x)/1000 for x in relativeListOfTimeStamps]
    beginningOfInterval = math.floor(newListOfTimeStamps[0]/duration) * duration
    counter = counter + beginningOfInterval/duration
    for i in range(len(newListOfTimeStamps)):
        intervalTime = float(newListOfTimeStamps[i]) - beginningOfInterval
        if intervalTime >= duration:
            listOfTimesPeriods.append(counter*duration)
            beginningOfInterval = beginningOfInterval + duration
            intervalTime = float(newListOfTimeStamps[i]) - beginningOfInterval
            counter = counter + 1
            
    if(len(listOfTimesPeriods) < math.ceil((float(newListOfTimeStamps[len(newListOfTimeStamps)-1]) - float(newListOfTimeStamps[0]))/duration)):
            listOfTimesPeriods.append(counter*duration)
    return listOfTimesPeriods



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



def eliminateRetransmittedFrames(results):
    # This method is used to remove re-transmission attempts from the data1,data2, and data3 lists 
    # input: list of HMD results
    # output: a list of HMD results without the re-transmission attempts in data1, data2, and data3 lists
    HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates,\
        HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes, HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times,\
        HMD_DWN_MANAGEMENT_FRAMES_DataRates, HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes, HMD_UP_DATA1_FRAMES_NBs, \
        HMD_UP_DATA1_FRAMES_Times, HMD_UP_DATA1_FRAMES_DataRates, HMD_UP_DATA1_FRAMES_Frames_Sizes,\
        HMD_UP_DATA1_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA1_FRAMES_NBs, HMD_UP_RE_DATA1_FRAMES_Times, \
        HMD_UP_RE_DATA1_FRAMES_DataRates, HMD_UP_RE_DATA1_FRAMES_Frames_Sizes, HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB,\
        HMD_UP_DATA2_FRAMES_NBs, HMD_UP_DATA2_FRAMES_Times, HMD_UP_DATA2_FRAMES_DataRates, HMD_UP_DATA2_FRAMES_Data_Sizes,\
        HMD_UP_DATA2_FRAMES_Frames_Sizes, HMD_UP_DATA2_FRAMES_Frames_SeqNB, HMD_DWN_DATA2_FRAMES_NBs, HMD_DWN_DATA2_FRAMES_Times, \
        HMD_DWN_DATA2_FRAMES_DataRates, HMD_DWN_DATA2_FRAMES_Data_Sizes, HMD_DWN_DATA2_FRAMES_Frames_Sizes, \
        HMD_DWN_DATA2_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA2_FRAMES_NBs, HMD_UP_RE_DATA2_FRAMES_Times, HMD_UP_RE_DATA2_FRAMES_DataRates,\
        HMD_UP_RE_DATA2_FRAMES_Data_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB, \
        HMD_DWN_RE_DATA2_FRAMES_NBs, HMD_DWN_RE_DATA2_FRAMES_Times, HMD_DWN_RE_DATA2_FRAMES_DataRates, HMD_DWN_RE_DATA2_FRAMES_Data_Sizes,\
        HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB, HMD_UP_DATA3_FRAMES_NBs, HMD_UP_DATA3_FRAMES_Times, \
        HMD_UP_DATA3_FRAMES_DataRates, HMD_UP_DATA3_FRAMES_Data_Sizes, HMD_UP_DATA3_FRAMES_Frames_Sizes, HMD_UP_DATA3_FRAMES_Frames_SeqNB,\
        HMD_DWN_DATA3_FRAMES_NBs, HMD_DWN_DATA3_FRAMES_Times, HMD_DWN_DATA3_FRAMES_DataRates, HMD_DWN_DATA3_FRAMES_Data_Sizes,\
        HMD_DWN_DATA3_FRAMES_Frames_Sizes, HMD_DWN_DATA3_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA3_FRAMES_NBs, HMD_UP_RE_DATA3_FRAMES_Times, \
        HMD_UP_RE_DATA3_FRAMES_DataRates, HMD_UP_RE_DATA3_FRAMES_Data_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_Sizes, \
        HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB, HMD_DWN_RE_DATA3_FRAMES_NBs, HMD_DWN_RE_DATA3_FRAMES_Times, HMD_DWN_RE_DATA3_FRAMES_DataRates, \
        HMD_DWN_RE_DATA3_FRAMES_Data_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB = results  

    newHMD_UP_DATA1_FRAMES_NBs           = []
    newHMD_UP_DATA1_FRAMES_Times         = []
    newHMD_UP_DATA1_FRAMES_DataRates     = [] 
    newHMD_UP_DATA1_FRAMES_Frames_Sizes  = []
    newHMD_UP_DATA1_FRAMES_Frames_SeqNB  = []
    newHMD_UP_DATA2_FRAMES_NBs           = []
    newHMD_UP_DATA2_FRAMES_Times         = []
    newHMD_UP_DATA2_FRAMES_DataRates     = []
    newHMD_UP_DATA2_FRAMES_Data_Sizes    = []
    newHMD_UP_DATA2_FRAMES_Frames_Sizes  = []
    newHMD_UP_DATA2_FRAMES_Frames_SeqNB  = []
    newHMD_DWN_DATA2_FRAMES_NBs          = []
    newHMD_DWN_DATA2_FRAMES_Times        = []
    newHMD_DWN_DATA2_FRAMES_DataRates    = []
    newHMD_DWN_DATA2_FRAMES_Data_Sizes   = []
    newHMD_DWN_DATA2_FRAMES_Frames_Sizes = []
    newHMD_DWN_DATA2_FRAMES_Frames_SeqNB = []
    newHMD_UP_DATA3_FRAMES_NBs           = []
    newHMD_UP_DATA3_FRAMES_Times         = []
    newHMD_UP_DATA3_FRAMES_DataRates     = []
    newHMD_UP_DATA3_FRAMES_Data_Sizes    = []
    newHMD_UP_DATA3_FRAMES_Frames_Sizes  = []
    newHMD_UP_DATA3_FRAMES_Frames_SeqNB  = []
    newHMD_DWN_DATA3_FRAMES_NBs          = []
    newHMD_DWN_DATA3_FRAMES_Times        = []
    newHMD_DWN_DATA3_FRAMES_DataRates    = []
    newHMD_DWN_DATA3_FRAMES_Data_Sizes   = []
    newHMD_DWN_DATA3_FRAMES_Frames_Sizes = []
    newHMD_DWN_DATA3_FRAMES_Frames_SeqNB = []

    # Data I

    newHMD_UP_DATA1_FRAMES_NBs,newHMD_UP_DATA1_FRAMES_Times,newHMD_UP_DATA1_FRAMES_DataRates, \
        newHMD_UP_DATA1_FRAMES_Frames_Sizes,newHMD_UP_DATA1_FRAMES_Frames_SeqNB = getUniqueFrames((HMD_UP_DATA1_FRAMES_NBs,
        HMD_UP_DATA1_FRAMES_Times, HMD_UP_DATA1_FRAMES_DataRates, HMD_UP_DATA1_FRAMES_Frames_Sizes,HMD_UP_DATA1_FRAMES_Frames_SeqNB))

    
    # Data II
    newHMD_UP_DATA2_FRAMES_NBs, newHMD_UP_DATA2_FRAMES_Times, newHMD_UP_DATA2_FRAMES_DataRates, newHMD_UP_DATA2_FRAMES_Data_Sizes,\
        newHMD_UP_DATA2_FRAMES_Frames_Sizes, newHMD_UP_DATA2_FRAMES_Frames_SeqNB = getUniqueFrames((HMD_UP_DATA2_FRAMES_NBs, HMD_UP_DATA2_FRAMES_Times, 
        HMD_UP_DATA2_FRAMES_DataRates, HMD_UP_DATA2_FRAMES_Data_Sizes,HMD_UP_DATA2_FRAMES_Frames_Sizes, HMD_UP_DATA2_FRAMES_Frames_SeqNB))
    
    newHMD_DWN_DATA2_FRAMES_NBs, newHMD_DWN_DATA2_FRAMES_Times, newHMD_DWN_DATA2_FRAMES_DataRates, newHMD_DWN_DATA2_FRAMES_Data_Sizes,\
        newHMD_DWN_DATA2_FRAMES_Frames_Sizes, newHMD_DWN_DATA2_FRAMES_Frames_SeqNB = getUniqueFrames((HMD_DWN_DATA2_FRAMES_NBs, HMD_DWN_DATA2_FRAMES_Times, 
        HMD_DWN_DATA2_FRAMES_DataRates, HMD_DWN_DATA2_FRAMES_Data_Sizes,HMD_DWN_DATA2_FRAMES_Frames_Sizes, HMD_DWN_DATA2_FRAMES_Frames_SeqNB))

    
    # Data III
    newHMD_UP_DATA3_FRAMES_NBs, newHMD_UP_DATA3_FRAMES_Times, newHMD_UP_DATA3_FRAMES_DataRates, newHMD_UP_DATA3_FRAMES_Data_Sizes,\
        newHMD_UP_DATA3_FRAMES_Frames_Sizes, newHMD_UP_DATA3_FRAMES_Frames_SeqNB = getUniqueFrames((HMD_UP_DATA3_FRAMES_NBs, HMD_UP_DATA3_FRAMES_Times, 
        HMD_UP_DATA3_FRAMES_DataRates, HMD_UP_DATA3_FRAMES_Data_Sizes,HMD_UP_DATA3_FRAMES_Frames_Sizes, HMD_UP_DATA3_FRAMES_Frames_SeqNB))
    
    newHMD_DWN_DATA3_FRAMES_NBs, newHMD_DWN_DATA3_FRAMES_Times, newHMD_DWN_DATA3_FRAMES_DataRates, newHMD_DWN_DATA3_FRAMES_Data_Sizes,\
        newHMD_DWN_DATA3_FRAMES_Frames_Sizes, newHMD_DWN_DATA3_FRAMES_Frames_SeqNB = getUniqueFrames((HMD_DWN_DATA3_FRAMES_NBs, HMD_DWN_DATA3_FRAMES_Times, 
        HMD_DWN_DATA3_FRAMES_DataRates, HMD_DWN_DATA3_FRAMES_Data_Sizes,HMD_DWN_DATA3_FRAMES_Frames_Sizes, HMD_DWN_DATA3_FRAMES_Frames_SeqNB))


    newResults = (HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates,
        HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes, HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times,
        HMD_DWN_MANAGEMENT_FRAMES_DataRates, HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes, newHMD_UP_DATA1_FRAMES_NBs, 
        newHMD_UP_DATA1_FRAMES_Times, newHMD_UP_DATA1_FRAMES_DataRates, newHMD_UP_DATA1_FRAMES_Frames_Sizes,
        newHMD_UP_DATA1_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA1_FRAMES_NBs, HMD_UP_RE_DATA1_FRAMES_Times, 
        HMD_UP_RE_DATA1_FRAMES_DataRates, HMD_UP_RE_DATA1_FRAMES_Frames_Sizes, HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB,
        newHMD_UP_DATA2_FRAMES_NBs, newHMD_UP_DATA2_FRAMES_Times, newHMD_UP_DATA2_FRAMES_DataRates, newHMD_UP_DATA2_FRAMES_Data_Sizes,
        newHMD_UP_DATA2_FRAMES_Frames_Sizes, newHMD_UP_DATA2_FRAMES_Frames_SeqNB, newHMD_DWN_DATA2_FRAMES_NBs, newHMD_DWN_DATA2_FRAMES_Times, 
        newHMD_DWN_DATA2_FRAMES_DataRates, newHMD_DWN_DATA2_FRAMES_Data_Sizes, newHMD_DWN_DATA2_FRAMES_Frames_Sizes, 
        newHMD_DWN_DATA2_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA2_FRAMES_NBs, HMD_UP_RE_DATA2_FRAMES_Times, HMD_UP_RE_DATA2_FRAMES_DataRates,
        HMD_UP_RE_DATA2_FRAMES_Data_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB, 
        HMD_DWN_RE_DATA2_FRAMES_NBs, HMD_DWN_RE_DATA2_FRAMES_Times, HMD_DWN_RE_DATA2_FRAMES_DataRates, HMD_DWN_RE_DATA2_FRAMES_Data_Sizes,
        HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB, newHMD_UP_DATA3_FRAMES_NBs, newHMD_UP_DATA3_FRAMES_Times, 
        newHMD_UP_DATA3_FRAMES_DataRates, newHMD_UP_DATA3_FRAMES_Data_Sizes, newHMD_UP_DATA3_FRAMES_Frames_Sizes, newHMD_UP_DATA3_FRAMES_Frames_SeqNB,
        newHMD_DWN_DATA3_FRAMES_NBs, newHMD_DWN_DATA3_FRAMES_Times, newHMD_DWN_DATA3_FRAMES_DataRates, newHMD_DWN_DATA3_FRAMES_Data_Sizes,
        newHMD_DWN_DATA3_FRAMES_Frames_Sizes, newHMD_DWN_DATA3_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA3_FRAMES_NBs, HMD_UP_RE_DATA3_FRAMES_Times, 
        HMD_UP_RE_DATA3_FRAMES_DataRates, HMD_UP_RE_DATA3_FRAMES_Data_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_Sizes, 
        HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB, HMD_DWN_RE_DATA3_FRAMES_NBs, HMD_DWN_RE_DATA3_FRAMES_Times, HMD_DWN_RE_DATA3_FRAMES_DataRates, 
        HMD_DWN_RE_DATA3_FRAMES_Data_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB)
    return newResults



def getUniqueFrames(setOfLists):
    # This method is used by eliminateRetransmittedFrames method to remove re-transmission attempts from the data1,data2, and data3 lists 
    # input: relevant HMD lists as a tuple of lists (5 in case of data 1 and 6 in case of data 2 & 3)
    # output: the relevant HMD lists after removing the re-transmission attempts
    newHMD_FRAMES_NBs          = []
    newHMD_FRAMES_Times        = []
    newHMD_FRAMES_DataRates    = []
    newHMD_FRAMES_Data_Sizes   = []
    newHMD_FRAMES_Frames_Sizes = []
    newHMD_FRAMES_Frames_SeqNB = []
    
    if(len(setOfLists)==5): # DATA I
        HMD_FRAMES_NBs,HMD_FRAMES_Times,HMD_FRAMES_DataRates,HMD_FRAMES_Frames_Sizes,HMD_FRAMES_Frames_SeqNB = setOfLists
        for i in range (len(HMD_FRAMES_NBs)):
            if(len(newHMD_FRAMES_Frames_SeqNB)-1 >= 0 and HMD_FRAMES_Frames_SeqNB[i] == newHMD_FRAMES_Frames_SeqNB[len(newHMD_FRAMES_Frames_SeqNB)-1]):
                index = len(newHMD_FRAMES_Frames_SeqNB)-1
                newHMD_FRAMES_NBs[index]          = HMD_FRAMES_NBs[i]
                newHMD_FRAMES_Times[index]        = HMD_FRAMES_Times[i]
                newHMD_FRAMES_DataRates[index]    = HMD_FRAMES_DataRates[i]
                newHMD_FRAMES_Frames_Sizes[index] = HMD_FRAMES_Frames_Sizes[i]
                newHMD_FRAMES_Frames_SeqNB[index] = HMD_FRAMES_Frames_SeqNB[i]
            else:
                newHMD_FRAMES_NBs.append(HMD_FRAMES_NBs[i])
                newHMD_FRAMES_Times.append(HMD_FRAMES_Times[i])
                newHMD_FRAMES_DataRates.append(HMD_FRAMES_DataRates[i])
                newHMD_FRAMES_Frames_Sizes.append(HMD_FRAMES_Frames_Sizes[i])
                newHMD_FRAMES_Frames_SeqNB.append(HMD_FRAMES_Frames_SeqNB[i])
        newSetOfList = (newHMD_FRAMES_NBs,newHMD_FRAMES_Times,newHMD_FRAMES_DataRates,newHMD_FRAMES_Frames_Sizes,newHMD_FRAMES_Frames_SeqNB)

    elif(len(setOfLists)>5): # DATA II & DATA III
        HMD_FRAMES_NBs,HMD_FRAMES_Times,HMD_FRAMES_DataRates,HMD_FRAMES_Data_Sizes,HMD_FRAMES_Frames_Sizes,HMD_FRAMES_Frames_SeqNB = setOfLists
        for i in range (len(HMD_FRAMES_NBs)):
            if(len(newHMD_FRAMES_Frames_SeqNB)-1 >= 0 and HMD_FRAMES_Frames_SeqNB[i] == newHMD_FRAMES_Frames_SeqNB[len(newHMD_FRAMES_Frames_SeqNB)-1]):
                index = len(newHMD_FRAMES_Frames_SeqNB)-1
                newHMD_FRAMES_NBs[index]          = HMD_FRAMES_NBs[i]
                newHMD_FRAMES_Times[index]        = HMD_FRAMES_Times[i]
                newHMD_FRAMES_DataRates[index]    = HMD_FRAMES_DataRates[i]
                newHMD_FRAMES_Data_Sizes[index]   = HMD_FRAMES_Data_Sizes[i]
                newHMD_FRAMES_Frames_Sizes[index] = HMD_FRAMES_Frames_Sizes[i]
                newHMD_FRAMES_Frames_SeqNB[index] = HMD_FRAMES_Frames_SeqNB[i]
            else:
                newHMD_FRAMES_NBs.append(HMD_FRAMES_NBs[i])
                newHMD_FRAMES_Times.append(HMD_FRAMES_Times[i])
                newHMD_FRAMES_DataRates.append(HMD_FRAMES_DataRates[i])
                newHMD_FRAMES_Data_Sizes.append(HMD_FRAMES_Data_Sizes[i])
                newHMD_FRAMES_Frames_Sizes.append(HMD_FRAMES_Frames_Sizes[i])
                newHMD_FRAMES_Frames_SeqNB.append(HMD_FRAMES_Frames_SeqNB[i])
    
    newSetOfList = (newHMD_FRAMES_NBs,newHMD_FRAMES_Times,newHMD_FRAMES_DataRates,newHMD_FRAMES_Frames_Sizes,newHMD_FRAMES_Frames_SeqNB) if len(setOfLists)==5 else (newHMD_FRAMES_NBs,newHMD_FRAMES_Times,newHMD_FRAMES_DataRates,newHMD_FRAMES_Data_Sizes,newHMD_FRAMES_Frames_Sizes,newHMD_FRAMES_Frames_SeqNB)

    return newSetOfList



def checkExistence(filePath,line):
    # check if the line 'line' is existed in the file in the path 'filePath'
    with open(filePath) as f:
        if line in f.read():
            return True
    return False



def sort_two_lists(list1,list2):
    # this function is used to sort two related arrays with identical length based on one of them
    # eg: list1 and list2 will be sorted based on the values of list1
    # prerequisite: the two lists has to be with the same length, and list1 values have to be unique
    # input: list1 and list2
    # output: sortedList1 and sortedList2 based on the values of sortedList1
    
    if(len(list1)!=len(list2)):
        print("\033[91m\t{}\033[00m" .format("[-] the length of the two arrays is not identical"))
        return list1,list2
    sortedList1 = list1.copy()
    sortedList2 = list2.copy()
    dict_index_values = {}
    dict_values_index = {}
    
    for i in range(len(sortedList1)):
        dict_index_values[i] = sortedList1[i]
    
    sortedList1.sort()
    
    for i in range(len(sortedList1)):
        dict_values_index[sortedList1[i]] = i
    
    for i in range(len(sortedList1)):
        sortedList2[dict_values_index[dict_index_values[i]]] = list2[i]
    
    return sortedList1,sortedList2



def combinedResultsLists(results,flag = 0):
    # This method is used to combine all the results lists in a single ordered list 
    # input: list of HMD results
    #        a flag that accept a value of 0 or 1 (or anything else) where 0 mean combining the data frames (TYPE I, II, and III) only and 1 mean combining the data frames and management frames
    # output: a tuple that contain lists of combined results with retransmission attempts
    
    HMD_UP_MANAGEMENT_FRAMES_NBs, HMD_UP_MANAGEMENT_FRAMES_Times, HMD_UP_MANAGEMENT_FRAMES_DataRates,\
        HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes, HMD_DWN_MANAGEMENT_FRAMES_NBs, HMD_DWN_MANAGEMENT_FRAMES_Times,\
        HMD_DWN_MANAGEMENT_FRAMES_DataRates, HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes, HMD_UP_DATA1_FRAMES_NBs, \
        HMD_UP_DATA1_FRAMES_Times, HMD_UP_DATA1_FRAMES_DataRates, HMD_UP_DATA1_FRAMES_Frames_Sizes,\
        HMD_UP_DATA1_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA1_FRAMES_NBs, HMD_UP_RE_DATA1_FRAMES_Times, \
        HMD_UP_RE_DATA1_FRAMES_DataRates, HMD_UP_RE_DATA1_FRAMES_Frames_Sizes, HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB,\
        HMD_UP_DATA2_FRAMES_NBs, HMD_UP_DATA2_FRAMES_Times, HMD_UP_DATA2_FRAMES_DataRates, HMD_UP_DATA2_FRAMES_Data_Sizes,\
        HMD_UP_DATA2_FRAMES_Frames_Sizes, HMD_UP_DATA2_FRAMES_Frames_SeqNB, HMD_DWN_DATA2_FRAMES_NBs, HMD_DWN_DATA2_FRAMES_Times, \
        HMD_DWN_DATA2_FRAMES_DataRates, HMD_DWN_DATA2_FRAMES_Data_Sizes, HMD_DWN_DATA2_FRAMES_Frames_Sizes, \
        HMD_DWN_DATA2_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA2_FRAMES_NBs, HMD_UP_RE_DATA2_FRAMES_Times, HMD_UP_RE_DATA2_FRAMES_DataRates,\
        HMD_UP_RE_DATA2_FRAMES_Data_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_Sizes, HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB, \
        HMD_DWN_RE_DATA2_FRAMES_NBs, HMD_DWN_RE_DATA2_FRAMES_Times, HMD_DWN_RE_DATA2_FRAMES_DataRates, HMD_DWN_RE_DATA2_FRAMES_Data_Sizes,\
        HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB, HMD_UP_DATA3_FRAMES_NBs, HMD_UP_DATA3_FRAMES_Times, \
        HMD_UP_DATA3_FRAMES_DataRates, HMD_UP_DATA3_FRAMES_Data_Sizes, HMD_UP_DATA3_FRAMES_Frames_Sizes, HMD_UP_DATA3_FRAMES_Frames_SeqNB,\
        HMD_DWN_DATA3_FRAMES_NBs, HMD_DWN_DATA3_FRAMES_Times, HMD_DWN_DATA3_FRAMES_DataRates, HMD_DWN_DATA3_FRAMES_Data_Sizes,\
        HMD_DWN_DATA3_FRAMES_Frames_Sizes, HMD_DWN_DATA3_FRAMES_Frames_SeqNB, HMD_UP_RE_DATA3_FRAMES_NBs, HMD_UP_RE_DATA3_FRAMES_Times, \
        HMD_UP_RE_DATA3_FRAMES_DataRates, HMD_UP_RE_DATA3_FRAMES_Data_Sizes, HMD_UP_RE_DATA3_FRAMES_Frames_Sizes, \
        HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB, HMD_DWN_RE_DATA3_FRAMES_NBs, HMD_DWN_RE_DATA3_FRAMES_Times, HMD_DWN_RE_DATA3_FRAMES_DataRates, \
        HMD_DWN_RE_DATA3_FRAMES_Data_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes, HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB = results 
    
    # data frames (unique frames)
    if flag == 0:
        HMD_UP_NBs           = HMD_UP_DATA1_FRAMES_NBs + HMD_UP_DATA2_FRAMES_NBs + HMD_UP_DATA3_FRAMES_NBs
        HMD_UP_Times         = HMD_UP_DATA1_FRAMES_Times + HMD_UP_DATA2_FRAMES_Times + HMD_UP_DATA3_FRAMES_Times
        HMD_UP_DataRates     = HMD_UP_DATA1_FRAMES_DataRates + HMD_UP_DATA2_FRAMES_DataRates + HMD_UP_DATA3_FRAMES_DataRates
        HMD_UP_Data_Sizes    = [0 for x in range(len(HMD_UP_DATA1_FRAMES_NBs))] + HMD_UP_DATA2_FRAMES_Data_Sizes + HMD_UP_DATA3_FRAMES_Data_Sizes
        HMD_UP_Frames_Sizes  = HMD_UP_DATA1_FRAMES_Frames_Sizes + HMD_UP_DATA2_FRAMES_Frames_Sizes + HMD_UP_DATA3_FRAMES_Frames_Sizes
        HMD_UP_Frames_SeqNB  = HMD_UP_DATA1_FRAMES_Frames_SeqNB + HMD_UP_DATA2_FRAMES_Frames_SeqNB + HMD_UP_DATA3_FRAMES_Frames_SeqNB
        HMD_DWN_NBs          = HMD_DWN_DATA2_FRAMES_NBs + HMD_DWN_DATA3_FRAMES_NBs
        HMD_DWN_Times        = HMD_DWN_DATA2_FRAMES_Times + HMD_DWN_DATA3_FRAMES_Times
        HMD_DWN_DataRates    = HMD_DWN_DATA2_FRAMES_DataRates + HMD_DWN_DATA3_FRAMES_DataRates
        HMD_DWN_Data_Sizes   = HMD_DWN_DATA2_FRAMES_Data_Sizes + HMD_DWN_DATA3_FRAMES_Data_Sizes
        HMD_DWN_Frames_Sizes = HMD_DWN_DATA2_FRAMES_Frames_Sizes + HMD_DWN_DATA3_FRAMES_Frames_Sizes
        HMD_DWN_Frames_SeqNB = HMD_DWN_DATA2_FRAMES_Frames_SeqNB + HMD_DWN_DATA3_FRAMES_Frames_SeqNB
    
    # data + management frames (unique frames)
    else:
        HMD_UP_NBs           = HMD_UP_MANAGEMENT_FRAMES_NBs + HMD_UP_DATA1_FRAMES_NBs + HMD_UP_DATA2_FRAMES_NBs + HMD_UP_DATA3_FRAMES_NBs
        HMD_UP_Times         = HMD_UP_MANAGEMENT_FRAMES_Times + HMD_UP_DATA1_FRAMES_Times + HMD_UP_DATA2_FRAMES_Times + HMD_UP_DATA3_FRAMES_Times
        HMD_UP_DataRates     = HMD_UP_MANAGEMENT_FRAMES_DataRates + HMD_UP_DATA1_FRAMES_DataRates + HMD_UP_DATA2_FRAMES_DataRates + HMD_UP_DATA3_FRAMES_DataRates
        HMD_UP_Data_Sizes    = [0 for x in range(len(HMD_UP_MANAGEMENT_FRAMES_NBs))] + [0 for x in range(len(HMD_UP_DATA1_FRAMES_NBs))] + HMD_UP_DATA2_FRAMES_Data_Sizes + HMD_UP_DATA3_FRAMES_Data_Sizes
        HMD_UP_Frames_Sizes  = HMD_UP_MANAGEMENT_FRAMES_Frames_Sizes + HMD_UP_DATA1_FRAMES_Frames_Sizes + HMD_UP_DATA2_FRAMES_Frames_Sizes + HMD_UP_DATA3_FRAMES_Frames_Sizes
        HMD_UP_Frames_SeqNB  = [-1 for x in range(len(HMD_UP_MANAGEMENT_FRAMES_NBs))] + HMD_UP_DATA1_FRAMES_Frames_SeqNB + HMD_UP_DATA2_FRAMES_Frames_SeqNB + HMD_UP_DATA3_FRAMES_Frames_SeqNB
        HMD_DWN_NBs          = HMD_DWN_MANAGEMENT_FRAMES_NBs+ HMD_DWN_DATA2_FRAMES_NBs + HMD_DWN_DATA3_FRAMES_NBs
        HMD_DWN_Times        = HMD_DWN_MANAGEMENT_FRAMES_Times + HMD_DWN_DATA2_FRAMES_Times + HMD_DWN_DATA3_FRAMES_Times
        HMD_DWN_DataRates    = HMD_DWN_MANAGEMENT_FRAMES_DataRates + HMD_DWN_DATA2_FRAMES_DataRates + HMD_DWN_DATA3_FRAMES_DataRates
        HMD_DWN_Data_Sizes   = [0 for x in range(len(HMD_DWN_MANAGEMENT_FRAMES_NBs))] + HMD_DWN_DATA2_FRAMES_Data_Sizes + HMD_DWN_DATA3_FRAMES_Data_Sizes
        HMD_DWN_Frames_Sizes = HMD_DWN_MANAGEMENT_FRAMES_Frames_Sizes + HMD_DWN_DATA2_FRAMES_Frames_Sizes + HMD_DWN_DATA3_FRAMES_Frames_Sizes
        HMD_DWN_Frames_SeqNB = [-1 for x in range(len(HMD_DWN_MANAGEMENT_FRAMES_NBs))]  + HMD_DWN_DATA2_FRAMES_Frames_SeqNB + HMD_DWN_DATA3_FRAMES_Frames_SeqNB
    
    # data frames (retransmitted frames)
    HMD_UP_RE_NBs           = HMD_UP_RE_DATA1_FRAMES_NBs + HMD_UP_RE_DATA2_FRAMES_NBs + HMD_UP_RE_DATA3_FRAMES_NBs
    HMD_UP_RE_Times         = HMD_UP_RE_DATA1_FRAMES_Times + HMD_UP_RE_DATA2_FRAMES_Times + HMD_UP_RE_DATA3_FRAMES_Times
    HMD_UP_RE_DataRates     = HMD_UP_RE_DATA1_FRAMES_DataRates + HMD_UP_RE_DATA2_FRAMES_DataRates + HMD_UP_RE_DATA3_FRAMES_DataRates
    HMD_UP_RE_Data_Sizes    = [0 for x in range(len(HMD_UP_RE_DATA1_FRAMES_NBs))] + HMD_UP_RE_DATA2_FRAMES_Data_Sizes + HMD_UP_RE_DATA3_FRAMES_Data_Sizes
    HMD_UP_RE_Frames_Sizes  = HMD_UP_RE_DATA1_FRAMES_Frames_Sizes + HMD_UP_RE_DATA2_FRAMES_Frames_Sizes+ HMD_UP_RE_DATA3_FRAMES_Frames_Sizes
    HMD_UP_RE_Frames_SeqNB  = HMD_UP_RE_DATA1_FRAMES_Frames_SeqNB + HMD_UP_RE_DATA2_FRAMES_Frames_SeqNB + HMD_UP_RE_DATA3_FRAMES_Frames_SeqNB
    HMD_DWN_RE_NBs          = HMD_DWN_RE_DATA2_FRAMES_NBs + HMD_DWN_RE_DATA3_FRAMES_NBs
    HMD_DWN_RE_Times        = HMD_DWN_RE_DATA2_FRAMES_Times + HMD_DWN_RE_DATA3_FRAMES_Times
    HMD_DWN_RE_DataRates    = HMD_DWN_RE_DATA2_FRAMES_DataRates + HMD_DWN_RE_DATA3_FRAMES_DataRates
    HMD_DWN_RE_Data_Sizes   = HMD_DWN_RE_DATA2_FRAMES_Data_Sizes + HMD_DWN_RE_DATA3_FRAMES_Data_Sizes
    HMD_DWN_RE_Frames_Sizes = HMD_DWN_RE_DATA2_FRAMES_Frames_Sizes + HMD_DWN_RE_DATA3_FRAMES_Frames_Sizes
    HMD_DWN_RE_Frames_SeqNB = HMD_DWN_RE_DATA2_FRAMES_Frames_SeqNB + HMD_DWN_RE_DATA3_FRAMES_Frames_SeqNB

    # sorting the unique frames
    HMD_UP_NBs = [int(x) for x in HMD_UP_NBs]    
    HMD_DWN_NBs = [int(x) for x in HMD_DWN_NBs]   
    HMD_UP_NBs,HMD_UP_Times,HMD_UP_DataRates,HMD_UP_Data_Sizes,HMD_UP_Frames_Sizes,HMD_UP_Frames_SeqNB = zip(*sorted(zip(HMD_UP_NBs,HMD_UP_Times,HMD_UP_DataRates,HMD_UP_Data_Sizes,HMD_UP_Frames_Sizes,HMD_UP_Frames_SeqNB)))
    HMD_UP_NBs,HMD_UP_Times,HMD_UP_DataRates,HMD_UP_Data_Sizes,HMD_UP_Frames_Sizes,HMD_UP_Frames_SeqNB = (list(t) for t in zip(*sorted(zip(HMD_UP_NBs,HMD_UP_Times,HMD_UP_DataRates,HMD_UP_Data_Sizes,HMD_UP_Frames_Sizes,HMD_UP_Frames_SeqNB))))
    HMD_DWN_NBs,HMD_DWN_Times,HMD_DWN_DataRates,HMD_DWN_Data_Sizes,HMD_DWN_Frames_Sizes,HMD_DWN_Frames_SeqNB = zip(*sorted(zip(HMD_DWN_NBs,HMD_DWN_Times,HMD_DWN_DataRates,HMD_DWN_Data_Sizes,HMD_DWN_Frames_Sizes,HMD_DWN_Frames_SeqNB)))
    HMD_DWN_NBs,HMD_DWN_Times,HMD_DWN_DataRates,HMD_DWN_Data_Sizes,HMD_DWN_Frames_Sizes,HMD_DWN_Frames_SeqNB = (list(t) for t in zip(*sorted(zip(HMD_DWN_NBs,HMD_DWN_Times,HMD_DWN_DataRates,HMD_DWN_Data_Sizes,HMD_DWN_Frames_Sizes,HMD_DWN_Frames_SeqNB))))
    HMD_UP_NBs = [str(x) for x in HMD_UP_NBs]    
    HMD_DWN_NBs = [str(x) for x in HMD_DWN_NBs] 

    # sorting the retransmitted frames
    HMD_UP_RE_NBs = [int(x) for x in HMD_UP_RE_NBs]    
    HMD_DWN_RE_NBs = [int(x) for x in HMD_DWN_RE_NBs]   
    HMD_UP_RE_NBs,HMD_UP_RE_Times,HMD_UP_RE_DataRates,HMD_UP_RE_Data_Sizes,HMD_UP_RE_Frames_Sizes,HMD_UP_RE_Frames_SeqNB = zip(*sorted(zip(HMD_UP_RE_NBs,HMD_UP_RE_Times,HMD_UP_RE_DataRates,HMD_UP_RE_Data_Sizes,HMD_UP_RE_Frames_Sizes,HMD_UP_RE_Frames_SeqNB)))
    HMD_UP_RE_NBs,HMD_UP_RE_Times,HMD_UP_RE_DataRates,HMD_UP_RE_Data_Sizes,HMD_UP_RE_Frames_Sizes,HMD_UP_RE_Frames_SeqNB = (list(t) for t in zip(*sorted(zip(HMD_UP_RE_NBs,HMD_UP_RE_Times,HMD_UP_RE_DataRates,HMD_UP_RE_Data_Sizes,HMD_UP_RE_Frames_Sizes,HMD_UP_RE_Frames_SeqNB))))
    HMD_DWN_RE_NBs,HMD_DWN_RE_Times,HMD_DWN_RE_DataRates,HMD_DWN_RE_Data_Sizes,HMD_DWN_RE_Frames_Sizes,HMD_DWN_RE_Frames_SeqNB = zip(*sorted(zip(HMD_DWN_RE_NBs,HMD_DWN_RE_Times,HMD_DWN_RE_DataRates,HMD_DWN_RE_Data_Sizes,HMD_DWN_RE_Frames_Sizes,HMD_DWN_RE_Frames_SeqNB)))
    HMD_DWN_RE_NBs,HMD_DWN_RE_Times,HMD_DWN_RE_DataRates,HMD_DWN_RE_Data_Sizes,HMD_DWN_RE_Frames_Sizes,HMD_DWN_RE_Frames_SeqNB = (list(t) for t in zip(*sorted(zip(HMD_DWN_RE_NBs,HMD_DWN_RE_Times,HMD_DWN_RE_DataRates,HMD_DWN_RE_Data_Sizes,HMD_DWN_RE_Frames_Sizes,HMD_DWN_RE_Frames_SeqNB))))
    HMD_UP_RE_NBs = [str(x) for x in HMD_UP_RE_NBs]    
    HMD_DWN_RE_NBs = [str(x) for x in HMD_DWN_RE_NBs] 

    uniqueDataCombinedLists = (HMD_UP_NBs,HMD_UP_Times,HMD_UP_DataRates,HMD_UP_Data_Sizes,HMD_UP_Frames_Sizes,HMD_UP_Frames_SeqNB,HMD_DWN_NBs,HMD_DWN_Times,HMD_DWN_DataRates,HMD_DWN_Data_Sizes,HMD_DWN_Frames_Sizes,HMD_DWN_Frames_SeqNB)
    retransmittedDataCombinedLists = (HMD_UP_RE_NBs,HMD_UP_RE_Times,HMD_UP_RE_DataRates,HMD_UP_RE_Data_Sizes,HMD_UP_RE_Frames_Sizes,HMD_UP_RE_Frames_SeqNB,HMD_DWN_RE_NBs,HMD_DWN_RE_Times,HMD_DWN_RE_DataRates,HMD_DWN_RE_Data_Sizes,HMD_DWN_RE_Frames_Sizes,HMD_DWN_RE_Frames_SeqNB)
    combinedLists = (uniqueDataCombinedLists,retransmittedDataCombinedLists)
    return(combinedLists)



def combinedResultsListsNoReTransmittedFrames(results,flag = 0):
    # This method is used to combine all the results lists in a single ordered list after removing the retrnsmission attempts
    # input: list of HMD results
    #        a flag that accept a value of 0 or 1 (or anything else) where 0 mean combining the data frames (TYPE I, II, and III) only and 1 mean combining the data frames and management frames
    # output: a tuple that contain lists of combined results without retransmission attempts
    
    newResults = eliminateRetransmittedFrames(results)
    return combinedResultsLists(newResults,flag)



def computeInstantaneousRates(listOfTimeStamps,listOfSizes,duration=1):
    # This method is used to compute the transmission rate (capacity) from the traces
    # input: listOfTimeStamps in ms starting from 0
    #        listOfSizes in bytes
    #        duration of the rate in seconds
    # output: a list of instantaneous rates in Mbps
    listOfInstantaneousRates = []
    beginningOfInterval = 0
    intervalTime = 0
    sumOfSizes = 0
    #relativeListOfTimeStamps = listOfTimeStamps if listOfTimeStamps[0] == 0 else relativeTime(listOfTimeStamps)
    relativeListOfTimeStamps = listOfTimeStamps 
    newListOfTimeStamps = [float(x)/1000 for x in relativeListOfTimeStamps]
    beginningOfInterval = math.floor(newListOfTimeStamps[0]/duration) * duration

    for i in range(len(newListOfTimeStamps)):
        intervalTime = float(newListOfTimeStamps[i]) - beginningOfInterval
        if intervalTime < duration:
            tempSize = 0 if listOfSizes[i] == '' else float(listOfSizes[i])
            sumOfSizes = sumOfSizes + tempSize
        else:
            instantaneousRate = (sumOfSizes * 8)/(duration * ((1024)**2))
            listOfInstantaneousRates.append(instantaneousRate)
            beginningOfInterval = beginningOfInterval + duration
            intervalTime = float(newListOfTimeStamps[i]) - beginningOfInterval
            tempSize = 0 if listOfSizes[i] == '' else float(listOfSizes[i])
            sumOfSizes = tempSize
    if(len(listOfInstantaneousRates) < math.ceil((float(newListOfTimeStamps[len(newListOfTimeStamps)-1]) - float(newListOfTimeStamps[0]))/duration)):
            instantaneousRate = (sumOfSizes * 8)/(intervalTime * ((1024)**2)) 
            listOfInstantaneousRates.append(instantaneousRate)
    return listOfInstantaneousRates



def computeNBOfFrames(listOfTimeStamps,duration=1):
    # This method is used to compute the # of frames for a specific period of time
    # input: listOfTimeStamps in ms starting from 0
    #        duration of the # of frames in seconds
    # output: a list of average NB of frames for a period = the duration   
    duration = 1 if duration <= 0 else duration
    listOfNBOfFrames = []
    beginningOfInterval = 0
    intervalTime = 0
    counter = 0
    #relativeListOfTimeStamps = listOfTimeStamps if listOfTimeStamps[0] == 0 else relativeTime(listOfTimeStamps)
    relativeListOfTimeStamps = listOfTimeStamps 
    newListOfTimeStamps = [float(x)/1000 for x in relativeListOfTimeStamps]
    beginningOfInterval = math.floor(newListOfTimeStamps[0]/duration) * duration

    for i in range(len(newListOfTimeStamps)):
        intervalTime = float(newListOfTimeStamps[i]) - beginningOfInterval
        if intervalTime < duration:
            counter = counter + 1
        else:
            listOfNBOfFrames.append(counter)
            beginningOfInterval = beginningOfInterval + duration
            intervalTime = float(newListOfTimeStamps[i]) - beginningOfInterval
            counter = 1
    if(len(listOfNBOfFrames) < math.ceil((float(newListOfTimeStamps[len(newListOfTimeStamps)-1]) - float(newListOfTimeStamps[0]))/duration)):
            counter = counter/intervalTime * duration
            listOfNBOfFrames.append(counter)
    return listOfNBOfFrames



def computeTotalSize(listOfTimeStamps,listOfSizes,duration=1):
    # This method is used to compute the total size of frames (transmitted data) for a specific period of time
    # input: listOfTimeStamps in ms starting from 0
    #        listOfSizes in bytes
    #        duration of the total size of frames in seconds
    # output: a list of total sizes of frames (transmitted data) for a the specified duration
    listOfSizesOfFrames = []   
    beginningOfInterval = 0
    intervalTime = 0
    size = 0
    #relativeListOfTimeStamps = listOfTimeStamps if listOfTimeStamps[0] == 0 else relativeTime(listOfTimeStamps)
    relativeListOfTimeStamps = listOfTimeStamps     
    newListOfTimeStamps = [float(x)/1000 for x in relativeListOfTimeStamps]
    beginningOfInterval = math.floor(newListOfTimeStamps[0]/duration) * duration

    for i in range(len(newListOfTimeStamps)):
        intervalTime = float(newListOfTimeStamps[i]) - beginningOfInterval
        if intervalTime < duration:
            tempSize = 0 if listOfSizes[i] == '' else float(listOfSizes[i])
            size = size + tempSize
        else:
            listOfSizesOfFrames.append(size)
            beginningOfInterval = beginningOfInterval + duration
            intervalTime = float(newListOfTimeStamps[i]) - beginningOfInterval
            tempSize = 0 if listOfSizes[i] == '' else float(listOfSizes[i])
            size = tempSize
    if(len(listOfSizesOfFrames) < math.ceil((float(newListOfTimeStamps[len(newListOfTimeStamps)-1]) - float(newListOfTimeStamps[0]))/duration)):
            size = size/intervalTime * duration
            listOfSizesOfFrames.append(size)
    return listOfSizesOfFrames



def computeAVGSize(listOfTimeStamps,listOfSizes,duration=1):
    # This method is used to compute the average frame size for a specific period of time
    # input: listOfTimeStamps in ms starting from 0
    #        listOfSizes in bytes
    #        duration of the average frame's size in seconds
    # output: a list of average size of frames for a period = the duration
    listOfAvgSizeOfFrames = []   
    beginningOfInterval = 0
    intervalTime = 0
    size = 0
    counter = 0
    #relativeListOfTimeStamps = listOfTimeStamps if listOfTimeStamps[0] == 0 else relativeTime(listOfTimeStamps)
    relativeListOfTimeStamps = listOfTimeStamps 
    newListOfTimeStamps = [float(x)/1000 for x in relativeListOfTimeStamps]
    beginningOfInterval = math.floor(newListOfTimeStamps[0]/duration) * duration

    for i in range(len(newListOfTimeStamps)):
        intervalTime = float(newListOfTimeStamps[i]) - beginningOfInterval
        if intervalTime < duration:
            tempSize = 0 if listOfSizes[i] == '' else float(listOfSizes[i])
            size = size + tempSize
            counter = counter + 1
        else:
            avgSize = size/counter
            listOfAvgSizeOfFrames.append(avgSize)
            beginningOfInterval = beginningOfInterval + duration
            intervalTime = float(newListOfTimeStamps[i]) - beginningOfInterval
            tempSize = 0 if listOfSizes[i] == '' else float(listOfSizes[i])
            size = tempSize
            counter = 1
    if(len(listOfAvgSizeOfFrames) < math.ceil((float(newListOfTimeStamps[len(newListOfTimeStamps)-1]) - float(newListOfTimeStamps[0]))/duration)):
            avgSize = size/counter
            listOfAvgSizeOfFrames.append(avgSize)
    return listOfAvgSizeOfFrames



def computePeriodicNBOfHMDFrames(listOfTimeStamps,duration=1):
    # This method is used to compute the periodic nb of frames
    # prerequisite: it is used only by the method 'computePeriodicSucessRateNB'
    # input: the list of time stamps of the frames
    #        the period in seconds
    # output: a dict of # of frames in form of {beginningOfInterval:NBOfFrames}
    duration = 1 if duration <= 0 else duration
    NBOfFramesDict = {}
    beginningOfInterval = 0
    intervalTime = 0
    counter = 0
    newListOfTimeStamps = [float(x)/1000 for x in listOfTimeStamps]
    beginningOfInterval = math.floor(newListOfTimeStamps[0]/duration) * duration

    for i in range(len(newListOfTimeStamps)):
        intervalTime = float(newListOfTimeStamps[i]) - beginningOfInterval
        if intervalTime < duration:
            counter = counter + 1
        else:
            NBOfFramesDict[beginningOfInterval] = counter
            beginningOfInterval = beginningOfInterval + duration
            intervalTime = float(newListOfTimeStamps[i]) - beginningOfInterval
            counter = 1
    if(len(NBOfFramesDict.keys()) < math.ceil((float(newListOfTimeStamps[len(newListOfTimeStamps)-1]) - float(newListOfTimeStamps[0]))/duration)):
            counter = counter/intervalTime * duration
            NBOfFramesDict[beginningOfInterval] = counter
    return NBOfFramesDict    



def computePeriodicSizeOfHMDFrames(listOfTimeStamps,listOfSizes,duration=1):
    # This method is used to compute the periodic Size of frames
    # prerequisite: it is used only by the method 'computePeriodicSucessRateSize'
    # input: the list of time stamps of the frames 
    #        the list of frames sizes in bytes
    #        the period in seconds
    # output: a dict of # of frames in form of {beginningOfInterval:sizeOfFrames}
    duration = 1 if duration <= 0 else duration
    sizesOfFramesDict = {}   
    beginningOfInterval = 0
    intervalTime = 0
    size = 0 
    newListOfTimeStamps = [float(x)/1000 for x in listOfTimeStamps]
    beginningOfInterval = math.floor(newListOfTimeStamps[0]/duration) * duration

    for i in range(len(newListOfTimeStamps)):
        intervalTime = float(newListOfTimeStamps[i]) - beginningOfInterval
        if intervalTime < duration:
            tempSize = 0 if listOfSizes[i] == '' else float(listOfSizes[i])
            size = size + tempSize
        else:
            sizesOfFramesDict[beginningOfInterval] = size
            beginningOfInterval = beginningOfInterval + duration
            intervalTime = float(newListOfTimeStamps[i]) - beginningOfInterval
            tempSize = 0 if listOfSizes[i] == '' else float(listOfSizes[i])
            size = tempSize
    if(len(sizesOfFramesDict.keys()) < math.ceil((float(newListOfTimeStamps[len(newListOfTimeStamps)-1]) - float(newListOfTimeStamps[0]))/duration)):
            size = size/intervalTime * duration
            sizesOfFramesDict[beginningOfInterval] = size
    return sizesOfFramesDict



def computeOverallSucessRateNB(HMD_NBs,HMD_RE_NBs):
    # This method is used to compute the overall sucess rate based on the number of frames (ignoring the size of frames)
    # prerequisite: the retransmission attempts has to be removed from the data lists of the HMD results 'results' by using the method 'eliminateRetransmittedFrames'
    # input: the list of the frames NBs of the data
    #        the list of the frames NBs of the retransmitted frames
    # output: the overall sucess rate in form of a percentage 
    return ((len(HMD_NBs)/(len(HMD_NBs) + len(HMD_RE_NBs)))*100)



def computeOverallSucessRateSize(Sizes,RE_Sizes):
    # This method is used to compute the overall sucess rate based on the size of the transmitted data 
    # prerequisite: the retransmission attempts has to be removed from the data lists of the HMD results 'results' by using the method 'eliminateRetransmittedFrames'
    # input: the list of the frames sizes of the data
    #        the list of the frames sizes of the retransmitted frames
    # output: the overall sucess rate in form of a percentage 
    sumSizes = 0
    sumReSizes = 0
    for size in Sizes:
        if size == '':
            continue
        else:
            sumSizes = sumSizes + float(size)
    for size in RE_Sizes:
        if size == '':
            continue
        else:
            sumReSizes = sumReSizes + float(size)
    return ((sumSizes/(sumSizes+sumReSizes))*100)

    

def computePeriodicSucessRateNB(HMD_Times,HMD_RE_Times,duration=1):
    # This method is used to compute the periodic sucess rate based on the number of frames (ignoring the size of frames)
    # prerequisite: the retransmission attempts has to be removed from the data lists of the HMD results 'results' by using the method 'eliminateRetransmittedFrames'
    # input: the list of time stamps of the data
    #        the list of time stamps of the retransmitted frames
    #        the period in seconds
    # output: a list of periodic sucess rates in form of a percentage 
    duration = 1 if duration <= 0 else duration
    listOfSucessRates = []
    HMD_Dict = computePeriodicNBOfHMDFrames(HMD_Times,duration)
    HMD_RE_Dict = computePeriodicNBOfHMDFrames(HMD_RE_Times,duration)
    for key in HMD_Dict.keys():
        # the try except block is used to avoid throwing exceptions when there is no retransmitted frame at a specific period
        try:
            sucessRate = float(HMD_Dict[key]/(HMD_Dict[key]+HMD_RE_Dict[key])) * 100
            listOfSucessRates.append(sucessRate)
        except:
            listOfSucessRates.append(100.00)

    return listOfSucessRates



def computePeriodicSucessRateSize(HMD_Times,Sizes,HMD_RE_Times,RE_Sizes,duration=1):
    # This method is used to compute the periodic sucess rate based on the size of the transmitted data 
    # prerequisite: the retransmission attempts has to be removed from the data lists of the HMD results 'results' by using the method 'eliminateRetransmittedFrames'
    # input: the list of time stamps of the data
    #        the list of the frames sizes of the data
    #        the list of time stamps of the retransmitted frames
    #        the list of the frames sizes of the retransmitted frames 
    #        the period in seconds
    # output: a list of periodic sucess rates in form of a percentage 
    duration = 1 if duration <= 0 else duration
    listOfSucessRates = []
    HMD_Dict = computePeriodicSizeOfHMDFrames(HMD_Times,Sizes,duration)
    HMD_RE_Dict = computePeriodicSizeOfHMDFrames(HMD_RE_Times,RE_Sizes,duration)

    for key in HMD_Dict.keys():
        # the try except block is used to avoid throwing exceptions when there is no retransmitted frame at a specific period
        try:
            sucessRate = float(HMD_Dict[key]/(HMD_Dict[key]+HMD_RE_Dict[key])) * 100
            listOfSucessRates.append(sucessRate)
        except:
            listOfSucessRates.append(100.00)

    return listOfSucessRates