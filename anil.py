# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/test")
# def anil():
#     return {"Hello" : "anil"}
#
# from fastapi import FastAPI,Path
#
# phone = FastAPI()
#
# @phone.get("/test")
# def phone():
#     return {"hello" :"anil"}
#

# employee = {
#     1:{
#         "name": "Anil",
#         "role": "LoverBoy"
#     }
# }

# from fastapi import FastAPI,Path
#
# phone = FastAPI()
# @phone.get("/test/employee_id")
# def test(employee_id:int = Path(description = "ID is required", gt = 0, le =3)):
#     if employee_id in employee:
#         return employee[employee_id]
#     return{"data":"not found"}

#get API
# from fastapi import FastAPI,Path
#
# app = FastAPI()
#
# employee = {
#     1:{
#         "name": "Anil",
#         "role": "LoverBoy"
#     }
# }
#
# @app.get("/query/{employee_id}")
# def get_by_query(employee_id:int,name:str):
#     for employee_id in employee:
#         if employee[employee_id]["name"] == name:
#             return employee[employee_id]
#     return {"Data":"not found"}
#
# from fastapi import FastAPI, HTTPException, Path
# from pydantic import BaseModel
#
# app = FastAPI()
#
#
# class Employee(BaseModel):
#     name: str
#     age: int
#     position: str
#
# employee = {
#     1:{
#         "name": "Anil",
#         "role": "LoverBoy"
#     }
# }
#
# @app.post("/post/{employe_id}")
# def create(employe_id:int, employe:Employee):
#     if employe_id in employee:
#         return {"Employee":"ID already exsists"}
#     employee[employe_id] = employe

