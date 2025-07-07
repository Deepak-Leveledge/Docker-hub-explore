from app import app



def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Welcome to the Flask app!"}

def test_health_check():
    response = app.test_client().get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}

def test_about():
    response = app.test_client().get('/about')
    assert response.status_code == 200
    assert response.json == {"message": "This is a simple Flask application."}
