steks=[3,3,8,2,1,5]
print(steks)
steks.append("(")
steks.append(")")
print(steks)




#ievieto un izdzēš elementu
import queue
steks=queue.LifoQueue()
steks.put("pirmais")
steks.put("otrais")
print("izņemts",steks.get())
print("izņemts",steks.get())



steks=queue.LifoQueue()
steks.put("Pirmais")
steks.put("Otrais")
steks.put("Trešais")
print(steks.queue)
print(steks.qsize())