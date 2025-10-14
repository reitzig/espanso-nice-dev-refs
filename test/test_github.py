from assertpy import assert_that

from label_for_url import determine_label


def test_should_label_repository() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo")


def test_should_label_repository_without_seo() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo?utm_source=changelog-news"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo")


def test_should_label_repo_and_anchor() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo#some-headline"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo > Some Headline")


def test_should_label_issue() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/issues/77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo#77")


def test_should_label_issue_and_comment() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/issues/77#issuecomment-42"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo#77.42")


def test_should_label_issue_list_by_label() -> None:
    # Given:
    url = (
        "https://github.com/my-account/some-repo/issues"
        "?q=is%3Aissue+is%3Aopen+label%3Abug+label%3A%22feedback+needed%22"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo#[bug,feedback needed]")


def test_should_label_issue_list_with_search_query() -> None:
    # Given:
    url = (
        "https://github.com/my-account/some-repo/issues"
        "?q=is%3Aissue+is%3Aopen"
    )  # fmt: skip

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo#[🔍]")


def test_should_label_discussion() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/discussions/42"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo#42")


def test_should_label_discussion_and_comment() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/discussions/42#discussioncomment-77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo#42.77")


def test_should_label_pr() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/pull/119"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo#119")


def test_should_label_pr_and_commit() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/pull/119/commits/3577c55c6f18e164c37f332f98b4c08b1242f90e"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo#119@3577c55c")


def test_should_label_pr_and_commit_and_file() -> None:
    # Given:
    url = (
        "https://github.com/my-account/some-repo/pull/119/commits/3577c55c6f18e164c37f332f98b4c08b1242f90e"
        "#diff-e20ce122c39fb84454a31dab91b2648d7985906f50dff8d2936193e6152c33bf"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to(
        "my-account/some-repo#119@3577c55c"
    )  # NB: No filename to be found


def test_should_label_pr_and_commit_and_file_and_line() -> None:
    # Given:
    url = (
        "https://github.com/my-account/some-repo/pull/119/files"
        "#diff-e20ce122c39fb84454a31dab91b2648d7985906f50dff8d2936193e6152c33bf"
        "R42"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to(
        "my-account/some-repo#119:e20ce122#42"
    )  # NB: No filename to be found


def test_should_label_pr_and_commit_and_file_and_lines() -> None:
    # Given:
    url = (
        "https://github.com/my-account/some-repo/pull/119/files"
        "#diff-e20ce122c39fb84454a31dab91b2648d7985906f50dff8d2936193e6152c33bf"
        "R42-R77"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to(
        "my-account/some-repo#119:e20ce122#42-77"
    )  # NB: No filename to be found


def test_should_label_pr_and_review_comment() -> None:
    # Given:
    url = (
        "https://github.com/my-account/some-repo/pull/119/commits/3577c55c6f18e164c37f332f98b4c08b1242f90e"
        "#r2112066737"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo#119@3577c55c.2112066737")


def test_should_label_pr_and_review_on_file() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/pull/119/files#r2112066737"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo#119.2112066737")


def test_should_label_pr_list_by_label() -> None:
    # Given:
    url = (
        "https://github.com/my-account/some-repo/pulls"
        "?q=is%3Apr+is%3Aopen+label%3Adependencies+label%3A%22no+changelog%22"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo#[dependencies,no changelog]")


def test_should_label_review_comment() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/pull/42#discussion_r77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo#42.77")


def test_should_label_branch() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/tree/some-branch"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@some-branch")


def test_should_label_file() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/blob/main/some/file.md"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo:some/file.md")


def test_should_label_file_on_branch() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/blob/some-branch/some/file.md"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@some-branch:some/file.md")


def test_should_label_folder() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/tree/main/some/folder"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo:some/folder")


def test_should_label_folder_on_branch() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/tree/some-branch/some/folder"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@some-branch:some/folder")


def test_should_label_folder_and_anchor() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/tree/main/some/folder#some-headline"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo:some/folder > Some Headline")


def test_should_label_file_and_line() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/blob/main/some/file.md#L77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo:some/file.md#77")


def test_should_label_file_and_lines() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/blob/main/some/file.md#L42-L77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo:some/file.md#42-77")


def test_should_label_commit() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/commit/3577c55c6f18e164c37f332f98b4c08b1242f90e"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@3577c55c")


def test_should_label_commit_and_file() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/commit/3577c55c6f18e164c37f332f98b4c08b1242f90e#diff-2f754321d62f08ba8392b9b168b83e24ea2852bb5d815d63e767f6c3d23c6ac5"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@3577c55c:2f754321")


def test_should_label_commit_and_file_and_line() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/commit/3577c55c6f18e164c37f332f98b4c08b1242f90e#diff-2f754321d62f08ba8392b9b168b83e24ea2852bb5d815d63e767f6c3d23c6ac5R77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@3577c55c:2f754321#77")


def test_should_label_commit_diff() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/compare/3577c55c6f18e164c37f332f98b4c08b1242f90e...some-branch"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@3577c55c⭤some-branch")


def test_should_label_tag_diff() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/compare/v1.2.3...v1.2.4"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@v1.2.3⭤v1.2.4")


def test_should_label_markdown_and_anchor() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/blob/main/some/README.md#some-headline"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo:some/README > Some Headline")


def test_should_label_release() -> None:
    url = "https://github.com/my-account/some-repo/releases/tag/1.2.3"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo@1.2.3")


def test_should_label_gist() -> None:
    # Given:
    url = "https://gist.github.com/my-account/abcdef123456789"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/abcdef")


def test_should_label_gist_and_file() -> None:
    # Given:
    url = "https://gist.github.com/my-account/abcdef123456789#file-some_file-md"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/abcdef:some_file-md")
    # NB: We won't be able to determine which parts are file endings


def test_should_label_gist_and_file_and_line() -> None:
    # Given:
    url = "https://gist.github.com/my-account/abcdef123456789#file-some_file-md-L42"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/abcdef:some_file-md#42")
    # NB: We won't be able to determine which parts are file endings


def test_should_label_wiki_page() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/wiki/Some-Page"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo > Some Page")


def test_should_label_wiki_page_and_anchor() -> None:
    # Given:
    url = "https://github.com/my-account/some-repo/wiki/Some-Page#some-headline"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-account/some-repo > Some Page > Some Headline")


def test_should_label_security_advisories() -> None:
    # Given:
    url = "https://github.com/advisories/GHSA-7ww5-4wqc-m92c"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("GHSA-7ww5-4wqc-m92c")


def test_should_label_enterprise() -> None:
    # Given:
    url = "https://github.com/enterprises/my-big-company"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-big-company")

    # https://github.com/orgs/oscare-Digital-Layer/repositories


def test_should_label_organization() -> None:
    # Given:
    url = "https://github.com/orgs/my-cool-org/repositories"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-cool-org")
