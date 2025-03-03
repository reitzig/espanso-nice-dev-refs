from assertpy import assert_that

from label_for_url import determine_label


def test_should_label_link_to_fragment() -> None:
    # Given:
    url = "https://some.server/and/path#:~:text=Something%20important"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("some.server/and/path > Something important")


def test_should_label_link_to_long_fragment() -> None:
    # Given:
    url = (
        "https://some.server/and/path"
        "#:~:text=Something%20important%20that%20could%20have%20been%20written%20much%20more%20shortly"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("some.server/and/path > Something important …")


def test_should_label_mailto() -> None:
    # Given:
    url = "mailto:some.person@random-server.org"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("some.person@random-server.org")
