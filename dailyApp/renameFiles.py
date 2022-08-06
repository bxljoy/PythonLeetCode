import os, shutil

def copy_search_file(srcDir, desDir):
    ls = os.listdir(srcDir)
    for line in ls:
        filePath = os.path.join(srcDir, line)
        if os.path.isfile(filePath):
            print(filePath)
            shutil.copy(filePath, desDir)

def renameFiles(path):
    for file in os.listdir(path):
        array = file.split('.')
        # if len(array) < 5:
        #     continue
        if array[-1] not in ['mkv', 'mp4', 'MKV', 'MP4']:
            continue
        print(file)
        # newName = array[0].split(' ')[7] + '.' + array[-1]
        newName = array[0] + '.' + array[-1]
        # newName = array[0].split('【')[0] + '.' + array[-1]
        # newName = 'S07E' + array[0].split('.')[0] + '.' + array[-1]
        print(newName)

        # array2 = newName.split(' ')
        # newName2 = array2[8] + '.mkv'
        # print(newName2)
        # os.rename(os.path.join(path, file), os.path.join(path, newName))

def renameDirectory(path):
    for file in os.listdir(path):
        if file.startswith('PJ.Masks.S04E'):
            print(file)
            newName = 'PJ.Masks.' + file.split('.')[2]
            print(newName)
            os.rename(os.path.join(path, file), os.path.join(path, newName))

if __name__ == '__main__':
    rootPath = '/Users/bxl/Downloads/'
    srcPath = '/Users/bxl/Downloads/Miraculous.S02/'
    destPath = '/Users/bxl/Downloads/PJ.Masks.S05/'
    renameFiles(srcPath)
    # renameDirectory(rootPath)
    # copy_search_file(srcPath, destPath)

    # arr = os.listdir(rootPath)
    # arr.sort()
    # count = 0
    # for file in arr:
    #     if file.startswith('PJ.Masks.S05E'):
    #         if count == 30:
    #             break
    #         filePath = os.path.join(rootPath, file)
    #         print(filePath)
    #         count += 1
    #         copy_search_file(filePath, destPath)

