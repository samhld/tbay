from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Table, Integer, String, DateTime, Float, Date, ForeignKey

engine = create_engine('postgresql://ubuntu:Lambert12!@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# item_user_table = Table('item_user_association', Base.metadata,
#     Column('itemID', Integer, ForeignKey('item.id')), 
#     Column('userID', Integer, ForeignKey('user.id')),
#     Column('bidID', Integer, ForeignKey('bid.id')),
#     )
    


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # description = Column(String)
    # start_time = Column(DateTime, default=datetime.utcnow)
    
    auctionerID = Column(Integer, ForeignKey('user.id'), nullable=False)
    bidderID = Column(Integer, ForeignKey('user.id'), nullable=False)
    

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    auctions = relationship("Item", backref="auctioner")
    bids = relationship("Bid", backref="bidder")
    
class Bid(Base):
    __tablename__ = "bids"
    
    id = Column(Integer, primary_key=True)
    pointPrice = Column(Float, nullable=False)
    
    bidderID = Column(Integer, ForeignKey('item.id'), nullable=False)
    
    
Base.metadata.create_all(engine)

ben = User(name="ben", password="test", items=['baseball'])
sam = User(name="sam", password="demo", )
tom = User(name="tom", password="1234")

sam.bid.pointPrice = 12


baseball = Item(name="baseball", bidderId=([sam.id,tom.id]))



