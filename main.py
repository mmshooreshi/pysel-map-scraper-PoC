from array import array
from multiprocessing.dummy import Array
from tracemalloc import start
from selenium import webdriver
from selenium.webdriver.common.by import By
from drivers import create_driver
import csv
import time, os, datetime
from time import sleep

import geojson

from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import NoSuchElementException
from types import new_class
from typing import Counter, Type
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import keyboard

from tkinter import *

global ind,TypeVar,TypesList, csvfile,csvwriter, nextPointIJ, towrite, CurY,CurX




BASE_URL = "https://www.google.com/maps/search/{search}/@{lat},{lng},{zoom}z?hl=en"

driver = create_driver()
actions = ActionChains(driver)
driver.maximize_window()
print(driver.get_window_size())

global body_element

xx=50
yy=50
xpathVar="//*[@id='scene']/div[3]/div[2]/div/button"
idVar='.d4HG7-G0jgYd-OQl0D'
xpathVarElement=''' a= document.evaluate("{xpathVar}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; '''



dirscriptR="""
ab=document.getElementById("circleTracker");
ab.innerHTML = '→';
"""
dirscriptL="""
ab=document.getElementById("circleTracker");
ab.innerHTML = '←';
"""
dirscriptU="""
ab=document.getElementById("circleTracker");
ab.innerHTML = '↑';
"""
dirscriptD="""
ab=document.getElementById("circleTracker");
ab.innerHTML = '↓';
"""

circleDiv = """element = document.createElement('div');
element.setAttribute("id","circleTracker")
imgel=document.createElement('img');
imgel.setAttribute("id","parrot");
imgel.setAttribute("src","https://cultofthepartyparrot.com/parrots/hd/parrot.gif");
imgel.style.cssText = "width: 50px;" ;
element.append(imgel);
element.style.cssText = 'background: #34ff9169;width: 80px;height: 80px;position:absolute;z-index:100000000;left:50%;top:50%;border-radius: 22px;border-color: #b94e7d;border-style:solid;border-width: 1px;box-shadow: 1px -1px 30px rgb(149 0 0); font-size:40px; text-align:center; vertical-align: center;';
document.body.append(element); 
"""

TranspWindow="""
elementO = document.createElement('div');
elementO.setAttribute("id","windowOverlay");
elementO.style.cssText = 'position:fixed;top:200px;left:0;width:100%;height:100%;background:rgba(0,255,0,0.5);z-index:100000000';
document.body.prepend(elementO);
"""



sx = 650
sy = 400


def check_exists(path):
    try:
        l=driver.find_elements(By.XPATH, "//button[@aria-label='Collapse side panel']")
        #print("tedad:",len(l))
        if(len(l)==6):
            return True;
        else:
            return False;
        
        
    except NoSuchElementException:
        return False


def MoveUpdate(Value):
    return int((abs(Value)+1)*(abs(Value)/Value)*-1)

def tab():
    #print("azad")
    dragV(5,5)
    #actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
    # sleep(1)
    # actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()    
    # sleep(1)

    #actions.send_keys(Keys.TAB).perform()
    # actions.send_keys(Keys.TAB).perform()
    # actions.send_keys(Keys.TAB).perform()
    # actions.send_keys(Keys.TAB).perform()

    #actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
    
    
   
  
def MoveKeys(Direction,ValueHorizontal,ValueVertical):
    h=ValueHorizontal
    v=ValueVertical
    print(Direction,"Hor:",ValueHorizontal,"Ver:",ValueVertical)
    if(Direction == 1):
        Temp = abs(ValueHorizontal)
        if(ValueHorizontal > 0):
            driver.execute_script(dirscriptR)
            for i in range(Temp): 
                #actions.send_keys(Keys.ARROW_RIGHT).perform()
                print("R",i)
                dragV(-200,0)
                if(i%3==0):checkKon()
        else:
            driver.execute_script(dirscriptL)
            for i in range(Temp): 
                #actions.send_keys(Keys.ARROW_LEFT).perform()
                print("L",i)
                dragV(200,0)
                if(i%3==0):checkKon()
        h=MoveUpdate(ValueHorizontal)
    else:
        Temp = abs(ValueVertical)
        if(ValueVertical > 0):
            driver.execute_script(dirscriptD)
            for i in range(Temp): 
                #actions.send_keys(Keys.ARROW_DOWN).perform()
                print("D",i)
                dragV(0,-200)
                if(i%3==0):checkKon()
        else:
            driver.execute_script(dirscriptU)
            for i in range(Temp): 
                #actions.send_keys(Keys.ARROW_UP).perform()
                print("U",i)
                dragV(0,200)
                if(i%3==0):checkKon()
        v=MoveUpdate(ValueVertical)
    return [h,v]


