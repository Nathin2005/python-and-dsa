# DATA STRUCTURE 

# CRUD OPERATION

# stack OPERATION
# LIFO
# FIFO

# DATA STRUCTURE TYPES
    # LINEAR DATA STRUCTURE 
    # - THEY ARE IN SEQUENTIAL ORDER 
    # - THEY ARE NOT CONNECTED TO EACH OTHER
    # 1. List
    # 2. Tuple
    # 3. set
    
    # NON-LINEAR DATA STRUCTURE 
    # - THEY ARE NOT IN SEQUENTIAL ORDER 
    # - THERE IS A RELATIONSHIP BETWEEN THE ELEMENTS 
    # - THEY ARE CONNECTED TO EACH OTHER
    # 1. Array
    # 2. Linked List
    # 3. Tree
    # 4. Graph
    
    # HASH DATA STRUCTURE - KEY BASED DATA STRUCTURE
    # 1. Dictionary
    
    # BIG O NOTATION --> TIME COMPLEXITY AND SPACE COMPLEXITY
    # EXAMPLE:
    # 1. O(1) --> constant time complexity
    # 2. O(n) --> linear time complexity
    # 3. O(n^2) --> quadratic time complexity
    
    # WHICLE SPEEDOMETER
    # 1. O(1) --> constant time complexity
    # 2. O(n) --> linear time complexity
    # 3. O(n^2) --> quadratic time complexity
    
    # THE BIG O NOTATION IS USED TO DESCRIBE THE PERFORMANCE OR COMPLEXITY OF AN ALGORITHM. 
    # IT GIVES AN UPPER BOUND ON THE TIME OR SPACE REQUIRED BY AN ALGORITHM IN TERMS OF THE SIZE OF THE INPUT DATA. 
    # IT HELPS TO COMPARE THE EFFICIENCY OF DIFFERENT ALGORITHMS AND TO PREDICT HOW THEY WILL PERFORM AS THE INPUT SIZE GROWS.
    
    # 1.INSERTION
    # 2.DELETION
    # 3.SEARCHING
    # 4.TRAVERSAL
    
import queue

from matplotlib.pylab import empty



        
# 2. queue OPERATION
# ENQUEUE - adding an element to the rear of the queue
# DEQUEUE - removing an element from the front of the queue
# PEEK - getting the front element of the queue without removing it
# ISEMPTY - checking if the queue is empty
# size - getting the number of elements in the queue

# queue = [ 1,2,3,4,5]

# while True:
#     print("1.enqueue 2.dequeue 3.peek 4.display 5.exit")
#     choice=int(input("enter value"))
#     if choice == 1:
#         val=int(input("enter value"))
#         queue.append(val)
#     elif choice == 2:
#         if not queue:
#             print("queue underflow")    
#         else:
#             print("dequeued ",queue.pop(0))   
#     elif choice == 3:
#         if not queue:
#             print("queue is empty")    
#         else:
#             print("front",queue[0])
#     elif choice == 4:
#         print("queue is",queue)
#     elif choice == 5:
#         break
#     else:
#         print("invalid choice")
        
#  circular queue - reuses the empty space created by dequeuing elements
# ENQUEUE - adding an element to the rear of the queue
# DEQUEUE - removing an element from the front of the queue
# PEEK - getting the front element of the queue without removing it
# ISEMPTY - checking if the queue is empty
# size - getting the number of elements in the queue

# if front is free, rear can reuse it 

# n=3
# queue=[None]*n
# front=0
# rear=0

# insert
# queue[rear]=10
# rear=(rear+1)%n

# impotant condition 
# queue is full when (rear+1)%n == front
# queue is empty when rear == front

# circular movement
# rear=(rear+1)%n
# front=(front+1)%n

# PSEUDOCODE

# ENQUEUE

# IF QUEUE FULL PRINT--> QUEUE OVERFLOW
# if first element -->set  front = 0
# move rear circilarly

# dequeue

# IF QUEEE EMPTY PRINT --> QUEUE UNDERFLOW
# REMOVE ELEMENT FROM FRONT
# IF LAST ELEMENT REMOVED RESET FRONT AND REAR
# ELSE MOVE FRONT CIRCULARLY

# DISPLAY
# IF QUEUE IS EMPTY PRINT --> QUEUE IS EMPTY
# ELSE PRINT ELEMENTS FROM FRONT TO REAR CIRCULARLY

# | Type           | Insert      | Delete      | Special Feature       |
# | -------------- | ----------- | ----------- | --------------------- |
# | Simple Queue   | Rear        | Front       | FIFO                  |
# | Circular Queue | Rear        | Front       | Reuses space          |
# | Priority Queue | By priority | By priority | Important items first |
# | Deque          | Both ends   | Both ends   | Flexible              |
        


size = 5
queue = [None] * size
front = -1
rear = -1

def enqueue(value):
    global front, rear
    
    if (rear + 1) % size == front:
        print("Queue Full")
        return
    
    if front == -1:
        front = 0
    
    rear = (rear + 1) % size
    queue[rear] = value
    print(value, "inserted")

def dequeue():
    global front, rear
    
    if front == -1:
        print("Queue Empty")
        return
    
    removed = queue[front]
    
    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % size
    
    print(removed, "removed")

def display():
    if front == -1:
        print("Queue Empty")
        return
    
    i = front
    print("Queue elements:")
    
    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % size
    print()

while True:
    print("\n1.Enqueue")
    print("2.Dequeue")
    print("3.Display")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        enqueue(value)

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")
