from assertpy import assert_that

from label_for_url import determine_label


def test_should_label_repository() -> None:
    # Given:
    url = "https://gitea.some.org/my-account/some-repo"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo")


def test_should_label_file() -> None:
    # Given:
    url = "https://gitea.some.org/my-account/some-repo/src/branch/main/some/file.md"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo:some/file.md")


def test_should_label_file_and_line() -> None:
    # Given:
    url = "https://gitea.some.org/my-account/some-repo/src/branch/main/some/file.md#L77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo:some/file.md#77")


def test_should_label_file_and_lines() -> None:
    # Given:
    url = "https://gitea.some.org/my-account/some-repo/src/branch/main/some/file.md#L42-L77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo:some/file.md#42-77")


def test_should_label_file_on_branch() -> None:
    # Given:
    url = "https://gitea.some.org/my-account/some-repo/src/branch/some-branch/some/file.md"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@some-branch:some/file.md")


def test_should_label_file_at_revision() -> None:
    # Given:
    url = (
        "https://gitea.some.org/my-account/some-repo"
        "/src/commit/3577c55c6f18e164c37f332f98b4c08b1242f90e/some/file.md"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@3577c55c:some/file.md")


def test_should_label_folder() -> None:
    # Given:
    url = "https://gitea.some.org/my-account/some-repo/src/branch/main/some/folder"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo:some/folder")


def test_should_label_commit() -> None:
    # Given:
    url = "https://gitea.some.org/my-account/some-repo/commit/3577c55c6f18e164c37f332f98b4c08b1242f90e"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@3577c55c")


def test_should_label_branch() -> None:
    # Given:
    url = "https://gitea.some.org/my-account/some-repo/src/branch/some-branch"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@some-branch")


def test_should_label_branch_comparison() -> None:
    # Given:
    url = "https://gitea.some.org/my-account/some-repo/compare/feat/something...chore/else"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@feat/something⭤chore/else")


def test_should_label_pr_comment() -> None:
    # Given:
    url = "https://gitea.some.org/my-account/some-repo/pulls/42#issuecomment-77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo#42.77")


def test_should_label_pr_and_review_comment() -> None:
    # Given:
    url = "https://gitea.some.org/my-account/some-repo/pulls/42/files#issuecomment-77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo#42.77")


def test_should_label_pr_commit() -> None:
    # Given:
    url = (
        "https://gitea.some.org/my-account/some-repo"
        "/pulls/119/commits/3577c55c6f18e164c37f332f98b4c08b1242f90e"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo#119@3577c55c")
