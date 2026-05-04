from test_flow import TestFlow

def qa_form():
        if __name__ == '__main__':
                test = TestFlow(enable_logger=True, window_size="600,900")

                test.navigate("https://ultimateqa.com/filling-out-forms/")

                flow = test.wait_for_request("https://ultimateqa.com/filling-out-forms/", "GET")
                flow.assert_status(200)

                test.send_keys("id", "et_pb_contact_name_0", "Test Users")
                test.send_keys("id", "et_pb_contact_message_0", "Test message")
                test.click("name", "et_builder_submit_button")

                test.wait_for_request(endpoint="https://ultimateqa.com/filling-out-forms/",
                                          method="POST",
                                          timeout=10,
                                          headers={"accept-language": "es-ES,es;q=0.9"},
                                          form_urlencoded_body={
                                              "et_pb_contact_name_0": "Test Users",
                                              "et_pb_contact_message_0": "Test message",
                                              "et_pb_contactform_submit_0": "et_contact_proccess",
                                              "_wp_http_referer": "/filling-out-forms/"
                                          }
                                      )

                test.stop_test()
qa_form()