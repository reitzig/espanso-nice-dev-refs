from assertpy import assert_that

from label_for_url import determine_label


def test_should_label_space() -> None:
    # Given:
    url = "https://our-confluence.my-org.de/display/MYSPACE/"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MYSPACE")


def test_should_label_url_with_title() -> None:
    # Given:
    url = "https://our-confluence.my-org.de/display/MYSPACE/Some+Page+Nobody+Reads"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MYSPACE/Some Page Nobody Reads")


def test_should_revert_url_encoding() -> None:
    # Given:
    url = "https://our-confluence.my-org.de/display/MYSPACE/%5BWIP%5D+Some+Plan+Nobody+Reads"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MYSPACE/[WIP] Some Plan Nobody Reads")


def test_should_label_url_with_title_in_args_for_viewpage() -> None:
    # Given:
    url = "https://our-confluence.my-org.de/pages/viewpage.action?spaceKey=MYSPACE&title=Some+Page+Nobody+Reads"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MYSPACE/Some Page Nobody Reads")


def test_should_label_url_with_title_in_anchor_for_viewpage() -> None:
    # Given:
    url = "https://our-confluence.my-org.de/pages/viewpage.action?pageId=205489860#SomePage-Section"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("SomePage > Section")


def test_should_label_url_with_title_in_args_for_releaseview() -> None:
    # Given:
    url = "https://our-confluence.my-org.de/pages/releaseview.action?spaceKey=MYSPACE&title=Some+Page+Nobody+Reads"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MYSPACE/Some Page Nobody Reads")
