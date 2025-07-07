import pytest

@pytest.mark.ui
def test_validate_checkout_information(checkout_information):
    checkout_information.navigate()

    #validation of checkout information
    checkout_information.click_continue_button()
    checkout_information.expect_error_message("Error: First Name is required")
    checkout_information.type_first_name("Dvora")
    checkout_information.type_last_name("Hirhsuat")
    checkout_information.click_continue_button()
    checkout_information.expect_error_message("Error: Postal Code is required")
    checkout_information.type_zip_code("1234")
    checkout_information.click_continue_button()