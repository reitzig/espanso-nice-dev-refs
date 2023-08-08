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
