from typing import Any, Dict

create_new_user_account_data: Dict[str, Any] = {
    "name": "John Doe",
    "username": "johndoe"
}

invalid_user_account_data: Dict[str, Any] = {
    "name": "John123",
    "username": "jd",
    "email": "invalid-email",
    "photo": "http://example.com/photo.txt",
    "password": "weak"
}

user_account_data: Dict[str, Any] = {
    "name": "Jane Smith",
    "username": "janesmith",
    "email": "jane.smith@example.com",
    "photo": "http://example.com/photo.jpg",
    "password": "StrongPass1"
}

secondary_user_account_data: Dict[str, Any] = {
    "name": "Alice Johnson",
    "username": "alice_j",
    "email": "alice.johnson@example.com",
    "photo": "http://example.com/photo2.jpg",
    "password": "StrongPass2"
}