# Employee Management API (FastAPI + MongoDB)
 
It provides CRUD operations, department-based listing, average salary, and skill-based search for employees.

---

## 🚀 Tech Stack
- Python 3.12.7
- FastAPI
- MongoDB (Motor async driver)
- Pydantic for validation

---

## APIs Documentation
| 🧪 Postman Docs     | [View API Documentation](https://documenter.getpostman.com/view/39785896/2sB3HoqKkK) |
| or Swagger UI       | [Swagger APIs Docs](http://127.0.0.1:8000/docs) |

## Setup Instructions
1. Clone the repo:
   ```bash
   git clone <your-repo-url>
   cd project-root

2. Create a virtual environment
   ```bash
   python -m venv venv
   venv\scripts\activate

3. Install dependencies
   ```bash
   pip install -r requirements.txt

4. Copy `.env.sample` to `.env` and add your environment variable

5. Run the server
   ```bash
   uvicorn app.main:app --reload


## API Endpoints
- `POST` /employees → Create Employee
- `GET` /employees/{employee_id} → Get Employee by ID
- `PUT` /employees/{employee_id} → Update Employee
- `DELETE` /employees/{employee_id} → Delete Employee
- `GET` /employees?department=xyz → List employees by department
- `GET` /employees/avg-salary → Average salary by department
- `GET` /employees/search?skill=python → Search employees by skill


## ✅ Features
- Create, Read, Update, Delete employees
- Department-based listing
- Average salary calculation by department
- Skill-based search
- Async MongoDB operations for faster performance