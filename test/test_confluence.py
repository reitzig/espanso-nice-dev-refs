from assertpy import assert_that

from label_for_url import determine_label


def test_should_label_url_with_title():
    # Given:
    url = "https://our-confluence.my-org.de/display/MYSPACE/Some+Page+Nobody+Reads"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MYSPACE/Some Page Nobody Reads')


def test_should_label_url_with_title_in_args():
    # Given:
    url = "https://our-confluence.my-org.de/pages/viewpage.action?spaceKey=MYSPACE&title=Some+Page+Nobody+Reads"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MYSPACE/Some Page Nobody Reads')
