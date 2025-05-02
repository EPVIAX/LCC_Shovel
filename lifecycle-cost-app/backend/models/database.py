from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
DATABASE_URL = "sqlite:///lifecycle_cost.db"  # Cambia esto si usas otra base de datos
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Modelo para la tabla 'equipment'
class Equipo(Base):
    __tablename__ = 'equipment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    area = Column(String, nullable=False)
    flota = Column(String, nullable=False)
    codigo = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    horometro_actual = Column(Float, nullable=False)
    vida_util = Column(Integer, nullable=False)
    overhaul = Column(String, nullable=False)

# Modelo para la tabla 'components'
class Componente(Base):
    __tablename__ = 'components'
    id = Column(Integer, primary_key=True, autoincrement=True)
    equipment_codigo = Column(String, nullable=False)
    component_tipo = Column(String, nullable=False)
    component_name = Column(String, nullable=False)
    component_P_N = Column(String, nullable=False)
    component_reparable = Column(String, nullable=False)
    component_num_rep = Column(Integer, nullable=False)
    component_PCR = Column(Integer, nullable=False)
    component_fecha_instalacion = Column(String, nullable=False)
    component_horometro_instalacion = Column(Float, nullable=False)

# Crear las tablas en la base de datos
def create_tables():
    Base.metadata.create_all(engine)

# Llamar a la función para crear las tablas
if __name__ == "__main__":
    create_tables()

