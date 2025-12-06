from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

#http://localhost:8000/users > POST -> create user
@app.post("/users")
def create_user():
    return {"message": "User created"}

#http://localhost:8000/users > GET -> get all users
@app.get("/users")
def get_users():
    return []

#http://localhost:8000/users > GET -> get a single user
@app.get("/users/{user_id}")
def get_user(user_id):
    return{}

#http://localhost:8000/users > PATCH -> pdate a single user
@app.patch("/users/{user_id}")
def patch_user(user_id):
    return{}

#http://localhost:8000/users > DELETE -> delete a single user
@app.delete("/users/{user_id}")
def delete_user(user_id):
    return{}

