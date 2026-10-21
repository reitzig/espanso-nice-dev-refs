from assertpy import assert_that

from scripts.label_for_url import determine_label


def test_should_prettify_renovate_docs_link() -> None:
    # Given:
    url = "https://docs.renovatebot.com/configuration-options/#automergeschedule"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to(
        "docs.renovatebot.com > Configuration Options > Automergeschedule"
    )


def test_should_prettify_github_docs_link() -> None:
    # Given:
    url = "https://docs.github.com/en/actions/how-tos/write-workflows/use-workflow-templates"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to(
        "docs.github.com > Actions > How Tos > Write Workflows > Use Workflow Templates"
    )


def test_should_prettify_spring_docs_link() -> None:
    # Given:
    url = "https://docs.spring.io/spring-boot/reference/web/graceful-shutdown.html"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to(
        "docs.spring.io > Spring Boot > Reference > Web > Graceful Shutdown"
    )
