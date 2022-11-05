
def convertTime(time):
    # this method convert the time to ms from the beginning of the day
    splittedTime = time.split(":")
    if(len(splittedTime)>2):
        timeInMs = float(splittedTime[0])*60*60*1000 + float(splittedTime[1])*60*1000 + float(splittedTime[2])*1000
    else:
        timeInMs = float(splittedTime[0])*60*60*1000 + float(splittedTime[1])*60*1000 
    return timeInMs


def processSessionLog(sessionLogFilePath):
    # Experiment Info Parameters
    Vsync2Photons = 0 # time from vsync to photon in seconds
    refreshRate = 0 # the targeted refresh rate
    renderTarget = {'horizontal' : 0,'vertical':0}
    startTime = "22:00"
    endTime = "22:05"
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

def main():

    processSessionLog('session_log.txt')


                
            


if __name__ == "__main__":
   main()