def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok", "service": "cyberdb"}


def test_create_data(client):
    r = client.post("/api/data", json={"content": "data breach test", "source": "Arasaka"})
    assert r.status_code == 201
    body = r.json()
    assert "id" in body
    assert "handle" in body
    assert body["content"] == "data breach test"
    assert body["source"] == "Arasaka"
    assert "hash" in body
    assert "created_at" in body


def test_list_data(client):
    client.post("/api/data", json={"content": "item 1"})
    client.post("/api/data", json={"content": "item 2"})
    r = client.get("/api/data")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) >= 2


def test_get_data_by_id(client):
    post = client.post("/api/data", json={"content": "get me"}).json()
    r = client.get(f"/api/data/{post['id']}")
    assert r.status_code == 200
    assert r.json()["content"] == "get me"


def test_get_data_404(client):
    r = client.get("/api/data/does-not-exist")
    assert r.status_code == 404
    assert r.json()["detail"] == "Data not found"


def test_delete_data(client):
    post = client.post("/api/data", json={"content": "delete me"}).json()
    r = client.delete(f"/api/data/{post['id']}")
    assert r.status_code == 204
    r2 = client.get(f"/api/data/{post['id']}")
    assert r2.status_code == 404


def test_delete_data_404(client):
    r = client.delete("/api/data/does-not-exist")
    assert r.status_code == 404


def test_stats(client):
    client.post("/api/data", json={"content": "stats test"})
    r = client.get("/api/stats")
    assert r.status_code == 200
    body = r.json()
    assert "total" in body
    assert "top_handles" in body
    assert "recent" in body
    assert body["total"] > 0
