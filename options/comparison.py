def is_equal(requested, found):
    """Checks that values is equal."""
    assert requested == found, f'Found city is not correct. Should be {requested}, but was found {found}.'


def element_within(content, element):
    """Checks that element within content."""
    assert element in content, f"{element} is not presented in a requested content."