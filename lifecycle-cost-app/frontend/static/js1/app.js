

// Fetch and display equipment data
async function fetchEquipment() {
    const response = await fetch('/equipment');
    const equipment = await response.json();
    const tableBody = document.querySelector('#equipment-table tbody');
    tableBody.innerHTML = '';
    equipment.forEach(e => {
        const row = `<tr>
            <td>${e.id}</td>
            <td>${e.area}</td>
            <td>${e.flota}</td>
            <td>${e.codigo}</td>
            <td>${e.modelo}</td>
            <td>${e.horometro_actual}</td>
            <td>${e.vida_util}</td>
            <td>${e.overhaul}</td>
        </tr>`;
        tableBody.innerHTML += row;
    });
}

// Fetch and display components data
async function fetchComponents() {
    const response = await fetch('/components');
    const components = await response.json();
    const tableBody = document.querySelector('#components-table tbody');
    tableBody.innerHTML = '';
    components.forEach(c => {
        const row = `<tr>
            <td>${c.id}</td>
            <td>${c.equipment_codigo}</td>
            <td>${c.component_tipo}</td>
            <td>${c.component_name}</td>
            <td>${c.component_P_N}</td>
            <td>${c.component_reparable}</td>
            <td>${c.component_num_rep}</td>
            <td>${c.component_PCR}</td>
            <td>${c.component_fecha_instalacion}</td>
            <td>${c.component_horometro_instalacion}</td>
        </tr>`;
        tableBody.innerHTML += row;
    });
}

// Add new equipment
document.querySelector('#add-equipment-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = {
        area: document.querySelector('#area').value,
        flota: document.querySelector('#flota').value,
        codigo: document.querySelector('#codigo').value,
        modelo: document.querySelector('#modelo').value,
        horometro_actual: parseFloat(document.querySelector('#horometro_actual').value),
        vida_util: parseInt(document.querySelector('#vida_util').value),
        overhaul: document.querySelector('#overhaul').value
    };
    await fetch('/equipment', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    fetchEquipment(); // Refresh the equipment table
});

// Add new component
document.querySelector('#add-component-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = {
        equipment_codigo: document.querySelector('#equipment_codigo').value,
        component_tipo: document.querySelector('#component_tipo').value,
        component_name: document.querySelector('#component_name').value,
        component_P_N: document.querySelector('#component_P_N').value,
        component_reparable: document.querySelector('#component_reparable').value,
        component_num_rep: parseInt(document.querySelector('#component_num_rep').value),
        component_PCR: parseInt(document.querySelector('#component_PCR').value),
        component_fecha_instalacion: document.querySelector('#component_fecha_instalacion').value,
        component_horometro_instalacion: parseFloat(document.querySelector('#component_horometro_instalacion').value)
    };
    await fetch('/components', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    fetchComponents(); // Refresh the components table
});

// Fetch data on page load
fetchEquipment();
fetchComponents();