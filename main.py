import secrets
import time

from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security import APIKeyHeader

from utils.helper import BaseData, execute_js_code

description = """
OpenAI Automation Tool
"""

# Create a FastAPI application instance
app = FastAPI(
    title="OpenAIAT",
    description=description,
    summary="OpenAI Automation Tool",
    version="0.0.1",
    # terms_of_service="http://example.com/terms/",
    contact={
        "name": "Hiroyuki Kumazawa",
        # "url": "http://x-force.example.com/contact/",
        "email": "hiroyukikumazawa.jp@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


# Define a function to get the API key from the API Key header
def get_api_key(api_key_header: str = Security(APIKeyHeader(name="apikey"))):
    """
    Retrieve the API key from the API Key header in the request.

    Args:
        api_key_header (str): The API Key header name.

    Returns:
        str: The API key extracted from the header.
    """
    return api_key_header


# Define a function to generate a new API key
def generate_api_key():
    """
    Generate a new random API key.

    Returns:
        str: A new API key as a hexadecimal string.
    """
    new_api_key = secrets.token_hex(32)
    return new_api_key


# Define a dependency to validate the API key
async def validate_api_key(api_key: str = Depends(get_api_key)):
    """
    Validate the API key provided in the request.

    Args:
        api_key (str): The API key extracted from the request.

    Raises:
        HTTPException: If the API key is invalid, raise a 403 Forbidden error.

    Returns:
        None: If the API key is valid, no error is raised.
    """
    if api_key != BaseData.valid_api_key:
        raise HTTPException(status_code=403, detail="Invalid API key")


# Create an endpoint to republish a new API key
@app.post(
    "/republish-api-key/", response_model=dict, dependencies=[Depends(validate_api_key)]
)
async def republish_api_key():
    """
    Republish a new API key.

    This endpoint generates a new random API key and updates the valid API key.

    Returns:
        dict: A dictionary containing a success message and the new API key.
    """
    BaseData.valid_api_key = generate_api_key()
    return {
        "message": "New API key generated successfully",
        "api_key": BaseData.valid_api_key,
    }


# Create an endpoint to validate a position using a PositionModel
@app.post("/gpt35/", dependencies=[Depends(validate_api_key)])
async def request_gpt35(req_content: str):
    """
    Validate a position using the PositionModel.

    Args:
        item (PositionModel): The position data to validate.

    Returns:
        str: A string containing the validated position information.
    """
    BaseData.last_called_time = time.time()
    tab = BaseData.browser.list_tab()[-1]
    print(BaseData.browser.list_tab())
    tab.start()
    execute_js_code(tab, "console.log('first integratasdfe')")
    tab.stop()
    return BaseData.last_called_time


# Run the FastAPI application using uvicorn
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=7463, reload=True)
