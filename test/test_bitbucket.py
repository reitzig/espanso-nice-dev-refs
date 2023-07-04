from assertpy import assert_that

from label_for_url import determine_label


def test_should_label_project():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT')


def test_should_label_repository():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/browse"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project')


def test_should_label_user_repository():
    # Given:
    url = "https://our-bitbucket.my-org.de/users/user123/repos/" \
          "some-project/browse"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('user123/some-project')


def test_should_label_file():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/browse/some/file.md"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project:some/file.md')


def test_should_label_file_and_line():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/browse/some/file.md#42"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project:some/file.md#42')


def test_should_label_file_and_lines():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/browse/some/file.md#42,77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project:some/file.md#42,77')


def test_should_label_file_on_branch():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/browse/some/file.md" \
          "?at=refs%2Fheads%2Ffeature%2Fsome-feature"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project@feature/some-feature:some/file.md')


def test_should_label_file_and_line_on_branch():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/browse/some/file.md" \
          "?at=refs%2Fheads%2Ffeature%2Fsome-feature#42"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project@feature/some-feature:some/file.md#42')


def test_should_label_pr():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/pull-requests/77/"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project#77')


def test_should_label_pr_and_file():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/pull-requests/77/diff#some/file.md"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project#77:some/file.md')


def test_should_label_pr_and_file_and_line():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/pull-requests/77/diff#some/file.md?f=42"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project#77:some/file.md#42')


def test_should_label_pr_and_comment():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/pull-requests/77/overview?commentId=113324"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project#77.113324')


def test_should_label_pr_and_commit():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/pull-requests/77/commits/f3b751f5be406abcb020fc5eb72ff3260d0b4103"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project#77@f3b751f5')


def test_should_label_pr_and_commit_and_file():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/pull-requests/77/commits/f3b751f5be406abcb020fc5eb72ff3260d0b4103" \
          "#some/file.md"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project#77@f3b751f5:some/file.md')


def test_should_label_pr_and_commit_and_file_line():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/pull-requests/77/commits/f3b751f5be406abcb020fc5eb72ff3260d0b4103" \
          "#some/file.md?f=42"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project#77@f3b751f5:some/file.md#42')


def test_should_label_commit():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/commits/f3b751f5be406abcb020fc5eb72ff3260d0b4103"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project@f3b751f5')


def test_should_label_commit_and_file():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/commits/f3b751f5be406abcb020fc5eb72ff3260d0b4103#some/file.md"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project@f3b751f5:some/file.md')


def test_should_label_branch_via_commits():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/some-project/" \
          "commits?until=feature/some-feature"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project@feature/some-feature')


def test_should_label_branch_via_browse():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/some-project/" \
          "browse?at=refs%2Fheads%2Ffeature%2Fsome-feature"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project@feature/some-feature')


def test_should_label_branch_commits():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/compare/commits?sourceBranch=refs%2Fheads%2Ffeature%2Fsome-feature&targetRepoId=77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project@feature/some-feature')


def test_should_label_branch_diff():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/compare/diff?sourceBranch=refs%2Fheads%2Ffeature%2Fsome-feature&targetRepoId=77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project@feature/some-feature')


def test_should_label_file_diff():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/diff/some/file.md?until=8743ea85188c51b2c13aef82541b765bf3769d50"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project@8743ea85:some/file.md')


def test_should_label_arbitrary_diff():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/compare/diff" \
          "?targetBranch=b8aa09a9673c4b3af558313c3e08f10e7245708c" \
          "&sourceBranch=refs%2Fheads%2Fdevelop" \
          "&targetRepoId=77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project develop⭤b8aa09a9')
