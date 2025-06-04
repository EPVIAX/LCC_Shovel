from models.database import session, Equipo, Componente

# Fetch all records from the 'equipment' table
def fetch_all_equipment():
    equipment = session.query(Equipo).all()
    for e in equipment:
        print(f"ID: {e.id}, Area: {e.area}, Flota: {e.flota}, Codigo: {e.codigo}, Modelo: {e.modelo}, "
              f"Horometro Actual: {e.horometro_actual}, Vida Útil: {e.vida_util}, Overhaul: {e.overhaul}")

# Fetch all records from the 'components' table
def fetch_all_components():
    components = session.query(Componente).all()
    for c in components:
        print(f"ID: {c.id}, Equipment Codigo: {c.equipment_codigo}, Tipo: {c.component_tipo}, "
              f"Name: {c.component_name}, P/N: {c.component_P_N}, Reparable: {c.component_reparable}, "
              f"Num Rep: {c.component_num_rep}, PCR: {c.component_PCR}, "
              f"Fecha Instalacion: {c.component_fecha_instalacion}, "
              f"Horometro Instalacion: {c.component_horometro_instalacion}")

if __name__ == "__main__":
    print("Equipment Table:")
    fetch_all_equipment()
    print("\nComponents Table:")
    fetch_all_components()