import os
import xml.etree.ElementTree as ET

# r"변경하고자 하는 xml을 넣은 디렉토리"
# 해당 폴더 내의 모든 xml파일에 수정작업이 들어갑니다.
targetDir = r"C:\Users\User\Documents\GitHub\Study\Project\Project_for_Moon"
num = 1

##targetDir에서 .xml파일 이름들 리스트로 가져오기
file_list = os.listdir(targetDir)
xml_list = []
for file in file_list:
    if '.xml' in file:
        xml_list.append(file)

##모든 .xml파일에 대해 수정
for xml_file in xml_list:
    target_path = targetDir + "\\" + xml_file
    targetXML = open(target_path, 'rt', encoding='UTF8')

    tree = ET.parse(targetXML)

    root = tree.getroot()

    ##수정할 부분
    target_tag = root.find("food")

    original = target_tag.text
    
    modified = original.replace(r"",r"")
    target_tag.text = modified  #수정
    print("[" + str(num) + "]" + xml_file + "[success]")
    
    tree.write(target_path)
    num += 1

print("finished")