def NewMoveKeys(n,i):
    
    canvas_element = driver.find_element(By.TAG_NAME,'canvas') 
       
    driver.execute_script(dirscriptL)
    print("started")
    sleep(0.5)
    while(i<=n-1): 
        actions.click(canvas_element).move_by_offset(0, 0).perform()   
        #dragV(-200,0)
        print("started left",i)
        actions.send_keys(Keys.ARROW_LEFT).perform()
        sleep(0.3)
        actions.send_keys(Keys.ARROW_LEFT).perform()
        print("L",i)
        if(i % 3 ==0): checkKon(n,i)
        i=i+1
    driver.execute_script(dirscriptU)
    checkKon(n,i)
    while(i<=2*n-1):
        actions.click(canvas_element).move_by_offset(0, 0).perform()   
        #dragV(0,200)
        actions.send_keys(Keys.ARROW_UP).perform()
        sleep(0.3)
        actions.send_keys(Keys.ARROW_UP).perform()
        print("U",i)
        if(i % 2 ==0): checkKon(n,i)
        i=i+1
    driver.execute_script(dirscriptR)
    checkKon(n,i)
    while(i<=3*n):
        actions.click(canvas_element).move_by_offset(0, 0).perform()   
        #dragV(200,0)
        actions.send_keys(Keys.ARROW_RIGHT).perform()
        sleep(0.3)
        actions.send_keys(Keys.ARROW_RIGHT).perform()
        print("R",i)
        if(i % 3 ==0): checkKon(n,i)
        i=i+1
    driver.execute_script(dirscriptD)
    checkKon(n,i)
    while(i<=4*n+1): 
        actions.click(canvas_element).move_by_offset(0, 0).perform()   
        #dragV(0,-200)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        sleep(0.3)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        print("D",i)
        if(i % 2 ==0): checkKon(n,i)
        i=i+1
    checkKon(n,i)
    

def MoveInRatio(n,i):
    body_element= driver.find_element(By.TAG_NAME, 'body')
    canvas_element = driver.find_element(By.TAG_NAME,'canvas')    
    Aratio = int(getMoveRatio()[0]);
    Adistance = getMoveRatio()[1];
    Adirection = getMoveRatio()[2];
    print(Aratio,Adistance,Adirection)
    
    checkKon(n,i)
    if Adirection[0]>0:
        #body_element.send_keys(Keys.ARROW_UP + Keys.ARROW_UP)
        #actions.send_keys_to_element(canvas_element,Keys.ARROW_UP + Keys.ARROW_UP)
        actions.send_keys(Keys.ARROW_UP).perform() 
        sleep(0.4)
        actions.click(canvas_element).send_keys(Keys.ARROW_UP).perform() 
    elif Adirection[0]<0:
        #body_element.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN)
        #actions.send_keys_to_element(canvas_element,Keys.ARROW_DOWN + Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN).perform() 
        sleep(0.4)
        actions.click(canvas_element).send_keys(Keys.ARROW_DOWN).perform() 
    checkKon(n,i)
    if Adirection[1]>0:
        #body_element.send_keys(Keys.ARROW_RIGHT + Keys.ARROW_RIGHT)
        #actions.send_keys_to_element(canvas_element,Keys.ARROW_RIGHT + Keys.ARROW_RIGHT)
        actions.send_keys(Keys.ARROW_RIGHT).perform() 
        sleep(0.4)
        actions.click(canvas_element).send_keys(Keys.ARROW_RIGHT).perform()  
    elif Adirection[1]<0:
        #body_element.send_keys(Keys.ARROW_LEFT + Keys.ARROW_LEFT)
        #actions.send_keys_to_element(canvas_element,Keys.ARROW_LEFT + Keys.ARROW_LEFT)
        actions.send_keys(Keys.ARROW_LEFT).perform() 
        sleep(0.4)
        actions.click(canvas_element).send_keys(Keys.ARROW_LEFT).perform()  
    checkKon(n,i)
    
    

