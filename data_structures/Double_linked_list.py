class Node:
    def __init__(self,val,prev,next):
        self.val = val
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def show(self,mode='front'):  # It is kept default as front
        if self.head==None:
            print('Double Linked List is empty')
            return
        else:
            if mode.lower() == 'front':
                itr=self.head
                while itr:
                    print(itr.val," --> ",end="")
                    itr=itr.next 
                print("None")

            elif mode.lower() == 'back':
                itr=self.tail
                s=''
                while itr:
                    s= " <-- " + itr.val+s
                    itr=itr.prev 
                s='None '+s
                print(s)
    
    def getlength(self):
        itr = self.head
        c=0
        while itr:
            c+=1
            itr=itr.next
        return c
    
    def insert_at_beginning(self,val):
        node=Node(val,None,self.head)
        self.head=node
        self.tail=node 
    
    def insert_at_end(self,val):
        if self.head == None:
            node = Node(val,None,None)
            self.head = node
            self.tail = node 
            return
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.next=Node(val,itr,None)
            self.tail = itr.next
        
    def insert_values(self,v):
        for i in v:
            self.insert_at_end(i)

    def insert_at_pos(self,pos,val):
        if pos < 0 or pos >= self.getlength():
            raise Exception("Invalid Input")

        if pos == 0:
            self.insert_at_beginning(val)
        elif pos == self.getlength()-1:
            self.insert_at_end(val)

        else:
            itr = self.head
            c=0
            while itr:
                if c==pos-1:
                    node=Node(val,itr,itr.next)
                    itr.next=node
                    break
                c+=1
                itr=itr.next
    
    def remove_at_end(self):
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.prev.next=None
        self.tail = itr.prev
        itr=None 

    def remove_at_beginning(self):
        if self.getlength() == 1:
            self.head = self.tail = None 

        self.head.next.prev=None
        self.head=self.head.next

    def remove_at_pos(self,pos):
        if pos < 0 or pos >= self.getlength():
            raise Exception("Invalid Input")
        if pos == 0:
            self.remove_at_beginning()
        elif pos == self.getlength() -1 :
            self.remove_at_end()
            
        else:
            p=0
            itr = self.head
            while itr:
                if p == pos:
                    itr.prev.next = itr.next
                    itr.next.prev = itr.prev
                    break
                p += 1
                itr = itr.next

    def insert_after_value(self,val_before,val):
        if self.head is None:
            return

        itr = self.head
        p=0
        while itr:
            if itr.val == val_before:
                self.insert_at_pos(p+1,val)
                break
            p += 1
            itr = itr.next
        else:
            print("Data is not present in linked list:")

    def remove_by_val(self,val):
        if self.head is None:
            return
        if self.head.val == val:
            self.head.prev.next=None
            self.head=self.head.next
            return
        itr=self.head
        p=0
        while itr:
            if itr.val==val:
                self.remove_at_pos(p)
                break
            p += 1
            itr = itr.next
        else:
            print("Data is not present in linked list")

if __name__ == '__main__':
    dl = DoubleLinkedList()
    dl.insert_values(["A","B","C","D","E","F"])
    dl.show('front')
    dl.show('back')
    dl.insert_at_beginning("R")
    dl.insert_at_end("Z")
    dl.insert_at_pos(2,"T")
    dl.show()
    dl.remove_at_end()
    dl.remove_at_beginning()
    dl.remove_at_pos(2)
    dl.show()
    dl.insert_after_value("A","B")
    dl.show()
    dl.remove_by_val("F")
    dl.show()
