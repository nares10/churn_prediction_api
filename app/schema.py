from pydantic import BaseModel

class CustomerInput(BaseModel):
    tenure: int
    MonthlyCharges: float
    Contract: str
    InternetService: str
    PaymentMethod: str
