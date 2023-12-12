import pytest
from assertpy import assert_that

from label_for_url import determine_label


def test_should_label_repository() -> None:
    # Given:
    url = "https://gitlab.some.org/my-account/some-repo"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo")


def test_should_label_repo_and_anchor() -> None:
    # Given:
    url = "https://gitlab.some.org/my-account/some-repo#some-headline"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo > Some Headline")


def test_should_label_issue() -> None:
    # Given:
    url = "https://gitlab.some.org/my-account/some-repo/-/issues/77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo#77")


def test_should_label_mr() -> None:
    # Given:
    url = "https://gitlab.some.org/my-account/some-repo/-/merge_requests/119"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo#119")


def test_should_label_file() -> None:
    # Given:
    url = "https://gitlab.some.org/my-account/some-repo/-/blob/main/some/file.md"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo:some/file.md")


def test_should_label_file_on_main_branch() -> None:
    # Given:
    url = "https://gitlab.some.org/my-account/some-repo/-/blob/main/some/file.md?ref_type=heads"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo:some/file.md")


def test_should_label_file_on_other_branch() -> None:
    # Given:
    url = "https://gitlab.some.org/my-account/some-repo/-/blob/some-branch/some/file.md?ref_type=heads"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@some-branch:some/file.md")


def test_should_label_file_on_tag() -> None:
    # Given:
    url = "https://gitlab.some.org/my-account/some-repo/-/blob/v1.2.3/some/file.md"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@v1.2.3:some/file.md")


def test_should_label_file_on_commit() -> None:
    # Given:
    url = "https://gitlab.some.org/my-account/some-repo/-/blob/198c9f97383a262318558321414ee4695bd68549/some/file.md"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@198c9f97:some/file.md")


def test_should_label_folder() -> None:
    # Given:
    url = "https://gitlab.some.org/my-account/some-repo/-/tree/main/some/folder"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo:some/folder")


def test_should_label_folder_and_anchor() -> None:
    # Given:
    url = "https://gitlab.some.org/my-account/some-repo/-/tree/main/some/folder/#some-headline"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo:some/folder > Some Headline")


def test_should_label_file_and_line() -> None:
    # Given:
    url = "https://gitlab.some.org/my-account/some-repo/-/blob/main/some/file.md#L77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo:some/file.md#77")


def test_should_label_commit() -> None:
    # Given:
    url = "https://gitlab.some.org/my-account/some-repo/-/commit/5ad8783f34a650e6a5c8ad8948b0bdc1131e1a10"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@5ad8783f")


@pytest.mark.skip(reason="impossible due to URL format, can't separate branch and file name!")
def test_should_label_branch() -> None:
    # Given:
    url = "https://gitlab.some.org/my-account/some-repo/-/tree/feature/something"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@feature/something")


def test_should_label_asciidoc_and_anchor() -> None:
    # Given:
    url = "https://gitlab.com/my-account/some-repo/-/blob/main/some/README.adoc#some-headline"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo:some/README > Some Headline")


def test_should_label_repo_snippet() -> None:
    # Given:
    url = "https://gitlab.some.org/my-account/some-repo/-/snippets/123456"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo$123456")


def test_should_label_global_snippet() -> None:
    # Given:
    url = "https://gitlab.some.org/-/snippets/123456"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("gitlab.some.org$123456")


# TODO: line in snippet?
