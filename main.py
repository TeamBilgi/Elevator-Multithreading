import random
import threading
import time

f=[0,0,0,0,0]

def girenSayisi():
    insan = random.randint(1, 10)
    return insan

def hedefKat():
    kat = random.randint(1, 4)
    return kat

def prints(cikiskati,insan):
    liste = list()
    liste.append([insan,cikiskati])
    print("cikis yapan insansayisi,kat :",liste)
    return liste

def hedefKatcikis(f):
    cikisKati = list()
    for a in range(len(f)):
        if(f[a]>0):
            cikisKati.append(a)
    kat = random.choice(cikisKati)
    return kat

def cikanSayisicikis(f):
    cikiskati = hedefKatcikis(f)
    if(f[cikiskati]>=5):
        insan = random.randint(1, 5)
    elif(f[cikiskati]<5):
        insan = random.randint(1,f[cikiskati])
    f[cikiskati] -= insan
    prints(cikiskati,insan)
    cikisYapan = [insan,0]
    return cikisYapan

def quekle(counter):
    while counter:
        kat = hedefKat()
        ins = girenSayisi()
        time.sleep(0.5)
        print("gireninsan : %s kat :%s time : %s" % (ins, kat, time.ctime(time.time())))
        queue.enque([ins, kat])
        counter -= 1

def qucikar(f):
        ins = list()
        ins = cikanSayisicikis(f)
        time.sleep(1)
        print("cikaninsan : %s time : %s" % (ins, time.ctime(time.time())))
        if(ins[1]==1):
            queue1.enque(ins)
        elif(ins[1]==2):
            queue2.enque(ins)
        elif(ins[1]==3):
            queue3.enque(ins)
        elif(ins[1] == 4):
            queue4.enque(ins)

#def kuyruk(queue1,queue2,queue3,queue4):



def asansorBinis(queue, asansio1):
    tmp = queue.deque()
    binecek = 0
    for i in range(0, tmp):
        print("evveti", i)
        asansio1.customer.append(queue.item[i])
        print("customa", asansio1.customer)
        binecek += asansio1.customer[i][0]
        print("aha:", binecek)

    if (binecek < 10):
        queue.item[tmp][0] -= (10 - binecek)
        asansio1.customer.append([(10 - binecek), queue.item[tmp][1]])
        print(asansio1.customer)

    for i in range(0, tmp):
        queue.item.pop(0)

def asansorInis(asansio1, f):
    print("merhaba")
    hedef(asansio1)
    grupsayisi = len(asansio1.customer)
    a = 0
    copyitem = asansio1.customer.copy()
    if (asansio1.floor == asansio1.destination):
        while (a != grupsayisi):
            if (asansio1.customer[a][1] == asansio1.floor):
                f[asansio1.floor] += asansio1.customer[a][0]
                print(f[asansio1.floor])
                copyitem.remove(asansio1.customer[a])
            a += 1
    asansio1.customer = copyitem.copy()
    print("customerlar",asansio1.customer)

def hedef(asansio1):

    if(bool(asansio1.customer)==True):
        temp = list()
        for a in range(len(asansio1.customer)):
            temp.append(asansio1.customer[a][1])
        print(min(temp))
        asansio1.destination = min(temp)
    elif(bool(asansio1.customer)==False):
        destinationLength = None
        if (bool(queue1) == True):
            destinationLength = abs(asansio1.floor-1)
            asansio1.destination = 1
        if(bool(queue2) == True and destinationLength > abs(asansio1.floor-2)):
            destinationLength = abs(asansio1.floor-2)
            asansio1.destination = 2
        if (bool(queue3) == True and destinationLength > abs(asansio1.floor - 3)):
            destinationLength = abs(asansio1.floor - 3)
            asansio1.destination = 3
        if (bool(queue4) == True and destinationLength > abs(asansio1.floor - 4)):
            destinationLength = abs(asansio1.floor - 4)
            asansio1.destination = 4

    if (asansio1.destination < asansio1.floor):
        asansio1.direction = "down"
    else:
        asansio1.direction = "up"
    while (asansio1.floor != asansio1.destination):
        time.sleep(0.2)
        if(asansio1.direction == "up"):
            asansio1.floor += 1
        elif(asansio1.direction == "down"):
            if(asansio1.customer[0][1]==0):
                if(bool(queue1) and asansio1.floor==1):
                    asansio1.destination
                    break
                if(bool(queue2) and asansio1.floor==2):
                    break
                if(bool(queue3) and asansio1.floor==3):
                    break
                if(bool(queue4) and asansio1.floor==4):
                    break
            asansio1.floor -= 1

        print("floor : %d time : %s" % (asansio1.floor, time.ctime(time.time())))

def countinside(asansio1):

    totalinside=0
    for i in range(len(asansio1.customer)):
        totalinside += asansio1.customer[i][0]

    return totalinside


def asansor(asansio1, queue, f):
    isEmpty = False
    asansorBinis(queue, asansio1)
    while(isEmpty==False):
        hedef(asansio1)
        asansorInis(asansio1, f)
        if not asansio1.customer:
            isEmpty = True

class Asansor(object):
    def __init__(self, name):
        self.name = name
        self.customer = []
        self.mode = "working"
        self.floor = 0
        self.destination = 0
        self.direction = "up"
        self.capacity = 10
        self.count_inside = 0
        self.inside = []
        self.active = "Active"

class Queue(object):

    def __init__(self):
        self.item = []

    def __repr__(self):
        return "{}".format(self.item)

    def __str__(self):
        return "{}".format(self.item)

    def enque(self, add):
        self.item.append(add)
        return True

    def size(self):
        return len(self.item)

    def isempty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def deque(self):
        binecek = 0
        i = 0
        temp = 0
        if self.size() == 0:
            return None
        else:
            for i in range(len(self.item)):
                if ((binecek + temp) > 10):
                    break
                binecek += self.item[i][0]
                i += 1
                temp = self.item[i][0]

            return i


queue = Queue()
queue1 = Queue()
queue2 = Queue()
queue3 = Queue()
queue4 = Queue()
asansio1 = Asansor("birinci asansör")
counter = 5

try:
    threadgiris = threading.Thread(target=quekle, args=(counter,))
except:
    print("Error: unable to start thread")

try:
    threadcikis = threading.Thread(target=qucikar, args=(f,))
except:
    print("Error: unable to start thread")

try:
    threadAsansor = threading.Thread(target=asansor, args=(asansio1, queue, f,))
except:
    print("Error: unable to start thread")

threadgiris.start()
threadgiris.join()
print("somecode")
threadAsansor.start()
threadAsansor.join()
threadcikis.start()
threadcikis.join()
