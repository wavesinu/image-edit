# 미니 프토샵 프로그램 만들기
import os
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
# 이미지 처리 기능을 제공하는 Pillow 라이브러리를 import 함
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

# 전역변수 선언 및 초기화
window, canvas, paper = None, None, None
photo, photo2 = None, None
oriX, oriY = 0, 0
angle = 0

def displayImage(img, width, height):
    global window, canvas, paper, photo, photo2, oriX, oriY, angle

    # 화면 크기 설정
    window.geometry(str(width)+'x'+str(height))
    # print(str(width)+", "+str(height))
    # 기존에 canvas 에 출력한 그림이 있다면
    if canvas != None:
        canvas.destroy()    # canvas를 깨끗하게 만든다.

    # canvas 생성
    canvas = Canvas(window, width=width, height=height)
    paper = PhotoImage(width=width, height=height)
    # 이미지의 폭을 절반의 값과 높이의 절반의 값의 위치에 이미지를 생성한다.
    canvas.create_image((width/2, height/2), image=paper)

    rgbString = ''
    rgbImage = img.convert("RGB")
    cnt = 0
    # 높이와 너비만큼 더블루프 돌면서 rgb 값을 getpixel() 로 추출하여 16진수 형태로 rgbString 에 누적시키고 있다.
    for i in range(0, height):
        tmpString = ""
        for j in range(0,width):
            # 복사된 이미지 객체에 getpixel() 를 이용하여 rgb값을 얻어낼 수 있다.
            r, g, b = rgbImage.getpixel((j, i))
            tmpString += "#%02x%02x%02x " %(r, g, b) # x 값 뒤에 한 칸을 공백으로 두어야한다.
            cnt += 1
        rgbString += "{" + tmpString + "} " # } 뒤에 한칸 공백(중요)
    # print(rgbString, "cnt: ",cnt)
    # rgb 문자열 값을 paper 에 대입시키면서 papar 에 이미지를 출력시키고 있다.
    paper.put(rgbString)
    canvas.pack()

# 파일 열기
def func_open():
    # photo 는 원본 이미지 저장할 변수, photo2 는 이미지 처리후 나타나는 결과 이미지를 저장할 변수,
    # oriX, oriY 원본 이미지의 폭과 높이를 저장할 변수
    global window, canvas, paper, photo, photo2, oriX, oriY, angle
    # 파일다이얼로그(열기)를 통하여 원하는 이미지를 사용자가 선택할 수 있도록 한다.
    readFp = askopenfilename(parent=window, filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;"
                                                        "*.tif;*.gif"),("모든 파일","*.*")))

    # 파이썬에서 제공하는 PhotoImage() 가 아닌 Pillow 라이브러리에서 제공하는 Image.open() 함수를 사용하도록 한다.
    # 파이썬에서 제공하는 PhotoImage()0 클래스는 이미지 파일의 확장자가 .gif, .png 만 지원하므로 한계가 있다.
    # 사용자가 선택한 이미지를 읽고 RGB 모드로 변환시키고 있다.
    photo = Image.open(readFp).convert("RGB")
    # 원본 이미지의 너비와 높이를 저장하고 있다.
    oriX = photo.width
    oriY = photo.height
    # 원본 이미지를 photo2 변수에 복사하여 대입한다.
    photo2 = photo.copy()
    newX = photo2.width
    newY = photo2.height
    print(newX, ", ",newY)  # 복사된 이미지의 높이와 너비값을 출력해봄
    # 복사한 내용을 가지고 displayImage() 함수를 호출하고 있다.
    displayImage(photo2, newX, newY)

# 파일 저장
def func_save():
    global window, canvas, paper, photo, photo2, oriX, oriY, angle
    # photo2 가 None 이라는 것은 복사된 이미지 객체가 없다...라면
    if photo is None:
        return  # return 을 이용하여 함수를 종료시킨다.
    # 파일 다이얼로그(저장)을 띄어서 사용자로부터 파일명을 입력받고 저장하는 방식 여기서는 이미지 파이리을 저장할 때
    # 기본값으로 .jpg 파일로 저장하게끔 하였다.
    saveFp = asksaveasfile(parent= window, mode='w', defaultextension='.jpg',
                           filetypes=(("JPG 파일", "*.jpg;*.jpeg"),("모든파일","*.*")))
    # 사용자가 입력한 파일명으로 저장
    photo2.save(saveFp.name)


# 프로그램 종료
def func_exit():
    exit()

