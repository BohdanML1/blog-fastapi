from database import Base, engine
import models

# Чисте створення таблиць
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

print("Tables created successfully")
