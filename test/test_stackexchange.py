from assertpy import assert_that

from scripts.label_for_url import determine_label


def test_should_label_stackoverflow_questions() -> None:
    # Given:
    url = "https://stackoverflow.com/questions/74206388/espanso-replacement-not-working-outside-of-terminal"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("SO#74206388")


def test_should_label_stackoverflow_answers() -> None:
    # Given:
    url = "https://stackoverflow.com/a/470376/539599"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("SO#470376")


def test_should_label_network_questions() -> None:
    # Given:
    url = "https://cs.stackexchange.com/q/45486/98"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("cs.SE#45486")


def test_should_label_network_answers() -> None:
    # Given:
    url = (
        "https://cs.stackexchange.com/questions/45486/"
        "how-can-a-language-whose-compiler-is-written-in-c-ever-be-faster-than-c/45505#45505"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("cs.SE#45505")
