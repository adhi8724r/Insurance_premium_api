from pydantic import BaseModel,Field,computed_field
from typing import Literal, Annotated


class UserInput(BaseModel):
    age: Annotated[int,Field(..., ge=18,le=64,description='Age of user')]
    sex: Annotated[Literal['male','female'],Field(..., description='Gender of user')]
    bmi: Annotated[float,Field(...,description='bmi of user')]
    smoker:	Annotated[Literal['no','yes'],Field(..., description='is user smoker?')]
    region:	Annotated[Literal['northeast','southeast','northwest','southwest'],Field(..., description='Region user belong to')]
    children: Annotated[int,Field(...,ge=0,description='No of children')]