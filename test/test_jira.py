from assertpy import assert_that

from label_for_url import determine_label


def test_should_label_project():
    # Given:
    url = "https://our-jira.my-org.de/browse/FANCY"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('FANCY')


def test_should_label_repository():
    # Given:
    url = "https://our-jira.my-org.de/browse/FANCY-77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('FANCY-77')
