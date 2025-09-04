from assertpy import assert_that

from scripts.label_for_url import determine_label


def test_should_top_level_repository() -> None:
    # Given:
    url = "https://hub.docker.com/_/alpine"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("alpine")


def test_should_top_level_repository_and_tag() -> None:
    # Given:
    url = (
        "https://hub.docker.com/layers/library/alpine/3.18.3"
        "/images/sha256-c5c5fda71656f28e49ac9c5416b3643eaa6a108a8093151d6d1afc9463be8e33"
        "?context=explore"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("alpine:3.18.3")


def test_should_org_repository() -> None:
    # Given:
    url = "https://hub.docker.com/r/bitnami/postgresql"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("bitnami/postgresql")


def test_should_org_repository_and_tag() -> None:
    # Given:
    url = (
        "https://hub.docker.com/layers/bitnami/postgresql/15.4.0"
        "/images/sha256-034d84dbc017e6013c8e189b4614a675ee2a5e88279ff6776c3b8c339bcdcf9e"
        "?context=explore"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("bitnami/postgresql:15.4.0")
