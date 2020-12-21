#name: Tarini Srikanth
#Instructor: Clark Turner
#Project 5- Masters and Transaction

class Entry:
    #takes in all the parameters and assigns it to the feilds in the class
    def __init__(self,accountNumber,name, balance, phoneNum, city):
        self.account_num = accountNumber
        self.name = name
        self.balance = balance
        self.phone = phoneNum
        self.city = city

    def __eq__(self,Entry2):
        #sees if two objects are entirely equal, meaning all their fields are equal
        ac = self.account_num==Entry2.account_num
        nm = self.name == Entry2.name
        bal = self.balance == Entry2.balance
        phone = self.phone == Entry2.phone
        ct = self.city == Entry2.city
        if ((ac and nm and bal and phone and ct)==True):
            return True
        else:
            return False

def read_file(filename):
    #cretes a final list
    finalListOfEntrys=[]
    f = open(filename)
    data = f.readline().split()
    #opens and splits the strings
    while(len(data)!=0):
        #this while loop goes until there isn't anything on the read line
        nameString = str(data[1]) + " " +str(data[2])
        balanceFloat = float(data[3])
        accountNum = int(data[0])
        #taking in all the values from the file
        newEntry = Entry(accountNum,nameString,balanceFloat,data[4],data[5])
        #creating a new object with these values
        finalListOfEntrys.append(newEntry)
        data = f.readline().split()
    return finalListOfEntrys

def read_transactionData(filename):
    finalListOfEntrys=[]
    f = open(filename)
    #reading and opening the transaction data
    data = f.readline().split()
    while(len(data)!=0):
         accountNum = int(data[0])
         balance = float(data[1])
         #getting the data
         newEntry = Entry(accountNum,"",balance,"","")
         #creating a new object
         finalListOfEntrys.append(newEntry)
         data = f.readline().split()
    return finalListOfEntrys


#takes the entry objects of the oldMaster
def sort_master(listOfEntryObjects,filename):
    f = open(filename,'w')
    for i in range(len(listOfEntryObjects)):
        min_index = i
        for j in range(i+1,len(listOfEntryObjects)):
            if listOfEntryObjects[min_index].account_num > listOfEntryObjects[j].account_num:
                min_index=j
                #using selection sort concept
        listOfEntryObjects[i],listOfEntryObjects[min_index]= listOfEntryObjects[min_index],listOfEntryObjects[i]
   
    for object1 in listOfEntryObjects:
        if object1.balance=="":
            f.write(toStringError(object1))
            #writing the new object into the file
        else:
            f.write(toString(object1)+"\n")
        

def sort(listOfObjects):
     for i in range(len(listOfObjects)):
        min_index=i
        for j in range(i+1,len(listOfObjects)): #goes through the remaining list
            if listOfObjects[min_index].account_num>listOfObjects[j].account_num:
                min_index=j
        listOfObjects[i],listOfObjects[min_index]= listOfObjects[min_index],listOfObjects[i] #swaps
     return listOfObjects



def toString(entryObject):
    accountNum = str(entryObject.account_num)
    name1 = str(entryObject.name)
    balance1 = str(entryObject.balance)
    phone1 = str(entryObject.phone)
    city1 = str(entryObject.city)
    #converting each field into a string
    finalString = accountNum +"  "+name1+"    "+balance1+"   "+phone1+"    "+city1
    return finalString

def update(transactionData, oldMasterData,filename):
    #updates transaction data
    f = open(filename,'w')
    listOfObjects =[]
    for entry in oldMasterData:
        for trans in transactionData:
            if entry.account_num == trans.account_num:
                entry.balance+=trans.balance
                #updating the data
        listOfObjects.append(entry)

    for trans in transactionData:
        index=0
        for entry in listOfObjects:
            if trans.account_num == entry.account_num:
                index=index+1
                #testing for the edge case
        if index==0:
            newEntry = Entry(trans.account_num,"","","","")
            listOfObjects.append(newEntry)
            
    # for object1 in listOfObjects:
    #     if object1.balance=="":
    #         f.write(toStringError(object1)+"\n")
    #     else:
    #         f.write(toString(object1)+"\n")
    value1 = sort(listOfObjects)
    sort_master(value1,filename)
    #sorting at the end

def toStringError(entryObject):
    string1 = "Unmatched transaction record for account number " + str(entryObject.account_num)+"\n"
    return string1
    #string for the edge case error

   



def main():
    read_file("test0.dat")
    #reading the file
    listOfEntrys = read_file("oldMaster.dat")
    fileNameMaster = "sorted_oldMaster.dat"
    #sorting the master
    sort_master(listOfEntrys,fileNameMaster)
    masterData = read_file("oldMaster.dat")
    #reading oldMaster
    transactionData = read_transactionData("transaction.dat")
    updatedMasterfile = "newMaster.dat"
    update(transactionData,masterData,updatedMasterfile)
    #updating old master using transaction data
    



if __name__ == '__main__':
    main()


        
