checkValue=True
userInfo=[]
while True:

    name=input("put name :")
    userInfo.append(name)
    number=int(input("put number :"))
    userInfo.append(number)
    movieName=input("put moive name : ")
    userInfo.append(movieName)
    movieTime=input("What time you wanna watch movie?(morning, lunch, afternoon)")
    userInfo.append(movieTime)
    userSeat=input("Which seat you want to sit? (1,2,3,4,5)")
    userInfo.append(userSeat)
    checkPrint=input("You want to see your INFO? Y/N")
    if checkPrint=="Y":
        print(userInfo)
        break