def Scrape(n,i):    
    while True:
        #tab()
        MoveInRatio(n,i)
        n=n+2
        i=0
        # try:
        #     SearchAreaButton = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Search this area"]')))
        #     SearchAreaButton.click()
        #     CurrentX=getLatLng()[1]
        #     #print(CurrentX)
        #     #print(LimitX)
        #     #print("ama:",horizontalMove,verticalMove)
        #     #dragV(horizontalMove*200,verticalMove*200)
        #     #sleep(1.5)
        # except:
        #     n=n+2
        #     NewMoveKeys(n)

            
            # Move = MoveKeys(Direction,horizontalMove,verticalMove)
            # horizontalMove = Move[0]
            # verticalMove = Move[1]
            # Direction=Direction*-1
            # print(horizontalMove,verticalMove)
            #dragV(horizontalMove*200,verticalMove*200)
CurrentX =35.70517
CurrentY =51.398052

def checkKon(n,i):
    global CurrentX
    global CurrentY

    print(CurrentX,CurrentY)
    try:
        SearchAreaButton = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Search this area"]')))
        SearchAreaButton.click()
        latlngC=getLatLng()
        if (latlngC != False): 
            CurrentX=getLatLng()[0]
            CurrentY=getLatLng()[1]
        tab()
        #sleep(1)
        #driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.TAB)
        #sleep(1.5)
    except:
        print("an")

    sidebarcheck("cont",CurrentX,CurrentY,n,i)

def sidebarcheck(text,CurrentX,CurrentY,n,i):
    if(check_exists("Collapse side panel")):
        actions.send_keys(",").perform()
        tab()
        if(text=="cont" and ("/place/" in driver.current_url)):
            print(CurrentX,CurrentY,ZoomZ,TypeVar)
            azaval()
            #startMain(CurrentX,CurrentY,ZoomZ,TypeVar,n,i)
        #sleep(0.5)
        #print("t")
        #print("khodafez")


                
def getLatLng():
    url =driver.current_url
    if("/place/" in url):
        return False
    temp = str.split(url,",")
    lat = str.split(temp[0],"@")[1]
    lng=temp[1]
    return [lat,lng]
    
def CircleDiv():
    driver.execute_script(circleDiv)
    #driver.execute_script(TranspWindow)
    zero_elem = driver.find_element_by_tag_name('body')
    x_body_offset = zero_elem.location["x"]
    y_body_offset = zero_elem.location["y"]
    #print("Body coordinates: {}, {}".format(x_body_offset, y_body_offset))
    actions.move_by_offset(-x_body_offset, -y_body_offset)


def moveIcon(X,Y):
    global sx
    global sy
    sx=sx+X
    sy=sy+Y
    print(sx,sy,X,Y)
    script=f'''
    a=document.getElementById("circleTracker")
    a.style.left="{sx}px";
    a.style.top="{sy}px";
    a.style.position="absolute";
    '''
    #print(script)
    driver.execute_script(script)

    
def moveToXY(x,y,ifClick):
    if ifClick:
        actions.move_by_offset(x,y).click().perform()
    else:
        actions.move_by_offset(x,y).perform()
    #moveIcon(x,y)
       
def SearchURLGenerator(SEARCH, LAT,LNG,ZOOM):
    URL = BASE_URL.format(search=SEARCH,lat=LAT,lng=LNG,zoom=ZOOM)
    return URL


def dragV(dx,dy):
    canvas_element = driver.find_element(By.TAG_NAME,'canvas')    
    actions.click_and_hold(canvas_element).move_by_offset(dx, dy).move_by_offset(dx, dy).release().perform()
    #print("drag")
    sleep(0.5)

    # if(check_exists("Collapse side panel")):
    #     actions.send_keys(",").perform()
    #     #print("t")
    #     #print("khodafez")



