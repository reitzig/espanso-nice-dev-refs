from assertpy import assert_that

from label_for_url import determine_label


def test_should_label_project() -> None:
    # Given:
    url = "https://our-jira.my-org.de/browse/FANCY"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("FANCY")


def test_should_label_issue() -> None:
    # Given:
    url = "https://our-jira.my-org.de/browse/FANCY-77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("FANCY-77")


def test_should_label_issue_and_comment() -> None:
    # Given:
    url = (
        "https://our-jira.my-org.de/browse/FANCY-77"
        "?focusedCommentId=123456"
        "&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel"
        "#comment-123456"
    )
    # Yup, that's the URL format they went with. 👀

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("FANCY-77.123456")


def test_should_label_issue_and_comment_alternative() -> None:
    # Given:
    url = (
        "https://our-jira.my-org.de/browse/FANCY-77"
        "?focusedId=123456"
        "&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel"
        "#comment-123456"
    )
    # Yup, that's _another_ URL format they went with. 👀

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("FANCY-77.123456")


def test_should_label_servicedesk_issue() -> None:
    # https://our-jira.my-org.de/servicedesk/customer/portal/77/SUPPORT-123
    # Given:
    url = "https://our-jira.my-org.de/servicedesk/customer/portal/77/SUPPORT-123"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("SUPPORT-123")
