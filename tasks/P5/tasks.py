# favourite_fruits=["apple","mango","orange"]
# print(f"my favourite fruits:" )
# for i, fruits in enumerate(favourite_fruits,start=1):
#     print(f"\t{i}\t{fruits}")
taskmanager=[]
print("taskmanager:")
while True:
    print("\n\t1\t add task")
    print("\t2\t remove task")
    print("\t3\t show task")
    print("\t4\t completed task")
    print("\t5\t show completed task")
    print("\t6\t show task")

choice=input("enter choice:")
if choice==1:
    item=input("enter the item:")
    taskmanager.append(item)
    print("f '{item}' added to task manager")
else if choice==2