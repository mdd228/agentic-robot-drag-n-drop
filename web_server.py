import logging
from flask import Flask, render_template, request, jsonify
from top import TOP

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
top = TOP()

@app.route('/')
def index():
    logger.info("Accessing main page")
    # Get list of available agents with capabilities
    agents = top.get_agents()
    logger.info(f"Found agents: {agents}")
    return render_template('index.html', agents=agents)

@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()
    agent_id = data.get('agent_id')
    input_data = data.get('input_data')
    logger.info(f"Executing task for agent {agent_id} with input {input_data}")
    
    try:
        result = top.execute(agent_id, input_data)
        return jsonify(result)
    except Exception as e:
        logger.error(f"Error executing task: {str(e)}")
        return jsonify({"error": str(e)})

@app.route('/test', methods=['POST'])
def test_agent():
    data = request.json
    agent_id = data.get('agent_id')
    test_input = data.get('test_input')
    logger.info(f"Testing agent {agent_id} with input {test_input}")
    
    try:
        result = top.test_agent(agent_id, test_input)
        return jsonify(result)
    except Exception as e:
        logger.error(f"Error testing agent: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/capabilities', methods=['GET'])
def get_capabilities():
    """Get capabilities for all agents."""
    agents = top.discover_agents()
    capabilities = {}
    for agent in agents:
        capabilities[agent['id']] = agent['capabilities']
    return jsonify(capabilities)

if __name__ == '__main__':
    logger.info("Starting TOP web server...")
    app.run(debug=True, port=8080) 