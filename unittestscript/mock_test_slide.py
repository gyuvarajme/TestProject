To choose the random person
1. should not show  the same person
2. should not select the person already seen


def get_next_person(user):
    person = get_random_person()
    while person in user['people_seen']:
        person = get_random_person()
    return person


def test_new_person():
    user = {'people_seen':[]}
    expected_person = 'Katie'
    actual_person = get_next_person(user)
    assert_equals(actual_person,expected_person)


from mock import patch



