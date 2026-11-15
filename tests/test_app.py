from app import app


def test_homepage_returns_success():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200


def test_homepage_displays_menu():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/")

    html = response.get_data(as_text=True)

    assert "Python Bistro" in html
    assert "Margherita Pizza" in html
    assert "€12.00" in html
