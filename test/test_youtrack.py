from assertpy import assert_that

from scripts.label_for_url import determine_label


def test_should_label_issue() -> None:
    # Given:
    url = "https://youtrack.jetbrains.com/issue/IDEA-7742/Some-Title-I-came-up-with"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("IDEA-7742")


def test_should_label_issue_and_comment() -> None:
    # Given:
    url = "https://youtrack.jetbrains.com/issue/IDEA-7742/Some-Title-I-came-up-with#focus=Comments-27-9914365.0-0"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("IDEA-7742.9914365")
