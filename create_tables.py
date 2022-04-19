from config.database import Base, engine

# Models
from app.reservations.models.reservations import Reservations

def main():
    print("Creating database...")

    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()