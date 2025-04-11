import requests
import pytest
import random
import string


# Функция для генерации случайного названия проекта
def generate_random_project_name(length=10):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))


# Ваши учетные данные
LOGIN = "815601@gmail.com"
PASSWORD = "Grn-ctB-3V6-7wA"
COMPANY_ID = "15009487-79c1-49e0-bc64-b80e4ba1da21"

# Базовая информация для запроса
BASE_URL = "https://yougile.com"
AUTH_KEYS_ENDPOINT = "/api-v2/auth/keys"
PROJECTS_ENDPOINT = "/api-v2/projects"


def get_auth_key(company_id):
    """
    Функция для получения ключа авторизации.
    """
    payload = {
        "login": LOGIN,
        "password": PASSWORD,
        "companyId": company_id
    }
    response = requests.post(BASE_URL + AUTH_KEYS_ENDPOINT, json=payload)
    if response.status_code == 201:
        return response.json()["key"]
    else:
        raise ValueError(f"Не удалось получить ключ авторизации: {response.text}")


def create_project(auth_key, project_title):
    """
    Функция для создания нового проекта.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_key}"
    }
    payload = {
        "title": project_title
    }
    response = requests.post(BASE_URL + PROJECTS_ENDPOINT, json=payload, headers=headers)
    return response


def update_project(auth_key, project_id, user_data):
    """
    Функция для обновления проекта с добавлением пользователя.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_key}"
    }
    payload = {
        "users": user_data
    }
    response = requests.put(BASE_URL + PROJECTS_ENDPOINT + "/" + project_id, json=payload, headers=headers)
    return response


def get_project_by_id(auth_key, project_id):
    """
    Функция для получения проекта по его идентификатору.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_key}"
    }
    response = requests.get(BASE_URL + PROJECTS_ENDPOINT + "/" + project_id, headers=headers)
    return response


# Фикстуры для pytest

@pytest.fixture(scope="session")
def auth_key():
    """
    Фикстура для получения ключа авторизации.
    """
    payload = {
        "login": LOGIN,
        "password": PASSWORD,
        "companyId": COMPANY_ID
    }
    response = requests.post(BASE_URL + AUTH_KEYS_ENDPOINT, json=payload)
    if response.status_code == 201:
        return response.json()["key"]
    else:
        raise ValueError(f"Не удалось получить ключ авторизации: {response.text}")


@pytest.fixture(scope="session")
def auth_headers(auth_key):
    """
    Фикстура для получения заголовков авторизации.
    """
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_key}"
    }


@pytest.fixture(scope="session")
def existing_project_id(auth_headers):
    """
    Фикстура для создания существующего проекта.
    """
    project_title = generate_random_project_name()
    response = requests.post(BASE_URL + PROJECTS_ENDPOINT, json={"title": project_title}, headers=auth_headers)
    if response.status_code == 201:
        return response.json()["id"]
    else:
        raise ValueError(f"Не удалось создать проект: {response.text}")


@pytest.fixture(scope="session")
def nonexistent_project_id():
    """
    Фикстура для создания несуществующего проекта.
    """
    return "nonexistent-project-id"


# Класс для тестов

class TestProjectsAPI:
    @pytest.mark.positive
    def test_create_project(self, auth_headers):
        """
        Позитивный тест на создание проекта.
        """
        project_title = generate_random_project_name()
        response = requests.post(BASE_URL + PROJECTS_ENDPOINT, json={"title": project_title}, headers=auth_headers)
        assert response.status_code == 201, f"Ошибка при создании проекта: {response.text}"
        project_data = response.json()
        print(f"Ответ сервера: {project_data}")  # Отладка: выводим ответ сервера
        assert 'id' in project_data, f"Поле 'id' отсутствует в ответе сервера: {project_data}"  # Проверяем наличие поля 'id'

    @pytest.mark.negative
    def test_create_project_invalid_title(self, auth_headers):
        """
        Негативный тест на создание проекта с недопустимым названием.
        """
        project_title = ""  # Недопустимое название проекта
        response = requests.post(BASE_URL + PROJECTS_ENDPOINT, json={"title": project_title}, headers=auth_headers)
        assert response.status_code != 201, f"Ожидался отказ в создании проекта, но проект был создан"

    @pytest.mark.positive
    def test_get_project_by_id(self, auth_headers, existing_project_id):
        """
        Позитивный тест на получение проекта по идентификатору.
        """
        response = requests.get(BASE_URL + PROJECTS_ENDPOINT + "/" + existing_project_id, headers=auth_headers)
        assert response.status_code == 200, f"Ошибка при получении проекта: {response.text}"
        project_data = response.json()
        print(f"Ответ сервера: {project_data}")  # Отладка: выводим ответ сервера
        assert 'id' in project_data, f"Поле 'id' отсутствует в ответе сервера: {project_data}"  # Проверяем наличие поля 'id'
        assert project_data['id'] == existing_project_id, f"Идентификатор проекта не совпадает"

    @pytest.mark.negative
    def test_get_nonexistent_project(self, auth_headers, nonexistent_project_id):
        """
        Негативный тест на получение несуществующего проекта.
        """
        response = requests.get(BASE_URL + PROJECTS_ENDPOINT + "/" + nonexistent_project_id, headers=auth_headers)
        assert response.status_code == 404, f"Ожидался 404 статус, но проект был найден"

    @pytest.mark.positive
    def test_update_project(self, auth_headers, existing_project_id):
        """
        Позитивный тест на обновление проекта.
        """
        new_title = generate_random_project_name()
        response = requests.put(BASE_URL + PROJECTS_ENDPOINT + "/" + existing_project_id, json={"title": new_title},
                                headers=auth_headers)
        assert response.status_code == 200, f"Ошибка при обновлении проекта: {response.text}"
        project_data = response.json()
        print(f"Ответ сервера: {project_data}")  # Отладка: выводим ответ сервера
        assert 'id' in project_data, f"Поле 'id' отсутствует в ответе сервера: {project_data}"  # Проверяем наличие поля 'id'

    @pytest.mark.negative
    def test_update_project_invalid_title(self, auth_headers, existing_project_id):
        """
        Негативный тест на обновление проекта с недопустимым названием.
        """
        new_title = ""  # Недопустимое название проекта
        response = requests.put(BASE_URL + PROJECTS_ENDPOINT + "/" + existing_project_id, json={"title": new_title},
                                headers=auth_headers)
        assert response.status_code != 200, f"Ожидался отказ в обновлении проекта, но проект был обновлен"

    @pytest.mark.negative
    def test_update_nonexistent_project(self, auth_headers, nonexistent_project_id):
        """
        Негативный тест на обновление несуществующего проекта.
        """
        new_title = generate_random_project_name()
        response = requests.put(BASE_URL + PROJECTS_ENDPOINT + "/" + nonexistent_project_id, json={"title": new_title},
                                headers=auth_headers)
        assert response.status_code == 404, f"Ожидался 404 статус, но проект был обновлен"
