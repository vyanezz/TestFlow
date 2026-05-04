from test_flow import TestFlow

def qa_form():
        if __name__ == '__main__':
                test = TestFlow(enable_logger=True, headless=True)

                test.navigate("https://httpbin.org/forms/post")

                test.wait_for_request("https://httpbin.org/forms/post", "GET")

                with test.expect_request(
                        endpoint="https://httpbin.org/post",
                        method="POST",
                        timeout=10,
                        headers={
                            "accept-language": "es-ES,es;q=0.9"
                        },
                        form_urlencoded_body={
                            "custname": "Jhon",
                            "custtel": "600123456",
                            "custemail": "Jhon@test.com",
                            "size": "medium",
                            "topping": ["bacon", "cheese", "mushroom"],
                            "delivery": "11:00",
                        }
                ) as flow:
                    test.send_keys("name", "custname", "Jhon")
                    test.send_keys("name", "custtel", "600123456")
                    test.send_keys("name", "custemail", "Jhon@test.com")

                    test.click("xpath", "//input[@name='size' and @value='medium']")
                    test.click("xpath", "//input[@value='bacon']")
                    test.click("xpath", "//input[@value='cheese']")
                    test.click("xpath", "//input[@value='mushroom']")

                    test.send_keys("name", "delivery", "11:00")

                    test.click("xpath", "//button[contains(text(),'Submit')]")

                flow.assert_status(200)
                flow.assert_json({"form": { "comments": "",  "custemail": "Jhon@test.com", "custname": "Jhon", "custtel": "600123456", "delivery": "11:00", "size": "medium", "topping": ["bacon", "cheese", "mushroom"]}})

                test.stop_test()
qa_form()