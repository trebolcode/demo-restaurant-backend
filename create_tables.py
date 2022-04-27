from config.database import Base, engine

# Models
from app.reservations.models.reservations import Reservations
from app.users.models.users import Users


def main():
    print("Creating database...")

    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
