from contextlib import contextmanager
from validators.request_validator import RequestValidator
from validators.response_validator import ResponseValidator
from validators.flow_wrapper import FlowWrapper

class ApiValidator:

    def __init__(self, interceptor, logger=None, default_timeout=10):
        self.interceptor = interceptor
        self.logger = logger
        self.default_timeout = default_timeout

        self.request = RequestValidator(
            interceptor=interceptor,
            logger=logger,
            default_timeout=default_timeout
        )

        self.response = ResponseValidator(logger)

    @contextmanager
    def expect_request(
        self,
        endpoint,
        method=None,
        headers=None,
        json_body=None,
        form_urlencoded_body=None,
        timeout=None
    ):
        timeout = timeout or self.default_timeout

        if self.logger:
            self.logger.log_wait(
                f"Expecting request → {endpoint}",
                action_type="EXPECT_REQUEST"
            )

        if hasattr(self.interceptor, "flows"):
            self.interceptor.flows.clear()

        wrapper = FlowWrapper(
            flow=None,
            request_validator=self.request,
            response_validator=self.response,
            logger=self.logger
        )

        try:
            yield wrapper

        finally:
            flow = self.request.wait_for_request(
                endpoint=endpoint,
                method=method,
                headers=headers,
                json_body=json_body,
                form_urlencoded_body=form_urlencoded_body,
                timeout=timeout
            )

            wrapper.flow = flow

    def wait_for_request(
            self,
            endpoint,
            method=None,
            headers=None,
            json_body=None,
            form_urlencoded_body=None,
            timeout=None
    ):
        timeout = timeout or self.default_timeout

        flow = self.request.wait_for_request(
            endpoint=endpoint,
            method=method,
            headers=headers,
            json_body=json_body,
            form_urlencoded_body=form_urlencoded_body,
            timeout=timeout
        )

        return FlowWrapper(
            flow=flow,
            request_validator=self.request,
            response_validator=self.response,
            logger=self.logger
        )