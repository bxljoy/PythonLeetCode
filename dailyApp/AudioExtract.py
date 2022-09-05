import os

def convertVideoToAudio(path):
    '''
        -q:a 0 means the quality of audio (0-highest, 6-lowest)
        -map a means the default stream, use the command line: / ffmpeg -i input.mp4 /
        to show the metadata for the mp4, i.e. : Stream #0:0 for English; Stream #0:1 for Chinese
        use the command line: / ffmpeg -i input.mp4 -q:a 5 -map 0:1 output.mp3 / to get the English audio
    '''
    '''
        / ffmpeg -i input.mp4  -map 0:0 -map 0:2 -c copy -disposition:a:0 default -y output.mp4 /
        -map 0:0 means the video stream, -map 0:1 means Chinese stream,  -map 0:2 means English stream,
        I only want to remain the video and English stream , so I use the command line above to get that.
    '''
    cmd = '/Users/bxl/Downloads/ffmpeg -i '
    suffix = ' -vn -ar 44100 -ac 2 -ab 128k -f mp3 '
    # suffix = ' -q:a 0 -map a '
    # suffix = ' -q:a 3 -map 0:2 '
    # suffix = ' -map 0:0 -map 0:2 -c copy -disposition:a:0 default -y '
    for file in os.listdir(path):
        if file.split('.')[-1] not in ['mp4', 'mkv']:
            continue
        newFile = path + file
        print(newFile)
        newSuffix = file.split('.')[0] + '.mp3'
        # newSuffix = file.split('.')[0] + 'New' + '.mp4'
        print(newSuffix)
        finalCmd = cmd + '\"' + newFile + '\"' + suffix + '\"' + path + newSuffix + '\"'
        print(finalCmd)
        os.system(finalCmd)

if __name__ == '__main__':
    path = '/Users/bxl/Downloads/LankyBox26/'
    convertVideoToAudio(path)