# 이미지 사이즈 조절
def func_resize():
    global window, canvas, paper, photo, photo2, oriX, oriY, angle
    width = askinteger("가로 크기", '가로 크기를 입력해주세요.')
    length = askinteger("세로 크기", '세로 크기를 입력해주세요.')

    photo2 = photo.copy()
    photo2 = photo2.resize((int(width), int(length)))
    newX =photo2.width
    newY =photo2.height
    displayImage(photo2,newX,newY)

    photo = photo2 # 이렇게 해야지 계속 편집 가능(안 적을 시 연속 편집 불가능)    
     
# 이미지 상하반전
def func_mirror1():
    global window, canvas, paper, photo, photo2, oriX, oriY, angle


# 이미지 좌우반전
def func_mirror2():
    global window, canvas, paper, photo, photo2, oriX, oriY, angle


# 이미지 회전
def func_rotate():
     global window, canvas, paper, photo, photo2, oriX, oriY, angle
     angle1 = askinteger("이미지 회전", '이미지 회전 각도를 입력해주세요(90, 180, 270, 360).') # 각도 입력받기
     angle +=angle1
     photo2 = photo.copy()
     photo2 = photo2.rotate(angle1, expand = 1)  # expand = 1 이미지 안잘리게 해줌 / True도 가능

     if (angle%360 == 90 or angle%360 == 270):
         displayImage(photo2, oriY, oriX)        # 가로 세로를 바꿔서 이미지를 안잘리게 해줌
     else:
         displayImage(photo2, oriX, oriY)

     photo2.show()

     photo = photo2  # 이렇게 해야지 계속 편집 가능(안 적을 시 연속 편집 불가능)
    

# 이미지를 흑백으로 하는 기능
def func_bw():
    global window, canvas, paper, photo, photo2, oriX, oriY, angle
    photo2 = photo.copy()
    
    photo2 = ImageOps.grayscale(photo2) # 컬러 -> 흑백
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)
    photo = photo2

# 이미지 품질 저하
def func_requality():
    global window, canvas, paper, photo, photo2, oriX, oriY, angle
    photo2 = photo.copy()
    qual = askinteger("품질값", '품질값을 입력해주세요.')
    #이미지를 저장시키는데 퀄리티를 낯춘 상태로 저장
    photo2.save(readFp,'JPEG', quality=int(qual))

    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

    photo = photo2    
    
        

# 이미지 크롭
def func_crop(): 
    global window, canvas, paper, photo, photo2, oriX, oriY, angle

    photo2 = photo.copy()
    width_start = askinteger("가로시작점", '가로 시작점을 입력해주세요.')
    height_start = askinteger("세로시작점", '세로 시작점을 입력해주세요.')
    width_range = askinteger("가로범위", '가로 범위를 입력해주세요.')
    height_range = askinteger("세로범위", '세로 범위를 입력해주세요.')

    area = (width_start, height_start, width_range, height_range)
    photo2 = photo2.crop(area)        # 이미지 crop
    newX = photo2.width               # 새로운 가로 길이
    newY = photo2.height              # 새로운 세로 길이
    displayImage(photo2, newX, newY)
    photo = photo2
    
    
# 메인코드 부분
if __name__ == '__main__':
    window = Tk() # 윈도우 생성
    window.geometry("400x400") # 윈도우 크기 설정
    window.title("미니 포토샵")

    mainMenu = Menu(window) # 메뉴바를 생성
    window.config(menu= mainMenu) # 윈도우의 메뉴를 mainMenu 로 설정

    fileMenu = Menu(mainMenu, tearoff=False) # tearoff 속성은 메뉴의 점선을 없애준다.
    # add_cascade() 함수는 상위메뉴와 하위메뉴를 연결해준다.(상위 메뉴=mainMenu)
    mainMenu.add_cascade(label='파일', menu = fileMenu)
    # add_command() 는 메뉴 항목을 생성해준다.
    fileMenu.add_command(label='파일 열기', command=func_open)
    fileMenu.add_command(label='파일 저장', command=func_save)
    # 구분선 추가하기
    fileMenu.add_separator()
    fileMenu.add_command(label='종료', command=func_exit)


    image1Menu = Menu(mainMenu, tearoff=False)
    mainMenu.add_cascade(label='메뉴1', menu=image1Menu)
    image1Menu.add_command(label='사이즈 조절', command=func_resize)
    image1Menu.add_command(label='품질 저하', command=func_requality)    
    image1Menu.add_separator()
    image1Menu.add_command(label='상하 반전', command=func_mirror1)
    image1Menu.add_command(label='좌우 반전', command=func_mirror2)
    image1Menu.add_command(label='회전', command=func_rotate)

    image2Menu = Menu(mainMenu,tearoff=False)
    mainMenu.add_cascade(label="메뉴2", menu=image2Menu)
    image2Menu.add_command(label='흑백', command=func_bw)
    image2Menu.add_separator()
    image2Menu.add_command(label='사진 자르기', command=func_crop)

    window.mainloop()
