from pydantic import BaseModel


class PositionModel(BaseModel):
    altitude: float  # Altitude in meters
    longitude: float  # Longitude coordinate
    latitude: float  # Latitude coordinate