def checkLimits(CurrentX , LimitX):
    if CurrentX>LimitX:
        return 0
    else:
        return 1 



def startMain(startPosX,startPosY,ZoomZ,TypeVar,n,i):
    global body_element
    print(ZoomZ)
    # for Line in GmapLineList[1:]:
        #print(TypeVar[0]," ",Line[2], Line[3], Line[4], Line[5],"\n")
    URL= SearchURLGenerator(TypeVar,startPosX,startPosY,ZoomZ)
    #print(URL)
    driver.get(URL)
    CircleDiv()
    body_element = driver.find_element(By.TAG_NAME,'body')    
    canvas_element = driver.find_element(By.TAG_NAME,'canvas')    
    moveToXY(0,0,False)
    #LimitX= Line[4]
    #sleep(0.5)
    sleep(2)
    sidebarcheck("start",startPosX,startPosY,n,i)
    sleep(3)
    actions.context_click(canvas_element).perform()
    sleep(0.5)
    actions.key_down(Keys.ALT).send_keys(Keys.ARROW_UP).key_up(Keys.ALT).perform()
    sleep(0.5)
    actions.send_keys(Keys.RETURN).move_by_offset(100, 0).perform()
    sleep(0.5)
    moveToXY(10,0,True)
    moveToXY(10,0,True)
    moveToXY(10,0,True)
    actions.send_keys(",").perform()
    print("Type:",TypeVar," line was sucessfully scraped :D ",Scrape(n,i))


     
#     # with open(r'gmap_lines copy.csv', encoding="utf-8-sig") as csvfile_gmaps:
#     #     GmapLine = csv.reader(csvfile_gmaps)
#     #     GmapLineList = list(GmapLine)
#     #     GmapLineList=GmapLineList[::4]
#     #     print(GmapLineList[1:])

#         ZoomZ=TypeArr[1]
#         startMain(35.70517,51.398052,ZoomZ,TypeVar,1,0)  
with open(r'INPUT_queries.csv', encoding="utf-8-sig") as csvfile_types: 
    Types = csv.reader(csvfile_types)
    TypesList = list(Types)
    #print(TypesList)


ind=0 
TypeVar=TypesList[ind][0]
ZoomZ=16
latestPoint=[]
layersCoord=[]
latestpointIJ=[]
nextPointIJ=[]
directionvar=[]

with open(r"INPUT_path.geojson") as f:
    tehran = geojson.load(f)

    
def getNextPoint():

    if len(tehran['features'][nextPointIJ[0]]["geometry"]["coordinates"][0])-1> nextPointIJ[1]:
        nextPointIJ[1]=nextPointIJ[1]+1
        return tehran['features'][nextPointIJ[0]]["geometry"]["coordinates"][0][nextPointIJ[1]]
    elif len(tehran['features'])-1> nextPointIJ[0]:
        nextPointIJ[0]=nextPointIJ[0]+1
        nextPointIJ[1]=0
        return tehran['features'][nextPointIJ[0]]["geometry"]["coordinates"][0][nextPointIJ[1]]
    else:
        return [0,0]


def getMoveRatio():
    global csvwriter, ind, TypeVar, TypesList, towrite, CurY, CurX
    towrite=[1,1]
    if(getLatLng()!=False):
        CurY=float(getLatLng()[0])
        CurX=float(getLatLng()[1])
    else:
        #print("an")
        azaval()

    
    nextPoint = tehran['features'][nextPointIJ[0]]["geometry"]["coordinates"][0][nextPointIJ[1]]
    
    print("CurrentPosition:",CurY,CurX)
    print("Destination:",nextPoint)

    #currentPoint = tehran['features'][latestpointIJ[0]]["geometry"]["coordinates"][0][latestpointIJ[1]]
    ratioYtoX = abs((nextPoint[1]-CurY) /(nextPoint[0]-CurX))
    try:
        directionvar=[(nextPoint[1]-CurY) / abs(nextPoint[1]-CurY) , (nextPoint[0]-CurX) / abs(nextPoint[0]-CurX) ]
        distance = (nextPoint[1]-CurY)**2 + (nextPoint[0]-CurX)**2 
    except:
        directionvar=[1,1]
        distance=0
    
    if(distance <= 0.0007):
        towrite= getNextPoint()
        if(towrite!=[]):
            csvwriter.writerow(towrite)
        csvfile.flush()

    if(towrite!=[0,0]):
        return ratioYtoX,distance,directionvar
    else:
        ind=ind+1
        TypeVar=TypesList[ind][0]
        azaval()
        return 0


