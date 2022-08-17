import os

def convertWebmToMp4(path):
    cmd = '/Users/bxl/Downloads/ffmpeg -i '
    # suffix = ' -crf 23 '
    for file in os.listdir(path):
        if file.split('.')[-1] not in ['webm']:
            continue
        newFile = path + file
        print(newFile)
        newSuffix = file.split('.')[0] + '.mp4'
        print(newSuffix)
        # finalCmd = cmd + '\"' + newFile + '\"' + suffix + '\"' + path + newSuffix + '\"'
        finalCmd = cmd + '\"' + newFile + '\" ' + ' \"' + path + newSuffix + '\"'
        print(finalCmd)
        os.system(finalCmd)

if __name__ == '__main__':
    path = '/Users/bxl/Downloads/LankyBox21/'
    convertWebmToMp4(path)

