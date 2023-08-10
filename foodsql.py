from sqlalchemy import Column, ForeignKey, create_engine, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
 
class Food(Base):    #baza de date propiu zisă
    __tablename__ = "foods"

    foodname = Column("foodname", String, primary_key="True")
    kcal = Column("kcal", Integer)
    carbohydrates = Column("carbohydrates", Integer)
    proteins = Column("proteins", Integer)
    fats = Column("fats", Integer)

    def __init__(self, foodname, kcal, carbohydrates, proteins, fats): #Initializarea
        self.foodname = foodname
        self.kcal = kcal
        self.carbohydrates = carbohydrates
        self.proteins = proteins
        self.fats = fats
    
    def __ret__(self):
        return f"({self.foodname} {self.kcal} {self.carbohydrates} {self.proteins} {self.fats})"
    
engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

foods1 = Food("waffles",310,49,7,10)  #add
session.add(foods1)
session.commit()

#record_to_delete = session.query(Food).filter_by(foodname="Pizza").first()  #delete
#if record_to_delete:
    #session.delete(record_to_delete)
    #session.commit()
