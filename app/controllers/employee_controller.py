from app.db.db import get_db
from app.model.employee import Employee, UpdateEmployee
from app.utils.exceptions import ApiError
from app.utils.response import ApiResponse
from app.utils.helper import serialize_document

# Create Employee
async def create_employee(employee: Employee):
    db = get_db()
    emp_data = employee.model_dump()
    
    exists = await db.employees.find_one({
        "employee_id": employee.employee_id
    })
    
    if exists:
        raise ApiError(400, "Employee ID must be unique")
    
    # Normalizing
    if "department" in emp_data and emp_data["department"]:
        emp_data["department"] = emp_data["department"].lower()
        
    if "skills" in emp_data and emp_data["skills"]:
        emp_data["skills"] = [s.lower() for s in emp_data["skills"]]
    
    result = await db.employees.insert_one(emp_data)
    
    return ApiResponse.create(
        status_code=201, 
        data={"id": str(result.inserted_id)},
        message="Employee created"
    )
    
# Get Employee
async def get_employee(employee_id: str):
    db = get_db()
    employee = await db.employees.find_one({
        "employee_id": employee_id
    })
    
    if not employee:
        raise ApiError(status_code=404, message="Employee not found")
    return ApiResponse.create(
        status_code=200, 
        data=serialize_document(employee),
        message="Employee found"
    )

# Update Employee
async def update_employee(employee_id: str, update_data: UpdateEmployee):
    db = get_db()
    update = update_data.model_dump()
    
    exists = await db.employees.find_one({
        "employee_id": employee_id
    })
    
    if not exists:
        raise ApiError(400, "Employee not found")
    
    # Normalizing
    if "department" in update and update["department"]:
        update["department"] = update["department"].lower()

    if "skills" in update and update["skills"]:
        update["skills"] = [s.lower() for s in update["skills"]]
    
    result = await db.employees.update_one(
        {"employee_id": employee_id},
        {"$set": update}
    )
    if result.modified_count == 0:
        return ApiResponse.create(status_code=201, data={"updated_count": 0}, message="Employee already up-to-date")
    
    return ApiResponse.create(
        status_code=200, 
        data={
            "updated_count": result.modified_count
        }, 
        message="Employee updated successfully"
    )
    
# Delete Employee
async def delete_employee(employee_id: str):
    db = get_db()
    result = await db.employees.delete_one({
        "employee_id": employee_id
    })
    
    if result.deleted_count == 0:
        raise ApiError(status_code=404, message="Employee not found")
    
    return ApiResponse(
        status_code=200,
        data={
            "employee_id": employee_id
        },
        message="Employee deleted successfully"
    )
    
# List Employees by department
async def list_by_department(dept: str):
    db = get_db()
    employees = db.employees.find({
        "department": dept.lower()
    }).sort("joining_date", -1)
    data = [serialize_document(emp) async for emp in employees]
    return ApiResponse.create(
        status_code=200, 
        data=data,
        message=f"Employees in deparment {dept}"
    )

# Average salary by department
async def avg_salary_by_department():
    db = get_db()
    pipeline = [
        {"$group": {"_id": "$department", "avg_salary": {"$avg": "$salary"}}},
        {"$project": {"department": "$_id", "avg_salary": 1, "_id": 0}}
    ]
    
    result = await db.employees.aggregate(pipeline).to_list(length=None)
    if not result:
        raise ApiError(status_code=404, message="No employees found in any department")
    
    return ApiResponse.create(
        status_code=200, 
        data=result,
        message="Average salary by department"
    )

# Search by skills
async def search_by_skill(skill: str):
    db = get_db()
    employees = db.employees.find({"skills": skill.lower()})
    data = [serialize_document(emp) async for emp in employees]
     
    return ApiResponse.create(
        status_code=200, 
        data=data,
        message=f"Employees with skill {skill}" if data else f"No employees found with skill {skill}"
    )