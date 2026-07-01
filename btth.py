from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

courses = [
    {
        "id": 1,
        "name": "Python Basic",
        "category": "backend",
        "price": 3000000,
        "mode": "online",
    },
    {
        "id": 2,
        "name": "Java Web",
        "category": "backend",
        "price": 5000000,
        "mode": "offline",
    },
    {
        "id": 3,
        "name": "Web Frontend",
        "category": "frontend",
        "price": 4000000,
        "mode": "online",
    },
]
app = FastAPI()


@app.get("/courses")
def get_all_courses():
    return {"message": "Lấy danh sách khóa học thành công", "data": courses}


@app.get("/courses/search")
def filter_course(mode: str = None, category: str = None):
    result = courses
    if mode:
        temp = [course for course in result if course["mode"] == mode]
        result = temp
    if category:
        temp = [course for course in result if course["category"] == category]
        result = temp
    return result


@app.get("/courses/{course_id}")
def get_course_detail(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return {"Message": "Chi tiết khóa học", "data": course}

    raise HTTPException(status_code=404, detail="Không tìm thấy khóa học")
