#crate node 
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
#crate linklist
class linknode:
    def __init__(self):
        self.head=None

    def inserthead(self,node):
        t=self.head
        self.head=node
        node.next=t
        del t
    #adding node
    def insertmid(self,x,y,midnode):
        
        x.next=midnode
        midnode.next=y

    def insertend(self,nextnode):
        if self.head is None:
            self.head=nextnode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                else:
                    lastnode=lastnode.next
            finalnode=lastnode
            lastnode.next=nextnode
    def print(self):
       currentnode=self.head
       while True:
           if currentnode is None:
               break
           
           print(currentnode.data)
           currentnode=currentnode.next
    def point(self,postition):
        currentnode=self.head
        s=0
        while True:
            if s==position:
               return(currentnode)
            s+=1
    def length(self):
        currentnode=self.head
        count=0
        while currentnode.next is not  None :
            count+=1

        return(count)


def merge(list1,list2):
    list3=linknode()
    p1=0
    p2=0
    while True:
        if list1.point(p1)>list2.point(p2):
           list3.insertend(list1.point(p2))
           if p2==list2.length():
               for i in range(p1,list1.length()+1):
                   list3.insertend(list1.point(i))
                   break
        elif list1.point(p1)<list.point(p2):
            list3.insertend(list1.point(p1))
            if p1==list1.length():
                for i in range(p2,list2.length()+1):
                        list3.insertend(list2.point(i))
                        break



       
node1=node('ram')
l=linknode()
l.insertend(node1)
node2=node('sham')
l.insertend(node2)

node0=node("love")
l.inserthead(node0)
node3=node("sita")
l.insertmid(node1,node2,node3)
print(l.length())
