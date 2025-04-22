from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))

# Определение строки подключения
DATABASE_URL = 'postgresql://postgres:123@localhost:5432/postgres'

# Создание двигателя базы данных
engine = create_engine(DATABASE_URL)

# Автоматически создаем таблицы в базе данных
Base.metadata.create_all(engine)