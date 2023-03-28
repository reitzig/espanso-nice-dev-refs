from assertpy import assert_that

from label_for_url import determine_label


# TODO: What about file links to other refs?


def test_should_label_repository():
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT/repos/" \
          "some-project/browse"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('MY-PROJECT/some-project')


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
