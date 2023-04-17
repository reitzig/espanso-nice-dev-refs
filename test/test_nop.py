from assertpy import assert_that

from label_for_url import determine_label


def test_should_return_trimmed_host_for_urls():
    # Given:
    url = "https://some.server/"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to("some.server")


def test_should_return_only_path_for_urls():
    # Given:
    url = "https://some.server/and/path?with=args&that=are&annoying=reading"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to("some.server/and/path")


def test_should_drop_boring_subdomains_from_path():
    # Given:
    url = "https://www.some.server/and/path?with=args&that=are&annoying=reading"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to("some.server/and/path")


def test_should_return_unmatched_input():
    # Given:
    something = "anything-that's-not-supported"

    # When:
    label = determine_label(something)

    # Then:
    assert_that(label) \
        .is_equal_to(something)
