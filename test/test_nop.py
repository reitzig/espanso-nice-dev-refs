from assertpy import assert_that

from label_for_url import determine_label


def test_should_return_unmatched_input():
    # Given:
    something = "anything-that's-not-supported"

    # When:
    label = determine_label(something)

    # Then:
    assert_that(label) \
        .is_equal_to(something)
