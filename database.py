import datetime
import json


class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.machines = {}
        self.file = None
        self.load()

    def load(self):

        # self.machines = {}
        with open(self.filename,encoding='utf-8-sig') as f:

            machinery = json.load(f)
            print(machinery)
        f.close()
        for mach,values in machinery.items():

            self.machines[mach] = values

    def get_machine(self, name):
        if name in self.machines:
            return self.machines[id]
        else:
            return -1

    def add_machine(self, name):
        if name not in self.machines:
            self.machines[name] = {}
            self.save()
            return 1
        else:
            print("Machine exists already")
            return -1
    def add_part(self,name,name_part):
        if name_part not in self.machines[name]:
            self.machines[name][name_part] = {}
            self.save()
            return 1
        else:
            print("Machine exists already")
            return -1
    # def update_part(self,name,name_part):
    #     self.machines[name][name_part] =
    #     self.save()
    # def add_part(self,name,part_name,last_main,next_main,comms):
    #     try :
    #         self.machines[name][part_name] = {"Last Maintenance": last_main,"Next Maintenance": next_main,"Comments": comms}
    #     except:
    #         print('Could not add part')

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def save(self):

        with open('machines.json', 'w+', encoding='utf-8') as f:
            json.dump(self.machines, f, ensure_ascii=False, indent=4)

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]


# db = DataBase('jsonformatter.json')
# db.load()
# db.save()
# print(db.machines['Machine 1'])
# db.add_machine('Extruder')

