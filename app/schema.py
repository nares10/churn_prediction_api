from pydantic import BaseModel

class CustomerInput(BaseModel):
    Tenure: int
    MonthlyCharges: float
    Contract: str
<<<<<<< HEAD
    TotalCharges : float
=======
    TotalCharges: float
>>>>>>> 7747779 (Fixed mistake)
    PaymentMethod: str
