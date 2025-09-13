from fastapi import APIRouter
from app.controllers import employee_controller
from app.model.employee import Employee, UpdateEmployee

router = APIRouter(tags=["Employees"])

@router.get("/employees/avg-salary")
async def avg_salary():
    return await employee_controller.avg_salary_by_department()

@router.get("/employees/search")
async def search_employees(skill: str):
    return await employee_controller.search_by_skill(skill)

@router.post("/employees")
async def create_employee(employee: Employee):
    return await employee_controller.create_employee(employee)

@router.get("/employees/{employee_id}")
async def get_employee(employee_id: str):
    return await employee_controller.get_employee(employee_id)

@router.put("/employees/{employee_id}")
async def update_employee(employee_id: str, update_data: UpdateEmployee):
    return await employee_controller.update_employee(employee_id, update_data)

@router.delete("/employees/{employee_id}")
async def delete_employee(employee_id: str):
    return await employee_controller.delete_employee(employee_id)

@router.get("/employees")
async def list_by_department(department: str):
    return await employee_controller.list_by_department(department)