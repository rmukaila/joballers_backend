from pydantic import BaseModel

class User(BaseModel):    
    full_name: str
    email: str

#Example usage
#data = {'full_name':'Rashid Mukaila', email:'example@gmail.com'}
# new_user = User(**data)
# inserted_user = self.user_col.insert_one(new_user)


class Job(BaseModel):
    title :str
