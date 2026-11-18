import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def test_create_and_get_booking():
    print("\n--- Starting API Automation Test ---")
    
    payload = {
        "firstname": "Samukelo",
        "lastname": "Cele",
        "totalprice": 1500,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Breakfast"
    }

    print("Sending POST request to create booking...")
    post_response = requests.post(f"{BASE_URL}/booking", json=payload)

    assert post_response.status_code == 200, f"Expected 200, got {post_response.status_code}"
    print("✅ Status Code 200 OK")
    
    post_data = post_response.json()
    
    assert "bookingid" in post_data, "Bug: No booking ID returned!"
    new_booking_id = post_data["bookingid"]
    print(f"✅ Booking created successfully. ID: {new_booking_id}")

    print(f"\nSending GET request for booking {new_booking_id}...")
    get_response = requests.get(f"{BASE_URL}/booking/{new_booking_id}")

    assert get_response.status_code == 200, "Failed to retrieve the booking!"
    print("✅ Status Code 200 OK")
    
    get_data = get_response.json()
    assert get_data["firstname"] == "Samukelo", "Bug: First name mismatch!"
    assert get_data["totalprice"] == 1500, "Bug: Price mismatch!"
    
    print("\n🎉 All API Tests Passed Successfully!")