from flask import Blueprint, request, jsonify
from backend.services.calculations import calculate_lifecycle_cost

api = Blueprint('api', __name__)

@api.route('/lifecycle-cost', methods=['POST'])
def lifecycle_cost():
    data = request.json
    # Assuming data contains necessary fields for calculation
    try:
        cost = calculate_lifecycle_cost(data)
        return jsonify({'lifecycle_cost': cost}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400