class ChatRoom:
    username = ""
    password = ""
    roomName = ""
    nickname = ""
    allUser = 0
    onlineUser = 0
    allUserList = []
    onlineUserList = []
    notAllowUserList = ["hacker","ronaldo","elon mask","amin","ali"]

    def __init__(self,nickname):
        
        if nickname not in ChatRoom.notAllowUserList:
            self.nickname = nickname
            ChatRoom.allUser += 1
            ChatRoom.onlineUser += 1
            print(f"welcome chatroom app {self.nickname} -- all users : {ChatRoom.allUser}")
            ChatRoom.allUserList.append(self.nickname)
            ChatRoom.onlineUserList.append(self.nickname)
        else:
            print(f"you cant login to app my friend {nickname}")


    def delete_account(self):
        ChatRoom.allUser -= 1
        ChatRoom.onlineUser -= 1
        ChatRoom.allUserList.remove(self.nickname)
        ChatRoom.onlineUserList.remove(self.nickname)
        print(f"good bye {self.nickname}")


    def login_user(self,name):
        if name in ChatRoom.notAllowUserList:
            print(f"you cant login to app my friend {name}")

        elif self.nickname in ChatRoom.allUserList:
            ChatRoom.onlineUser += 1
            print(f"welcome chatroom app {self.nickname} -- all users : {ChatRoom.allUser} online users {self.onlineUser}")
            ChatRoom.onlineUserList.append(self.nickname)
            
        else:
            ChatRoom.allUser += 1
            ChatRoom.allUserList.append(self.nickname)
            ChatRoom.onlineUser += 1
            print(f"welcome back to the app {self.nickname} -- all users : {ChatRoom.allUser} online users {self.onlineUser}")
            ChatRoom.onlineUserList.append(self.nickname)


        


    def showUsers(self,listUser):
        i = 1
        print(f"-------all users is {ChatRoom.allUserList}--------")
        for name in listUser:
            print(i,name)
            i += 1

    def show_online_users(self):
        print(f"online users count : {ChatRoom.onlineUser}")
        print(f"list online users : {ChatRoom.onlineUserList}")
        i = 1
        for name in ChatRoom.onlineUserList:
            print(i,name)
            i += 1
    def logOut(self):
        ChatRoom.onlineUser -= 1
        ChatRoom.onlineUserList.remove(self.nickname)
        print(f"good luck {self.nickname}")

        
mohammadjavad = ChatRoom("mohammad javad")
reza = ChatRoom("reza")
elia = ChatRoom("elia")
tara = ChatRoom("tara")
capitan = ChatRoom("capitan")
jamshidi = ChatRoom("jamshidi")
amin = ChatRoom("amin")
mohandes = ChatRoom("mohandes")
eisa = ChatRoom("eisa")
ali = ChatRoom("ali")

print("--------part1--------------")

reza.showUsers(ChatRoom.allUserList)

print("--------part2--------------")


mohandes.logOut()

reza.logOut()

capitan.logOut()

amin.login_user("amin")

print("--------part3--------------")

eisa.show_online_users()


print("--------part4--------------")

capitan.login_user("capitan")

print("--------part5--------------")

amin.login_user("amin")
