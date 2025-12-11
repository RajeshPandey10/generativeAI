from pydantic import BaseModel,EmailStr,Field
from typing import Optional
class Student (BaseModel):
    name:str='Rajesh'
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,default=5,description='A decimal value representing the cgpa of the student')#we send the description to better train the llm 



new_student = {'age':'22','email':'abc@gmail.com','cgpa':5} #type coercing--->as we define age as integer above and give the number in string.
#.pydantic is intelligent enough to understand the string is integer and do implicit type conversion..so we will not get the error

student = Student(**new_student)
student_dict =dict(student)

print(student_dict['age'])