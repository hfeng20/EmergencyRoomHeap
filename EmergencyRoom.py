import math


class EmergencyRoom:
    def __init__(self):
        self.heap = []

    def addPatient(self, patient):
        self.heap.append(patient)
        self.fixHeapUp()

    def fixHeapUp(self):
        index = len(self.heap) - 1
        val = self.heap[index].priority
        parentIndex = math.floor((index - 1) / 2)
        while index > 0 and self.heap[parentIndex].priority < val:
            self.swap(index, parentIndex)
            index = parentIndex
            parentIndex = math.floor((index - 1) / 2)

    def list(self):
        names = []
        for patient in self.heap:
            names.append(patient.name)
        return names

    def priorities(self):
        priorities = []
        for patient in self.heap:
            priorities.append(patient.priority)
        return priorities

    def seePatient(self):
      if(len(self.heap) == 0):
        print("No patients to see!")
        return
      self.swap(0, len(self.heap) - 1)
      self.heap.pop(len(self.heap) - 1)
      self.heapify()
    

    def swap(self,index, targetIndex):
      temp = self.heap[index]
      self.heap[index] = self.heap[targetIndex]
      self.heap[targetIndex] = temp
  
    def numChildren(self, index):
      if index * 2 + 1 >= len(self.heap):
        return 0
      elif index * 2 + 1 == len(self.heap) - 1:
        return 1
      else:
        return 2

    def heapify(self):
      index = 0
      while index < len(self.heap):
        numChildren = self.numChildren(index)
        if numChildren == 0:
          return
        if numChildren == 1:
          if self.heap[index * 2 + 1].priority >= self.heap[index].priority:
            self.swap(index, index * 2 + 1)
          return
        else:
          if self.heap[index * 2 + 1].priority < self.heap[index].priority and self.heap[index * 2 + 2].priority < self.heap[index].priority:
            return
          else:
            if self.heap[index * 2 + 1].priority > self.heap[index].priority and self.heap[index * 2 + 2].priority > self.heap[index].priority:
              if self.heap[index * 2 + 1].priority > self.heap[index * 2 + 2].priority:
                self.swap(index, index * 2 + 1)
                index = index * 2 + 1
              else:
                self.swap(index, index * 2 + 2)
                index = index * 2 + 2
            elif self.heap[index].priority < self.heap[index * 2 + 1].priority:
              self.swap(index, index * 2 + 1)
              index = index * 2 + 1
            else:
              self.swap(index, index * 2 + 2)
              index = index * 2 + 2
        
      



      

class Patient:
    def __init__(self, name, severity):
        # injuries = {"head": 5, "arm": 2, "leg": 2, "torso": 3, "other": 1}
        self.name = name
        #self.injury = injury
        self.priority = severity
        #self.priority = injuries[injury] * severity



# jeff = Patient("Jeff", "leg", 1)
# bob = Patient("Bob", "head", 2)
# john = Patient("John", "head", 3)
# ethan = Patient("Ethan", "torso", 2)
# jack = Patient("Jack", "leg", 4)
# sam = Patient("Sam", "head", 4)

# room = EmergencyRoom()
# room.addPatient(jeff)
# room.addPatient(bob)
# room.addPatient(john)
# room.addPatient(ethan)
# room.addPatient(jack)
# room.addPatient(sam)

# print(room.list())

# print(room.priorities())
# room.seePatient()
# print(room.list())
# print(room.priorities())
# room.seePatient()
# print(room.list())
# print(room.priorities())
# room.seePatient()
# print(room.list())
# print(room.priorities())

print("Actions:")
print("1: Add Patient")
print("2: See Patient")
print("3: Show Room")
print("4: Exit")
room = EmergencyRoom()
going = True
while(going):
  action = (input("Next Action: "))
  while not action.isnumeric():
    print("Invalid Action!")
    action = (input("Next Action: "))
  action = (int)(action)
  if action == 1:
    name = input("Name: ")
    #injury = input("Injury: ").lower()
    severity = (int)(input("Severity: "))
    patient = Patient(name,severity)
    room.addPatient(patient)
  elif action == 2:
    room.seePatient()
  elif action == 3:
    print(room.list())
  elif action == 4:
    going = False
  else:
    print("Invalid Action!")
