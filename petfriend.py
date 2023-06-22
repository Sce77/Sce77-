def add_photo_to_pet(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
    """Метод отправляет на сервер фото к добавленному ранее ранее питомцу. Возвращает статус
    запроса  и данные питомца в JSON"""

    data = MultipartEncoder(
        fields={
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
        })
    headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

    res = requests.post(self.base_url + '/api/pets/set_photo/' + pet_id, headers=headers, data=data)
    status = res.status_code
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    return status, result