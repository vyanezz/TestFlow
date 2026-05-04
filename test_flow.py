from modules.embedded_mitmproxy import EmbeddedMitmProxy
from modules.webdriver import WebDriver
from validators.api_validator import ApiValidator
from utils.logger import Logger
from modules.driver_config import DriverConfig

class TestFlow:

    def __init__(
        self,
        proxy_port=8080,
        enable_logger=False,
        headless=False,
        window_size="1920,1080",
        user_agent=None,
        extra_args=None
    ):
        self.logger = Logger(enabled=enable_logger)

        self.traffic = EmbeddedMitmProxy(port=proxy_port)
        self.traffic.start()

        driver_config = DriverConfig(
            headless=headless,
            window_size=window_size,
            user_agent=user_agent,
            extra_args=extra_args,
            proxy=f"http://localhost:{proxy_port}"
        )

        self.driver = WebDriver(
            logger=self.logger,
            config=driver_config
        )
        self.api = ApiValidator(
            interceptor=self.traffic.interceptor,
            logger=self.logger
        )

    def stop_test(self):
        if self.driver:
            self.driver.quit()
        if self.traffic:
            self.traffic.stop()

    def __getattr__(self, name):
        if hasattr(self.api, name):
            return getattr(self.api, name)
        if hasattr(self.traffic, name):
            return getattr(self.traffic, name)
        if hasattr(self.driver, name):
            return getattr(self.driver, name)
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")