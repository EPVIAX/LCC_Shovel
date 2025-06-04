from flask import Flask, request, jsonify, render_template
from models.database import session, Equipo, Componente

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

# Serve the homepage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view-data')
def view_data():
    return render_template('view_data.html')

# Routes for Equipment (Equipo)
@app.route('/equipment', methods=['GET'])
def get_all_equipment():
    equipment = session.query(Equipo).all()
    return jsonify([{
        'id': e.id,
        'area': e.area,
        'flota': e.flota,
        'codigo': e.codigo,
        'modelo': e.modelo,
        'horometro_actual': e.horometro_actual,
        'vida_util': e.vida_util,
        'overhaul': e.overhaul
    } for e in equipment])

@app.route('/equipment', methods=['POST'])
def add_equipment():
    data = request.json
    new_equipment = Equipo(
        area=data['area'],
        flota=data['flota'],
        codigo=data['codigo'],
        modelo=data['modelo'],
        horometro_actual=data['horometro_actual'],
        vida_util=data['vida_util'],
        overhaul=data['overhaul']
    )
    session.add(new_equipment)
    session.commit()
    return jsonify({'message': 'Equipment added successfully'}), 201

@app.route('/equipment/<int:id>', methods=['PUT'])
def update_equipment(id):
    data = request.json
    equipment = session.query(Equipo).get(id)
    if not equipment:
        return jsonify({'message': 'Equipment not found'}), 404
    equipment.area = data['area']
    equipment.flota = data['flota']
    equipment.codigo = data['codigo']
    equipment.modelo = data['modelo']
    equipment.horometro_actual = data['horometro_actual']
    equipment.vida_util = data['vida_util']
    equipment.overhaul = data['overhaul']
    session.commit()
    return jsonify({'message': 'Equipment updated successfully'})

@app.route('/equipment/<int:id>', methods=['DELETE'])
def delete_equipment(id):
    equipment = session.query(Equipo).get(id)
    if not equipment:
        return jsonify({'message': 'Equipment not found'}), 404
    session.delete(equipment)
    session.commit()
    return jsonify({'message': 'Equipment deleted successfully'})

# Routes for Components (Componente)
@app.route('/components', methods=['GET'])
def get_all_components():
    components = session.query(Componente).all()
    return jsonify([{
        'id': c.id,
        'equipment_codigo': c.equipment_codigo,
        'component_tipo': c.component_tipo,
        'component_name': c.component_name,
        'component_P_N': c.component_P_N,
        'component_reparable': c.component_reparable,
        'component_num_rep': c.component_num_rep,
        'component_PCR': c.component_PCR,
        'component_fecha_instalacion': c.component_fecha_instalacion,
        'component_horometro_instalacion': c.component_horometro_instalacion
    } for c in components])

@app.route('/components', methods=['POST'])
def add_component():
    data = request.json
    new_component = Componente(
        equipment_codigo=data['equipment_codigo'],
        component_tipo=data['component_tipo'],
        component_name=data['component_name'],
        component_P_N=data['component_P_N'],
        component_reparable=data['component_reparable'],
        component_num_rep=data['component_num_rep'],
        component_PCR=data['component_PCR'],
        component_fecha_instalacion=data['component_fecha_instalacion'],
        component_horometro_instalacion=data['component_horometro_instalacion']
    )
    session.add(new_component)
    session.commit()
    return jsonify({'message': 'Component added successfully'}), 201

@app.route('/components/<int:id>', methods=['PUT'])
def update_component(id):
    data = request.json
    component = session.query(Componente).get(id)
    if not component:
        return jsonify({'message': 'Component not found'}), 404
    component.equipment_codigo = data['equipment_codigo']
    component.component_tipo = data['component_tipo']
    component.component_name = data['component_name']
    component.component_P_N = data['component_P_N']
    component.component_reparable = data['component_reparable']
    component.component_num_rep = data['component_num_rep']
    component.component_PCR = data['component_PCR']
    component.component_fecha_instalacion = data['component_fecha_instalacion']
    component.component_horometro_instalacion = data['component_horometro_instalacion']
    session.commit()
    return jsonify({'message': 'Component updated successfully'})

@app.route('/components/<int:id>', methods=['DELETE'])
def delete_component(id):
    component = session.query(Componente).get(id)
    if not component:
        return jsonify({'message': 'Component not found'}), 404
    session.delete(component)
    session.commit()
    return jsonify({'message': 'Component deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)