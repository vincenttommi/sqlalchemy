from  sqlalchemy import String,Integer,Column,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker
from Review import Review



engine = create_engine('sqlite://customer.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()







class Customer(Base):

    __tablename__ = 'customers'

    customer_id  = Column(Integer,primary_key=True)
    first_name = Column(String)
    last_name = Column(String)


    all_customers = []



    def __init__(self,firstname,lastname):
        self.firstname
        self.lastname
        Customer.all_customers.append(self)
    def firstname(self):
        return self.firstname
    
    def lastname(self):
        return self.lastname
    
    def  full_name(self):
        return f"{self.firstname}{self.lastname}"

    def  all(self):
     return Customer.all()
    
    def restaurants(self):
        engine = create_engine('sqlite://review.db') 
        Session = sessionmaker(bind=engine)
        session = Session()
        the_reviews = session.query(Review).all()
        restaurants_reviewed = []
        if that_review.restaurant_customer ==  self.first_name:
            restaurants_reviewed.append(that_review.restaurant)

        else:
            return 'restaurant not found'
        return(set(restaurants_reviewed))
    


add_review(self,restaurant_,rating):
engine = create_engine('sqlite://review.db')
Session = sessionmaker(bind=engine)
session = Session()


new = Review(restaurant_name =restaurant_, customer_rating=rating, restaurant_customer= self.first_name)
session.add(new)
session.commit()
session.close()








    