def azaval():
    global nextPointIJ,csvwriter,csvfile, latestPoint, ind , TypeVar
    
    filename = "DOWNLOADED/latest_"+TypeVar+".csv"
    if os.path.exists(filename):
        with open(filename,'r') as csvfile: 
            latest = csv.reader(csvfile,quoting=csv.QUOTE_NONNUMERIC)
            breakV=False
            for line in latest:
                print(line)
                if(line==[0,0]):
                    ind=ind+1
                    TypeVar=TypesList[ind][0]
                    azaval()
                    break
                latestPoint = line
                #print(line)
            next=False;
            with open(filename,'a',) as csvfile: 
                csvwriter = csv.writer(csvfile) 
                for i in range(len(tehran['features'])):
                    layersCoord = tehran['features'][i]["geometry"]["coordinates"][0]
                    for j in range(len(layersCoord)):
                        Layer=layersCoord[j]
                        if(next):
                            csvwriter.writerow(Layer)
                            csvfile.flush()
                            nextPointIJ=[i,j]    
                            #print(tehran['features'][nextPointIJ[0]]["geometry"]["coordinates"][0][nextPointIJ[1]],tehran['features'][latestpointIJ[0]]["geometry"]["coordinates"][0][latestpointIJ[1]])
                            #print(getMoveRatio())
                            startMain(prev[1],prev[0],ZoomZ,TypeVar,1,0)
                            
                            breakV=True
                            break
                        if(Layer == latestPoint):
                            latestpointIJ=[i,j]    
                            next= True
                            prev=Layer
                    if breakV:
                        break
                    
                    #csvwriter.writerow(Layer) 
    else:
        with open(filename, 'x') as csvfile:
            csvwriter = csv.writer(csvfile) 
            Layer = tehran['features'][0]["geometry"]["coordinates"][0][0]
            #print(Layer)
            csvwriter.writerow(Layer) 
            csvfile.flush()
            sleep(1)
            azaval()
        
azaval()


#driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_RIGHT)
#driver.find_element(By.XPATH, '//button[@aria-label="Search this area"]').click()
        

    
# while True:
#     try:
#     if EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Search this area"]')):
#         aa#SearchAreaButton = WebDriverWait(driver, 0.5).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Search this area"]')))
#         SearchAreaButton=driver.find_element(By.XPATH, '//button[@aria-label="Search this area"]').click()
#         SearchAreaButton.click()
#         sleep(2)
#     aa#print("search area button was founded!")
# except:
#     dragV(-300,0)



#driver = webdriver.Chrome('D:\chromedriver.exe', chrome_options=chrome_options)
#while True:
#for row in rasmiolisttemp:
#driver.get(row[0])
# while True:
#     print(keyboard.read_key())
#     if keyboard.read_key() == "d":
#         moveToXY(xx,yy,False)
#         sx=sx+50
#         #print("right")
#     elif keyboard.read_key() == "a":
#         moveToXY(xx,yy,False)
#         sx=sx-50
#         #print("left")
#     elif keyboard.read_key() == "s":
#         moveToXY(xx,yy,False)
#         sy=sy+50
#         #print("down")
#     elif keyboard.read_key() == "w":
#         moveToXY(xx,yy,False)            
#         sy=sy-50
#         #print("up")
#     elif keyboard.read_key() == "esc":
#         print("esc")
#         break
    #moveToXY(xx,yy,False)
    #actions.click_and_hold(canvas_element)
    #sleep(3)
    #print("click 2")
    #moveToXY(xx,yy,False)
    #actions.release(body_element)
    # driver.find_element(By.XPATH, '//button[@aria-label="Search this area"]').click()
