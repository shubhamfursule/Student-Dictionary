from copy import deepcopy
student_detail={}


N = int(input("Total no. of student: "))
if N>=0:
    while N:
        
        try:
            student_dict={}
            roll_no=int(input("please Enter student Roll_no: "))
            if roll_no not in student_detail and roll_no>=1:
                student_dict.update({'roll_no':roll_no})
                Name= input("Enter Student Name:")
                if not Name.isdigit():
                    student_dict.update({'Name':Name})
                    Phone_no= input("Enter student Phone_no: ")
                    if len(Phone_no)==10 and Phone_no.isdigit():
                        student_dict.update({'Phone_no':Phone_no})
                        total_marks=int(input("Enter marks of student:"))
                        if total_marks>=0:
                            N-=1
                            student_dict.update({'total_marks':total_marks})
                            print(student_dict,end='\n\n')
                            student_detail.update({roll_no: student_dict})                       
                            #print(student_detail)
                        else:
                            raise ValueError
                    else:
                        raise ValueError
                else:
                    raise ValueError
            else:
                raise ValueError
        except:
            print("Please input correct Information")
print("student Dictionary")
print("ROLL NO  STUDENT DETAIL")          
for x,y in sorted(student_detail.items()):
    print(x,y)

min_roll=min(list(student_detail.keys()))
a=deepcopy(student_detail.get(min_roll))
a.pop('total_marks')
print(f"Smallest Roll no of student {a}")
avg_mark=0
for mark in student_detail:
    avg_mark+=student_detail[mark]['total_marks']
print(f"Average marks of all students is : {avg_mark/len(student_detail)}")