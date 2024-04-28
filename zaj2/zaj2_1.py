from sqlalchemy import create_engine, Column, Integer, String, text, inspect
from sqlalchemy.orm import declarative_base, Session


engine = create_engine('sqlite:///census.sqlite', echo=False, future=True)

inspector = inspect(engine)
table_names = inspector.get_table_names()
columns_census = inspector.get_columns(table_names[0])
columns_states = inspector.get_columns(table_names[1])

with Session(engine) as session:
    states = session.execute(text('SELECT DISTINCT state FROM census')).all()
    print(states)

with Session(engine) as session:
    states = ['Alaska', 'New York']
    years = [2000, 2008]
    for state in states:
        for year in years:
            population_sum = session.execute(text(f'SELECT sum(pop{year}) FROM census where state="{state}"')).all()
            print(f'Population in state {state} in year {year} = {population_sum[0][0]}')

with Session(engine) as session:
    year = 2008
    state = "New York"
    population_sum = session.execute(text(f'SELECT sum(pop{year}) FROM census where state="{state}" group by sex')).all()
    print(f'Male population in {state} in {year} = {population_sum[1][0]}')
    print(f'Female population in {state} in {year} = {population_sum[0][0]}')


