# A complete working Python program to find length of a
# Linked List iteratively

# Node class


from asyncio.windows_events import NULL


class Node:
	# Function to initialise the node object
	def __init__(self,data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=NULL
        if self.head==None:
            self.head=new_node
        else:
            t=self.head
            while(t.next!=NULL):
                t=t.next
                continue
            t.next=new_node

    def append(self,new_data):
        new_node=Node(new_data)
        new_node.next=NULL
        t=self.head
        while(t.next!=NULL):
            t=t.next
            continue
        t.next=new_node
    
    def insetAthead(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def insertAtindex(self,new_data,i):
        new_node=Node(new_data)
        if i==0:
            LinkedList.insetAthead(self,new_data)
        else:
            count=0
            flag=0
            temp = self.head # Initialise temp
            while (temp):
                if count==i-1:
                    new_node.next=temp.next
                    temp.next=new_node
                    flag=1
                    break
                temp=temp.next
                count=count+1
            if(flag==0):
                print("Index Out of Bound")

    def delete(self,data):
        temp=self.head
        i=0
        while(i<LinkedList.getCount(self)-1):
            if temp.next.data==data:
                if temp.next.next==NULL:
                    temp.next=NULL
                    i=i+1
                else:
                    temp.next=temp.next.next
                    i=i+1
            temp=temp.next
            i=i+1

    def getCount(self):
        count=0
        temp = self.head # Initialise temp
        while (temp):
            temp=temp.next
            count=count+1
        return count

    def reverse(self):
        current=self.head
        prev=NULL
        while(current!=NULL):
            n=current.next
            current.next=prev
            prev=current
            current=n
        self.head=prev


    def print_list(self):
        temp = self.head # Initialise temp
        print("\n")
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next



# Code execution starts here
if __name__=='__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push("scscsc")
    llist.append(90)
    llist.insetAthead(98)
    llist.insertAtindex(23,1)
    #llist.print_list()
    #print ("Count of nodes is :",llist.getCount())
    llist.delete(1)
    llist.print_list()
    #print ("Count of nodes is :",llist.getCount())
    llist.reverse()
    llist.print_list()
