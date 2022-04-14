# import sqlalchemy
# print(sqlalchemy.__version__)

from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("mysql+pymysql://root:@localhost/superheroes", echo=False, future=True)

# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE martina (x int, y int)"))
#     conn.execute(
#         text("INSERT INTO martina (x, y) VALUES (:x, :y)"),
#         [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
#     )
#     conn.commit()

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT x, y FROM martina"))
#     for row in result:
#         print(f"x: {row.x}  y: {row.y}")

# print('******parameterised query ********')
#
# num = int(input("What number would you like? "))
# with engine.connect() as conn:
#     result = conn.execute(
#         text("SELECT x, y FROM some_table WHERE y > :param"),
#         {"param": num}
#     )
#     for row in result:
#         print(f"x: {row.x}  y: {row.y}")

print('************* join *********')
num = int(input("What superhero would you like? "))

with engine.connect() as conn:
    result = conn.execute(
        text("""select name, alias, superpower, affiliation, objective from heroes inner join teams
        on heroes.teamID= teams.id where heroes.id = :id"""),
        {"id": num}
    )
    for row in result:
        print(f"name: {row.name}  alias: {row.alias} superpower: {row.superpower} affiliation: {row.affiliation} objective: {row.objective}")


with engine.connect() as conn:
    result = conn.execute(
        text("""update heroes set name = 'martina' where id = 1""")
    )
    conn.commit()