from pydantic import BaseModel

class CustomerInput(BaseModel):
    Tenure: int
    MonthlyCharges: float
    Contract: str
    TotalCharges : float
    PaymentMethod: str
