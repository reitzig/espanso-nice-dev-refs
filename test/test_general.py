from assertpy import assert_that

from label_for_url import determine_label


def test_should_mailto() -> None:
    # Given:
    url = "mailto:some.person@random-server.org"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("some.person@random-server.org")
