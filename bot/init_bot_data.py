import csv
import datetime
import paths

class BotInit:
    def __init__(self) -> None:
        self.admins = []
        self.chat_ids = []
        self.token = ""
        self.users_access = []
        self.update()
    
    def update(self):
        self.upload_admins_ids()
        self.upload_chat_ids()
        self.upload_token()
        self.upload_access_users()

    def upload_token(self):
        file = open(paths.path_data + '/API_TOKEN.txt')
        self.token = file.readline()        

    def upload_chat_ids(self):
    #IDs users
        with open(paths.path_data + '/chat_id.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                id = line.strip()
                if id != '':
                    if int(id) not in self.chat_ids:
                        self.chat_ids.append(int(id))

    def upload_admins_ids(self):
        #IDs admins
        
        with open(paths.path_data + '/admins_id.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                id = line.strip()
                if id != '':
                    self.admins.append(int(id))

    def upload_access_users(self):
        with open(paths.path_data + '/users.csv', 'r') as file:
            reader = csv.DictReader(file, delimiter='\t')
            for row in reader:
                user = {}
                user['user_name'] = row['user_name']
                user['id'] = int(row['id'])
                dt = datetime.datetime.strptime(row['date'], '%d.%m.%Y %H:%M')
                user['date'] = dt
                # print(row['user_name'], '|', row['id'], '|', row['date'])
                self.users_access.append(user)
                
    def PrintDebug(self):
        for i in self.users_access:
            print (i)

    def isAdmin(self, id):
        if id in self.admins:
            return True
        else:
            return False

    def getChats(self):
        return self.chat_ids

    def getToken(self):
        return self.token


if __name__ == '__main__':
    bi = BotInit()
    bi.PrintDebug()