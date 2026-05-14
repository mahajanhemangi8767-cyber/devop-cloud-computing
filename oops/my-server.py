class Server:

    def __init__(self,name,ip):
        self.name=name
        self.ip=ip
        self.status="offline"

    def start(self):
        self.status="Started"
        print(f"Server {self.name}-{self.ip} :: {self.status} ")


    def stop(self):
        self.status="Stopped"
        print(f"Server {self.name}-{self.ip} :: {self.status} ")


# creating objects from outside the class
s1= Server("Prod-Server", "192.168.1.10")
s1.start()
s1.stop

s2= Server("Dev-Server", "192.168.1.11")
s2.start()
s2.stop()






