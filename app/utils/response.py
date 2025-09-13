from pydantic import BaseModel
from typing import Any, Optional

class ApiResponse(BaseModel):
    status_code: int
    data: Optional[Any] = None
    message: str = "Success"
    success: bool = True
    
    @classmethod
    def create(cls, status_code: int, data: Any = None, message: str = "Success"):
        return cls(
            status_code=status_code,
            data=data,
            message=message,
            success=status_code < 400
        )