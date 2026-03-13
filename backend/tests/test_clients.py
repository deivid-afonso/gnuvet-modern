def test_create_client(client):

    response = client.post(
        "/clients",
        json={
            "name": "João Silva",
            "email": "joao@example.com",
            "phone": "11999999999"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["email"] == "joao@example.com"