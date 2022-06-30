from datetime import datetime
import datetime as dt
import csv
from bot.init_bot_data import BotInit
from bot.create_bot import Bot
from paths import path_data


class BotController:
    def __init__(self, data: BotInit, bot: Bot) -> None:
        self.data = data
        self.bot = bot

    def getBot(self) -> Bot:
        return self.bot

    def changeAccessUser(self,date:datetime, username='', id=-1) -> bool:
        if id != -1:
            #check id
            for i in self.data.users_access:
                if i['id'] == str(id):
                    i['date'] = date
                    self.updateTableAccess()
                    return True
        elif username != '':
            #check username
            for i in self.data.users_access:
                if i['user_name'] == username:
                    i['date'] = date
                    self.updateTableAccess()
                    return True
            
        return False

    def updateTableAccess(self):
        with open(path_data + '/users.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter='\t')
            writer.writerow(['user_name', 'id', 'date'])
            for i in self.data.users_access:
                writer.writerow([i['user_name'], i['id'], i['date'].strftime('%d.%m.%Y %H:%M')])

    def updateTableChatIds(self):
        with open(path_data + '/chat_id.txt', 'w') as file:
            for i in self.data.chat_ids:
                file.write(str(i)+'\n')

    def trialAccessForUser(self, username:str, id:int):
        #now + 1 week
        now = datetime.now()
        delta = dt.timedelta(weeks=1)
        res = now + delta
        self.data.users_access.append({'user_name':username, 'id':id, 'date':res})
        self.updateTableAccess()

    def getAccessUser(self, username='', id=-1) -> bool:
        now = datetime.now()
        if username == '' and id == -1:
            return False

        if id != -1:
            #check id
            for i in self.data.users_access:
                if i['id'] == id:
                    user_date = i['date']
                    print((user_date - now).seconds)
                    if user_date > now:
                        return True
                    else:
                        return False

        elif username != '':
            #check username
            for i in self.data.users_access:
                if i['user_name'] == username:
                    user_date = i['date']
                    if (user_date - now).seconds > 0:
                        return True
                    else:
                        return False

        return False


    def isAdmin(self, id) -> bool:
        if id in self.data.admins:
            return True
        else:
            return False
    
    def getDateFromUsername(self, username:str) -> datetime | bool:
        for i in self.data.users_access:
            if i['user_name'] == username:
                return i['date'], True
        return None, False

    def isUser(self, id) -> bool:
        for i in self.data.users_access:
             if i['id'] == id:
                return True
        return False

    def addUser(self, username, id:int) -> bool:
        if not self.isUser(id):
            self.trialAccessForUser(username, id)
            self.data.chat_ids.append(id)
            self.updateTableChatIds()
            
if __name__ == "__main__":
    bc = BotController()
    # bc.addUser('new1',21)
    print(bc.getAccessUser(id=451720314))
    # dt = datetime.strptime('07.01.2022 20:00', '%d.%m.%Y %H:%M')
    # print (bc.changeAccessUser(dt, username='new1'))