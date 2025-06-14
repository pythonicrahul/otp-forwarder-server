from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class OTPRequest(BaseModel):
    code: str
    ts: str
    tpa: str


@app.post("/otp")
def create_otp(body: OTPRequest):
    return {"message": "OTP created successfully!", "data": body}