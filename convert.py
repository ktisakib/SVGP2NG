import os
import cairosvg

# bash color scheme
begin_success_label = '\x1b[6;32;40m'
begin_error_label   = '\x1b[6;30;41m'
end_label = '\x1b[0m'

sourceDir = "./src"
distDir = "./dst"
if not os.path.exists(distDir):
      os.makedirs(distDir)

convertList = []
for root, dirs, files in os.walk(sourceDir, topdown=False):
  for name in files:
    if '.svg' in name:
      sourceName = os.path.join(root, name)
      distName = sourceName.replace(sourceDir, distDir) # replace ./src to ./dst
      distName = distName.replace(".svg", ".png") # replace .svg to .png
      convertList.append((sourceName, distName))
  for name in dirs:
    dir = os.path.join(root, name)
    dir = dir.replace(sourceDir, distDir) # replace ./src to ./dst
    if not os.path.exists(dir):
      os.makedirs(dir)

print("======================================================")
print('Start converting {0} files...'.format(len(convertList)))
print("======================================================")
success = 0
error = 0
for index, (source, dist) in enumerate(convertList):
  progress = '{0}/{1}'.format(index, len(convertList))
  print(progress + ":\t" + source + " is converting... ")
  try:
    cairosvg.svg2png(url=source, write_to=dist)
    print("\t" +begin_success_label+ dist + " is converted."+end_label)
    success = success + 1
  except:
    print("\t"+begin_error_label+"error"+end_label)
    error = error + 1
  
print("======================================================")
print('{0} files are tried to convert. {1} files are succeeded. {2} files are failed.'.format(len(convertList), success, error))
print("======================================================")