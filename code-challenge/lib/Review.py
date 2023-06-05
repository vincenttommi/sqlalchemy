from  sqlalchemy import String,Integer,Column,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Review import  Review


engine = create_engine('sqlite://restaurant.db')



Base =  declarative_base()
session = sessionmaker(bind=engine)
session = session()




class  Review(Base):

    __tablename__ = 'reviews'
    review_id = Column(Integer,primary_key = True)
    restaurant_name  = Column
    restaurant_customer = Column(String)
    customer_rating  = Column(String)


    def __init__(self,restaurant,restaurant_Customer,Customer_rating):
        self.restaurant = restaurant
        self.restaurant_Customer = restaurant_Customer
        self.Customer_rating = Customer_rating
        Review.all_reviews.append(self)  


    def Customer_rating(self):
        return self.Customer_rating
    

    

