class FlowWrapper:

    def __init__(self, flow, request_validator, response_validator, logger=None):
        self.flow = flow
        self.request = request_validator
        self.response_validator = response_validator
        self.logger = logger

    # =========================================================
    # INTERNAL SAFETY
    # =========================================================

    def _get_response(self):
        response = getattr(self.flow, "response", None)
        if response is None:
            raise AssertionError("Response not available for this flow")
        return response

    def _get_request(self):
        request = getattr(self.flow, "request", None)
        if request is None:
            raise AssertionError("Request not available for this flow")
        return request

    # =========================================================
    # REQUEST ASSERTIONS
    # =========================================================

    def assert_request_headers(self, expected_headers):
        request = self._get_request()

        self.request._validate_headers(
            expected_headers,
            request.headers
        )
        return self

    def assert_request_json(self, expected_body):
        request = self._get_request()

        try:
            actual = request.json()
        except Exception as e:
            raise AssertionError(f"Request body is not valid JSON: {e}")

        self.request._validate_json_body(expected_body, actual)
        return self

    def assert_request_form(self, expected_body):
        request = self._get_request()

        self.request._validate_form_urlencoded_body(
            expected_body,
            request.text
        )
        return self

    # =========================================================
    # RESPONSE ASSERTIONS
    # =========================================================

    def assert_status(self, expected_status):
        response = self._get_response()

        actual = response.status_code
        if actual != expected_status:
            raise AssertionError(
                f"Expected status {expected_status}, got {actual}"
            )
        return self

    def assert_response_headers(self, expected_headers):
        response = self._get_response()

        self.response_validator._validate_headers(
            expected_headers,
            response.headers
        )
        return self

    def assert_json(self, expected_body):
        response = self._get_response()

        try:
            actual = response.json()
        except Exception as e:
            raise AssertionError(f"Response body is not valid JSON: {e}")

        self.response_validator._validate_json_body(expected_body, actual)
        return self

    def assert_form(self, expected_body):
        response = self._get_response()

        self.response_validator._validate_form_urlencoded_body(
            expected_body,
            response.text
        )
        return self