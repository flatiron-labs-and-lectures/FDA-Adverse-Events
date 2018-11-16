from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, ForeignKey, create_engine
from sqlalchemy.orm import relationship
import sqlalchemy
Base = declarative_base()





class Adverse_Events(Base): #association table
    __tablename__ = 'events'
    id = Column(Integer, primary_key = True)
    sex = Column(Integer) #should we do int or text here?
    age = Column(Integer)

    # manufacturers = relationship('Manufacturers', back_populates='events')
    # manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'))

    brands = relationship('Brands', secondary = 'brands_events', back_populates='events')


    reactions = relationship('Reactions', secondary = 'reactions_events', back_populates='events')


    holidays = relationship('Holidays', back_populates='events',uselist=False)
    holiday_id = Column(Integer, ForeignKey('holidays.id'))


class Brands(Base): # many brand-drugs are associated with many manufacturers through adverse events
    __tablename__ = 'brands'
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    events = relationship('Adverse_Events', secondary = 'brands_events',back_populates='brands') #many:many
    # manufacturers = relationship('Manufacturers', secondary='events', back_populates='brands')

     # many:many through association table

class Brands_Events(Base):
    __tablename__ = 'brands_events'
    brand_id = Column(Integer, ForeignKey('brands.id'), primary_key = True)
    event_id = Column(Integer, ForeignKey('events.id'), primary_key = True)



class Reactions(Base): #many reactions from 1 or more drugs through an adverse event
    __tablename__ = 'reactions'
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    events = relationship('Adverse_Events', secondary='reactions_events', back_populates='reactions')


class Reactions_Events(Base):
    __tablename__ = 'reactions_events'
    reactions_id = Column(Integer, ForeignKey('reactions.id'), primary_key = True)
    event_id = Column(Integer, ForeignKey('events.id'), primary_key = True)



class Holidays(Base): # one holiday to many adverse events
    __tablename__ = 'holidays'
    id = Column(Integer, primary_key = True)
    name = Column(Text)
    date = Column(Text) #text? YYYY-MM-DD?
    events = relationship('Adverse_Events', back_populates='holidays')

engine = sqlalchemy.create_engine('sqlite:///adverse-events.db', echo=True)
Base.metadata.create_all(engine)
