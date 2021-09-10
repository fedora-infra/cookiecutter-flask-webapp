from bs4 import BeautifulSoup


def test_root(client):
    """Test the root page"""
    response = client.get("/")
    assert response.status_code == 200
    page = BeautifulSoup(response.data, "html.parser")
    assert page.title
    assert page.title.string is not None
    assert "{{ cookiecutter.name }}" in page.title.string
