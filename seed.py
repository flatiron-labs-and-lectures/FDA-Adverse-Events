import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base,Brands,Holidays,Adverse_Events,Manufacturers,Reactions
import models

engine = sqlalchemy.create_engine('sqlite:///adverse-events.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

### INSTANTIATING OUR HOLIDAYS
# advil = Brands(name='Advil')
# lala = Manufacturers(name='La La Pharma')


christmas = Holidays(name='Christmas',date='20171225')
new_years_eve = Holidays(name='New Years Eve',date='20171231')
valentines_day = Holidays(name='Valentines Day',date='20170214')
mardi_gras = Holidays(name='Mardi Gras',date='20170228')
st_patricks_day = Holidays(name='St. Patricks Day',date='20170317')
cannabis_day = Holidays(name='Cannabis Day',date='20170420')
cinco_de_mayo = Holidays(name='Cinco de Mayo',date='20170505')
independence_day = Holidays(name='Independence Day',date='20170704')
halloween = Holidays(name='Halloween',date='20171031')
thanksgiving = Holidays(name='Thanksgiving',date='20171123')




# dizziness = Reactions(name='dizziness')

session.add_all([christmas, new_years_eve, valentines_day, mardi_gras, st_patricks_day, cannabis_day, cinco_de_mayo, independence_day, halloween, thanksgiving])


# some_event = Adverse_Events(sex=1,weight=210,age=27)
# some_event.brands = advil
# some_event.manufacturers = lala
# some_event.holidays = christmas
# some_event.reactions = dizziness

# session.add_all([some_event])




session.commit()
