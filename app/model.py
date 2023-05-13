from pydantic import BaseModel, Field, EmailStr

# config = {
#   'user': 'root',
#   'password': "J]91kx6G&S:^]'Gu",
#   'host': '34.69.199.102',
#   'database': 'component',
#   'raise_on_warnings': True
# }

class PostSchema(BaseModel):
    id : int = Field(default=None)
    title : str = Field(default=None)
    content : str = Field(default=None)
    class Config:
        schema_extra = {
            "post_demo" : {
                "title" : "some title about animes",
                "content" : "some content about animes"
            }

        }


class UserSchema(BaseModel):
    fullname : str = Field(default = None)
    email : EmailStr = Field(default = None)
    password : str = Field(default = None)
    class Config:
        the_schema = {
            "user_demo": {
                "name":"deez",
                "email":"deez@nutz.com",
                "password":"123"

            }
        }



class UserLoginSchema(BaseModel):
    email : EmailStr = Field(default = None)
    password : str = Field(default = None)
    class Config:
        the_schema = {
            "user_demo": {
                "email":"deez@nutz.com",
                "password":"123"

            }

        }

class getComponent(BaseModel):
    id : int = Field(default=None)
    name : str = Field(default=None)
    desc : str = Field(default=None)
    example : str = Field(default=None)
    class Config:
        the_schema = {
            "getComp_demo": {
                "id":"0",
                "name":"cable",
                "desc":"some stuff",
                "example":"cable.com"
            }

        }


    