from pydantic import BaseModel, EmailStr, Field

def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]), #_id es la forma en la que mongodb guarda el id
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }


def usersEntity(entity) -> list:  #entity es una lista que hay que recorrer 
    return [userEntity(item) for item in entity] #de la lista recibida de usuarios, me genera individualmente cada usuario 


def userAuth(BaseModel):
    username: str = Field(..., description="user username")
    Email: EmailStr = Field(..., description="user Email")
    password: str = Field(..., description="user password")
