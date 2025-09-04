from assertpy import assert_that

from scripts.label_for_url import determine_label


def test_should_label_project() -> None:
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT")


def test_should_label_repository() -> None:
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/some-project/browse"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project")


def test_should_label_user_repository() -> None:
    # Given:
    url = "https://our-bitbucket.my-org.de/users/user123/repos/some-project/browse"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("user123/some-project")


def test_should_label_file() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"  # keep linebreak
        "some-project/browse/some/file.md"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project:some/file.md")


def test_should_label_file_until_revision() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/browse/some/file.md"
        "?until=f3b751f5be406abcb020fc5eb72ff3260d0b4103"
        "&autoSincePath=false"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project@f3b751f5:some/file.md")


def test_should_label_file_at_revision() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/browse/some/file.md"
        "?at=f3b751f5be406abcb020fc5eb72ff3260d0b4103"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project@f3b751f5:some/file.md")


def test_should_label_file_with_spaces_in_filename() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/browse/some/spacey%20file.md"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project:some/spacey file.md")


def test_should_label_file_and_line() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/browse/some/file.md#42"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project:some/file.md#42")


def test_should_label_file_and_lines() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/browse/some/file.md#42,77"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project:some/file.md#42,77")


def test_should_label_file_and_line_range() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/browse/some/file.md#42-77"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project:some/file.md#42-77")


def test_should_label_file_on_branch() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/browse/some/file.md"
        "?at=refs%2Fheads%2Ffeature%2Fsome-feature"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project@feature/some-feature:some/file.md")


def test_should_label_file_and_line_on_branch() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/browse/some/file.md"
        "?at=refs%2Fheads%2Ffeature%2Fsome-feature#42"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project@feature/some-feature:some/file.md#42")


def test_should_label_raw_file() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/raw/some/file.md"
    )  # fmt: skip

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project:some/file.md")


def test_should_label_raw_file_at_revision() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/raw/some/file.md"
        "?at=refs%2Fheads%2Ffeature%2Fsome-feature"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project@feature/some-feature:some/file.md")


def test_should_label_pr() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"  # keep linebreak
        "some-project/pull-requests/77/"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project#77")


def test_should_label_pr_and_file() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/pull-requests/77/diff#some/file.md"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project#77:some/file.md")


def test_should_label_pr_and_file_and_line() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/pull-requests/77/diff#some/file.md?f=42"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project#77:some/file.md#42")


def test_should_label_pr_and_file_and_line_alternative() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/pull-requests/77/diff#some/file.md?t=42"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project#77:some/file.md#42")


def test_should_label_pr_and_comment() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/pull-requests/77/overview?commentId=113324"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project#77.113324")


def test_should_label_pr_and_commit() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/pull-requests/77/commits/f3b751f5be406abcb020fc5eb72ff3260d0b4103"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project#77@f3b751f5")


def test_should_label_pr_and_commit_and_file() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/pull-requests/77/commits/f3b751f5be406abcb020fc5eb72ff3260d0b4103"
        "#some/file.md"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project#77@f3b751f5:some/file.md")


def test_should_label_pr_and_commit_and_file_line() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/pull-requests/77/commits/f3b751f5be406abcb020fc5eb72ff3260d0b4103"
        "#some/file.md?f=42"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project#77@f3b751f5:some/file.md#42")


def test_should_label_commit() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/commits/f3b751f5be406abcb020fc5eb72ff3260d0b4103"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project@f3b751f5")


def test_should_label_commit_and_file() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/commits/f3b751f5be406abcb020fc5eb72ff3260d0b4103#some/file.md"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project@f3b751f5:some/file.md")


def test_should_label_commit_range() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/compare/commits?sourceBranch=b7912386fb6adad455963291da83ffb3da29761f&targetRepoId=3262&targetBranch=9c4fd5effec87136bfe92e9ac96886cd35ea9872"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project b7912386⭤9c4fd5ef")


def test_should_label_branch_via_branches() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/branches?base=feature%2Fsome-feature"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project@feature/some-feature")


def test_should_label_branch_via_commits() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/some-project/"
        "commits?until=feature/some-feature"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project@feature/some-feature")


def test_should_label_branch_via_commits_alternative() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/some-project/"
        "commits?until=refs%2Fheads%2Ffeature%2Fsome-feature"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project@feature/some-feature")


def test_should_label_branch_via_browse() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/some-project/"
        "browse?at=refs%2Fheads%2Ffeature%2Fsome-feature"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project@feature/some-feature")


def test_should_label_branch_commits() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/compare/commits?sourceBranch=refs%2Fheads%2Ffeature%2Fsome-feature&targetRepoId=77"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project@feature/some-feature")


def test_should_label_branch_diff() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/compare/diff?sourceBranch=refs%2Fheads%2Ffeature%2Fsome-feature&targetRepoId=77"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project@feature/some-feature")


def test_should_label_diff_of_tag_and_commit() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/compare/diff"
        "?sourceBranch=refs%2Ftags%2Fv2.1.0"
        "&targetBranch=3fa55ecbcd377c10b08c7ec2417492c083c14e13"
        "#some%2Ffile.md"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project v2.1.0⭤3fa55ecb")


def test_should_label_tag_via_branches() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"  # keep linebreak
        "some-project/branches?base=1.2.3"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project@1.2.3")


def test_should_label_tag_via_branches_alternative() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/branches"
        "?base=refs%2Ftags%2Fv2.1.0"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project@v2.1.0")


def test_should_label_file_diff() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/diff/some/file.md"
        "?until=8743ea85188c51b2c13aef82541b765bf3769d50"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project@8743ea85:some/file.md")


def test_should_label_commit_diff() -> None:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/compare/diff"
        "?sourceBranch=2efa13c3c03ace36bbbf9337c2ab82185a566a56"
        "&targetRepoId=77"
        "&targetBranch=ab3ee327d5ec2f0658a44f1f1192e4bfc0243101"
        "#some%2Ffile.md"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project 2efa13c3⭤ab3ee327")


def test_should_label_arbitrary_diff() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/"
        "some-project/compare/diff"
        "?targetBranch=b8aa09a9673c4b3af558313c3e08f10e7245708c"
        "&sourceBranch=refs%2Fheads%2Fdevelop"
        "&targetRepoId=77"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT/some-project develop⭤b8aa09a9")


def test_should_label_search_query() -> None:
    # Given:
    url = "https://our-bitbucket.my-org.de/plugins/servlet/search?q=some search in project:STUFF"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("🔍/some search in project:STUFF/")


def test_should_label_search_query_with_url_encoding() -> None:
    # Given:
    url = (
        "https://our-bitbucket.my-org.de/plugins/servlet/search"
        "?q=some%20search%20in%20project:STUFF"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("🔍/some search in project:STUFF/")
