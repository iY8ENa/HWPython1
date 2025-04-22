import pytest
from sqlalchemy.orm import sessionmaker
from models import Student, engine

# Используем ранее созданный двигатель
SessionLocal = sessionmaker(bind=engine)

# Фикстура для создания сессии
@pytest.fixture(scope="module")
def db_session():
    session = SessionLocal()
    yield session
    session.query(Student).delete()  # Чистим данные после тестов
    session.commit()

# Тест на создание студента
def test_create_student(db_session):
    new_student = Student(first_name='Иван', last_name='Иванов', email='ivan@example.com')
    db_session.add(new_student)
    db_session.commit()
    retrieved_student = db_session.query(Student).filter_by(email='ivan@example.com').first()
    assert retrieved_student is not None

# Тест на обновление студента
def test_update_student(db_session):
    existing_student = db_session.query(Student).first()
    if existing_student:
        existing_student.first_name = 'Алексей'
        db_session.commit()
        updated_student = db_session.query(Student).filter_by(id=existing_student.id).first()
        assert updated_student.first_name == 'Алексей'

# Тест на удаление студента
def test_delete_student(db_session):
    student_to_delete = db_session.query(Student).first()
    if student_to_delete:
        db_session.delete(student_to_delete)
        db_session.commit()
        deleted_student = db_session.query(Student).filter_by(id=student_to_delete.id).first()
        assert deleted_student is None