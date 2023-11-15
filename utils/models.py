from pydantic import BaseModel


class PositionModel(BaseModel):
    altitude: float  # Altitude in meters
    longitude: float  # Longitude coordinate
    latitude: float  # Latitude coordinate


class GptRequestModel(BaseModel):
    max_timeout: float = 20
    request_text: str


class GptResultModel(BaseModel):
    result_text: str
