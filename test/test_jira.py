import pytest
from assertpy import assert_that

from label_for_url import determine_label


@pytest.mark.parametrize(
    "url_prefix", ["https://our-jira.my-org.de", "https://my-org.atlassian.net"]
)
def test_should_label_project(url_prefix: str) -> None:
    # Given:
    url = f"{url_prefix}/browse/FANCY"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("FANCY")


@pytest.mark.parametrize(
    "url_prefix", ["https://our-jira.my-org.de", "https://my-org.atlassian.net"]
)
def test_should_label_issue(url_prefix: str) -> None:
    # Given:
    url = f"{url_prefix}/browse/FANCY-77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("FANCY-77")


@pytest.mark.parametrize(
    "url_prefix", ["https://our-jira.my-org.de", "https://my-org.atlassian.net"]
)
def test_should_label_issue_and_comment(url_prefix: str) -> None:
    # Given:
    url = (
        f"{url_prefix}/browse/FANCY-77"
        "?focusedCommentId=123456"
        "&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel"
        "#comment-123456"
    )
    # Yup, that's the URL format they went with. 👀

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("FANCY-77.123456")


@pytest.mark.parametrize(
    "url_prefix", ["https://our-jira.my-org.de", "https://my-org.atlassian.net"]
)
def test_should_label_issue_and_comment_alternative(url_prefix: str) -> None:
    # Given:
    url = (
        f"{url_prefix}/browse/FANCY-77"
        "?focusedId=123456"
        "&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel"
        "#comment-123456"
    )
    # Yup, that's _another_ URL format they went with. 👀

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("FANCY-77.123456")


@pytest.mark.parametrize(
    "url_prefix", ["https://our-jira.my-org.de", "https://my-org.atlassian.net"]
)
def test_should_label_servicedesk_issue(url_prefix: str) -> None:
    # https://our-jira.my-org.de/servicedesk/customer/portal/77/SUPPORT-123
    # Given:
    url = f"{url_prefix}/servicedesk/customer/portal/77/SUPPORT-123"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("SUPPORT-123")
