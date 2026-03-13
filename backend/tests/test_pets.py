def test_create_pet(client):

    client_response = client.post(
        "/clients",
        json={
            "name": "Owner",
            "email": "owner@email.com",
            "phone": "11999999999"
        }
    )

    owner_id = client_response.json()["id"]

    response = client.post(
        "/pets",
        json={
            "name": "Rex",
            "species": "dog",
            "breed": "Labrador",
            "age": 5,
            "owner_id": owner_id
        }
    )

    assert response.status_code == 201