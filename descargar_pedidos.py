import pandas as pd
from sqlalchemy import create_engine, text

user = "user_class"
pwd = "pwd_sqlalchemy"
READONLY_DSN = f"postgresql+psycopg2://{user}:{pwd}@dpg-d29qb6ripnbc73b70q00-a.oregon-postgres.render.com/centrocapacitacion"
engine_postgres = create_engine(READONLY_DSN)
data = pd.read_sql_query(text("select * from st_pedidos;"),engine_postgres)
data['fecha_registro'] = data["fecha_registro"].dt.tz_localize(None)
data.to_excel("Reporte.xlsx",index=False)
input("Fin del programa... Reporte.xlsx generado")