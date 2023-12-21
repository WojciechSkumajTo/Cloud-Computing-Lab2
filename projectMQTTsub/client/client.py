import httpx

api_url = "http://projectFastAPI:8000"


async def get_data(item_id):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{api_url}/get_data/{item_id}")
    return response.json()


async def add_data(item_id, data):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{api_url}/add_data/{item_id}?data={data}")
    return response.json()

