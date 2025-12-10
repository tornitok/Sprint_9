import allure


@allure.feature("Регистрация")
@allure.story("Создание аккаунта")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_account(registration_page, new_user_data, upload_file_path):
    with allure.step("Открыть форму регистрации"):
        registration_page.open_registration_form()

    with allure.step("Заполнить форму регистрации"):
        registration_page.fill_registration_form(
            username=new_user_data["username"],
            email=new_user_data["email"],
            password=new_user_data["password"],
        )

    with allure.step("Отправить форму регистрации"):
        registration_page.submit()

    with allure.step("Проверить, что открылась страница авторизации"):
        assert registration_page.is_login_page_displayed(), "Форма авторизации не отображается после регистрации"

