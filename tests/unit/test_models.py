def test_new_user(new_user):
    assert new_user.firstname == "Ronald"
    assert new_user.lastname == "Ndirangu"

def test_new_request(new_request):
    assert new_request.date == "15/04/2018"
    assert new_request.title == "Repair Motor"