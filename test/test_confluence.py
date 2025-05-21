import pytest
from assertpy import assert_that

from label_for_url import determine_label


@pytest.mark.parametrize(
    "url",
    [
        "https://our-confluence.my-org.de/display/MYSPACE/",
        "https://my-org.atlassian.net/wiki/spaces/MYSPACE/overview",
    ],
)
def test_should_label_space(url: str) -> None:
    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MYSPACE")


@pytest.mark.parametrize(
    "url",
    [
        "https://our-confluence.my-org.de/display/MYSPACE/Some+Page+Nobody+Reads",
        "https://my-org.atlassian.net/wiki/spaces/MYSPACE/pages/1333624914/Some+Page+Nobody+Reads",
    ],
)
def test_should_label_url_with_title(url: str) -> None:
    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MYSPACE/Some Page Nobody Reads")


@pytest.mark.parametrize(
    "url",
    [
        "https://our-confluence.my-org.de/display/MYSPACE/Some+Page+Nobody+Reads?focusedCommentId=241754794#comment-241754794",
        "https://my-org.atlassian.net/wiki/spaces/MYSPACE/pages/1333624914/Some+Page+Nobody+Reads?focusedCommentId=241754794",
    ],
)
def test_should_label_url_with_title_and_comment(url: str) -> None:
    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MYSPACE/Some Page Nobody Reads > Comment 241754794")


def test_should_revert_url_encoding() -> None:
    # When:
    label = determine_label(
        "https://our-confluence.my-org.de/display/MYSPACE/%5BWIP%5D+Some+Page+Nobody+Reads"
    )

    # Then:
    assert_that(label).is_equal_to("MYSPACE/[WIP] Some Page Nobody Reads")


def test_should_label_url_with_title_in_args_for_viewpage() -> None:
    # Given:
    url = (
        "https://our-confluence.my-org.de/pages/viewpage.action"
        "?spaceKey=MYSPACE&title=Some+Page+Nobody+Reads"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MYSPACE/Some Page Nobody Reads")


def test_should_label_url_with_title_in_anchor_for_viewpage() -> None:
    # Given:
    url = (
        "https://our-confluence.my-org.de/pages/viewpage.action"
        "?pageId=205489860#SomePage-S%C3%A4ction"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("SomePage > Säction")


def test_should_label_url_with_title_in_args_for_releaseview() -> None:
    # Given:
    url = (
        "https://our-confluence.my-org.de/pages/releaseview.action"
        "?spaceKey=MYSPACE&title=Some+Page+Nobody+Reads"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MYSPACE/Some Page Nobody Reads")


def test_should_label_url_without_info() -> None:
    # Given:
    url = "https://our-confluence.my-org.de/pages/viewpage.action?pageId=241739726&src=contextnavpagetreemode"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("our-confluence.my-org.de/241739726")
