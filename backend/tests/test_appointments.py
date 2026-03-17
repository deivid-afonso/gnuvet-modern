def test_create_appointment(client):

    response = client.post(
        "/appointments/",
        json={
            "pet_id": 1,
            "user_id": 1,
            "date": "2026-03-20T10:00:00"
        }
    )

    assert response.status_code == 200