import json


class APIClient:
    def __init__(self, base_url, request_context):
        self.base_url = base_url
        self.request_context = request_context

    def post(self, endpoint, data=None, headers=None):
        headers = headers or {}
        headers["Content-Type"] = "application/json"

        return self.request_context.post(
            f"{self.base_url}{endpoint}",
            data=json.dumps(data) if data else None,
            headers=headers
        )

    def get(self, endpoint):
        return self.request_context.get(
            f"{self.base_url}{endpoint}"
        )