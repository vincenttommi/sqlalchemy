from  sqlalchemy import String,Integer,Column,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Review import  Review


engine = create_engine('sqlite://restaurant.db')


Base =  declarative_base()
session = sessionmaker(bind=engine)
session = session()




class  Restaurant(Base):
    __tablename__ ='restaurants'
    restaurant_id  = Column(Integer,primary_key = True)
    restaurant_name  = Column(String)


    all_reviews = []
    def __init__(self,restaurant_name):
        self.restaurant_name = self.restaurant_name

    def restaurant_name(self):
        return self.restaurant_name





     